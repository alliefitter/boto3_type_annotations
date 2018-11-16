from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeListeners(Paginator):
    def paginate(self, LoadBalancerArn: str = None, ListenerArns: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeListeners>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              LoadBalancerArn=\'string\',
              ListenerArns=[
                  \'string\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type LoadBalancerArn: string
        :param LoadBalancerArn: 
        
          The Amazon Resource Name (ARN) of the load balancer.
        
        :type ListenerArns: list
        :param ListenerArns: 
        
          The Amazon Resource Names (ARN) of the listeners.
        
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
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeLoadBalancers(Paginator):
    def paginate(self, LoadBalancerArns: List = None, Names: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancers>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              LoadBalancerArns=[
                  \'string\',
              ],
              Names=[
                  \'string\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type LoadBalancerArns: list
        :param LoadBalancerArns: 
        
          The Amazon Resource Names (ARN) of the load balancers. You can specify up to 20 load balancers in a single call.
        
          - *(string) --* 
        
        :type Names: list
        :param Names: 
        
          The names of the load balancers.
        
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
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeTargetGroups(Paginator):
    def paginate(self, LoadBalancerArn: str = None, TargetGroupArns: List = None, Names: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeTargetGroups>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              LoadBalancerArn=\'string\',
              TargetGroupArns=[
                  \'string\',
              ],
              Names=[
                  \'string\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
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
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
