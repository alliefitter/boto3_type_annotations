from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def add_listener_certificates(self, ListenerArn: str, Certificates: List) -> Dict:
        """
        
        If the certificate was already added, the call is successful but the certificate is not added again.
        
        To list the certificates for your listener, use  DescribeListenerCertificates . To remove certificates from your listener, use  RemoveListenerCertificates .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/AddListenerCertificates>`_
        
        **Request Syntax** 
        ::
        
          response = client.add_listener_certificates(
              ListenerArn=\'string\',
              Certificates=[
                  {
                      \'CertificateArn\': \'string\',
                      \'IsDefault\': True|False
                  },
              ]
          )
        :type ListenerArn: string
        :param ListenerArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the listener.
        
        :type Certificates: list
        :param Certificates: **[REQUIRED]** 
        
          The certificate to add. You can specify one certificate per call.
        
          - *(dict) --* 
        
            Information about an SSL server certificate.
        
            - **CertificateArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the certificate.
        
            - **IsDefault** *(boolean) --* 
        
              Indicates whether the certificate is the default certificate.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Certificates\': [
                    {
                        \'CertificateArn\': \'string\',
                        \'IsDefault\': True|False
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Certificates** *(list) --* 
        
              Information about the certificates.
        
              - *(dict) --* 
        
                Information about an SSL server certificate.
        
                - **CertificateArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the certificate.
        
                - **IsDefault** *(boolean) --* 
        
                  Indicates whether the certificate is the default certificate.
        
        """
        pass

    def add_tags(self, ResourceArns: List, Tags: List) -> Dict:
        """
        
        Each tag consists of a key and an optional value. If a resource already has a tag with the same key, ``AddTags`` updates its value.
        
        To list the current tags for your resources, use  DescribeTags . To remove tags from your resources, use  RemoveTags .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/AddTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.add_tags(
              ResourceArns=[
                  \'string\',
              ],
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type ResourceArns: list
        :param ResourceArns: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the resource.
        
          - *(string) --* 
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          The tags. Each resource can have a maximum of 10 tags.
        
          - *(dict) --* 
        
            Information about a tag.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The key of the tag.
        
            - **Value** *(string) --* 
        
              The value of the tag.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
        """
        
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

    def create_listener(self, LoadBalancerArn: str, Protocol: str, Port: int, DefaultActions: List, SslPolicy: str = None, Certificates: List = None) -> Dict:
        """
        
        To update a listener, use  ModifyListener . When you are finished with a listener, you can delete it using  DeleteListener . If you are finished with both the listener and the load balancer, you can delete them both using  DeleteLoadBalancer .
        
        This operation is idempotent, which means that it completes at most one time. If you attempt to create multiple listeners with the same settings, each call succeeds.
        
        For more information, see `Listeners for Your Application Load Balancers <http://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html>`__ in the *Application Load Balancers Guide* and `Listeners for Your Network Load Balancers <http://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-listeners.html>`__ in the *Network Load Balancers Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/CreateListener>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_listener(
              LoadBalancerArn=\'string\',
              Protocol=\'HTTP\'|\'HTTPS\'|\'TCP\',
              Port=123,
              SslPolicy=\'string\',
              Certificates=[
                  {
                      \'CertificateArn\': \'string\',
                      \'IsDefault\': True|False
                  },
              ],
              DefaultActions=[
                  {
                      \'Type\': \'forward\'|\'authenticate-oidc\'|\'authenticate-cognito\'|\'redirect\'|\'fixed-response\',
                      \'TargetGroupArn\': \'string\',
                      \'AuthenticateOidcConfig\': {
                          \'Issuer\': \'string\',
                          \'AuthorizationEndpoint\': \'string\',
                          \'TokenEndpoint\': \'string\',
                          \'UserInfoEndpoint\': \'string\',
                          \'ClientId\': \'string\',
                          \'ClientSecret\': \'string\',
                          \'SessionCookieName\': \'string\',
                          \'Scope\': \'string\',
                          \'SessionTimeout\': 123,
                          \'AuthenticationRequestExtraParams\': {
                              \'string\': \'string\'
                          },
                          \'OnUnauthenticatedRequest\': \'deny\'|\'allow\'|\'authenticate\'
                      },
                      \'AuthenticateCognitoConfig\': {
                          \'UserPoolArn\': \'string\',
                          \'UserPoolClientId\': \'string\',
                          \'UserPoolDomain\': \'string\',
                          \'SessionCookieName\': \'string\',
                          \'Scope\': \'string\',
                          \'SessionTimeout\': 123,
                          \'AuthenticationRequestExtraParams\': {
                              \'string\': \'string\'
                          },
                          \'OnUnauthenticatedRequest\': \'deny\'|\'allow\'|\'authenticate\'
                      },
                      \'Order\': 123,
                      \'RedirectConfig\': {
                          \'Protocol\': \'string\',
                          \'Port\': \'string\',
                          \'Host\': \'string\',
                          \'Path\': \'string\',
                          \'Query\': \'string\',
                          \'StatusCode\': \'HTTP_301\'|\'HTTP_302\'
                      },
                      \'FixedResponseConfig\': {
                          \'MessageBody\': \'string\',
                          \'StatusCode\': \'string\',
                          \'ContentType\': \'string\'
                      }
                  },
              ]
          )
        :type LoadBalancerArn: string
        :param LoadBalancerArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the load balancer.
        
        :type Protocol: string
        :param Protocol: **[REQUIRED]** 
        
          The protocol for connections from clients to the load balancer. For Application Load Balancers, the supported protocols are HTTP and HTTPS. For Network Load Balancers, the supported protocol is TCP.
        
        :type Port: integer
        :param Port: **[REQUIRED]** 
        
          The port on which the load balancer is listening.
        
        :type SslPolicy: string
        :param SslPolicy: 
        
          [HTTPS listeners] The security policy that defines which ciphers and protocols are supported. The default is the current predefined security policy.
        
        :type Certificates: list
        :param Certificates: 
        
          [HTTPS listeners] The default SSL server certificate. You must provide exactly one default certificate. To create a certificate list, use  AddListenerCertificates .
        
          - *(dict) --* 
        
            Information about an SSL server certificate.
        
            - **CertificateArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the certificate.
        
            - **IsDefault** *(boolean) --* 
        
              Indicates whether the certificate is the default certificate.
        
        :type DefaultActions: list
        :param DefaultActions: **[REQUIRED]** 
        
          The actions for the default rule. The rule must include one forward action or one or more fixed-response actions.
        
          If the action type is ``forward`` , you can specify a single target group. The protocol of the target group must be HTTP or HTTPS for an Application Load Balancer or TCP for a Network Load Balancer.
        
          [HTTPS listener] If the action type is ``authenticate-oidc`` , you can use an identity provider that is OpenID Connect (OIDC) compliant to authenticate users as they access your application.
        
          [HTTPS listener] If the action type is ``authenticate-cognito`` , you can use Amazon Cognito to authenticate users as they access your application.
        
          [Application Load Balancer] If the action type is ``redirect`` , you can redirect HTTP and HTTPS requests.
        
          [Application Load Balancer] If the action type is ``fixed-response`` , you can return a custom HTTP response.
        
          - *(dict) --* 
        
            Information about an action.
        
            - **Type** *(string) --* **[REQUIRED]** 
        
              The type of action. Each rule must include exactly one of the following types of actions: ``forward`` , ``fixed-response`` , or ``redirect`` .
        
            - **TargetGroupArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is ``forward`` .
        
            - **AuthenticateOidcConfig** *(dict) --* 
        
              [HTTPS listener] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .
        
              - **Issuer** *(string) --* **[REQUIRED]** 
        
                The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
              - **AuthorizationEndpoint** *(string) --* **[REQUIRED]** 
        
                The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
              - **TokenEndpoint** *(string) --* **[REQUIRED]** 
        
                The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
              - **UserInfoEndpoint** *(string) --* **[REQUIRED]** 
        
                The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
              - **ClientId** *(string) --* **[REQUIRED]** 
        
                The OAuth 2.0 client identifier.
        
              - **ClientSecret** *(string) --* **[REQUIRED]** 
        
                The OAuth 2.0 client secret.
        
              - **SessionCookieName** *(string) --* 
        
                The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.
        
              - **Scope** *(string) --* 
        
                The set of user claims to be requested from the IdP. The default is ``openid`` .
        
                To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.
        
              - **SessionTimeout** *(integer) --* 
        
                The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).
        
              - **AuthenticationRequestExtraParams** *(dict) --* 
        
                The query parameters (up to 10) to include in the redirect request to the authorization endpoint.
        
                - *(string) --* 
        
                  - *(string) --* 
        
              - **OnUnauthenticatedRequest** *(string) --* 
        
                The behavior if the user is not authenticated. The following are possible values:
        
                * deny- Return an HTTP 401 Unauthorized error. 
                 
                * allow- Allow the request to be forwarded to the target. 
                 
                * authenticate- Redirect the request to the IdP authorization endpoint. This is the default value. 
                 
            - **AuthenticateCognitoConfig** *(dict) --* 
        
              [HTTPS listener] Information for using Amazon Cognito to authenticate users. Specify only when ``Type`` is ``authenticate-cognito`` .
        
              - **UserPoolArn** *(string) --* **[REQUIRED]** 
        
                The Amazon Resource Name (ARN) of the Amazon Cognito user pool.
        
              - **UserPoolClientId** *(string) --* **[REQUIRED]** 
        
                The ID of the Amazon Cognito user pool client.
        
              - **UserPoolDomain** *(string) --* **[REQUIRED]** 
        
                The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.
        
              - **SessionCookieName** *(string) --* 
        
                The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.
        
              - **Scope** *(string) --* 
        
                The set of user claims to be requested from the IdP. The default is ``openid`` .
        
                To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.
        
              - **SessionTimeout** *(integer) --* 
        
                The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).
        
              - **AuthenticationRequestExtraParams** *(dict) --* 
        
                The query parameters (up to 10) to include in the redirect request to the authorization endpoint.
        
                - *(string) --* 
        
                  - *(string) --* 
        
              - **OnUnauthenticatedRequest** *(string) --* 
        
                The behavior if the user is not authenticated. The following are possible values:
        
                * deny- Return an HTTP 401 Unauthorized error. 
                 
                * allow- Allow the request to be forwarded to the target. 
                 
                * authenticate- Redirect the request to the IdP authorization endpoint. This is the default value. 
                 
            - **Order** *(integer) --* 
        
              The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first. The final action to be performed must be a ``forward`` or a ``fixed-response`` action.
        
            - **RedirectConfig** *(dict) --* 
        
              [Application Load Balancer] Information for creating a redirect action. Specify only when ``Type`` is ``redirect`` .
        
              - **Protocol** *(string) --* 
        
                The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.
        
              - **Port** *(string) --* 
        
                The port. You can specify a value from 1 to 65535 or #{port}.
        
              - **Host** *(string) --* 
        
                The hostname. This component is not percent-encoded. The hostname can contain #{host}.
        
              - **Path** *(string) --* 
        
                The absolute path, starting with the leading \"/\". This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}.
        
              - **Query** *(string) --* 
        
                The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading \"?\", as it is automatically added. You can specify any of the reserved keywords.
        
              - **StatusCode** *(string) --* **[REQUIRED]** 
        
                The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).
        
            - **FixedResponseConfig** *(dict) --* 
        
              [Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when ``Type`` is ``fixed-response`` .
        
              - **MessageBody** *(string) --* 
        
                The message.
        
              - **StatusCode** *(string) --* **[REQUIRED]** 
        
                The HTTP response code (2XX, 4XX, or 5XX).
        
              - **ContentType** *(string) --* 
        
                The content type.
        
                Valid Values: text/plain | text/css | text/html | application/javascript | application/json
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Listeners\': [
                    {
                        \'ListenerArn\': \'string\',
                        \'LoadBalancerArn\': \'string\',
                        \'Port\': 123,
                        \'Protocol\': \'HTTP\'|\'HTTPS\'|\'TCP\',
                        \'Certificates\': [
                            {
                                \'CertificateArn\': \'string\',
                                \'IsDefault\': True|False
                            },
                        ],
                        \'SslPolicy\': \'string\',
                        \'DefaultActions\': [
                            {
                                \'Type\': \'forward\'|\'authenticate-oidc\'|\'authenticate-cognito\'|\'redirect\'|\'fixed-response\',
                                \'TargetGroupArn\': \'string\',
                                \'AuthenticateOidcConfig\': {
                                    \'Issuer\': \'string\',
                                    \'AuthorizationEndpoint\': \'string\',
                                    \'TokenEndpoint\': \'string\',
                                    \'UserInfoEndpoint\': \'string\',
                                    \'ClientId\': \'string\',
                                    \'ClientSecret\': \'string\',
                                    \'SessionCookieName\': \'string\',
                                    \'Scope\': \'string\',
                                    \'SessionTimeout\': 123,
                                    \'AuthenticationRequestExtraParams\': {
                                        \'string\': \'string\'
                                    },
                                    \'OnUnauthenticatedRequest\': \'deny\'|\'allow\'|\'authenticate\'
                                },
                                \'AuthenticateCognitoConfig\': {
                                    \'UserPoolArn\': \'string\',
                                    \'UserPoolClientId\': \'string\',
                                    \'UserPoolDomain\': \'string\',
                                    \'SessionCookieName\': \'string\',
                                    \'Scope\': \'string\',
                                    \'SessionTimeout\': 123,
                                    \'AuthenticationRequestExtraParams\': {
                                        \'string\': \'string\'
                                    },
                                    \'OnUnauthenticatedRequest\': \'deny\'|\'allow\'|\'authenticate\'
                                },
                                \'Order\': 123,
                                \'RedirectConfig\': {
                                    \'Protocol\': \'string\',
                                    \'Port\': \'string\',
                                    \'Host\': \'string\',
                                    \'Path\': \'string\',
                                    \'Query\': \'string\',
                                    \'StatusCode\': \'HTTP_301\'|\'HTTP_302\'
                                },
                                \'FixedResponseConfig\': {
                                    \'MessageBody\': \'string\',
                                    \'StatusCode\': \'string\',
                                    \'ContentType\': \'string\'
                                }
                            },
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Listeners** *(list) --* 
        
              Information about the listener.
        
              - *(dict) --* 
        
                Information about a listener.
        
                - **ListenerArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the listener.
        
                - **LoadBalancerArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the load balancer.
        
                - **Port** *(integer) --* 
        
                  The port on which the load balancer is listening.
        
                - **Protocol** *(string) --* 
        
                  The protocol for connections from clients to the load balancer.
        
                - **Certificates** *(list) --* 
        
                  The SSL server certificate. You must provide a certificate if the protocol is HTTPS.
        
                  - *(dict) --* 
        
                    Information about an SSL server certificate.
        
                    - **CertificateArn** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the certificate.
        
                    - **IsDefault** *(boolean) --* 
        
                      Indicates whether the certificate is the default certificate.
        
                - **SslPolicy** *(string) --* 
        
                  The security policy that defines which ciphers and protocols are supported. The default is the current predefined security policy.
        
                - **DefaultActions** *(list) --* 
        
                  The default actions for the listener.
        
                  - *(dict) --* 
        
                    Information about an action.
        
                    - **Type** *(string) --* 
        
                      The type of action. Each rule must include exactly one of the following types of actions: ``forward`` , ``fixed-response`` , or ``redirect`` .
        
                    - **TargetGroupArn** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is ``forward`` .
        
                    - **AuthenticateOidcConfig** *(dict) --* 
        
                      [HTTPS listener] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .
        
                      - **Issuer** *(string) --* 
        
                        The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **AuthorizationEndpoint** *(string) --* 
        
                        The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **TokenEndpoint** *(string) --* 
        
                        The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **UserInfoEndpoint** *(string) --* 
        
                        The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **ClientId** *(string) --* 
        
                        The OAuth 2.0 client identifier.
        
                      - **ClientSecret** *(string) --* 
        
                        The OAuth 2.0 client secret.
        
                      - **SessionCookieName** *(string) --* 
        
                        The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.
        
                      - **Scope** *(string) --* 
        
                        The set of user claims to be requested from the IdP. The default is ``openid`` .
        
                        To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.
        
                      - **SessionTimeout** *(integer) --* 
        
                        The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).
        
                      - **AuthenticationRequestExtraParams** *(dict) --* 
        
                        The query parameters (up to 10) to include in the redirect request to the authorization endpoint.
        
                        - *(string) --* 
                          
                          - *(string) --* 
                    
                      - **OnUnauthenticatedRequest** *(string) --* 
        
                        The behavior if the user is not authenticated. The following are possible values:
        
                        * deny- Return an HTTP 401 Unauthorized error. 
                         
                        * allow- Allow the request to be forwarded to the target. 
                         
                        * authenticate- Redirect the request to the IdP authorization endpoint. This is the default value. 
                         
                    - **AuthenticateCognitoConfig** *(dict) --* 
        
                      [HTTPS listener] Information for using Amazon Cognito to authenticate users. Specify only when ``Type`` is ``authenticate-cognito`` .
        
                      - **UserPoolArn** *(string) --* 
        
                        The Amazon Resource Name (ARN) of the Amazon Cognito user pool.
        
                      - **UserPoolClientId** *(string) --* 
        
                        The ID of the Amazon Cognito user pool client.
        
                      - **UserPoolDomain** *(string) --* 
        
                        The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.
        
                      - **SessionCookieName** *(string) --* 
        
                        The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.
        
                      - **Scope** *(string) --* 
        
                        The set of user claims to be requested from the IdP. The default is ``openid`` .
        
                        To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.
        
                      - **SessionTimeout** *(integer) --* 
        
                        The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).
        
                      - **AuthenticationRequestExtraParams** *(dict) --* 
        
                        The query parameters (up to 10) to include in the redirect request to the authorization endpoint.
        
                        - *(string) --* 
                          
                          - *(string) --* 
                    
                      - **OnUnauthenticatedRequest** *(string) --* 
        
                        The behavior if the user is not authenticated. The following are possible values:
        
                        * deny- Return an HTTP 401 Unauthorized error. 
                         
                        * allow- Allow the request to be forwarded to the target. 
                         
                        * authenticate- Redirect the request to the IdP authorization endpoint. This is the default value. 
                         
                    - **Order** *(integer) --* 
        
                      The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first. The final action to be performed must be a ``forward`` or a ``fixed-response`` action.
        
                    - **RedirectConfig** *(dict) --* 
        
                      [Application Load Balancer] Information for creating a redirect action. Specify only when ``Type`` is ``redirect`` .
        
                      - **Protocol** *(string) --* 
        
                        The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.
        
                      - **Port** *(string) --* 
        
                        The port. You can specify a value from 1 to 65535 or #{port}.
        
                      - **Host** *(string) --* 
        
                        The hostname. This component is not percent-encoded. The hostname can contain #{host}.
        
                      - **Path** *(string) --* 
        
                        The absolute path, starting with the leading \"/\". This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}.
        
                      - **Query** *(string) --* 
        
                        The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading \"?\", as it is automatically added. You can specify any of the reserved keywords.
        
                      - **StatusCode** *(string) --* 
        
                        The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).
        
                    - **FixedResponseConfig** *(dict) --* 
        
                      [Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when ``Type`` is ``fixed-response`` .
        
                      - **MessageBody** *(string) --* 
        
                        The message.
        
                      - **StatusCode** *(string) --* 
        
                        The HTTP response code (2XX, 4XX, or 5XX).
        
                      - **ContentType** *(string) --* 
        
                        The content type.
        
                        Valid Values: text/plain | text/css | text/html | application/javascript | application/json
        
        """
        pass

    def create_load_balancer(self, Name: str, Subnets: List = None, SubnetMappings: List = None, SecurityGroups: List = None, Scheme: str = None, Tags: List = None, Type: str = None, IpAddressType: str = None) -> Dict:
        """
        
        When you create a load balancer, you can specify security groups, public subnets, IP address type, and tags. Otherwise, you could do so later using  SetSecurityGroups ,  SetSubnets ,  SetIpAddressType , and  AddTags .
        
        To create listeners for your load balancer, use  CreateListener . To describe your current load balancers, see  DescribeLoadBalancers . When you are finished with a load balancer, you can delete it using  DeleteLoadBalancer .
        
        For limit information, see `Limits for Your Application Load Balancer <http://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-limits.html>`__ in the *Application Load Balancers Guide* and `Limits for Your Network Load Balancer <http://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-limits.html>`__ in the *Network Load Balancers Guide* .
        
        This operation is idempotent, which means that it completes at most one time. If you attempt to create multiple load balancers with the same settings, each call succeeds.
        
        For more information, see `Application Load Balancers <http://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html>`__ in the *Application Load Balancers Guide* and `Network Load Balancers <http://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html>`__ in the *Network Load Balancers Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/CreateLoadBalancer>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_load_balancer(
              Name=\'string\',
              Subnets=[
                  \'string\',
              ],
              SubnetMappings=[
                  {
                      \'SubnetId\': \'string\',
                      \'AllocationId\': \'string\'
                  },
              ],
              SecurityGroups=[
                  \'string\',
              ],
              Scheme=\'internet-facing\'|\'internal\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ],
              Type=\'application\'|\'network\',
              IpAddressType=\'ipv4\'|\'dualstack\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the load balancer.
        
          This name must be unique per region per account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, must not begin or end with a hyphen, and must not begin with \"internal-\".
        
        :type Subnets: list
        :param Subnets: 
        
          The IDs of the public subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings.
        
          [Application Load Balancers] You must specify subnets from at least two Availability Zones.
        
          [Network Load Balancers] You can specify subnets from one or more Availability Zones.
        
          - *(string) --* 
        
        :type SubnetMappings: list
        :param SubnetMappings: 
        
          The IDs of the public subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings.
        
          [Application Load Balancers] You must specify subnets from at least two Availability Zones. You cannot specify Elastic IP addresses for your subnets.
        
          [Network Load Balancers] You can specify subnets from one or more Availability Zones. You can specify one Elastic IP address per subnet.
        
          - *(dict) --* 
        
            Information about a subnet mapping.
        
            - **SubnetId** *(string) --* 
        
              The ID of the subnet.
        
            - **AllocationId** *(string) --* 
        
              [Network Load Balancers] The allocation ID of the Elastic IP address.
        
        :type SecurityGroups: list
        :param SecurityGroups: 
        
          [Application Load Balancers] The IDs of the security groups for the load balancer.
        
          - *(string) --* 
        
        :type Scheme: string
        :param Scheme: 
        
          The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of an Internet-facing load balancer is publicly resolvable to the public IP addresses of the nodes. Therefore, Internet-facing load balancers can route requests from clients over the internet.
        
          The nodes of an internal load balancer have only private IP addresses. The DNS name of an internal load balancer is publicly resolvable to the private IP addresses of the nodes. Therefore, internal load balancers can only route requests from clients with access to the VPC for the load balancer.
        
          The default is an Internet-facing load balancer.
        
        :type Tags: list
        :param Tags: 
        
          One or more tags to assign to the load balancer.
        
          - *(dict) --* 
        
            Information about a tag.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The key of the tag.
        
            - **Value** *(string) --* 
        
              The value of the tag.
        
        :type Type: string
        :param Type: 
        
          The type of load balancer. The default is ``application`` .
        
        :type IpAddressType: string
        :param IpAddressType: 
        
          [Application Load Balancers] The type of IP addresses used by the subnets for your load balancer. The possible values are ``ipv4`` (for IPv4 addresses) and ``dualstack`` (for IPv4 and IPv6 addresses). Internal load balancers must use ``ipv4`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'LoadBalancers\': [
                    {
                        \'LoadBalancerArn\': \'string\',
                        \'DNSName\': \'string\',
                        \'CanonicalHostedZoneId\': \'string\',
                        \'CreatedTime\': datetime(2015, 1, 1),
                        \'LoadBalancerName\': \'string\',
                        \'Scheme\': \'internet-facing\'|\'internal\',
                        \'VpcId\': \'string\',
                        \'State\': {
                            \'Code\': \'active\'|\'provisioning\'|\'active_impaired\'|\'failed\',
                            \'Reason\': \'string\'
                        },
                        \'Type\': \'application\'|\'network\',
                        \'AvailabilityZones\': [
                            {
                                \'ZoneName\': \'string\',
                                \'SubnetId\': \'string\',
                                \'LoadBalancerAddresses\': [
                                    {
                                        \'IpAddress\': \'string\',
                                        \'AllocationId\': \'string\'
                                    },
                                ]
                            },
                        ],
                        \'SecurityGroups\': [
                            \'string\',
                        ],
                        \'IpAddressType\': \'ipv4\'|\'dualstack\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **LoadBalancers** *(list) --* 
        
              Information about the load balancer.
        
              - *(dict) --* 
        
                Information about a load balancer.
        
                - **LoadBalancerArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the load balancer.
        
                - **DNSName** *(string) --* 
        
                  The public DNS name of the load balancer.
        
                - **CanonicalHostedZoneId** *(string) --* 
        
                  The ID of the Amazon Route 53 hosted zone associated with the load balancer.
        
                - **CreatedTime** *(datetime) --* 
        
                  The date and time the load balancer was created.
        
                - **LoadBalancerName** *(string) --* 
        
                  The name of the load balancer.
        
                - **Scheme** *(string) --* 
        
                  The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of an Internet-facing load balancer is publicly resolvable to the public IP addresses of the nodes. Therefore, Internet-facing load balancers can route requests from clients over the internet.
        
                  The nodes of an internal load balancer have only private IP addresses. The DNS name of an internal load balancer is publicly resolvable to the private IP addresses of the nodes. Therefore, internal load balancers can only route requests from clients with access to the VPC for the load balancer.
        
                - **VpcId** *(string) --* 
        
                  The ID of the VPC for the load balancer.
        
                - **State** *(dict) --* 
        
                  The state of the load balancer.
        
                  - **Code** *(string) --* 
        
                    The state code. The initial state of the load balancer is ``provisioning`` . After the load balancer is fully set up and ready to route traffic, its state is ``active`` . If the load balancer could not be set up, its state is ``failed`` .
        
                  - **Reason** *(string) --* 
        
                    A description of the state.
        
                - **Type** *(string) --* 
        
                  The type of load balancer.
        
                - **AvailabilityZones** *(list) --* 
        
                  The Availability Zones for the load balancer.
        
                  - *(dict) --* 
        
                    Information about an Availability Zone.
        
                    - **ZoneName** *(string) --* 
        
                      The name of the Availability Zone.
        
                    - **SubnetId** *(string) --* 
        
                      The ID of the subnet.
        
                    - **LoadBalancerAddresses** *(list) --* 
        
                      [Network Load Balancers] The static IP address.
        
                      - *(dict) --* 
        
                        Information about a static IP address for a load balancer.
        
                        - **IpAddress** *(string) --* 
        
                          The static IP address.
        
                        - **AllocationId** *(string) --* 
        
                          [Network Load Balancers] The allocation ID of the Elastic IP address.
        
                - **SecurityGroups** *(list) --* 
        
                  The IDs of the security groups for the load balancer.
        
                  - *(string) --* 
              
                - **IpAddressType** *(string) --* 
        
                  The type of IP addresses used by the subnets for your load balancer. The possible values are ``ipv4`` (for IPv4 addresses) and ``dualstack`` (for IPv4 and IPv6 addresses).
        
        """
        pass

    def create_rule(self, ListenerArn: str, Conditions: List, Priority: int, Actions: List) -> Dict:
        """
        
        Rules are evaluated in priority order, from the lowest value to the highest value. When the conditions for a rule are met, its actions are performed. If the conditions for no rules are met, the actions for the default rule are performed. For more information, see `Listener Rules <http://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html#listener-rules>`__ in the *Application Load Balancers Guide* .
        
        To view your current rules, use  DescribeRules . To update a rule, use  ModifyRule . To set the priorities of your rules, use  SetRulePriorities . To delete a rule, use  DeleteRule .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/CreateRule>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_rule(
              ListenerArn=\'string\',
              Conditions=[
                  {
                      \'Field\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              Priority=123,
              Actions=[
                  {
                      \'Type\': \'forward\'|\'authenticate-oidc\'|\'authenticate-cognito\'|\'redirect\'|\'fixed-response\',
                      \'TargetGroupArn\': \'string\',
                      \'AuthenticateOidcConfig\': {
                          \'Issuer\': \'string\',
                          \'AuthorizationEndpoint\': \'string\',
                          \'TokenEndpoint\': \'string\',
                          \'UserInfoEndpoint\': \'string\',
                          \'ClientId\': \'string\',
                          \'ClientSecret\': \'string\',
                          \'SessionCookieName\': \'string\',
                          \'Scope\': \'string\',
                          \'SessionTimeout\': 123,
                          \'AuthenticationRequestExtraParams\': {
                              \'string\': \'string\'
                          },
                          \'OnUnauthenticatedRequest\': \'deny\'|\'allow\'|\'authenticate\'
                      },
                      \'AuthenticateCognitoConfig\': {
                          \'UserPoolArn\': \'string\',
                          \'UserPoolClientId\': \'string\',
                          \'UserPoolDomain\': \'string\',
                          \'SessionCookieName\': \'string\',
                          \'Scope\': \'string\',
                          \'SessionTimeout\': 123,
                          \'AuthenticationRequestExtraParams\': {
                              \'string\': \'string\'
                          },
                          \'OnUnauthenticatedRequest\': \'deny\'|\'allow\'|\'authenticate\'
                      },
                      \'Order\': 123,
                      \'RedirectConfig\': {
                          \'Protocol\': \'string\',
                          \'Port\': \'string\',
                          \'Host\': \'string\',
                          \'Path\': \'string\',
                          \'Query\': \'string\',
                          \'StatusCode\': \'HTTP_301\'|\'HTTP_302\'
                      },
                      \'FixedResponseConfig\': {
                          \'MessageBody\': \'string\',
                          \'StatusCode\': \'string\',
                          \'ContentType\': \'string\'
                      }
                  },
              ]
          )
        :type ListenerArn: string
        :param ListenerArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the listener.
        
        :type Conditions: list
        :param Conditions: **[REQUIRED]** 
        
          The conditions. Each condition specifies a field name and a single value.
        
          If the field name is ``host-header`` , you can specify a single host name (for example, my.example.com). A host name is case insensitive, can be up to 128 characters in length, and can contain any of the following characters. You can include up to three wildcard characters.
        
          * A-Z, a-z, 0-9 
           
          * - . 
           
          * * (matches 0 or more characters) 
           
          * ? (matches exactly 1 character) 
           
          If the field name is ``path-pattern`` , you can specify a single path pattern. A path pattern is case-sensitive, can be up to 128 characters in length, and can contain any of the following characters. You can include up to three wildcard characters.
        
          * A-Z, a-z, 0-9 
           
          * _ - . $ / ~ \" \' @ : + 
           
          * & (using &amp;) 
           
          * * (matches 0 or more characters) 
           
          * ? (matches exactly 1 character) 
           
          - *(dict) --* 
        
            Information about a condition for a rule.
        
            - **Field** *(string) --* 
        
              The name of the field. The possible values are ``host-header`` and ``path-pattern`` .
        
            - **Values** *(list) --* 
        
              The condition value.
        
              If the field name is ``host-header`` , you can specify a single host name (for example, my.example.com). A host name is case insensitive, can be up to 128 characters in length, and can contain any of the following characters. You can include up to three wildcard characters.
        
              * A-Z, a-z, 0-9 
               
              * - . 
               
              * * (matches 0 or more characters) 
               
              * ? (matches exactly 1 character) 
               
              If the field name is ``path-pattern`` , you can specify a single path pattern (for example, /img/*). A path pattern is case-sensitive, can be up to 128 characters in length, and can contain any of the following characters. You can include up to three wildcard characters.
        
              * A-Z, a-z, 0-9 
               
              * _ - . $ / ~ \" \' @ : + 
               
              * & (using &amp;) 
               
              * * (matches 0 or more characters) 
               
              * ? (matches exactly 1 character) 
               
              - *(string) --* 
        
        :type Priority: integer
        :param Priority: **[REQUIRED]** 
        
          The rule priority. A listener can\'t have multiple rules with the same priority.
        
        :type Actions: list
        :param Actions: **[REQUIRED]** 
        
          The actions. Each rule must include exactly one of the following types of actions: ``forward`` , ``fixed-response`` , or ``redirect`` .
        
          If the action type is ``forward`` , you can specify a single target group.
        
          [HTTPS listener] If the action type is ``authenticate-oidc`` , you can use an identity provider that is OpenID Connect (OIDC) compliant to authenticate users as they access your application.
        
          [HTTPS listener] If the action type is ``authenticate-cognito`` , you can use Amazon Cognito to authenticate users as they access your application.
        
          [Application Load Balancer] If the action type is ``redirect`` , you can redirect HTTP and HTTPS requests.
        
          [Application Load Balancer] If the action type is ``fixed-response`` , you can return a custom HTTP response.
        
          - *(dict) --* 
        
            Information about an action.
        
            - **Type** *(string) --* **[REQUIRED]** 
        
              The type of action. Each rule must include exactly one of the following types of actions: ``forward`` , ``fixed-response`` , or ``redirect`` .
        
            - **TargetGroupArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is ``forward`` .
        
            - **AuthenticateOidcConfig** *(dict) --* 
        
              [HTTPS listener] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .
        
              - **Issuer** *(string) --* **[REQUIRED]** 
        
                The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
              - **AuthorizationEndpoint** *(string) --* **[REQUIRED]** 
        
                The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
              - **TokenEndpoint** *(string) --* **[REQUIRED]** 
        
                The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
              - **UserInfoEndpoint** *(string) --* **[REQUIRED]** 
        
                The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
              - **ClientId** *(string) --* **[REQUIRED]** 
        
                The OAuth 2.0 client identifier.
        
              - **ClientSecret** *(string) --* **[REQUIRED]** 
        
                The OAuth 2.0 client secret.
        
              - **SessionCookieName** *(string) --* 
        
                The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.
        
              - **Scope** *(string) --* 
        
                The set of user claims to be requested from the IdP. The default is ``openid`` .
        
                To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.
        
              - **SessionTimeout** *(integer) --* 
        
                The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).
        
              - **AuthenticationRequestExtraParams** *(dict) --* 
        
                The query parameters (up to 10) to include in the redirect request to the authorization endpoint.
        
                - *(string) --* 
        
                  - *(string) --* 
        
              - **OnUnauthenticatedRequest** *(string) --* 
        
                The behavior if the user is not authenticated. The following are possible values:
        
                * deny- Return an HTTP 401 Unauthorized error. 
                 
                * allow- Allow the request to be forwarded to the target. 
                 
                * authenticate- Redirect the request to the IdP authorization endpoint. This is the default value. 
                 
            - **AuthenticateCognitoConfig** *(dict) --* 
        
              [HTTPS listener] Information for using Amazon Cognito to authenticate users. Specify only when ``Type`` is ``authenticate-cognito`` .
        
              - **UserPoolArn** *(string) --* **[REQUIRED]** 
        
                The Amazon Resource Name (ARN) of the Amazon Cognito user pool.
        
              - **UserPoolClientId** *(string) --* **[REQUIRED]** 
        
                The ID of the Amazon Cognito user pool client.
        
              - **UserPoolDomain** *(string) --* **[REQUIRED]** 
        
                The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.
        
              - **SessionCookieName** *(string) --* 
        
                The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.
        
              - **Scope** *(string) --* 
        
                The set of user claims to be requested from the IdP. The default is ``openid`` .
        
                To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.
        
              - **SessionTimeout** *(integer) --* 
        
                The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).
        
              - **AuthenticationRequestExtraParams** *(dict) --* 
        
                The query parameters (up to 10) to include in the redirect request to the authorization endpoint.
        
                - *(string) --* 
        
                  - *(string) --* 
        
              - **OnUnauthenticatedRequest** *(string) --* 
        
                The behavior if the user is not authenticated. The following are possible values:
        
                * deny- Return an HTTP 401 Unauthorized error. 
                 
                * allow- Allow the request to be forwarded to the target. 
                 
                * authenticate- Redirect the request to the IdP authorization endpoint. This is the default value. 
                 
            - **Order** *(integer) --* 
        
              The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first. The final action to be performed must be a ``forward`` or a ``fixed-response`` action.
        
            - **RedirectConfig** *(dict) --* 
        
              [Application Load Balancer] Information for creating a redirect action. Specify only when ``Type`` is ``redirect`` .
        
              - **Protocol** *(string) --* 
        
                The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.
        
              - **Port** *(string) --* 
        
                The port. You can specify a value from 1 to 65535 or #{port}.
        
              - **Host** *(string) --* 
        
                The hostname. This component is not percent-encoded. The hostname can contain #{host}.
        
              - **Path** *(string) --* 
        
                The absolute path, starting with the leading \"/\". This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}.
        
              - **Query** *(string) --* 
        
                The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading \"?\", as it is automatically added. You can specify any of the reserved keywords.
        
              - **StatusCode** *(string) --* **[REQUIRED]** 
        
                The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).
        
            - **FixedResponseConfig** *(dict) --* 
        
              [Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when ``Type`` is ``fixed-response`` .
        
              - **MessageBody** *(string) --* 
        
                The message.
        
              - **StatusCode** *(string) --* **[REQUIRED]** 
        
                The HTTP response code (2XX, 4XX, or 5XX).
        
              - **ContentType** *(string) --* 
        
                The content type.
        
                Valid Values: text/plain | text/css | text/html | application/javascript | application/json
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Rules\': [
                    {
                        \'RuleArn\': \'string\',
                        \'Priority\': \'string\',
                        \'Conditions\': [
                            {
                                \'Field\': \'string\',
                                \'Values\': [
                                    \'string\',
                                ]
                            },
                        ],
                        \'Actions\': [
                            {
                                \'Type\': \'forward\'|\'authenticate-oidc\'|\'authenticate-cognito\'|\'redirect\'|\'fixed-response\',
                                \'TargetGroupArn\': \'string\',
                                \'AuthenticateOidcConfig\': {
                                    \'Issuer\': \'string\',
                                    \'AuthorizationEndpoint\': \'string\',
                                    \'TokenEndpoint\': \'string\',
                                    \'UserInfoEndpoint\': \'string\',
                                    \'ClientId\': \'string\',
                                    \'ClientSecret\': \'string\',
                                    \'SessionCookieName\': \'string\',
                                    \'Scope\': \'string\',
                                    \'SessionTimeout\': 123,
                                    \'AuthenticationRequestExtraParams\': {
                                        \'string\': \'string\'
                                    },
                                    \'OnUnauthenticatedRequest\': \'deny\'|\'allow\'|\'authenticate\'
                                },
                                \'AuthenticateCognitoConfig\': {
                                    \'UserPoolArn\': \'string\',
                                    \'UserPoolClientId\': \'string\',
                                    \'UserPoolDomain\': \'string\',
                                    \'SessionCookieName\': \'string\',
                                    \'Scope\': \'string\',
                                    \'SessionTimeout\': 123,
                                    \'AuthenticationRequestExtraParams\': {
                                        \'string\': \'string\'
                                    },
                                    \'OnUnauthenticatedRequest\': \'deny\'|\'allow\'|\'authenticate\'
                                },
                                \'Order\': 123,
                                \'RedirectConfig\': {
                                    \'Protocol\': \'string\',
                                    \'Port\': \'string\',
                                    \'Host\': \'string\',
                                    \'Path\': \'string\',
                                    \'Query\': \'string\',
                                    \'StatusCode\': \'HTTP_301\'|\'HTTP_302\'
                                },
                                \'FixedResponseConfig\': {
                                    \'MessageBody\': \'string\',
                                    \'StatusCode\': \'string\',
                                    \'ContentType\': \'string\'
                                }
                            },
                        ],
                        \'IsDefault\': True|False
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Rules** *(list) --* 
        
              Information about the rule.
        
              - *(dict) --* 
        
                Information about a rule.
        
                - **RuleArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the rule.
        
                - **Priority** *(string) --* 
        
                  The priority.
        
                - **Conditions** *(list) --* 
        
                  The conditions.
        
                  - *(dict) --* 
        
                    Information about a condition for a rule.
        
                    - **Field** *(string) --* 
        
                      The name of the field. The possible values are ``host-header`` and ``path-pattern`` .
        
                    - **Values** *(list) --* 
        
                      The condition value.
        
                      If the field name is ``host-header`` , you can specify a single host name (for example, my.example.com). A host name is case insensitive, can be up to 128 characters in length, and can contain any of the following characters. You can include up to three wildcard characters.
        
                      * A-Z, a-z, 0-9 
                       
                      * - . 
                       
                      * * (matches 0 or more characters) 
                       
                      * ? (matches exactly 1 character) 
                       
                      If the field name is ``path-pattern`` , you can specify a single path pattern (for example, /img/*). A path pattern is case-sensitive, can be up to 128 characters in length, and can contain any of the following characters. You can include up to three wildcard characters.
        
                      * A-Z, a-z, 0-9 
                       
                      * _ - . $ / ~ \" \' @ : + 
                       
                      * & (using &amp;) 
                       
                      * * (matches 0 or more characters) 
                       
                      * ? (matches exactly 1 character) 
                       
                      - *(string) --* 
                  
                - **Actions** *(list) --* 
        
                  The actions.
        
                  - *(dict) --* 
        
                    Information about an action.
        
                    - **Type** *(string) --* 
        
                      The type of action. Each rule must include exactly one of the following types of actions: ``forward`` , ``fixed-response`` , or ``redirect`` .
        
                    - **TargetGroupArn** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is ``forward`` .
        
                    - **AuthenticateOidcConfig** *(dict) --* 
        
                      [HTTPS listener] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .
        
                      - **Issuer** *(string) --* 
        
                        The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **AuthorizationEndpoint** *(string) --* 
        
                        The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **TokenEndpoint** *(string) --* 
        
                        The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **UserInfoEndpoint** *(string) --* 
        
                        The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **ClientId** *(string) --* 
        
                        The OAuth 2.0 client identifier.
        
                      - **ClientSecret** *(string) --* 
        
                        The OAuth 2.0 client secret.
        
                      - **SessionCookieName** *(string) --* 
        
                        The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.
        
                      - **Scope** *(string) --* 
        
                        The set of user claims to be requested from the IdP. The default is ``openid`` .
        
                        To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.
        
                      - **SessionTimeout** *(integer) --* 
        
                        The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).
        
                      - **AuthenticationRequestExtraParams** *(dict) --* 
        
                        The query parameters (up to 10) to include in the redirect request to the authorization endpoint.
        
                        - *(string) --* 
                          
                          - *(string) --* 
                    
                      - **OnUnauthenticatedRequest** *(string) --* 
        
                        The behavior if the user is not authenticated. The following are possible values:
        
                        * deny- Return an HTTP 401 Unauthorized error. 
                         
                        * allow- Allow the request to be forwarded to the target. 
                         
                        * authenticate- Redirect the request to the IdP authorization endpoint. This is the default value. 
                         
                    - **AuthenticateCognitoConfig** *(dict) --* 
        
                      [HTTPS listener] Information for using Amazon Cognito to authenticate users. Specify only when ``Type`` is ``authenticate-cognito`` .
        
                      - **UserPoolArn** *(string) --* 
        
                        The Amazon Resource Name (ARN) of the Amazon Cognito user pool.
        
                      - **UserPoolClientId** *(string) --* 
        
                        The ID of the Amazon Cognito user pool client.
        
                      - **UserPoolDomain** *(string) --* 
        
                        The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.
        
                      - **SessionCookieName** *(string) --* 
        
                        The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.
        
                      - **Scope** *(string) --* 
        
                        The set of user claims to be requested from the IdP. The default is ``openid`` .
        
                        To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.
        
                      - **SessionTimeout** *(integer) --* 
        
                        The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).
        
                      - **AuthenticationRequestExtraParams** *(dict) --* 
        
                        The query parameters (up to 10) to include in the redirect request to the authorization endpoint.
        
                        - *(string) --* 
                          
                          - *(string) --* 
                    
                      - **OnUnauthenticatedRequest** *(string) --* 
        
                        The behavior if the user is not authenticated. The following are possible values:
        
                        * deny- Return an HTTP 401 Unauthorized error. 
                         
                        * allow- Allow the request to be forwarded to the target. 
                         
                        * authenticate- Redirect the request to the IdP authorization endpoint. This is the default value. 
                         
                    - **Order** *(integer) --* 
        
                      The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first. The final action to be performed must be a ``forward`` or a ``fixed-response`` action.
        
                    - **RedirectConfig** *(dict) --* 
        
                      [Application Load Balancer] Information for creating a redirect action. Specify only when ``Type`` is ``redirect`` .
        
                      - **Protocol** *(string) --* 
        
                        The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.
        
                      - **Port** *(string) --* 
        
                        The port. You can specify a value from 1 to 65535 or #{port}.
        
                      - **Host** *(string) --* 
        
                        The hostname. This component is not percent-encoded. The hostname can contain #{host}.
        
                      - **Path** *(string) --* 
        
                        The absolute path, starting with the leading \"/\". This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}.
        
                      - **Query** *(string) --* 
        
                        The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading \"?\", as it is automatically added. You can specify any of the reserved keywords.
        
                      - **StatusCode** *(string) --* 
        
                        The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).
        
                    - **FixedResponseConfig** *(dict) --* 
        
                      [Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when ``Type`` is ``fixed-response`` .
        
                      - **MessageBody** *(string) --* 
        
                        The message.
        
                      - **StatusCode** *(string) --* 
        
                        The HTTP response code (2XX, 4XX, or 5XX).
        
                      - **ContentType** *(string) --* 
        
                        The content type.
        
                        Valid Values: text/plain | text/css | text/html | application/javascript | application/json
        
                - **IsDefault** *(boolean) --* 
        
                  Indicates whether this is the default rule.
        
        """
        pass

    def create_target_group(self, Name: str, Protocol: str, Port: int, VpcId: str, HealthCheckProtocol: str = None, HealthCheckPort: str = None, HealthCheckPath: str = None, HealthCheckIntervalSeconds: int = None, HealthCheckTimeoutSeconds: int = None, HealthyThresholdCount: int = None, UnhealthyThresholdCount: int = None, Matcher: Dict = None, TargetType: str = None) -> Dict:
        """
        
        To register targets with the target group, use  RegisterTargets . To update the health check settings for the target group, use  ModifyTargetGroup . To monitor the health of targets in the target group, use  DescribeTargetHealth .
        
        To route traffic to the targets in a target group, specify the target group in an action using  CreateListener or  CreateRule .
        
        To delete a target group, use  DeleteTargetGroup .
        
        This operation is idempotent, which means that it completes at most one time. If you attempt to create multiple target groups with the same settings, each call succeeds.
        
        For more information, see `Target Groups for Your Application Load Balancers <http://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html>`__ in the *Application Load Balancers Guide* or `Target Groups for Your Network Load Balancers <http://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html>`__ in the *Network Load Balancers Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/CreateTargetGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_target_group(
              Name=\'string\',
              Protocol=\'HTTP\'|\'HTTPS\'|\'TCP\',
              Port=123,
              VpcId=\'string\',
              HealthCheckProtocol=\'HTTP\'|\'HTTPS\'|\'TCP\',
              HealthCheckPort=\'string\',
              HealthCheckPath=\'string\',
              HealthCheckIntervalSeconds=123,
              HealthCheckTimeoutSeconds=123,
              HealthyThresholdCount=123,
              UnhealthyThresholdCount=123,
              Matcher={
                  \'HttpCode\': \'string\'
              },
              TargetType=\'instance\'|\'ip\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name of the target group.
        
          This name must be unique per region per account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.
        
        :type Protocol: string
        :param Protocol: **[REQUIRED]** 
        
          The protocol to use for routing traffic to the targets. For Application Load Balancers, the supported protocols are HTTP and HTTPS. For Network Load Balancers, the supported protocol is TCP.
        
        :type Port: integer
        :param Port: **[REQUIRED]** 
        
          The port on which the targets receive traffic. This port is used unless you specify a port override when registering the target.
        
        :type VpcId: string
        :param VpcId: **[REQUIRED]** 
        
          The identifier of the virtual private cloud (VPC).
        
        :type HealthCheckProtocol: string
        :param HealthCheckProtocol: 
        
          The protocol the load balancer uses when performing health checks on targets. The TCP protocol is supported only if the protocol of the target group is TCP. For Application Load Balancers, the default is HTTP. For Network Load Balancers, the default is TCP.
        
        :type HealthCheckPort: string
        :param HealthCheckPort: 
        
          The port the load balancer uses when performing health checks on targets. The default is ``traffic-port`` , which is the port on which each target receives traffic from the load balancer.
        
        :type HealthCheckPath: string
        :param HealthCheckPath: 
        
          [HTTP/HTTPS health checks] The ping path that is the destination on the targets for health checks. The default is /.
        
        :type HealthCheckIntervalSeconds: integer
        :param HealthCheckIntervalSeconds: 
        
          The approximate amount of time, in seconds, between health checks of an individual target. For Application Load Balancers, the range is 5–300 seconds. For Network Load Balancers, the supported values are 10 or 30 seconds. The default is 30 seconds.
        
        :type HealthCheckTimeoutSeconds: integer
        :param HealthCheckTimeoutSeconds: 
        
          The amount of time, in seconds, during which no response from a target means a failed health check. For Application Load Balancers, the range is 2–60 seconds and the default is 5 seconds. For Network Load Balancers, this is 10 seconds for TCP and HTTPS health checks and 6 seconds for HTTP health checks.
        
        :type HealthyThresholdCount: integer
        :param HealthyThresholdCount: 
        
          The number of consecutive health checks successes required before considering an unhealthy target healthy. For Application Load Balancers, the default is 5. For Network Load Balancers, the default is 3.
        
        :type UnhealthyThresholdCount: integer
        :param UnhealthyThresholdCount: 
        
          The number of consecutive health check failures required before considering a target unhealthy. For Application Load Balancers, the default is 2. For Network Load Balancers, this value must be the same as the healthy threshold count.
        
        :type Matcher: dict
        :param Matcher: 
        
          [HTTP/HTTPS health checks] The HTTP codes to use when checking for a successful response from a target.
        
          - **HttpCode** *(string) --* **[REQUIRED]** 
        
            The HTTP codes.
        
            For Application Load Balancers, you can specify values between 200 and 499, and the default value is 200. You can specify multiple values (for example, \"200,202\") or a range of values (for example, \"200-299\").
        
            For Network Load Balancers, this is 200–399.
        
        :type TargetType: string
        :param TargetType: 
        
          The type of target that you must specify when registering targets with this target group. The possible values are ``instance`` (targets are specified by instance ID) or ``ip`` (targets are specified by IP address). The default is ``instance`` . You can\'t specify targets for a target group using both instance IDs and IP addresses.
        
          If the target type is ``ip`` , specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group, the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10). You can\'t specify publicly routable IP addresses.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TargetGroups\': [
                    {
                        \'TargetGroupArn\': \'string\',
                        \'TargetGroupName\': \'string\',
                        \'Protocol\': \'HTTP\'|\'HTTPS\'|\'TCP\',
                        \'Port\': 123,
                        \'VpcId\': \'string\',
                        \'HealthCheckProtocol\': \'HTTP\'|\'HTTPS\'|\'TCP\',
                        \'HealthCheckPort\': \'string\',
                        \'HealthCheckIntervalSeconds\': 123,
                        \'HealthCheckTimeoutSeconds\': 123,
                        \'HealthyThresholdCount\': 123,
                        \'UnhealthyThresholdCount\': 123,
                        \'HealthCheckPath\': \'string\',
                        \'Matcher\': {
                            \'HttpCode\': \'string\'
                        },
                        \'LoadBalancerArns\': [
                            \'string\',
                        ],
                        \'TargetType\': \'instance\'|\'ip\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TargetGroups** *(list) --* 
        
              Information about the target group.
        
              - *(dict) --* 
        
                Information about a target group.
        
                - **TargetGroupArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the target group.
        
                - **TargetGroupName** *(string) --* 
        
                  The name of the target group.
        
                - **Protocol** *(string) --* 
        
                  The protocol to use for routing traffic to the targets.
        
                - **Port** *(integer) --* 
        
                  The port on which the targets are listening.
        
                - **VpcId** *(string) --* 
        
                  The ID of the VPC for the targets.
        
                - **HealthCheckProtocol** *(string) --* 
        
                  The protocol to use to connect with the target.
        
                - **HealthCheckPort** *(string) --* 
        
                  The port to use to connect with the target.
        
                - **HealthCheckIntervalSeconds** *(integer) --* 
        
                  The approximate amount of time, in seconds, between health checks of an individual target.
        
                - **HealthCheckTimeoutSeconds** *(integer) --* 
        
                  The amount of time, in seconds, during which no response means a failed health check.
        
                - **HealthyThresholdCount** *(integer) --* 
        
                  The number of consecutive health checks successes required before considering an unhealthy target healthy.
        
                - **UnhealthyThresholdCount** *(integer) --* 
        
                  The number of consecutive health check failures required before considering the target unhealthy.
        
                - **HealthCheckPath** *(string) --* 
        
                  The destination for the health check request.
        
                - **Matcher** *(dict) --* 
        
                  The HTTP codes to use when checking for a successful response from a target.
        
                  - **HttpCode** *(string) --* 
        
                    The HTTP codes.
        
                    For Application Load Balancers, you can specify values between 200 and 499, and the default value is 200. You can specify multiple values (for example, \"200,202\") or a range of values (for example, \"200-299\").
        
                    For Network Load Balancers, this is 200–399.
        
                - **LoadBalancerArns** *(list) --* 
        
                  The Amazon Resource Names (ARN) of the load balancers that route traffic to this target group.
        
                  - *(string) --* 
              
                - **TargetType** *(string) --* 
        
                  The type of target that you must specify when registering targets with this target group. The possible values are ``instance`` (targets are specified by instance ID) or ``ip`` (targets are specified by IP address).
        
        """
        pass

    def delete_listener(self, ListenerArn: str) -> Dict:
        """
        
        Alternatively, your listener is deleted when you delete the load balancer to which it is attached, using  DeleteLoadBalancer .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DeleteListener>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_listener(
              ListenerArn=\'string\'
          )
        :type ListenerArn: string
        :param ListenerArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the listener.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_load_balancer(self, LoadBalancerArn: str) -> Dict:
        """
        
        You can\'t delete a load balancer if deletion protection is enabled. If the load balancer does not exist or has already been deleted, the call succeeds.
        
        Deleting a load balancer does not affect its registered targets. For example, your EC2 instances continue to run and are still registered to their target groups. If you no longer need these EC2 instances, you can stop or terminate them.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DeleteLoadBalancer>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_load_balancer(
              LoadBalancerArn=\'string\'
          )
        :type LoadBalancerArn: string
        :param LoadBalancerArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the load balancer.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_rule(self, RuleArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DeleteRule>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_rule(
              RuleArn=\'string\'
          )
        :type RuleArn: string
        :param RuleArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the rule.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_target_group(self, TargetGroupArn: str) -> Dict:
        """
        
        You can delete a target group if it is not referenced by any actions. Deleting a target group also deletes any associated health checks.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DeleteTargetGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_target_group(
              TargetGroupArn=\'string\'
          )
        :type TargetGroupArn: string
        :param TargetGroupArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the target group.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def deregister_targets(self, TargetGroupArn: str, Targets: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DeregisterTargets>`_
        
        **Request Syntax** 
        ::
        
          response = client.deregister_targets(
              TargetGroupArn=\'string\',
              Targets=[
                  {
                      \'Id\': \'string\',
                      \'Port\': 123,
                      \'AvailabilityZone\': \'string\'
                  },
              ]
          )
        :type TargetGroupArn: string
        :param TargetGroupArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the target group.
        
        :type Targets: list
        :param Targets: **[REQUIRED]** 
        
          The targets. If you specified a port override when you registered a target, you must specify both the target ID and the port when you deregister it.
        
          - *(dict) --* 
        
            Information about a target.
        
            - **Id** *(string) --* **[REQUIRED]** 
        
              The ID of the target. If the target type of the target group is ``instance`` , specify an instance ID. If the target type is ``ip`` , specify an IP address.
        
            - **Port** *(integer) --* 
        
              The port on which the target is listening.
        
            - **AvailabilityZone** *(string) --* 
        
              An Availability Zone or ``all`` . This determines whether the target receives traffic from the load balancer nodes in the specified Availability Zone or from all enabled Availability Zones for the load balancer.
        
              This parameter is not supported if the target type of the target group is ``instance`` . If the IP address is in a subnet of the VPC for the target group, the Availability Zone is automatically detected and this parameter is optional. If the IP address is outside the VPC, this parameter is required.
        
              With an Application Load Balancer, if the IP address is outside the VPC for the target group, the only supported value is ``all`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def describe_account_limits(self, Marker: str = None, PageSize: int = None) -> Dict:
        """
        
        For more information, see `Limits for Your Application Load Balancers <http://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-limits.html>`__ in the *Application Load Balancer Guide* or `Limits for Your Network Load Balancers <http://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-limits.html>`__ in the *Network Load Balancers Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeAccountLimits>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_account_limits(
              Marker=\'string\',
              PageSize=123
          )
        :type Marker: string
        :param Marker: 
        
          The marker for the next set of results. (You received this marker from a previous call.)
        
        :type PageSize: integer
        :param PageSize: 
        
          The maximum number of results to return with this call.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Limits\': [
                    {
                        \'Name\': \'string\',
                        \'Max\': \'string\'
                    },
                ],
                \'NextMarker\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Limits** *(list) --* 
        
              Information about the limits.
        
              - *(dict) --* 
        
                Information about an Elastic Load Balancing resource limit for your AWS account.
        
                - **Name** *(string) --* 
        
                  The name of the limit. The possible values are:
        
                  * application-load-balancers 
                   
                  * listeners-per-application-load-balancer 
                   
                  * listeners-per-network-load-balancer 
                   
                  * network-load-balancers 
                   
                  * rules-per-application-load-balancer 
                   
                  * target-groups 
                   
                  * targets-per-application-load-balancer 
                   
                  * targets-per-availability-zone-per-network-load-balancer 
                   
                  * targets-per-network-load-balancer 
                   
                - **Max** *(string) --* 
        
                  The maximum value of the limit.
        
            - **NextMarker** *(string) --* 
        
              The marker to use when requesting the next set of results. If there are no additional results, the string is empty.
        
        """
        pass

    def describe_listener_certificates(self, ListenerArn: str, Marker: str = None, PageSize: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeListenerCertificates>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_listener_certificates(
              ListenerArn=\'string\',
              Marker=\'string\',
              PageSize=123
          )
        :type ListenerArn: string
        :param ListenerArn: **[REQUIRED]** 
        
          The Amazon Resource Names (ARN) of the listener.
        
        :type Marker: string
        :param Marker: 
        
          The marker for the next set of results. (You received this marker from a previous call.)
        
        :type PageSize: integer
        :param PageSize: 
        
          The maximum number of results to return with this call.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Certificates\': [
                    {
                        \'CertificateArn\': \'string\',
                        \'IsDefault\': True|False
                    },
                ],
                \'NextMarker\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Certificates** *(list) --* 
        
              Information about the certificates.
        
              - *(dict) --* 
        
                Information about an SSL server certificate.
        
                - **CertificateArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the certificate.
        
                - **IsDefault** *(boolean) --* 
        
                  Indicates whether the certificate is the default certificate.
        
            - **NextMarker** *(string) --* 
        
              The marker to use when requesting the next set of results. If there are no additional results, the string is empty.
        
        """
        pass

    def describe_listeners(self, LoadBalancerArn: str = None, ListenerArns: List = None, Marker: str = None, PageSize: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeListeners>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_listeners(
              LoadBalancerArn=\'string\',
              ListenerArns=[
                  \'string\',
              ],
              Marker=\'string\',
              PageSize=123
          )
        :type LoadBalancerArn: string
        :param LoadBalancerArn: 
        
          The Amazon Resource Name (ARN) of the load balancer.
        
        :type ListenerArns: list
        :param ListenerArns: 
        
          The Amazon Resource Names (ARN) of the listeners.
        
          - *(string) --* 
        
        :type Marker: string
        :param Marker: 
        
          The marker for the next set of results. (You received this marker from a previous call.)
        
        :type PageSize: integer
        :param PageSize: 
        
          The maximum number of results to return with this call.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Listeners\': [
                    {
                        \'ListenerArn\': \'string\',
                        \'LoadBalancerArn\': \'string\',
                        \'Port\': 123,
                        \'Protocol\': \'HTTP\'|\'HTTPS\'|\'TCP\',
                        \'Certificates\': [
                            {
                                \'CertificateArn\': \'string\',
                                \'IsDefault\': True|False
                            },
                        ],
                        \'SslPolicy\': \'string\',
                        \'DefaultActions\': [
                            {
                                \'Type\': \'forward\'|\'authenticate-oidc\'|\'authenticate-cognito\'|\'redirect\'|\'fixed-response\',
                                \'TargetGroupArn\': \'string\',
                                \'AuthenticateOidcConfig\': {
                                    \'Issuer\': \'string\',
                                    \'AuthorizationEndpoint\': \'string\',
                                    \'TokenEndpoint\': \'string\',
                                    \'UserInfoEndpoint\': \'string\',
                                    \'ClientId\': \'string\',
                                    \'ClientSecret\': \'string\',
                                    \'SessionCookieName\': \'string\',
                                    \'Scope\': \'string\',
                                    \'SessionTimeout\': 123,
                                    \'AuthenticationRequestExtraParams\': {
                                        \'string\': \'string\'
                                    },
                                    \'OnUnauthenticatedRequest\': \'deny\'|\'allow\'|\'authenticate\'
                                },
                                \'AuthenticateCognitoConfig\': {
                                    \'UserPoolArn\': \'string\',
                                    \'UserPoolClientId\': \'string\',
                                    \'UserPoolDomain\': \'string\',
                                    \'SessionCookieName\': \'string\',
                                    \'Scope\': \'string\',
                                    \'SessionTimeout\': 123,
                                    \'AuthenticationRequestExtraParams\': {
                                        \'string\': \'string\'
                                    },
                                    \'OnUnauthenticatedRequest\': \'deny\'|\'allow\'|\'authenticate\'
                                },
                                \'Order\': 123,
                                \'RedirectConfig\': {
                                    \'Protocol\': \'string\',
                                    \'Port\': \'string\',
                                    \'Host\': \'string\',
                                    \'Path\': \'string\',
                                    \'Query\': \'string\',
                                    \'StatusCode\': \'HTTP_301\'|\'HTTP_302\'
                                },
                                \'FixedResponseConfig\': {
                                    \'MessageBody\': \'string\',
                                    \'StatusCode\': \'string\',
                                    \'ContentType\': \'string\'
                                }
                            },
                        ]
                    },
                ],
                \'NextMarker\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Listeners** *(list) --* 
        
              Information about the listeners.
        
              - *(dict) --* 
        
                Information about a listener.
        
                - **ListenerArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the listener.
        
                - **LoadBalancerArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the load balancer.
        
                - **Port** *(integer) --* 
        
                  The port on which the load balancer is listening.
        
                - **Protocol** *(string) --* 
        
                  The protocol for connections from clients to the load balancer.
        
                - **Certificates** *(list) --* 
        
                  The SSL server certificate. You must provide a certificate if the protocol is HTTPS.
        
                  - *(dict) --* 
        
                    Information about an SSL server certificate.
        
                    - **CertificateArn** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the certificate.
        
                    - **IsDefault** *(boolean) --* 
        
                      Indicates whether the certificate is the default certificate.
        
                - **SslPolicy** *(string) --* 
        
                  The security policy that defines which ciphers and protocols are supported. The default is the current predefined security policy.
        
                - **DefaultActions** *(list) --* 
        
                  The default actions for the listener.
        
                  - *(dict) --* 
        
                    Information about an action.
        
                    - **Type** *(string) --* 
        
                      The type of action. Each rule must include exactly one of the following types of actions: ``forward`` , ``fixed-response`` , or ``redirect`` .
        
                    - **TargetGroupArn** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is ``forward`` .
        
                    - **AuthenticateOidcConfig** *(dict) --* 
        
                      [HTTPS listener] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .
        
                      - **Issuer** *(string) --* 
        
                        The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **AuthorizationEndpoint** *(string) --* 
        
                        The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **TokenEndpoint** *(string) --* 
        
                        The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **UserInfoEndpoint** *(string) --* 
        
                        The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **ClientId** *(string) --* 
        
                        The OAuth 2.0 client identifier.
        
                      - **ClientSecret** *(string) --* 
        
                        The OAuth 2.0 client secret.
        
                      - **SessionCookieName** *(string) --* 
        
                        The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.
        
                      - **Scope** *(string) --* 
        
                        The set of user claims to be requested from the IdP. The default is ``openid`` .
        
                        To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.
        
                      - **SessionTimeout** *(integer) --* 
        
                        The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).
        
                      - **AuthenticationRequestExtraParams** *(dict) --* 
        
                        The query parameters (up to 10) to include in the redirect request to the authorization endpoint.
        
                        - *(string) --* 
                          
                          - *(string) --* 
                    
                      - **OnUnauthenticatedRequest** *(string) --* 
        
                        The behavior if the user is not authenticated. The following are possible values:
        
                        * deny- Return an HTTP 401 Unauthorized error. 
                         
                        * allow- Allow the request to be forwarded to the target. 
                         
                        * authenticate- Redirect the request to the IdP authorization endpoint. This is the default value. 
                         
                    - **AuthenticateCognitoConfig** *(dict) --* 
        
                      [HTTPS listener] Information for using Amazon Cognito to authenticate users. Specify only when ``Type`` is ``authenticate-cognito`` .
        
                      - **UserPoolArn** *(string) --* 
        
                        The Amazon Resource Name (ARN) of the Amazon Cognito user pool.
        
                      - **UserPoolClientId** *(string) --* 
        
                        The ID of the Amazon Cognito user pool client.
        
                      - **UserPoolDomain** *(string) --* 
        
                        The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.
        
                      - **SessionCookieName** *(string) --* 
        
                        The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.
        
                      - **Scope** *(string) --* 
        
                        The set of user claims to be requested from the IdP. The default is ``openid`` .
        
                        To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.
        
                      - **SessionTimeout** *(integer) --* 
        
                        The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).
        
                      - **AuthenticationRequestExtraParams** *(dict) --* 
        
                        The query parameters (up to 10) to include in the redirect request to the authorization endpoint.
        
                        - *(string) --* 
                          
                          - *(string) --* 
                    
                      - **OnUnauthenticatedRequest** *(string) --* 
        
                        The behavior if the user is not authenticated. The following are possible values:
        
                        * deny- Return an HTTP 401 Unauthorized error. 
                         
                        * allow- Allow the request to be forwarded to the target. 
                         
                        * authenticate- Redirect the request to the IdP authorization endpoint. This is the default value. 
                         
                    - **Order** *(integer) --* 
        
                      The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first. The final action to be performed must be a ``forward`` or a ``fixed-response`` action.
        
                    - **RedirectConfig** *(dict) --* 
        
                      [Application Load Balancer] Information for creating a redirect action. Specify only when ``Type`` is ``redirect`` .
        
                      - **Protocol** *(string) --* 
        
                        The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.
        
                      - **Port** *(string) --* 
        
                        The port. You can specify a value from 1 to 65535 or #{port}.
        
                      - **Host** *(string) --* 
        
                        The hostname. This component is not percent-encoded. The hostname can contain #{host}.
        
                      - **Path** *(string) --* 
        
                        The absolute path, starting with the leading \"/\". This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}.
        
                      - **Query** *(string) --* 
        
                        The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading \"?\", as it is automatically added. You can specify any of the reserved keywords.
        
                      - **StatusCode** *(string) --* 
        
                        The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).
        
                    - **FixedResponseConfig** *(dict) --* 
        
                      [Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when ``Type`` is ``fixed-response`` .
        
                      - **MessageBody** *(string) --* 
        
                        The message.
        
                      - **StatusCode** *(string) --* 
        
                        The HTTP response code (2XX, 4XX, or 5XX).
        
                      - **ContentType** *(string) --* 
        
                        The content type.
        
                        Valid Values: text/plain | text/css | text/html | application/javascript | application/json
        
            - **NextMarker** *(string) --* 
        
              The marker to use when requesting the next set of results. If there are no additional results, the string is empty.
        
        """
        pass

    def describe_load_balancer_attributes(self, LoadBalancerArn: str) -> Dict:
        """
        
        For more information, see `Load Balancer Attributes <http://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html#load-balancer-attributes>`__ in the *Application Load Balancers Guide* or `Load Balancer Attributes <http://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html#load-balancer-attributes>`__ in the *Network Load Balancers Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancerAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_load_balancer_attributes(
              LoadBalancerArn=\'string\'
          )
        :type LoadBalancerArn: string
        :param LoadBalancerArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the load balancer.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Attributes\': [
                    {
                        \'Key\': \'string\',
                        \'Value\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Attributes** *(list) --* 
        
              Information about the load balancer attributes.
        
              - *(dict) --* 
        
                Information about a load balancer attribute.
        
                - **Key** *(string) --* 
        
                  The name of the attribute.
        
                  The following attributes are supported by both Application Load Balancers and Network Load Balancers:
        
                  * ``deletion_protection.enabled`` - Indicates whether deletion protection is enabled. The value is ``true`` or ``false`` . The default is ``false`` . 
                   
                  The following attributes are supported by only Application Load Balancers:
        
                  * ``access_logs.s3.enabled`` - Indicates whether access logs are enabled. The value is ``true`` or ``false`` . The default is ``false`` . 
                   
                  * ``access_logs.s3.bucket`` - The name of the S3 bucket for the access logs. This attribute is required if access logs are enabled. The bucket must exist in the same region as the load balancer and have a bucket policy that grants Elastic Load Balancing permissions to write to the bucket. 
                   
                  * ``access_logs.s3.prefix`` - The prefix for the location in the S3 bucket for the access logs. 
                   
                  * ``idle_timeout.timeout_seconds`` - The idle timeout value, in seconds. The valid range is 1-4000 seconds. The default is 60 seconds. 
                   
                  * ``routing.http2.enabled`` - Indicates whether HTTP/2 is enabled. The value is ``true`` or ``false`` . The default is ``true`` . 
                   
                  The following attributes are supported by only Network Load Balancers:
        
                  * ``load_balancing.cross_zone.enabled`` - Indicates whether cross-zone load balancing is enabled. The value is ``true`` or ``false`` . The default is ``false`` . 
                   
                - **Value** *(string) --* 
        
                  The value of the attribute.
        
        """
        pass

    def describe_load_balancers(self, LoadBalancerArns: List = None, Names: List = None, Marker: str = None, PageSize: int = None) -> Dict:
        """
        
        To describe the listeners for a load balancer, use  DescribeListeners . To describe the attributes for a load balancer, use  DescribeLoadBalancerAttributes .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancers>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_load_balancers(
              LoadBalancerArns=[
                  \'string\',
              ],
              Names=[
                  \'string\',
              ],
              Marker=\'string\',
              PageSize=123
          )
        :type LoadBalancerArns: list
        :param LoadBalancerArns: 
        
          The Amazon Resource Names (ARN) of the load balancers. You can specify up to 20 load balancers in a single call.
        
          - *(string) --* 
        
        :type Names: list
        :param Names: 
        
          The names of the load balancers.
        
          - *(string) --* 
        
        :type Marker: string
        :param Marker: 
        
          The marker for the next set of results. (You received this marker from a previous call.)
        
        :type PageSize: integer
        :param PageSize: 
        
          The maximum number of results to return with this call.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'LoadBalancers\': [
                    {
                        \'LoadBalancerArn\': \'string\',
                        \'DNSName\': \'string\',
                        \'CanonicalHostedZoneId\': \'string\',
                        \'CreatedTime\': datetime(2015, 1, 1),
                        \'LoadBalancerName\': \'string\',
                        \'Scheme\': \'internet-facing\'|\'internal\',
                        \'VpcId\': \'string\',
                        \'State\': {
                            \'Code\': \'active\'|\'provisioning\'|\'active_impaired\'|\'failed\',
                            \'Reason\': \'string\'
                        },
                        \'Type\': \'application\'|\'network\',
                        \'AvailabilityZones\': [
                            {
                                \'ZoneName\': \'string\',
                                \'SubnetId\': \'string\',
                                \'LoadBalancerAddresses\': [
                                    {
                                        \'IpAddress\': \'string\',
                                        \'AllocationId\': \'string\'
                                    },
                                ]
                            },
                        ],
                        \'SecurityGroups\': [
                            \'string\',
                        ],
                        \'IpAddressType\': \'ipv4\'|\'dualstack\'
                    },
                ],
                \'NextMarker\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **LoadBalancers** *(list) --* 
        
              Information about the load balancers.
        
              - *(dict) --* 
        
                Information about a load balancer.
        
                - **LoadBalancerArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the load balancer.
        
                - **DNSName** *(string) --* 
        
                  The public DNS name of the load balancer.
        
                - **CanonicalHostedZoneId** *(string) --* 
        
                  The ID of the Amazon Route 53 hosted zone associated with the load balancer.
        
                - **CreatedTime** *(datetime) --* 
        
                  The date and time the load balancer was created.
        
                - **LoadBalancerName** *(string) --* 
        
                  The name of the load balancer.
        
                - **Scheme** *(string) --* 
        
                  The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of an Internet-facing load balancer is publicly resolvable to the public IP addresses of the nodes. Therefore, Internet-facing load balancers can route requests from clients over the internet.
        
                  The nodes of an internal load balancer have only private IP addresses. The DNS name of an internal load balancer is publicly resolvable to the private IP addresses of the nodes. Therefore, internal load balancers can only route requests from clients with access to the VPC for the load balancer.
        
                - **VpcId** *(string) --* 
        
                  The ID of the VPC for the load balancer.
        
                - **State** *(dict) --* 
        
                  The state of the load balancer.
        
                  - **Code** *(string) --* 
        
                    The state code. The initial state of the load balancer is ``provisioning`` . After the load balancer is fully set up and ready to route traffic, its state is ``active`` . If the load balancer could not be set up, its state is ``failed`` .
        
                  - **Reason** *(string) --* 
        
                    A description of the state.
        
                - **Type** *(string) --* 
        
                  The type of load balancer.
        
                - **AvailabilityZones** *(list) --* 
        
                  The Availability Zones for the load balancer.
        
                  - *(dict) --* 
        
                    Information about an Availability Zone.
        
                    - **ZoneName** *(string) --* 
        
                      The name of the Availability Zone.
        
                    - **SubnetId** *(string) --* 
        
                      The ID of the subnet.
        
                    - **LoadBalancerAddresses** *(list) --* 
        
                      [Network Load Balancers] The static IP address.
        
                      - *(dict) --* 
        
                        Information about a static IP address for a load balancer.
        
                        - **IpAddress** *(string) --* 
        
                          The static IP address.
        
                        - **AllocationId** *(string) --* 
        
                          [Network Load Balancers] The allocation ID of the Elastic IP address.
        
                - **SecurityGroups** *(list) --* 
        
                  The IDs of the security groups for the load balancer.
        
                  - *(string) --* 
              
                - **IpAddressType** *(string) --* 
        
                  The type of IP addresses used by the subnets for your load balancer. The possible values are ``ipv4`` (for IPv4 addresses) and ``dualstack`` (for IPv4 and IPv6 addresses).
        
            - **NextMarker** *(string) --* 
        
              The marker to use when requesting the next set of results. If there are no additional results, the string is empty.
        
        """
        pass

    def describe_rules(self, ListenerArn: str = None, RuleArns: List = None, Marker: str = None, PageSize: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeRules>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_rules(
              ListenerArn=\'string\',
              RuleArns=[
                  \'string\',
              ],
              Marker=\'string\',
              PageSize=123
          )
        :type ListenerArn: string
        :param ListenerArn: 
        
          The Amazon Resource Name (ARN) of the listener.
        
        :type RuleArns: list
        :param RuleArns: 
        
          The Amazon Resource Names (ARN) of the rules.
        
          - *(string) --* 
        
        :type Marker: string
        :param Marker: 
        
          The marker for the next set of results. (You received this marker from a previous call.)
        
        :type PageSize: integer
        :param PageSize: 
        
          The maximum number of results to return with this call.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Rules\': [
                    {
                        \'RuleArn\': \'string\',
                        \'Priority\': \'string\',
                        \'Conditions\': [
                            {
                                \'Field\': \'string\',
                                \'Values\': [
                                    \'string\',
                                ]
                            },
                        ],
                        \'Actions\': [
                            {
                                \'Type\': \'forward\'|\'authenticate-oidc\'|\'authenticate-cognito\'|\'redirect\'|\'fixed-response\',
                                \'TargetGroupArn\': \'string\',
                                \'AuthenticateOidcConfig\': {
                                    \'Issuer\': \'string\',
                                    \'AuthorizationEndpoint\': \'string\',
                                    \'TokenEndpoint\': \'string\',
                                    \'UserInfoEndpoint\': \'string\',
                                    \'ClientId\': \'string\',
                                    \'ClientSecret\': \'string\',
                                    \'SessionCookieName\': \'string\',
                                    \'Scope\': \'string\',
                                    \'SessionTimeout\': 123,
                                    \'AuthenticationRequestExtraParams\': {
                                        \'string\': \'string\'
                                    },
                                    \'OnUnauthenticatedRequest\': \'deny\'|\'allow\'|\'authenticate\'
                                },
                                \'AuthenticateCognitoConfig\': {
                                    \'UserPoolArn\': \'string\',
                                    \'UserPoolClientId\': \'string\',
                                    \'UserPoolDomain\': \'string\',
                                    \'SessionCookieName\': \'string\',
                                    \'Scope\': \'string\',
                                    \'SessionTimeout\': 123,
                                    \'AuthenticationRequestExtraParams\': {
                                        \'string\': \'string\'
                                    },
                                    \'OnUnauthenticatedRequest\': \'deny\'|\'allow\'|\'authenticate\'
                                },
                                \'Order\': 123,
                                \'RedirectConfig\': {
                                    \'Protocol\': \'string\',
                                    \'Port\': \'string\',
                                    \'Host\': \'string\',
                                    \'Path\': \'string\',
                                    \'Query\': \'string\',
                                    \'StatusCode\': \'HTTP_301\'|\'HTTP_302\'
                                },
                                \'FixedResponseConfig\': {
                                    \'MessageBody\': \'string\',
                                    \'StatusCode\': \'string\',
                                    \'ContentType\': \'string\'
                                }
                            },
                        ],
                        \'IsDefault\': True|False
                    },
                ],
                \'NextMarker\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Rules** *(list) --* 
        
              Information about the rules.
        
              - *(dict) --* 
        
                Information about a rule.
        
                - **RuleArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the rule.
        
                - **Priority** *(string) --* 
        
                  The priority.
        
                - **Conditions** *(list) --* 
        
                  The conditions.
        
                  - *(dict) --* 
        
                    Information about a condition for a rule.
        
                    - **Field** *(string) --* 
        
                      The name of the field. The possible values are ``host-header`` and ``path-pattern`` .
        
                    - **Values** *(list) --* 
        
                      The condition value.
        
                      If the field name is ``host-header`` , you can specify a single host name (for example, my.example.com). A host name is case insensitive, can be up to 128 characters in length, and can contain any of the following characters. You can include up to three wildcard characters.
        
                      * A-Z, a-z, 0-9 
                       
                      * - . 
                       
                      * * (matches 0 or more characters) 
                       
                      * ? (matches exactly 1 character) 
                       
                      If the field name is ``path-pattern`` , you can specify a single path pattern (for example, /img/*). A path pattern is case-sensitive, can be up to 128 characters in length, and can contain any of the following characters. You can include up to three wildcard characters.
        
                      * A-Z, a-z, 0-9 
                       
                      * _ - . $ / ~ \" \' @ : + 
                       
                      * & (using &amp;) 
                       
                      * * (matches 0 or more characters) 
                       
                      * ? (matches exactly 1 character) 
                       
                      - *(string) --* 
                  
                - **Actions** *(list) --* 
        
                  The actions.
        
                  - *(dict) --* 
        
                    Information about an action.
        
                    - **Type** *(string) --* 
        
                      The type of action. Each rule must include exactly one of the following types of actions: ``forward`` , ``fixed-response`` , or ``redirect`` .
        
                    - **TargetGroupArn** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is ``forward`` .
        
                    - **AuthenticateOidcConfig** *(dict) --* 
        
                      [HTTPS listener] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .
        
                      - **Issuer** *(string) --* 
        
                        The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **AuthorizationEndpoint** *(string) --* 
        
                        The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **TokenEndpoint** *(string) --* 
        
                        The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **UserInfoEndpoint** *(string) --* 
        
                        The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **ClientId** *(string) --* 
        
                        The OAuth 2.0 client identifier.
        
                      - **ClientSecret** *(string) --* 
        
                        The OAuth 2.0 client secret.
        
                      - **SessionCookieName** *(string) --* 
        
                        The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.
        
                      - **Scope** *(string) --* 
        
                        The set of user claims to be requested from the IdP. The default is ``openid`` .
        
                        To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.
        
                      - **SessionTimeout** *(integer) --* 
        
                        The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).
        
                      - **AuthenticationRequestExtraParams** *(dict) --* 
        
                        The query parameters (up to 10) to include in the redirect request to the authorization endpoint.
        
                        - *(string) --* 
                          
                          - *(string) --* 
                    
                      - **OnUnauthenticatedRequest** *(string) --* 
        
                        The behavior if the user is not authenticated. The following are possible values:
        
                        * deny- Return an HTTP 401 Unauthorized error. 
                         
                        * allow- Allow the request to be forwarded to the target. 
                         
                        * authenticate- Redirect the request to the IdP authorization endpoint. This is the default value. 
                         
                    - **AuthenticateCognitoConfig** *(dict) --* 
        
                      [HTTPS listener] Information for using Amazon Cognito to authenticate users. Specify only when ``Type`` is ``authenticate-cognito`` .
        
                      - **UserPoolArn** *(string) --* 
        
                        The Amazon Resource Name (ARN) of the Amazon Cognito user pool.
        
                      - **UserPoolClientId** *(string) --* 
        
                        The ID of the Amazon Cognito user pool client.
        
                      - **UserPoolDomain** *(string) --* 
        
                        The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.
        
                      - **SessionCookieName** *(string) --* 
        
                        The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.
        
                      - **Scope** *(string) --* 
        
                        The set of user claims to be requested from the IdP. The default is ``openid`` .
        
                        To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.
        
                      - **SessionTimeout** *(integer) --* 
        
                        The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).
        
                      - **AuthenticationRequestExtraParams** *(dict) --* 
        
                        The query parameters (up to 10) to include in the redirect request to the authorization endpoint.
        
                        - *(string) --* 
                          
                          - *(string) --* 
                    
                      - **OnUnauthenticatedRequest** *(string) --* 
        
                        The behavior if the user is not authenticated. The following are possible values:
        
                        * deny- Return an HTTP 401 Unauthorized error. 
                         
                        * allow- Allow the request to be forwarded to the target. 
                         
                        * authenticate- Redirect the request to the IdP authorization endpoint. This is the default value. 
                         
                    - **Order** *(integer) --* 
        
                      The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first. The final action to be performed must be a ``forward`` or a ``fixed-response`` action.
        
                    - **RedirectConfig** *(dict) --* 
        
                      [Application Load Balancer] Information for creating a redirect action. Specify only when ``Type`` is ``redirect`` .
        
                      - **Protocol** *(string) --* 
        
                        The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.
        
                      - **Port** *(string) --* 
        
                        The port. You can specify a value from 1 to 65535 or #{port}.
        
                      - **Host** *(string) --* 
        
                        The hostname. This component is not percent-encoded. The hostname can contain #{host}.
        
                      - **Path** *(string) --* 
        
                        The absolute path, starting with the leading \"/\". This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}.
        
                      - **Query** *(string) --* 
        
                        The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading \"?\", as it is automatically added. You can specify any of the reserved keywords.
        
                      - **StatusCode** *(string) --* 
        
                        The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).
        
                    - **FixedResponseConfig** *(dict) --* 
        
                      [Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when ``Type`` is ``fixed-response`` .
        
                      - **MessageBody** *(string) --* 
        
                        The message.
        
                      - **StatusCode** *(string) --* 
        
                        The HTTP response code (2XX, 4XX, or 5XX).
        
                      - **ContentType** *(string) --* 
        
                        The content type.
        
                        Valid Values: text/plain | text/css | text/html | application/javascript | application/json
        
                - **IsDefault** *(boolean) --* 
        
                  Indicates whether this is the default rule.
        
            - **NextMarker** *(string) --* 
        
              The marker to use when requesting the next set of results. If there are no additional results, the string is empty.
        
        """
        pass

    def describe_ssl_policies(self, Names: List = None, Marker: str = None, PageSize: int = None) -> Dict:
        """
        
        For more information, see `Security Policies <http://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#describe-ssl-policies>`__ in the *Application Load Balancers Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeSSLPolicies>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_ssl_policies(
              Names=[
                  \'string\',
              ],
              Marker=\'string\',
              PageSize=123
          )
        :type Names: list
        :param Names: 
        
          The names of the policies.
        
          - *(string) --* 
        
        :type Marker: string
        :param Marker: 
        
          The marker for the next set of results. (You received this marker from a previous call.)
        
        :type PageSize: integer
        :param PageSize: 
        
          The maximum number of results to return with this call.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SslPolicies\': [
                    {
                        \'SslProtocols\': [
                            \'string\',
                        ],
                        \'Ciphers\': [
                            {
                                \'Name\': \'string\',
                                \'Priority\': 123
                            },
                        ],
                        \'Name\': \'string\'
                    },
                ],
                \'NextMarker\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SslPolicies** *(list) --* 
        
              Information about the policies.
        
              - *(dict) --* 
        
                Information about a policy used for SSL negotiation.
        
                - **SslProtocols** *(list) --* 
        
                  The protocols.
        
                  - *(string) --* 
              
                - **Ciphers** *(list) --* 
        
                  The ciphers.
        
                  - *(dict) --* 
        
                    Information about a cipher used in a policy.
        
                    - **Name** *(string) --* 
        
                      The name of the cipher.
        
                    - **Priority** *(integer) --* 
        
                      The priority of the cipher.
        
                - **Name** *(string) --* 
        
                  The name of the policy.
        
            - **NextMarker** *(string) --* 
        
              The marker to use when requesting the next set of results. If there are no additional results, the string is empty.
        
        """
        pass

    def describe_tags(self, ResourceArns: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_tags(
              ResourceArns=[
                  \'string\',
              ]
          )
        :type ResourceArns: list
        :param ResourceArns: **[REQUIRED]** 
        
          The Amazon Resource Names (ARN) of the resources.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TagDescriptions\': [
                    {
                        \'ResourceArn\': \'string\',
                        \'Tags\': [
                            {
                                \'Key\': \'string\',
                                \'Value\': \'string\'
                            },
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TagDescriptions** *(list) --* 
        
              Information about the tags.
        
              - *(dict) --* 
        
                The tags associated with a resource.
        
                - **ResourceArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the resource.
        
                - **Tags** *(list) --* 
        
                  Information about the tags.
        
                  - *(dict) --* 
        
                    Information about a tag.
        
                    - **Key** *(string) --* 
        
                      The key of the tag.
        
                    - **Value** *(string) --* 
        
                      The value of the tag.
        
        """
        pass

    def describe_target_group_attributes(self, TargetGroupArn: str) -> Dict:
        """
        
        For more information, see `Target Group Attributes <http://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html#target-group-attributes>`__ in the *Application Load Balancers Guide* or `Target Group Attributes <http://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#target-group-attributes>`__ in the *Network Load Balancers Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeTargetGroupAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_target_group_attributes(
              TargetGroupArn=\'string\'
          )
        :type TargetGroupArn: string
        :param TargetGroupArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the target group.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Attributes\': [
                    {
                        \'Key\': \'string\',
                        \'Value\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Attributes** *(list) --* 
        
              Information about the target group attributes
        
              - *(dict) --* 
        
                Information about a target group attribute.
        
                - **Key** *(string) --* 
        
                  The name of the attribute.
        
                  The following attributes are supported by both Application Load Balancers and Network Load Balancers:
        
                  * ``deregistration_delay.timeout_seconds`` - The amount of time, in seconds, for Elastic Load Balancing to wait before changing the state of a deregistering target from ``draining`` to ``unused`` . The range is 0-3600 seconds. The default value is 300 seconds. 
                   
                  The following attributes are supported by only Application Load Balancers:
        
                  * ``slow_start.duration_seconds`` - The time period, in seconds, during which a newly registered target receives a linearly increasing share of the traffic to the target group. After this time period ends, the target receives its full share of traffic. The range is 30-900 seconds (15 minutes). Slow start mode is disabled by default. 
                   
                  * ``stickiness.enabled`` - Indicates whether sticky sessions are enabled. The value is ``true`` or ``false`` . The default is ``false`` . 
                   
                  * ``stickiness.type`` - The type of sticky sessions. The possible value is ``lb_cookie`` . 
                   
                  * ``stickiness.lb_cookie.duration_seconds`` - The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). The default value is 1 day (86400 seconds). 
                   
                  The following attributes are supported by only Network Load Balancers:
        
                  * ``proxy_protocol_v2.enabled`` - Indicates whether Proxy Protocol version 2 is enabled. The value is ``true`` or ``false`` . The default is ``false`` . 
                   
                - **Value** *(string) --* 
        
                  The value of the attribute.
        
        """
        pass

    def describe_target_groups(self, LoadBalancerArn: str = None, TargetGroupArns: List = None, Names: List = None, Marker: str = None, PageSize: int = None) -> Dict:
        """
        
        To describe the targets for a target group, use  DescribeTargetHealth . To describe the attributes of a target group, use  DescribeTargetGroupAttributes .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeTargetGroups>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_target_groups(
              LoadBalancerArn=\'string\',
              TargetGroupArns=[
                  \'string\',
              ],
              Names=[
                  \'string\',
              ],
              Marker=\'string\',
              PageSize=123
          )
        :type LoadBalancerArn: string
        :param LoadBalancerArn: 
        
          The Amazon Resource Name (ARN) of the load balancer.
        
        :type TargetGroupArns: list
        :param TargetGroupArns: 
        
          The Amazon Resource Names (ARN) of the target groups.
        
          - *(string) --* 
        
        :type Names: list
        :param Names: 
        
          The names of the target groups.
        
          - *(string) --* 
        
        :type Marker: string
        :param Marker: 
        
          The marker for the next set of results. (You received this marker from a previous call.)
        
        :type PageSize: integer
        :param PageSize: 
        
          The maximum number of results to return with this call.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TargetGroups\': [
                    {
                        \'TargetGroupArn\': \'string\',
                        \'TargetGroupName\': \'string\',
                        \'Protocol\': \'HTTP\'|\'HTTPS\'|\'TCP\',
                        \'Port\': 123,
                        \'VpcId\': \'string\',
                        \'HealthCheckProtocol\': \'HTTP\'|\'HTTPS\'|\'TCP\',
                        \'HealthCheckPort\': \'string\',
                        \'HealthCheckIntervalSeconds\': 123,
                        \'HealthCheckTimeoutSeconds\': 123,
                        \'HealthyThresholdCount\': 123,
                        \'UnhealthyThresholdCount\': 123,
                        \'HealthCheckPath\': \'string\',
                        \'Matcher\': {
                            \'HttpCode\': \'string\'
                        },
                        \'LoadBalancerArns\': [
                            \'string\',
                        ],
                        \'TargetType\': \'instance\'|\'ip\'
                    },
                ],
                \'NextMarker\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TargetGroups** *(list) --* 
        
              Information about the target groups.
        
              - *(dict) --* 
        
                Information about a target group.
        
                - **TargetGroupArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the target group.
        
                - **TargetGroupName** *(string) --* 
        
                  The name of the target group.
        
                - **Protocol** *(string) --* 
        
                  The protocol to use for routing traffic to the targets.
        
                - **Port** *(integer) --* 
        
                  The port on which the targets are listening.
        
                - **VpcId** *(string) --* 
        
                  The ID of the VPC for the targets.
        
                - **HealthCheckProtocol** *(string) --* 
        
                  The protocol to use to connect with the target.
        
                - **HealthCheckPort** *(string) --* 
        
                  The port to use to connect with the target.
        
                - **HealthCheckIntervalSeconds** *(integer) --* 
        
                  The approximate amount of time, in seconds, between health checks of an individual target.
        
                - **HealthCheckTimeoutSeconds** *(integer) --* 
        
                  The amount of time, in seconds, during which no response means a failed health check.
        
                - **HealthyThresholdCount** *(integer) --* 
        
                  The number of consecutive health checks successes required before considering an unhealthy target healthy.
        
                - **UnhealthyThresholdCount** *(integer) --* 
        
                  The number of consecutive health check failures required before considering the target unhealthy.
        
                - **HealthCheckPath** *(string) --* 
        
                  The destination for the health check request.
        
                - **Matcher** *(dict) --* 
        
                  The HTTP codes to use when checking for a successful response from a target.
        
                  - **HttpCode** *(string) --* 
        
                    The HTTP codes.
        
                    For Application Load Balancers, you can specify values between 200 and 499, and the default value is 200. You can specify multiple values (for example, \"200,202\") or a range of values (for example, \"200-299\").
        
                    For Network Load Balancers, this is 200–399.
        
                - **LoadBalancerArns** *(list) --* 
        
                  The Amazon Resource Names (ARN) of the load balancers that route traffic to this target group.
        
                  - *(string) --* 
              
                - **TargetType** *(string) --* 
        
                  The type of target that you must specify when registering targets with this target group. The possible values are ``instance`` (targets are specified by instance ID) or ``ip`` (targets are specified by IP address).
        
            - **NextMarker** *(string) --* 
        
              The marker to use when requesting the next set of results. If there are no additional results, the string is empty.
        
        """
        pass

    def describe_target_health(self, TargetGroupArn: str, Targets: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeTargetHealth>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_target_health(
              TargetGroupArn=\'string\',
              Targets=[
                  {
                      \'Id\': \'string\',
                      \'Port\': 123,
                      \'AvailabilityZone\': \'string\'
                  },
              ]
          )
        :type TargetGroupArn: string
        :param TargetGroupArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the target group.
        
        :type Targets: list
        :param Targets: 
        
          The targets.
        
          - *(dict) --* 
        
            Information about a target.
        
            - **Id** *(string) --* **[REQUIRED]** 
        
              The ID of the target. If the target type of the target group is ``instance`` , specify an instance ID. If the target type is ``ip`` , specify an IP address.
        
            - **Port** *(integer) --* 
        
              The port on which the target is listening.
        
            - **AvailabilityZone** *(string) --* 
        
              An Availability Zone or ``all`` . This determines whether the target receives traffic from the load balancer nodes in the specified Availability Zone or from all enabled Availability Zones for the load balancer.
        
              This parameter is not supported if the target type of the target group is ``instance`` . If the IP address is in a subnet of the VPC for the target group, the Availability Zone is automatically detected and this parameter is optional. If the IP address is outside the VPC, this parameter is required.
        
              With an Application Load Balancer, if the IP address is outside the VPC for the target group, the only supported value is ``all`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TargetHealthDescriptions\': [
                    {
                        \'Target\': {
                            \'Id\': \'string\',
                            \'Port\': 123,
                            \'AvailabilityZone\': \'string\'
                        },
                        \'HealthCheckPort\': \'string\',
                        \'TargetHealth\': {
                            \'State\': \'initial\'|\'healthy\'|\'unhealthy\'|\'unused\'|\'draining\'|\'unavailable\',
                            \'Reason\': \'Elb.RegistrationInProgress\'|\'Elb.InitialHealthChecking\'|\'Target.ResponseCodeMismatch\'|\'Target.Timeout\'|\'Target.FailedHealthChecks\'|\'Target.NotRegistered\'|\'Target.NotInUse\'|\'Target.DeregistrationInProgress\'|\'Target.InvalidState\'|\'Target.IpUnusable\'|\'Elb.InternalError\',
                            \'Description\': \'string\'
                        }
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TargetHealthDescriptions** *(list) --* 
        
              Information about the health of the targets.
        
              - *(dict) --* 
        
                Information about the health of a target.
        
                - **Target** *(dict) --* 
        
                  The description of the target.
        
                  - **Id** *(string) --* 
        
                    The ID of the target. If the target type of the target group is ``instance`` , specify an instance ID. If the target type is ``ip`` , specify an IP address.
        
                  - **Port** *(integer) --* 
        
                    The port on which the target is listening.
        
                  - **AvailabilityZone** *(string) --* 
        
                    An Availability Zone or ``all`` . This determines whether the target receives traffic from the load balancer nodes in the specified Availability Zone or from all enabled Availability Zones for the load balancer.
        
                    This parameter is not supported if the target type of the target group is ``instance`` . If the IP address is in a subnet of the VPC for the target group, the Availability Zone is automatically detected and this parameter is optional. If the IP address is outside the VPC, this parameter is required.
        
                    With an Application Load Balancer, if the IP address is outside the VPC for the target group, the only supported value is ``all`` .
        
                - **HealthCheckPort** *(string) --* 
        
                  The port to use to connect with the target.
        
                - **TargetHealth** *(dict) --* 
        
                  The health information for the target.
        
                  - **State** *(string) --* 
        
                    The state of the target.
        
                  - **Reason** *(string) --* 
        
                    The reason code. If the target state is ``healthy`` , a reason code is not provided.
        
                    If the target state is ``initial`` , the reason code can be one of the following values:
        
                    * ``Elb.RegistrationInProgress`` - The target is in the process of being registered with the load balancer. 
                     
                    * ``Elb.InitialHealthChecking`` - The load balancer is still sending the target the minimum number of health checks required to determine its health status. 
                     
                    If the target state is ``unhealthy`` , the reason code can be one of the following values:
        
                    * ``Target.ResponseCodeMismatch`` - The health checks did not return an expected HTTP code. 
                     
                    * ``Target.Timeout`` - The health check requests timed out. 
                     
                    * ``Target.FailedHealthChecks`` - The health checks failed because the connection to the target timed out, the target response was malformed, or the target failed the health check for an unknown reason. 
                     
                    * ``Elb.InternalError`` - The health checks failed due to an internal error. 
                     
                    If the target state is ``unused`` , the reason code can be one of the following values:
        
                    * ``Target.NotRegistered`` - The target is not registered with the target group. 
                     
                    * ``Target.NotInUse`` - The target group is not used by any load balancer or the target is in an Availability Zone that is not enabled for its load balancer. 
                     
                    * ``Target.IpUnusable`` - The target IP address is reserved for use by a load balancer. 
                     
                    * ``Target.InvalidState`` - The target is in the stopped or terminated state. 
                     
                    If the target state is ``draining`` , the reason code can be the following value:
        
                    * ``Target.DeregistrationInProgress`` - The target is in the process of being deregistered and the deregistration delay period has not expired. 
                     
                  - **Description** *(string) --* 
        
                    A description of the target health that provides additional details. If the state is ``healthy`` , a description is not provided.
        
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
        """
        
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

    def get_paginator(self, operation_name: str = None) -> Paginator:
        """
        
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
        
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass

    def modify_listener(self, ListenerArn: str, Port: int = None, Protocol: str = None, SslPolicy: str = None, Certificates: List = None, DefaultActions: List = None) -> Dict:
        """
        
        Any properties that you do not specify retain their current values. However, changing the protocol from HTTPS to HTTP removes the security policy and SSL certificate properties. If you change the protocol from HTTP to HTTPS, you must add the security policy and server certificate.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/ModifyListener>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_listener(
              ListenerArn=\'string\',
              Port=123,
              Protocol=\'HTTP\'|\'HTTPS\'|\'TCP\',
              SslPolicy=\'string\',
              Certificates=[
                  {
                      \'CertificateArn\': \'string\',
                      \'IsDefault\': True|False
                  },
              ],
              DefaultActions=[
                  {
                      \'Type\': \'forward\'|\'authenticate-oidc\'|\'authenticate-cognito\'|\'redirect\'|\'fixed-response\',
                      \'TargetGroupArn\': \'string\',
                      \'AuthenticateOidcConfig\': {
                          \'Issuer\': \'string\',
                          \'AuthorizationEndpoint\': \'string\',
                          \'TokenEndpoint\': \'string\',
                          \'UserInfoEndpoint\': \'string\',
                          \'ClientId\': \'string\',
                          \'ClientSecret\': \'string\',
                          \'SessionCookieName\': \'string\',
                          \'Scope\': \'string\',
                          \'SessionTimeout\': 123,
                          \'AuthenticationRequestExtraParams\': {
                              \'string\': \'string\'
                          },
                          \'OnUnauthenticatedRequest\': \'deny\'|\'allow\'|\'authenticate\'
                      },
                      \'AuthenticateCognitoConfig\': {
                          \'UserPoolArn\': \'string\',
                          \'UserPoolClientId\': \'string\',
                          \'UserPoolDomain\': \'string\',
                          \'SessionCookieName\': \'string\',
                          \'Scope\': \'string\',
                          \'SessionTimeout\': 123,
                          \'AuthenticationRequestExtraParams\': {
                              \'string\': \'string\'
                          },
                          \'OnUnauthenticatedRequest\': \'deny\'|\'allow\'|\'authenticate\'
                      },
                      \'Order\': 123,
                      \'RedirectConfig\': {
                          \'Protocol\': \'string\',
                          \'Port\': \'string\',
                          \'Host\': \'string\',
                          \'Path\': \'string\',
                          \'Query\': \'string\',
                          \'StatusCode\': \'HTTP_301\'|\'HTTP_302\'
                      },
                      \'FixedResponseConfig\': {
                          \'MessageBody\': \'string\',
                          \'StatusCode\': \'string\',
                          \'ContentType\': \'string\'
                      }
                  },
              ]
          )
        :type ListenerArn: string
        :param ListenerArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the listener.
        
        :type Port: integer
        :param Port: 
        
          The port for connections from clients to the load balancer.
        
        :type Protocol: string
        :param Protocol: 
        
          The protocol for connections from clients to the load balancer. Application Load Balancers support HTTP and HTTPS and Network Load Balancers support TCP.
        
        :type SslPolicy: string
        :param SslPolicy: 
        
          [HTTPS listeners] The security policy that defines which protocols and ciphers are supported. For more information, see `Security Policies <http://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#describe-ssl-policies>`__ in the *Application Load Balancers Guide* .
        
        :type Certificates: list
        :param Certificates: 
        
          [HTTPS listeners] The default SSL server certificate. You must provide exactly one default certificate. To create a certificate list, use  AddListenerCertificates .
        
          - *(dict) --* 
        
            Information about an SSL server certificate.
        
            - **CertificateArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the certificate.
        
            - **IsDefault** *(boolean) --* 
        
              Indicates whether the certificate is the default certificate.
        
        :type DefaultActions: list
        :param DefaultActions: 
        
          The actions for the default rule. The rule must include one forward action or one or more fixed-response actions.
        
          If the action type is ``forward`` , you can specify a single target group. The protocol of the target group must be HTTP or HTTPS for an Application Load Balancer or TCP for a Network Load Balancer.
        
          [HTTPS listener] If the action type is ``authenticate-oidc`` , you can use an identity provider that is OpenID Connect (OIDC) compliant to authenticate users as they access your application.
        
          [HTTPS listener] If the action type is ``authenticate-cognito`` , you can use Amazon Cognito to authenticate users as they access your application.
        
          [Application Load Balancer] If the action type is ``redirect`` , you can redirect HTTP and HTTPS requests.
        
          [Application Load Balancer] If the action type is ``fixed-response`` , you can return a custom HTTP response.
        
          - *(dict) --* 
        
            Information about an action.
        
            - **Type** *(string) --* **[REQUIRED]** 
        
              The type of action. Each rule must include exactly one of the following types of actions: ``forward`` , ``fixed-response`` , or ``redirect`` .
        
            - **TargetGroupArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is ``forward`` .
        
            - **AuthenticateOidcConfig** *(dict) --* 
        
              [HTTPS listener] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .
        
              - **Issuer** *(string) --* **[REQUIRED]** 
        
                The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
              - **AuthorizationEndpoint** *(string) --* **[REQUIRED]** 
        
                The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
              - **TokenEndpoint** *(string) --* **[REQUIRED]** 
        
                The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
              - **UserInfoEndpoint** *(string) --* **[REQUIRED]** 
        
                The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
              - **ClientId** *(string) --* **[REQUIRED]** 
        
                The OAuth 2.0 client identifier.
        
              - **ClientSecret** *(string) --* **[REQUIRED]** 
        
                The OAuth 2.0 client secret.
        
              - **SessionCookieName** *(string) --* 
        
                The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.
        
              - **Scope** *(string) --* 
        
                The set of user claims to be requested from the IdP. The default is ``openid`` .
        
                To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.
        
              - **SessionTimeout** *(integer) --* 
        
                The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).
        
              - **AuthenticationRequestExtraParams** *(dict) --* 
        
                The query parameters (up to 10) to include in the redirect request to the authorization endpoint.
        
                - *(string) --* 
        
                  - *(string) --* 
        
              - **OnUnauthenticatedRequest** *(string) --* 
        
                The behavior if the user is not authenticated. The following are possible values:
        
                * deny- Return an HTTP 401 Unauthorized error. 
                 
                * allow- Allow the request to be forwarded to the target. 
                 
                * authenticate- Redirect the request to the IdP authorization endpoint. This is the default value. 
                 
            - **AuthenticateCognitoConfig** *(dict) --* 
        
              [HTTPS listener] Information for using Amazon Cognito to authenticate users. Specify only when ``Type`` is ``authenticate-cognito`` .
        
              - **UserPoolArn** *(string) --* **[REQUIRED]** 
        
                The Amazon Resource Name (ARN) of the Amazon Cognito user pool.
        
              - **UserPoolClientId** *(string) --* **[REQUIRED]** 
        
                The ID of the Amazon Cognito user pool client.
        
              - **UserPoolDomain** *(string) --* **[REQUIRED]** 
        
                The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.
        
              - **SessionCookieName** *(string) --* 
        
                The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.
        
              - **Scope** *(string) --* 
        
                The set of user claims to be requested from the IdP. The default is ``openid`` .
        
                To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.
        
              - **SessionTimeout** *(integer) --* 
        
                The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).
        
              - **AuthenticationRequestExtraParams** *(dict) --* 
        
                The query parameters (up to 10) to include in the redirect request to the authorization endpoint.
        
                - *(string) --* 
        
                  - *(string) --* 
        
              - **OnUnauthenticatedRequest** *(string) --* 
        
                The behavior if the user is not authenticated. The following are possible values:
        
                * deny- Return an HTTP 401 Unauthorized error. 
                 
                * allow- Allow the request to be forwarded to the target. 
                 
                * authenticate- Redirect the request to the IdP authorization endpoint. This is the default value. 
                 
            - **Order** *(integer) --* 
        
              The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first. The final action to be performed must be a ``forward`` or a ``fixed-response`` action.
        
            - **RedirectConfig** *(dict) --* 
        
              [Application Load Balancer] Information for creating a redirect action. Specify only when ``Type`` is ``redirect`` .
        
              - **Protocol** *(string) --* 
        
                The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.
        
              - **Port** *(string) --* 
        
                The port. You can specify a value from 1 to 65535 or #{port}.
        
              - **Host** *(string) --* 
        
                The hostname. This component is not percent-encoded. The hostname can contain #{host}.
        
              - **Path** *(string) --* 
        
                The absolute path, starting with the leading \"/\". This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}.
        
              - **Query** *(string) --* 
        
                The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading \"?\", as it is automatically added. You can specify any of the reserved keywords.
        
              - **StatusCode** *(string) --* **[REQUIRED]** 
        
                The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).
        
            - **FixedResponseConfig** *(dict) --* 
        
              [Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when ``Type`` is ``fixed-response`` .
        
              - **MessageBody** *(string) --* 
        
                The message.
        
              - **StatusCode** *(string) --* **[REQUIRED]** 
        
                The HTTP response code (2XX, 4XX, or 5XX).
        
              - **ContentType** *(string) --* 
        
                The content type.
        
                Valid Values: text/plain | text/css | text/html | application/javascript | application/json
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Listeners\': [
                    {
                        \'ListenerArn\': \'string\',
                        \'LoadBalancerArn\': \'string\',
                        \'Port\': 123,
                        \'Protocol\': \'HTTP\'|\'HTTPS\'|\'TCP\',
                        \'Certificates\': [
                            {
                                \'CertificateArn\': \'string\',
                                \'IsDefault\': True|False
                            },
                        ],
                        \'SslPolicy\': \'string\',
                        \'DefaultActions\': [
                            {
                                \'Type\': \'forward\'|\'authenticate-oidc\'|\'authenticate-cognito\'|\'redirect\'|\'fixed-response\',
                                \'TargetGroupArn\': \'string\',
                                \'AuthenticateOidcConfig\': {
                                    \'Issuer\': \'string\',
                                    \'AuthorizationEndpoint\': \'string\',
                                    \'TokenEndpoint\': \'string\',
                                    \'UserInfoEndpoint\': \'string\',
                                    \'ClientId\': \'string\',
                                    \'ClientSecret\': \'string\',
                                    \'SessionCookieName\': \'string\',
                                    \'Scope\': \'string\',
                                    \'SessionTimeout\': 123,
                                    \'AuthenticationRequestExtraParams\': {
                                        \'string\': \'string\'
                                    },
                                    \'OnUnauthenticatedRequest\': \'deny\'|\'allow\'|\'authenticate\'
                                },
                                \'AuthenticateCognitoConfig\': {
                                    \'UserPoolArn\': \'string\',
                                    \'UserPoolClientId\': \'string\',
                                    \'UserPoolDomain\': \'string\',
                                    \'SessionCookieName\': \'string\',
                                    \'Scope\': \'string\',
                                    \'SessionTimeout\': 123,
                                    \'AuthenticationRequestExtraParams\': {
                                        \'string\': \'string\'
                                    },
                                    \'OnUnauthenticatedRequest\': \'deny\'|\'allow\'|\'authenticate\'
                                },
                                \'Order\': 123,
                                \'RedirectConfig\': {
                                    \'Protocol\': \'string\',
                                    \'Port\': \'string\',
                                    \'Host\': \'string\',
                                    \'Path\': \'string\',
                                    \'Query\': \'string\',
                                    \'StatusCode\': \'HTTP_301\'|\'HTTP_302\'
                                },
                                \'FixedResponseConfig\': {
                                    \'MessageBody\': \'string\',
                                    \'StatusCode\': \'string\',
                                    \'ContentType\': \'string\'
                                }
                            },
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Listeners** *(list) --* 
        
              Information about the modified listener.
        
              - *(dict) --* 
        
                Information about a listener.
        
                - **ListenerArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the listener.
        
                - **LoadBalancerArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the load balancer.
        
                - **Port** *(integer) --* 
        
                  The port on which the load balancer is listening.
        
                - **Protocol** *(string) --* 
        
                  The protocol for connections from clients to the load balancer.
        
                - **Certificates** *(list) --* 
        
                  The SSL server certificate. You must provide a certificate if the protocol is HTTPS.
        
                  - *(dict) --* 
        
                    Information about an SSL server certificate.
        
                    - **CertificateArn** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the certificate.
        
                    - **IsDefault** *(boolean) --* 
        
                      Indicates whether the certificate is the default certificate.
        
                - **SslPolicy** *(string) --* 
        
                  The security policy that defines which ciphers and protocols are supported. The default is the current predefined security policy.
        
                - **DefaultActions** *(list) --* 
        
                  The default actions for the listener.
        
                  - *(dict) --* 
        
                    Information about an action.
        
                    - **Type** *(string) --* 
        
                      The type of action. Each rule must include exactly one of the following types of actions: ``forward`` , ``fixed-response`` , or ``redirect`` .
        
                    - **TargetGroupArn** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is ``forward`` .
        
                    - **AuthenticateOidcConfig** *(dict) --* 
        
                      [HTTPS listener] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .
        
                      - **Issuer** *(string) --* 
        
                        The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **AuthorizationEndpoint** *(string) --* 
        
                        The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **TokenEndpoint** *(string) --* 
        
                        The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **UserInfoEndpoint** *(string) --* 
        
                        The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **ClientId** *(string) --* 
        
                        The OAuth 2.0 client identifier.
        
                      - **ClientSecret** *(string) --* 
        
                        The OAuth 2.0 client secret.
        
                      - **SessionCookieName** *(string) --* 
        
                        The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.
        
                      - **Scope** *(string) --* 
        
                        The set of user claims to be requested from the IdP. The default is ``openid`` .
        
                        To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.
        
                      - **SessionTimeout** *(integer) --* 
        
                        The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).
        
                      - **AuthenticationRequestExtraParams** *(dict) --* 
        
                        The query parameters (up to 10) to include in the redirect request to the authorization endpoint.
        
                        - *(string) --* 
                          
                          - *(string) --* 
                    
                      - **OnUnauthenticatedRequest** *(string) --* 
        
                        The behavior if the user is not authenticated. The following are possible values:
        
                        * deny- Return an HTTP 401 Unauthorized error. 
                         
                        * allow- Allow the request to be forwarded to the target. 
                         
                        * authenticate- Redirect the request to the IdP authorization endpoint. This is the default value. 
                         
                    - **AuthenticateCognitoConfig** *(dict) --* 
        
                      [HTTPS listener] Information for using Amazon Cognito to authenticate users. Specify only when ``Type`` is ``authenticate-cognito`` .
        
                      - **UserPoolArn** *(string) --* 
        
                        The Amazon Resource Name (ARN) of the Amazon Cognito user pool.
        
                      - **UserPoolClientId** *(string) --* 
        
                        The ID of the Amazon Cognito user pool client.
        
                      - **UserPoolDomain** *(string) --* 
        
                        The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.
        
                      - **SessionCookieName** *(string) --* 
        
                        The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.
        
                      - **Scope** *(string) --* 
        
                        The set of user claims to be requested from the IdP. The default is ``openid`` .
        
                        To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.
        
                      - **SessionTimeout** *(integer) --* 
        
                        The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).
        
                      - **AuthenticationRequestExtraParams** *(dict) --* 
        
                        The query parameters (up to 10) to include in the redirect request to the authorization endpoint.
        
                        - *(string) --* 
                          
                          - *(string) --* 
                    
                      - **OnUnauthenticatedRequest** *(string) --* 
        
                        The behavior if the user is not authenticated. The following are possible values:
        
                        * deny- Return an HTTP 401 Unauthorized error. 
                         
                        * allow- Allow the request to be forwarded to the target. 
                         
                        * authenticate- Redirect the request to the IdP authorization endpoint. This is the default value. 
                         
                    - **Order** *(integer) --* 
        
                      The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first. The final action to be performed must be a ``forward`` or a ``fixed-response`` action.
        
                    - **RedirectConfig** *(dict) --* 
        
                      [Application Load Balancer] Information for creating a redirect action. Specify only when ``Type`` is ``redirect`` .
        
                      - **Protocol** *(string) --* 
        
                        The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.
        
                      - **Port** *(string) --* 
        
                        The port. You can specify a value from 1 to 65535 or #{port}.
        
                      - **Host** *(string) --* 
        
                        The hostname. This component is not percent-encoded. The hostname can contain #{host}.
        
                      - **Path** *(string) --* 
        
                        The absolute path, starting with the leading \"/\". This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}.
        
                      - **Query** *(string) --* 
        
                        The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading \"?\", as it is automatically added. You can specify any of the reserved keywords.
        
                      - **StatusCode** *(string) --* 
        
                        The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).
        
                    - **FixedResponseConfig** *(dict) --* 
        
                      [Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when ``Type`` is ``fixed-response`` .
        
                      - **MessageBody** *(string) --* 
        
                        The message.
        
                      - **StatusCode** *(string) --* 
        
                        The HTTP response code (2XX, 4XX, or 5XX).
        
                      - **ContentType** *(string) --* 
        
                        The content type.
        
                        Valid Values: text/plain | text/css | text/html | application/javascript | application/json
        
        """
        pass

    def modify_load_balancer_attributes(self, LoadBalancerArn: str, Attributes: List) -> Dict:
        """
        
        If any of the specified attributes can\'t be modified as requested, the call fails. Any existing attributes that you do not modify retain their current values.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/ModifyLoadBalancerAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_load_balancer_attributes(
              LoadBalancerArn=\'string\',
              Attributes=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type LoadBalancerArn: string
        :param LoadBalancerArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the load balancer.
        
        :type Attributes: list
        :param Attributes: **[REQUIRED]** 
        
          The load balancer attributes.
        
          - *(dict) --* 
        
            Information about a load balancer attribute.
        
            - **Key** *(string) --* 
        
              The name of the attribute.
        
              The following attributes are supported by both Application Load Balancers and Network Load Balancers:
        
              * ``deletion_protection.enabled`` - Indicates whether deletion protection is enabled. The value is ``true`` or ``false`` . The default is ``false`` . 
               
              The following attributes are supported by only Application Load Balancers:
        
              * ``access_logs.s3.enabled`` - Indicates whether access logs are enabled. The value is ``true`` or ``false`` . The default is ``false`` . 
               
              * ``access_logs.s3.bucket`` - The name of the S3 bucket for the access logs. This attribute is required if access logs are enabled. The bucket must exist in the same region as the load balancer and have a bucket policy that grants Elastic Load Balancing permissions to write to the bucket. 
               
              * ``access_logs.s3.prefix`` - The prefix for the location in the S3 bucket for the access logs. 
               
              * ``idle_timeout.timeout_seconds`` - The idle timeout value, in seconds. The valid range is 1-4000 seconds. The default is 60 seconds. 
               
              * ``routing.http2.enabled`` - Indicates whether HTTP/2 is enabled. The value is ``true`` or ``false`` . The default is ``true`` . 
               
              The following attributes are supported by only Network Load Balancers:
        
              * ``load_balancing.cross_zone.enabled`` - Indicates whether cross-zone load balancing is enabled. The value is ``true`` or ``false`` . The default is ``false`` . 
               
            - **Value** *(string) --* 
        
              The value of the attribute.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Attributes\': [
                    {
                        \'Key\': \'string\',
                        \'Value\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Attributes** *(list) --* 
        
              Information about the load balancer attributes.
        
              - *(dict) --* 
        
                Information about a load balancer attribute.
        
                - **Key** *(string) --* 
        
                  The name of the attribute.
        
                  The following attributes are supported by both Application Load Balancers and Network Load Balancers:
        
                  * ``deletion_protection.enabled`` - Indicates whether deletion protection is enabled. The value is ``true`` or ``false`` . The default is ``false`` . 
                   
                  The following attributes are supported by only Application Load Balancers:
        
                  * ``access_logs.s3.enabled`` - Indicates whether access logs are enabled. The value is ``true`` or ``false`` . The default is ``false`` . 
                   
                  * ``access_logs.s3.bucket`` - The name of the S3 bucket for the access logs. This attribute is required if access logs are enabled. The bucket must exist in the same region as the load balancer and have a bucket policy that grants Elastic Load Balancing permissions to write to the bucket. 
                   
                  * ``access_logs.s3.prefix`` - The prefix for the location in the S3 bucket for the access logs. 
                   
                  * ``idle_timeout.timeout_seconds`` - The idle timeout value, in seconds. The valid range is 1-4000 seconds. The default is 60 seconds. 
                   
                  * ``routing.http2.enabled`` - Indicates whether HTTP/2 is enabled. The value is ``true`` or ``false`` . The default is ``true`` . 
                   
                  The following attributes are supported by only Network Load Balancers:
        
                  * ``load_balancing.cross_zone.enabled`` - Indicates whether cross-zone load balancing is enabled. The value is ``true`` or ``false`` . The default is ``false`` . 
                   
                - **Value** *(string) --* 
        
                  The value of the attribute.
        
        """
        pass

    def modify_rule(self, RuleArn: str, Conditions: List = None, Actions: List = None) -> Dict:
        """
        
        Any existing properties that you do not modify retain their current values.
        
        To modify the actions for the default rule, use  ModifyListener .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/ModifyRule>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_rule(
              RuleArn=\'string\',
              Conditions=[
                  {
                      \'Field\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              Actions=[
                  {
                      \'Type\': \'forward\'|\'authenticate-oidc\'|\'authenticate-cognito\'|\'redirect\'|\'fixed-response\',
                      \'TargetGroupArn\': \'string\',
                      \'AuthenticateOidcConfig\': {
                          \'Issuer\': \'string\',
                          \'AuthorizationEndpoint\': \'string\',
                          \'TokenEndpoint\': \'string\',
                          \'UserInfoEndpoint\': \'string\',
                          \'ClientId\': \'string\',
                          \'ClientSecret\': \'string\',
                          \'SessionCookieName\': \'string\',
                          \'Scope\': \'string\',
                          \'SessionTimeout\': 123,
                          \'AuthenticationRequestExtraParams\': {
                              \'string\': \'string\'
                          },
                          \'OnUnauthenticatedRequest\': \'deny\'|\'allow\'|\'authenticate\'
                      },
                      \'AuthenticateCognitoConfig\': {
                          \'UserPoolArn\': \'string\',
                          \'UserPoolClientId\': \'string\',
                          \'UserPoolDomain\': \'string\',
                          \'SessionCookieName\': \'string\',
                          \'Scope\': \'string\',
                          \'SessionTimeout\': 123,
                          \'AuthenticationRequestExtraParams\': {
                              \'string\': \'string\'
                          },
                          \'OnUnauthenticatedRequest\': \'deny\'|\'allow\'|\'authenticate\'
                      },
                      \'Order\': 123,
                      \'RedirectConfig\': {
                          \'Protocol\': \'string\',
                          \'Port\': \'string\',
                          \'Host\': \'string\',
                          \'Path\': \'string\',
                          \'Query\': \'string\',
                          \'StatusCode\': \'HTTP_301\'|\'HTTP_302\'
                      },
                      \'FixedResponseConfig\': {
                          \'MessageBody\': \'string\',
                          \'StatusCode\': \'string\',
                          \'ContentType\': \'string\'
                      }
                  },
              ]
          )
        :type RuleArn: string
        :param RuleArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the rule.
        
        :type Conditions: list
        :param Conditions: 
        
          The conditions. Each condition specifies a field name and a single value.
        
          If the field name is ``host-header`` , you can specify a single host name (for example, my.example.com). A host name is case insensitive, can be up to 128 characters in length, and can contain any of the following characters. You can include up to three wildcard characters.
        
          * A-Z, a-z, 0-9 
           
          * - . 
           
          * * (matches 0 or more characters) 
           
          * ? (matches exactly 1 character) 
           
          If the field name is ``path-pattern`` , you can specify a single path pattern. A path pattern is case-sensitive, can be up to 128 characters in length, and can contain any of the following characters. You can include up to three wildcard characters.
        
          * A-Z, a-z, 0-9 
           
          * _ - . $ / ~ \" \' @ : + 
           
          * & (using &amp;) 
           
          * * (matches 0 or more characters) 
           
          * ? (matches exactly 1 character) 
           
          - *(dict) --* 
        
            Information about a condition for a rule.
        
            - **Field** *(string) --* 
        
              The name of the field. The possible values are ``host-header`` and ``path-pattern`` .
        
            - **Values** *(list) --* 
        
              The condition value.
        
              If the field name is ``host-header`` , you can specify a single host name (for example, my.example.com). A host name is case insensitive, can be up to 128 characters in length, and can contain any of the following characters. You can include up to three wildcard characters.
        
              * A-Z, a-z, 0-9 
               
              * - . 
               
              * * (matches 0 or more characters) 
               
              * ? (matches exactly 1 character) 
               
              If the field name is ``path-pattern`` , you can specify a single path pattern (for example, /img/*). A path pattern is case-sensitive, can be up to 128 characters in length, and can contain any of the following characters. You can include up to three wildcard characters.
        
              * A-Z, a-z, 0-9 
               
              * _ - . $ / ~ \" \' @ : + 
               
              * & (using &amp;) 
               
              * * (matches 0 or more characters) 
               
              * ? (matches exactly 1 character) 
               
              - *(string) --* 
        
        :type Actions: list
        :param Actions: 
        
          The actions.
        
          If the action type is ``forward`` , you can specify a single target group.
        
          If the action type is ``authenticate-oidc`` , you can use an identity provider that is OpenID Connect (OIDC) compliant to authenticate users as they access your application.
        
          If the action type is ``authenticate-cognito`` , you can use Amazon Cognito to authenticate users as they access your application.
        
          - *(dict) --* 
        
            Information about an action.
        
            - **Type** *(string) --* **[REQUIRED]** 
        
              The type of action. Each rule must include exactly one of the following types of actions: ``forward`` , ``fixed-response`` , or ``redirect`` .
        
            - **TargetGroupArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is ``forward`` .
        
            - **AuthenticateOidcConfig** *(dict) --* 
        
              [HTTPS listener] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .
        
              - **Issuer** *(string) --* **[REQUIRED]** 
        
                The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
              - **AuthorizationEndpoint** *(string) --* **[REQUIRED]** 
        
                The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
              - **TokenEndpoint** *(string) --* **[REQUIRED]** 
        
                The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
              - **UserInfoEndpoint** *(string) --* **[REQUIRED]** 
        
                The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
              - **ClientId** *(string) --* **[REQUIRED]** 
        
                The OAuth 2.0 client identifier.
        
              - **ClientSecret** *(string) --* **[REQUIRED]** 
        
                The OAuth 2.0 client secret.
        
              - **SessionCookieName** *(string) --* 
        
                The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.
        
              - **Scope** *(string) --* 
        
                The set of user claims to be requested from the IdP. The default is ``openid`` .
        
                To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.
        
              - **SessionTimeout** *(integer) --* 
        
                The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).
        
              - **AuthenticationRequestExtraParams** *(dict) --* 
        
                The query parameters (up to 10) to include in the redirect request to the authorization endpoint.
        
                - *(string) --* 
        
                  - *(string) --* 
        
              - **OnUnauthenticatedRequest** *(string) --* 
        
                The behavior if the user is not authenticated. The following are possible values:
        
                * deny- Return an HTTP 401 Unauthorized error. 
                 
                * allow- Allow the request to be forwarded to the target. 
                 
                * authenticate- Redirect the request to the IdP authorization endpoint. This is the default value. 
                 
            - **AuthenticateCognitoConfig** *(dict) --* 
        
              [HTTPS listener] Information for using Amazon Cognito to authenticate users. Specify only when ``Type`` is ``authenticate-cognito`` .
        
              - **UserPoolArn** *(string) --* **[REQUIRED]** 
        
                The Amazon Resource Name (ARN) of the Amazon Cognito user pool.
        
              - **UserPoolClientId** *(string) --* **[REQUIRED]** 
        
                The ID of the Amazon Cognito user pool client.
        
              - **UserPoolDomain** *(string) --* **[REQUIRED]** 
        
                The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.
        
              - **SessionCookieName** *(string) --* 
        
                The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.
        
              - **Scope** *(string) --* 
        
                The set of user claims to be requested from the IdP. The default is ``openid`` .
        
                To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.
        
              - **SessionTimeout** *(integer) --* 
        
                The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).
        
              - **AuthenticationRequestExtraParams** *(dict) --* 
        
                The query parameters (up to 10) to include in the redirect request to the authorization endpoint.
        
                - *(string) --* 
        
                  - *(string) --* 
        
              - **OnUnauthenticatedRequest** *(string) --* 
        
                The behavior if the user is not authenticated. The following are possible values:
        
                * deny- Return an HTTP 401 Unauthorized error. 
                 
                * allow- Allow the request to be forwarded to the target. 
                 
                * authenticate- Redirect the request to the IdP authorization endpoint. This is the default value. 
                 
            - **Order** *(integer) --* 
        
              The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first. The final action to be performed must be a ``forward`` or a ``fixed-response`` action.
        
            - **RedirectConfig** *(dict) --* 
        
              [Application Load Balancer] Information for creating a redirect action. Specify only when ``Type`` is ``redirect`` .
        
              - **Protocol** *(string) --* 
        
                The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.
        
              - **Port** *(string) --* 
        
                The port. You can specify a value from 1 to 65535 or #{port}.
        
              - **Host** *(string) --* 
        
                The hostname. This component is not percent-encoded. The hostname can contain #{host}.
        
              - **Path** *(string) --* 
        
                The absolute path, starting with the leading \"/\". This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}.
        
              - **Query** *(string) --* 
        
                The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading \"?\", as it is automatically added. You can specify any of the reserved keywords.
        
              - **StatusCode** *(string) --* **[REQUIRED]** 
        
                The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).
        
            - **FixedResponseConfig** *(dict) --* 
        
              [Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when ``Type`` is ``fixed-response`` .
        
              - **MessageBody** *(string) --* 
        
                The message.
        
              - **StatusCode** *(string) --* **[REQUIRED]** 
        
                The HTTP response code (2XX, 4XX, or 5XX).
        
              - **ContentType** *(string) --* 
        
                The content type.
        
                Valid Values: text/plain | text/css | text/html | application/javascript | application/json
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Rules\': [
                    {
                        \'RuleArn\': \'string\',
                        \'Priority\': \'string\',
                        \'Conditions\': [
                            {
                                \'Field\': \'string\',
                                \'Values\': [
                                    \'string\',
                                ]
                            },
                        ],
                        \'Actions\': [
                            {
                                \'Type\': \'forward\'|\'authenticate-oidc\'|\'authenticate-cognito\'|\'redirect\'|\'fixed-response\',
                                \'TargetGroupArn\': \'string\',
                                \'AuthenticateOidcConfig\': {
                                    \'Issuer\': \'string\',
                                    \'AuthorizationEndpoint\': \'string\',
                                    \'TokenEndpoint\': \'string\',
                                    \'UserInfoEndpoint\': \'string\',
                                    \'ClientId\': \'string\',
                                    \'ClientSecret\': \'string\',
                                    \'SessionCookieName\': \'string\',
                                    \'Scope\': \'string\',
                                    \'SessionTimeout\': 123,
                                    \'AuthenticationRequestExtraParams\': {
                                        \'string\': \'string\'
                                    },
                                    \'OnUnauthenticatedRequest\': \'deny\'|\'allow\'|\'authenticate\'
                                },
                                \'AuthenticateCognitoConfig\': {
                                    \'UserPoolArn\': \'string\',
                                    \'UserPoolClientId\': \'string\',
                                    \'UserPoolDomain\': \'string\',
                                    \'SessionCookieName\': \'string\',
                                    \'Scope\': \'string\',
                                    \'SessionTimeout\': 123,
                                    \'AuthenticationRequestExtraParams\': {
                                        \'string\': \'string\'
                                    },
                                    \'OnUnauthenticatedRequest\': \'deny\'|\'allow\'|\'authenticate\'
                                },
                                \'Order\': 123,
                                \'RedirectConfig\': {
                                    \'Protocol\': \'string\',
                                    \'Port\': \'string\',
                                    \'Host\': \'string\',
                                    \'Path\': \'string\',
                                    \'Query\': \'string\',
                                    \'StatusCode\': \'HTTP_301\'|\'HTTP_302\'
                                },
                                \'FixedResponseConfig\': {
                                    \'MessageBody\': \'string\',
                                    \'StatusCode\': \'string\',
                                    \'ContentType\': \'string\'
                                }
                            },
                        ],
                        \'IsDefault\': True|False
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Rules** *(list) --* 
        
              Information about the modified rule.
        
              - *(dict) --* 
        
                Information about a rule.
        
                - **RuleArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the rule.
        
                - **Priority** *(string) --* 
        
                  The priority.
        
                - **Conditions** *(list) --* 
        
                  The conditions.
        
                  - *(dict) --* 
        
                    Information about a condition for a rule.
        
                    - **Field** *(string) --* 
        
                      The name of the field. The possible values are ``host-header`` and ``path-pattern`` .
        
                    - **Values** *(list) --* 
        
                      The condition value.
        
                      If the field name is ``host-header`` , you can specify a single host name (for example, my.example.com). A host name is case insensitive, can be up to 128 characters in length, and can contain any of the following characters. You can include up to three wildcard characters.
        
                      * A-Z, a-z, 0-9 
                       
                      * - . 
                       
                      * * (matches 0 or more characters) 
                       
                      * ? (matches exactly 1 character) 
                       
                      If the field name is ``path-pattern`` , you can specify a single path pattern (for example, /img/*). A path pattern is case-sensitive, can be up to 128 characters in length, and can contain any of the following characters. You can include up to three wildcard characters.
        
                      * A-Z, a-z, 0-9 
                       
                      * _ - . $ / ~ \" \' @ : + 
                       
                      * & (using &amp;) 
                       
                      * * (matches 0 or more characters) 
                       
                      * ? (matches exactly 1 character) 
                       
                      - *(string) --* 
                  
                - **Actions** *(list) --* 
        
                  The actions.
        
                  - *(dict) --* 
        
                    Information about an action.
        
                    - **Type** *(string) --* 
        
                      The type of action. Each rule must include exactly one of the following types of actions: ``forward`` , ``fixed-response`` , or ``redirect`` .
        
                    - **TargetGroupArn** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is ``forward`` .
        
                    - **AuthenticateOidcConfig** *(dict) --* 
        
                      [HTTPS listener] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .
        
                      - **Issuer** *(string) --* 
        
                        The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **AuthorizationEndpoint** *(string) --* 
        
                        The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **TokenEndpoint** *(string) --* 
        
                        The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **UserInfoEndpoint** *(string) --* 
        
                        The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **ClientId** *(string) --* 
        
                        The OAuth 2.0 client identifier.
        
                      - **ClientSecret** *(string) --* 
        
                        The OAuth 2.0 client secret.
        
                      - **SessionCookieName** *(string) --* 
        
                        The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.
        
                      - **Scope** *(string) --* 
        
                        The set of user claims to be requested from the IdP. The default is ``openid`` .
        
                        To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.
        
                      - **SessionTimeout** *(integer) --* 
        
                        The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).
        
                      - **AuthenticationRequestExtraParams** *(dict) --* 
        
                        The query parameters (up to 10) to include in the redirect request to the authorization endpoint.
        
                        - *(string) --* 
                          
                          - *(string) --* 
                    
                      - **OnUnauthenticatedRequest** *(string) --* 
        
                        The behavior if the user is not authenticated. The following are possible values:
        
                        * deny- Return an HTTP 401 Unauthorized error. 
                         
                        * allow- Allow the request to be forwarded to the target. 
                         
                        * authenticate- Redirect the request to the IdP authorization endpoint. This is the default value. 
                         
                    - **AuthenticateCognitoConfig** *(dict) --* 
        
                      [HTTPS listener] Information for using Amazon Cognito to authenticate users. Specify only when ``Type`` is ``authenticate-cognito`` .
        
                      - **UserPoolArn** *(string) --* 
        
                        The Amazon Resource Name (ARN) of the Amazon Cognito user pool.
        
                      - **UserPoolClientId** *(string) --* 
        
                        The ID of the Amazon Cognito user pool client.
        
                      - **UserPoolDomain** *(string) --* 
        
                        The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.
        
                      - **SessionCookieName** *(string) --* 
        
                        The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.
        
                      - **Scope** *(string) --* 
        
                        The set of user claims to be requested from the IdP. The default is ``openid`` .
        
                        To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.
        
                      - **SessionTimeout** *(integer) --* 
        
                        The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).
        
                      - **AuthenticationRequestExtraParams** *(dict) --* 
        
                        The query parameters (up to 10) to include in the redirect request to the authorization endpoint.
        
                        - *(string) --* 
                          
                          - *(string) --* 
                    
                      - **OnUnauthenticatedRequest** *(string) --* 
        
                        The behavior if the user is not authenticated. The following are possible values:
        
                        * deny- Return an HTTP 401 Unauthorized error. 
                         
                        * allow- Allow the request to be forwarded to the target. 
                         
                        * authenticate- Redirect the request to the IdP authorization endpoint. This is the default value. 
                         
                    - **Order** *(integer) --* 
        
                      The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first. The final action to be performed must be a ``forward`` or a ``fixed-response`` action.
        
                    - **RedirectConfig** *(dict) --* 
        
                      [Application Load Balancer] Information for creating a redirect action. Specify only when ``Type`` is ``redirect`` .
        
                      - **Protocol** *(string) --* 
        
                        The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.
        
                      - **Port** *(string) --* 
        
                        The port. You can specify a value from 1 to 65535 or #{port}.
        
                      - **Host** *(string) --* 
        
                        The hostname. This component is not percent-encoded. The hostname can contain #{host}.
        
                      - **Path** *(string) --* 
        
                        The absolute path, starting with the leading \"/\". This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}.
        
                      - **Query** *(string) --* 
        
                        The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading \"?\", as it is automatically added. You can specify any of the reserved keywords.
        
                      - **StatusCode** *(string) --* 
        
                        The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).
        
                    - **FixedResponseConfig** *(dict) --* 
        
                      [Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when ``Type`` is ``fixed-response`` .
        
                      - **MessageBody** *(string) --* 
        
                        The message.
        
                      - **StatusCode** *(string) --* 
        
                        The HTTP response code (2XX, 4XX, or 5XX).
        
                      - **ContentType** *(string) --* 
        
                        The content type.
        
                        Valid Values: text/plain | text/css | text/html | application/javascript | application/json
        
                - **IsDefault** *(boolean) --* 
        
                  Indicates whether this is the default rule.
        
        """
        pass

    def modify_target_group(self, TargetGroupArn: str, HealthCheckProtocol: str = None, HealthCheckPort: str = None, HealthCheckPath: str = None, HealthCheckIntervalSeconds: int = None, HealthCheckTimeoutSeconds: int = None, HealthyThresholdCount: int = None, UnhealthyThresholdCount: int = None, Matcher: Dict = None) -> Dict:
        """
        
        To monitor the health of the targets, use  DescribeTargetHealth .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/ModifyTargetGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_target_group(
              TargetGroupArn=\'string\',
              HealthCheckProtocol=\'HTTP\'|\'HTTPS\'|\'TCP\',
              HealthCheckPort=\'string\',
              HealthCheckPath=\'string\',
              HealthCheckIntervalSeconds=123,
              HealthCheckTimeoutSeconds=123,
              HealthyThresholdCount=123,
              UnhealthyThresholdCount=123,
              Matcher={
                  \'HttpCode\': \'string\'
              }
          )
        :type TargetGroupArn: string
        :param TargetGroupArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the target group.
        
        :type HealthCheckProtocol: string
        :param HealthCheckProtocol: 
        
          The protocol the load balancer uses when performing health checks on targets. The TCP protocol is supported only if the protocol of the target group is TCP.
        
        :type HealthCheckPort: string
        :param HealthCheckPort: 
        
          The port the load balancer uses when performing health checks on targets.
        
        :type HealthCheckPath: string
        :param HealthCheckPath: 
        
          [HTTP/HTTPS health checks] The ping path that is the destination for the health check request.
        
        :type HealthCheckIntervalSeconds: integer
        :param HealthCheckIntervalSeconds: 
        
          The approximate amount of time, in seconds, between health checks of an individual target. For Application Load Balancers, the range is 5–300 seconds. For Network Load Balancers, the supported values are 10 or 30 seconds.
        
        :type HealthCheckTimeoutSeconds: integer
        :param HealthCheckTimeoutSeconds: 
        
          [HTTP/HTTPS health checks] The amount of time, in seconds, during which no response means a failed health check.
        
        :type HealthyThresholdCount: integer
        :param HealthyThresholdCount: 
        
          The number of consecutive health checks successes required before considering an unhealthy target healthy.
        
        :type UnhealthyThresholdCount: integer
        :param UnhealthyThresholdCount: 
        
          The number of consecutive health check failures required before considering the target unhealthy. For Network Load Balancers, this value must be the same as the healthy threshold count.
        
        :type Matcher: dict
        :param Matcher: 
        
          [HTTP/HTTPS health checks] The HTTP codes to use when checking for a successful response from a target.
        
          - **HttpCode** *(string) --* **[REQUIRED]** 
        
            The HTTP codes.
        
            For Application Load Balancers, you can specify values between 200 and 499, and the default value is 200. You can specify multiple values (for example, \"200,202\") or a range of values (for example, \"200-299\").
        
            For Network Load Balancers, this is 200–399.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TargetGroups\': [
                    {
                        \'TargetGroupArn\': \'string\',
                        \'TargetGroupName\': \'string\',
                        \'Protocol\': \'HTTP\'|\'HTTPS\'|\'TCP\',
                        \'Port\': 123,
                        \'VpcId\': \'string\',
                        \'HealthCheckProtocol\': \'HTTP\'|\'HTTPS\'|\'TCP\',
                        \'HealthCheckPort\': \'string\',
                        \'HealthCheckIntervalSeconds\': 123,
                        \'HealthCheckTimeoutSeconds\': 123,
                        \'HealthyThresholdCount\': 123,
                        \'UnhealthyThresholdCount\': 123,
                        \'HealthCheckPath\': \'string\',
                        \'Matcher\': {
                            \'HttpCode\': \'string\'
                        },
                        \'LoadBalancerArns\': [
                            \'string\',
                        ],
                        \'TargetType\': \'instance\'|\'ip\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TargetGroups** *(list) --* 
        
              Information about the modified target group.
        
              - *(dict) --* 
        
                Information about a target group.
        
                - **TargetGroupArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the target group.
        
                - **TargetGroupName** *(string) --* 
        
                  The name of the target group.
        
                - **Protocol** *(string) --* 
        
                  The protocol to use for routing traffic to the targets.
        
                - **Port** *(integer) --* 
        
                  The port on which the targets are listening.
        
                - **VpcId** *(string) --* 
        
                  The ID of the VPC for the targets.
        
                - **HealthCheckProtocol** *(string) --* 
        
                  The protocol to use to connect with the target.
        
                - **HealthCheckPort** *(string) --* 
        
                  The port to use to connect with the target.
        
                - **HealthCheckIntervalSeconds** *(integer) --* 
        
                  The approximate amount of time, in seconds, between health checks of an individual target.
        
                - **HealthCheckTimeoutSeconds** *(integer) --* 
        
                  The amount of time, in seconds, during which no response means a failed health check.
        
                - **HealthyThresholdCount** *(integer) --* 
        
                  The number of consecutive health checks successes required before considering an unhealthy target healthy.
        
                - **UnhealthyThresholdCount** *(integer) --* 
        
                  The number of consecutive health check failures required before considering the target unhealthy.
        
                - **HealthCheckPath** *(string) --* 
        
                  The destination for the health check request.
        
                - **Matcher** *(dict) --* 
        
                  The HTTP codes to use when checking for a successful response from a target.
        
                  - **HttpCode** *(string) --* 
        
                    The HTTP codes.
        
                    For Application Load Balancers, you can specify values between 200 and 499, and the default value is 200. You can specify multiple values (for example, \"200,202\") or a range of values (for example, \"200-299\").
        
                    For Network Load Balancers, this is 200–399.
        
                - **LoadBalancerArns** *(list) --* 
        
                  The Amazon Resource Names (ARN) of the load balancers that route traffic to this target group.
        
                  - *(string) --* 
              
                - **TargetType** *(string) --* 
        
                  The type of target that you must specify when registering targets with this target group. The possible values are ``instance`` (targets are specified by instance ID) or ``ip`` (targets are specified by IP address).
        
        """
        pass

    def modify_target_group_attributes(self, TargetGroupArn: str, Attributes: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/ModifyTargetGroupAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_target_group_attributes(
              TargetGroupArn=\'string\',
              Attributes=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type TargetGroupArn: string
        :param TargetGroupArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the target group.
        
        :type Attributes: list
        :param Attributes: **[REQUIRED]** 
        
          The attributes.
        
          - *(dict) --* 
        
            Information about a target group attribute.
        
            - **Key** *(string) --* 
        
              The name of the attribute.
        
              The following attributes are supported by both Application Load Balancers and Network Load Balancers:
        
              * ``deregistration_delay.timeout_seconds`` - The amount of time, in seconds, for Elastic Load Balancing to wait before changing the state of a deregistering target from ``draining`` to ``unused`` . The range is 0-3600 seconds. The default value is 300 seconds. 
               
              The following attributes are supported by only Application Load Balancers:
        
              * ``slow_start.duration_seconds`` - The time period, in seconds, during which a newly registered target receives a linearly increasing share of the traffic to the target group. After this time period ends, the target receives its full share of traffic. The range is 30-900 seconds (15 minutes). Slow start mode is disabled by default. 
               
              * ``stickiness.enabled`` - Indicates whether sticky sessions are enabled. The value is ``true`` or ``false`` . The default is ``false`` . 
               
              * ``stickiness.type`` - The type of sticky sessions. The possible value is ``lb_cookie`` . 
               
              * ``stickiness.lb_cookie.duration_seconds`` - The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). The default value is 1 day (86400 seconds). 
               
              The following attributes are supported by only Network Load Balancers:
        
              * ``proxy_protocol_v2.enabled`` - Indicates whether Proxy Protocol version 2 is enabled. The value is ``true`` or ``false`` . The default is ``false`` . 
               
            - **Value** *(string) --* 
        
              The value of the attribute.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Attributes\': [
                    {
                        \'Key\': \'string\',
                        \'Value\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Attributes** *(list) --* 
        
              Information about the attributes.
        
              - *(dict) --* 
        
                Information about a target group attribute.
        
                - **Key** *(string) --* 
        
                  The name of the attribute.
        
                  The following attributes are supported by both Application Load Balancers and Network Load Balancers:
        
                  * ``deregistration_delay.timeout_seconds`` - The amount of time, in seconds, for Elastic Load Balancing to wait before changing the state of a deregistering target from ``draining`` to ``unused`` . The range is 0-3600 seconds. The default value is 300 seconds. 
                   
                  The following attributes are supported by only Application Load Balancers:
        
                  * ``slow_start.duration_seconds`` - The time period, in seconds, during which a newly registered target receives a linearly increasing share of the traffic to the target group. After this time period ends, the target receives its full share of traffic. The range is 30-900 seconds (15 minutes). Slow start mode is disabled by default. 
                   
                  * ``stickiness.enabled`` - Indicates whether sticky sessions are enabled. The value is ``true`` or ``false`` . The default is ``false`` . 
                   
                  * ``stickiness.type`` - The type of sticky sessions. The possible value is ``lb_cookie`` . 
                   
                  * ``stickiness.lb_cookie.duration_seconds`` - The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). The default value is 1 day (86400 seconds). 
                   
                  The following attributes are supported by only Network Load Balancers:
        
                  * ``proxy_protocol_v2.enabled`` - Indicates whether Proxy Protocol version 2 is enabled. The value is ``true`` or ``false`` . The default is ``false`` . 
                   
                - **Value** *(string) --* 
        
                  The value of the attribute.
        
        """
        pass

    def register_targets(self, TargetGroupArn: str, Targets: List) -> Dict:
        """
        
        You can register targets by instance ID or by IP address. If the target is an EC2 instance, it must be in the ``running`` state when you register it.
        
        By default, the load balancer routes requests to registered targets using the protocol and port for the target group. Alternatively, you can override the port for a target when you register it. You can register each EC2 instance or IP address with the same target group multiple times using different ports.
        
        With a Network Load Balancer, you cannot register instances by instance ID if they have the following instance types: C1, CC1, CC2, CG1, CG2, CR1, CS1, G1, G2, HI1, HS1, M1, M2, M3, and T1. You can register instances of these types by IP address.
        
        To remove a target from a target group, use  DeregisterTargets .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/RegisterTargets>`_
        
        **Request Syntax** 
        ::
        
          response = client.register_targets(
              TargetGroupArn=\'string\',
              Targets=[
                  {
                      \'Id\': \'string\',
                      \'Port\': 123,
                      \'AvailabilityZone\': \'string\'
                  },
              ]
          )
        :type TargetGroupArn: string
        :param TargetGroupArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the target group.
        
        :type Targets: list
        :param Targets: **[REQUIRED]** 
        
          The targets.
        
          - *(dict) --* 
        
            Information about a target.
        
            - **Id** *(string) --* **[REQUIRED]** 
        
              The ID of the target. If the target type of the target group is ``instance`` , specify an instance ID. If the target type is ``ip`` , specify an IP address.
        
            - **Port** *(integer) --* 
        
              The port on which the target is listening.
        
            - **AvailabilityZone** *(string) --* 
        
              An Availability Zone or ``all`` . This determines whether the target receives traffic from the load balancer nodes in the specified Availability Zone or from all enabled Availability Zones for the load balancer.
        
              This parameter is not supported if the target type of the target group is ``instance`` . If the IP address is in a subnet of the VPC for the target group, the Availability Zone is automatically detected and this parameter is optional. If the IP address is outside the VPC, this parameter is required.
        
              With an Application Load Balancer, if the IP address is outside the VPC for the target group, the only supported value is ``all`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def remove_listener_certificates(self, ListenerArn: str, Certificates: List) -> Dict:
        """
        
        You can\'t remove the default certificate for a listener. To replace the default certificate, call  ModifyListener .
        
        To list the certificates for your listener, use  DescribeListenerCertificates .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/RemoveListenerCertificates>`_
        
        **Request Syntax** 
        ::
        
          response = client.remove_listener_certificates(
              ListenerArn=\'string\',
              Certificates=[
                  {
                      \'CertificateArn\': \'string\',
                      \'IsDefault\': True|False
                  },
              ]
          )
        :type ListenerArn: string
        :param ListenerArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the listener.
        
        :type Certificates: list
        :param Certificates: **[REQUIRED]** 
        
          The certificate to remove. You can specify one certificate per call.
        
          - *(dict) --* 
        
            Information about an SSL server certificate.
        
            - **CertificateArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the certificate.
        
            - **IsDefault** *(boolean) --* 
        
              Indicates whether the certificate is the default certificate.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def remove_tags(self, ResourceArns: List, TagKeys: List) -> Dict:
        """
        
        To list the current tags for your resources, use  DescribeTags .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/RemoveTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.remove_tags(
              ResourceArns=[
                  \'string\',
              ],
              TagKeys=[
                  \'string\',
              ]
          )
        :type ResourceArns: list
        :param ResourceArns: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the resource.
        
          - *(string) --* 
        
        :type TagKeys: list
        :param TagKeys: **[REQUIRED]** 
        
          The tag keys for the tags to remove.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def set_ip_address_type(self, LoadBalancerArn: str, IpAddressType: str) -> Dict:
        """
        
        Network Load Balancers must use ``ipv4`` .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/SetIpAddressType>`_
        
        **Request Syntax** 
        ::
        
          response = client.set_ip_address_type(
              LoadBalancerArn=\'string\',
              IpAddressType=\'ipv4\'|\'dualstack\'
          )
        :type LoadBalancerArn: string
        :param LoadBalancerArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the load balancer.
        
        :type IpAddressType: string
        :param IpAddressType: **[REQUIRED]** 
        
          The IP address type. The possible values are ``ipv4`` (for IPv4 addresses) and ``dualstack`` (for IPv4 and IPv6 addresses). Internal load balancers must use ``ipv4`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IpAddressType\': \'ipv4\'|\'dualstack\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **IpAddressType** *(string) --* 
        
              The IP address type.
        
        """
        pass

    def set_rule_priorities(self, RulePriorities: List) -> Dict:
        """
        
        You can reorder the rules as long as there are no priority conflicts in the new order. Any existing rules that you do not specify retain their current priority.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/SetRulePriorities>`_
        
        **Request Syntax** 
        ::
        
          response = client.set_rule_priorities(
              RulePriorities=[
                  {
                      \'RuleArn\': \'string\',
                      \'Priority\': 123
                  },
              ]
          )
        :type RulePriorities: list
        :param RulePriorities: **[REQUIRED]** 
        
          The rule priorities.
        
          - *(dict) --* 
        
            Information about the priorities for the rules for a listener.
        
            - **RuleArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the rule.
        
            - **Priority** *(integer) --* 
        
              The rule priority.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Rules\': [
                    {
                        \'RuleArn\': \'string\',
                        \'Priority\': \'string\',
                        \'Conditions\': [
                            {
                                \'Field\': \'string\',
                                \'Values\': [
                                    \'string\',
                                ]
                            },
                        ],
                        \'Actions\': [
                            {
                                \'Type\': \'forward\'|\'authenticate-oidc\'|\'authenticate-cognito\'|\'redirect\'|\'fixed-response\',
                                \'TargetGroupArn\': \'string\',
                                \'AuthenticateOidcConfig\': {
                                    \'Issuer\': \'string\',
                                    \'AuthorizationEndpoint\': \'string\',
                                    \'TokenEndpoint\': \'string\',
                                    \'UserInfoEndpoint\': \'string\',
                                    \'ClientId\': \'string\',
                                    \'ClientSecret\': \'string\',
                                    \'SessionCookieName\': \'string\',
                                    \'Scope\': \'string\',
                                    \'SessionTimeout\': 123,
                                    \'AuthenticationRequestExtraParams\': {
                                        \'string\': \'string\'
                                    },
                                    \'OnUnauthenticatedRequest\': \'deny\'|\'allow\'|\'authenticate\'
                                },
                                \'AuthenticateCognitoConfig\': {
                                    \'UserPoolArn\': \'string\',
                                    \'UserPoolClientId\': \'string\',
                                    \'UserPoolDomain\': \'string\',
                                    \'SessionCookieName\': \'string\',
                                    \'Scope\': \'string\',
                                    \'SessionTimeout\': 123,
                                    \'AuthenticationRequestExtraParams\': {
                                        \'string\': \'string\'
                                    },
                                    \'OnUnauthenticatedRequest\': \'deny\'|\'allow\'|\'authenticate\'
                                },
                                \'Order\': 123,
                                \'RedirectConfig\': {
                                    \'Protocol\': \'string\',
                                    \'Port\': \'string\',
                                    \'Host\': \'string\',
                                    \'Path\': \'string\',
                                    \'Query\': \'string\',
                                    \'StatusCode\': \'HTTP_301\'|\'HTTP_302\'
                                },
                                \'FixedResponseConfig\': {
                                    \'MessageBody\': \'string\',
                                    \'StatusCode\': \'string\',
                                    \'ContentType\': \'string\'
                                }
                            },
                        ],
                        \'IsDefault\': True|False
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Rules** *(list) --* 
        
              Information about the rules.
        
              - *(dict) --* 
        
                Information about a rule.
        
                - **RuleArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the rule.
        
                - **Priority** *(string) --* 
        
                  The priority.
        
                - **Conditions** *(list) --* 
        
                  The conditions.
        
                  - *(dict) --* 
        
                    Information about a condition for a rule.
        
                    - **Field** *(string) --* 
        
                      The name of the field. The possible values are ``host-header`` and ``path-pattern`` .
        
                    - **Values** *(list) --* 
        
                      The condition value.
        
                      If the field name is ``host-header`` , you can specify a single host name (for example, my.example.com). A host name is case insensitive, can be up to 128 characters in length, and can contain any of the following characters. You can include up to three wildcard characters.
        
                      * A-Z, a-z, 0-9 
                       
                      * - . 
                       
                      * * (matches 0 or more characters) 
                       
                      * ? (matches exactly 1 character) 
                       
                      If the field name is ``path-pattern`` , you can specify a single path pattern (for example, /img/*). A path pattern is case-sensitive, can be up to 128 characters in length, and can contain any of the following characters. You can include up to three wildcard characters.
        
                      * A-Z, a-z, 0-9 
                       
                      * _ - . $ / ~ \" \' @ : + 
                       
                      * & (using &amp;) 
                       
                      * * (matches 0 or more characters) 
                       
                      * ? (matches exactly 1 character) 
                       
                      - *(string) --* 
                  
                - **Actions** *(list) --* 
        
                  The actions.
        
                  - *(dict) --* 
        
                    Information about an action.
        
                    - **Type** *(string) --* 
        
                      The type of action. Each rule must include exactly one of the following types of actions: ``forward`` , ``fixed-response`` , or ``redirect`` .
        
                    - **TargetGroupArn** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the target group. Specify only when ``Type`` is ``forward`` .
        
                    - **AuthenticateOidcConfig** *(dict) --* 
        
                      [HTTPS listener] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when ``Type`` is ``authenticate-oidc`` .
        
                      - **Issuer** *(string) --* 
        
                        The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **AuthorizationEndpoint** *(string) --* 
        
                        The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **TokenEndpoint** *(string) --* 
        
                        The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **UserInfoEndpoint** *(string) --* 
        
                        The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.
        
                      - **ClientId** *(string) --* 
        
                        The OAuth 2.0 client identifier.
        
                      - **ClientSecret** *(string) --* 
        
                        The OAuth 2.0 client secret.
        
                      - **SessionCookieName** *(string) --* 
        
                        The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.
        
                      - **Scope** *(string) --* 
        
                        The set of user claims to be requested from the IdP. The default is ``openid`` .
        
                        To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.
        
                      - **SessionTimeout** *(integer) --* 
        
                        The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).
        
                      - **AuthenticationRequestExtraParams** *(dict) --* 
        
                        The query parameters (up to 10) to include in the redirect request to the authorization endpoint.
        
                        - *(string) --* 
                          
                          - *(string) --* 
                    
                      - **OnUnauthenticatedRequest** *(string) --* 
        
                        The behavior if the user is not authenticated. The following are possible values:
        
                        * deny- Return an HTTP 401 Unauthorized error. 
                         
                        * allow- Allow the request to be forwarded to the target. 
                         
                        * authenticate- Redirect the request to the IdP authorization endpoint. This is the default value. 
                         
                    - **AuthenticateCognitoConfig** *(dict) --* 
        
                      [HTTPS listener] Information for using Amazon Cognito to authenticate users. Specify only when ``Type`` is ``authenticate-cognito`` .
        
                      - **UserPoolArn** *(string) --* 
        
                        The Amazon Resource Name (ARN) of the Amazon Cognito user pool.
        
                      - **UserPoolClientId** *(string) --* 
        
                        The ID of the Amazon Cognito user pool client.
        
                      - **UserPoolDomain** *(string) --* 
        
                        The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.
        
                      - **SessionCookieName** *(string) --* 
        
                        The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.
        
                      - **Scope** *(string) --* 
        
                        The set of user claims to be requested from the IdP. The default is ``openid`` .
        
                        To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.
        
                      - **SessionTimeout** *(integer) --* 
        
                        The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).
        
                      - **AuthenticationRequestExtraParams** *(dict) --* 
        
                        The query parameters (up to 10) to include in the redirect request to the authorization endpoint.
        
                        - *(string) --* 
                          
                          - *(string) --* 
                    
                      - **OnUnauthenticatedRequest** *(string) --* 
        
                        The behavior if the user is not authenticated. The following are possible values:
        
                        * deny- Return an HTTP 401 Unauthorized error. 
                         
                        * allow- Allow the request to be forwarded to the target. 
                         
                        * authenticate- Redirect the request to the IdP authorization endpoint. This is the default value. 
                         
                    - **Order** *(integer) --* 
        
                      The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first. The final action to be performed must be a ``forward`` or a ``fixed-response`` action.
        
                    - **RedirectConfig** *(dict) --* 
        
                      [Application Load Balancer] Information for creating a redirect action. Specify only when ``Type`` is ``redirect`` .
        
                      - **Protocol** *(string) --* 
        
                        The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You cannot redirect HTTPS to HTTP.
        
                      - **Port** *(string) --* 
        
                        The port. You can specify a value from 1 to 65535 or #{port}.
        
                      - **Host** *(string) --* 
        
                        The hostname. This component is not percent-encoded. The hostname can contain #{host}.
        
                      - **Path** *(string) --* 
        
                        The absolute path, starting with the leading \"/\". This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}.
        
                      - **Query** *(string) --* 
        
                        The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading \"?\", as it is automatically added. You can specify any of the reserved keywords.
        
                      - **StatusCode** *(string) --* 
        
                        The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).
        
                    - **FixedResponseConfig** *(dict) --* 
        
                      [Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when ``Type`` is ``fixed-response`` .
        
                      - **MessageBody** *(string) --* 
        
                        The message.
        
                      - **StatusCode** *(string) --* 
        
                        The HTTP response code (2XX, 4XX, or 5XX).
        
                      - **ContentType** *(string) --* 
        
                        The content type.
        
                        Valid Values: text/plain | text/css | text/html | application/javascript | application/json
        
                - **IsDefault** *(boolean) --* 
        
                  Indicates whether this is the default rule.
        
        """
        pass

    def set_security_groups(self, LoadBalancerArn: str, SecurityGroups: List) -> Dict:
        """
        
        You can\'t specify a security group for a Network Load Balancer.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/SetSecurityGroups>`_
        
        **Request Syntax** 
        ::
        
          response = client.set_security_groups(
              LoadBalancerArn=\'string\',
              SecurityGroups=[
                  \'string\',
              ]
          )
        :type LoadBalancerArn: string
        :param LoadBalancerArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the load balancer.
        
        :type SecurityGroups: list
        :param SecurityGroups: **[REQUIRED]** 
        
          The IDs of the security groups.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SecurityGroupIds\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SecurityGroupIds** *(list) --* 
        
              The IDs of the security groups associated with the load balancer.
        
              - *(string) --* 
          
        """
        pass

    def set_subnets(self, LoadBalancerArn: str, Subnets: List = None, SubnetMappings: List = None) -> Dict:
        """
        
        You can\'t change the subnets for a Network Load Balancer.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/SetSubnets>`_
        
        **Request Syntax** 
        ::
        
          response = client.set_subnets(
              LoadBalancerArn=\'string\',
              Subnets=[
                  \'string\',
              ],
              SubnetMappings=[
                  {
                      \'SubnetId\': \'string\',
                      \'AllocationId\': \'string\'
                  },
              ]
          )
        :type LoadBalancerArn: string
        :param LoadBalancerArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the load balancer.
        
        :type Subnets: list
        :param Subnets: 
        
          The IDs of the public subnets. You must specify subnets from at least two Availability Zones. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings.
        
          - *(string) --* 
        
        :type SubnetMappings: list
        :param SubnetMappings: 
        
          The IDs of the public subnets. You must specify subnets from at least two Availability Zones. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings.
        
          You cannot specify Elastic IP addresses for your subnets.
        
          - *(dict) --* 
        
            Information about a subnet mapping.
        
            - **SubnetId** *(string) --* 
        
              The ID of the subnet.
        
            - **AllocationId** *(string) --* 
        
              [Network Load Balancers] The allocation ID of the Elastic IP address.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AvailabilityZones\': [
                    {
                        \'ZoneName\': \'string\',
                        \'SubnetId\': \'string\',
                        \'LoadBalancerAddresses\': [
                            {
                                \'IpAddress\': \'string\',
                                \'AllocationId\': \'string\'
                            },
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AvailabilityZones** *(list) --* 
        
              Information about the subnet and Availability Zone.
        
              - *(dict) --* 
        
                Information about an Availability Zone.
        
                - **ZoneName** *(string) --* 
        
                  The name of the Availability Zone.
        
                - **SubnetId** *(string) --* 
        
                  The ID of the subnet.
        
                - **LoadBalancerAddresses** *(list) --* 
        
                  [Network Load Balancers] The static IP address.
        
                  - *(dict) --* 
        
                    Information about a static IP address for a load balancer.
        
                    - **IpAddress** *(string) --* 
        
                      The static IP address.
        
                    - **AllocationId** *(string) --* 
        
                      [Network Load Balancers] The allocation ID of the Elastic IP address.
        
        """
        pass
