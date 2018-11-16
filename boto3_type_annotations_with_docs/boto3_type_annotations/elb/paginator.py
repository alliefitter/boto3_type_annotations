from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeLoadBalancers(Paginator):
    def paginate(self, LoadBalancerNames: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/DescribeLoadBalancers>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              LoadBalancerNames=[
                  \'string\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type LoadBalancerNames: list
        :param LoadBalancerNames: 
        
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
                \'LoadBalancerDescriptions\': [
                    {
                        \'LoadBalancerName\': \'string\',
                        \'DNSName\': \'string\',
                        \'CanonicalHostedZoneName\': \'string\',
                        \'CanonicalHostedZoneNameID\': \'string\',
                        \'ListenerDescriptions\': [
                            {
                                \'Listener\': {
                                    \'Protocol\': \'string\',
                                    \'LoadBalancerPort\': 123,
                                    \'InstanceProtocol\': \'string\',
                                    \'InstancePort\': 123,
                                    \'SSLCertificateId\': \'string\'
                                },
                                \'PolicyNames\': [
                                    \'string\',
                                ]
                            },
                        ],
                        \'Policies\': {
                            \'AppCookieStickinessPolicies\': [
                                {
                                    \'PolicyName\': \'string\',
                                    \'CookieName\': \'string\'
                                },
                            ],
                            \'LBCookieStickinessPolicies\': [
                                {
                                    \'PolicyName\': \'string\',
                                    \'CookieExpirationPeriod\': 123
                                },
                            ],
                            \'OtherPolicies\': [
                                \'string\',
                            ]
                        },
                        \'BackendServerDescriptions\': [
                            {
                                \'InstancePort\': 123,
                                \'PolicyNames\': [
                                    \'string\',
                                ]
                            },
                        ],
                        \'AvailabilityZones\': [
                            \'string\',
                        ],
                        \'Subnets\': [
                            \'string\',
                        ],
                        \'VPCId\': \'string\',
                        \'Instances\': [
                            {
                                \'InstanceId\': \'string\'
                            },
                        ],
                        \'HealthCheck\': {
                            \'Target\': \'string\',
                            \'Interval\': 123,
                            \'Timeout\': 123,
                            \'UnhealthyThreshold\': 123,
                            \'HealthyThreshold\': 123
                        },
                        \'SourceSecurityGroup\': {
                            \'OwnerAlias\': \'string\',
                            \'GroupName\': \'string\'
                        },
                        \'SecurityGroups\': [
                            \'string\',
                        ],
                        \'CreatedTime\': datetime(2015, 1, 1),
                        \'Scheme\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the parameters for DescribeLoadBalancers.
        
            - **LoadBalancerDescriptions** *(list) --* 
        
              Information about the load balancers.
        
              - *(dict) --* 
        
                Information about a load balancer.
        
                - **LoadBalancerName** *(string) --* 
        
                  The name of the load balancer.
        
                - **DNSName** *(string) --* 
        
                  The DNS name of the load balancer.
        
                - **CanonicalHostedZoneName** *(string) --* 
        
                  The DNS name of the load balancer.
        
                  For more information, see `Configure a Custom Domain Name <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/using-domain-names-with-elb.html>`__ in the *Classic Load Balancers Guide* .
        
                - **CanonicalHostedZoneNameID** *(string) --* 
        
                  The ID of the Amazon Route 53 hosted zone for the load balancer.
        
                - **ListenerDescriptions** *(list) --* 
        
                  The listeners for the load balancer.
        
                  - *(dict) --* 
        
                    The policies enabled for a listener.
        
                    - **Listener** *(dict) --* 
        
                      The listener.
        
                      - **Protocol** *(string) --* 
        
                        The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP, or SSL.
        
                      - **LoadBalancerPort** *(integer) --* 
        
                        The port on which the load balancer is listening. On EC2-VPC, you can specify any port from the range 1-65535. On EC2-Classic, you can specify any port from the following list: 25, 80, 443, 465, 587, 1024-65535.
        
                      - **InstanceProtocol** *(string) --* 
        
                        The protocol to use for routing traffic to instances: HTTP, HTTPS, TCP, or SSL.
        
                        If the front-end protocol is HTTP, HTTPS, TCP, or SSL, ``InstanceProtocol`` must be at the same protocol.
        
                        If there is another listener with the same ``InstancePort`` whose ``InstanceProtocol`` is secure, (HTTPS or SSL), the listener\'s ``InstanceProtocol`` must also be secure.
        
                        If there is another listener with the same ``InstancePort`` whose ``InstanceProtocol`` is HTTP or TCP, the listener\'s ``InstanceProtocol`` must be HTTP or TCP.
        
                      - **InstancePort** *(integer) --* 
        
                        The port on which the instance is listening.
        
                      - **SSLCertificateId** *(string) --* 
        
                        The Amazon Resource Name (ARN) of the server certificate.
        
                    - **PolicyNames** *(list) --* 
        
                      The policies. If there are no policies enabled, the list is empty.
        
                      - *(string) --* 
                  
                - **Policies** *(dict) --* 
        
                  The policies defined for the load balancer.
        
                  - **AppCookieStickinessPolicies** *(list) --* 
        
                    The stickiness policies created using  CreateAppCookieStickinessPolicy .
        
                    - *(dict) --* 
        
                      Information about a policy for application-controlled session stickiness.
        
                      - **PolicyName** *(string) --* 
        
                        The mnemonic name for the policy being created. The name must be unique within a set of policies for this load balancer.
        
                      - **CookieName** *(string) --* 
        
                        The name of the application cookie used for stickiness.
        
                  - **LBCookieStickinessPolicies** *(list) --* 
        
                    The stickiness policies created using  CreateLBCookieStickinessPolicy .
        
                    - *(dict) --* 
        
                      Information about a policy for duration-based session stickiness.
        
                      - **PolicyName** *(string) --* 
        
                        The name of the policy. This name must be unique within the set of policies for this load balancer.
        
                      - **CookieExpirationPeriod** *(integer) --* 
        
                        The time period, in seconds, after which the cookie should be considered stale. If this parameter is not specified, the stickiness session lasts for the duration of the browser session.
        
                  - **OtherPolicies** *(list) --* 
        
                    The policies other than the stickiness policies.
        
                    - *(string) --* 
                
                - **BackendServerDescriptions** *(list) --* 
        
                  Information about your EC2 instances.
        
                  - *(dict) --* 
        
                    Information about the configuration of an EC2 instance.
        
                    - **InstancePort** *(integer) --* 
        
                      The port on which the EC2 instance is listening.
        
                    - **PolicyNames** *(list) --* 
        
                      The names of the policies enabled for the EC2 instance.
        
                      - *(string) --* 
                  
                - **AvailabilityZones** *(list) --* 
        
                  The Availability Zones for the load balancer.
        
                  - *(string) --* 
              
                - **Subnets** *(list) --* 
        
                  The IDs of the subnets for the load balancer.
        
                  - *(string) --* 
              
                - **VPCId** *(string) --* 
        
                  The ID of the VPC for the load balancer.
        
                - **Instances** *(list) --* 
        
                  The IDs of the instances for the load balancer.
        
                  - *(dict) --* 
        
                    The ID of an EC2 instance.
        
                    - **InstanceId** *(string) --* 
        
                      The instance ID.
        
                - **HealthCheck** *(dict) --* 
        
                  Information about the health checks conducted on the load balancer.
        
                  - **Target** *(string) --* 
        
                    The instance being checked. The protocol is either TCP, HTTP, HTTPS, or SSL. The range of valid ports is one (1) through 65535.
        
                    TCP is the default, specified as a TCP: port pair, for example \"TCP:5000\". In this case, a health check simply attempts to open a TCP connection to the instance on the specified port. Failure to connect within the configured timeout is considered unhealthy.
        
                    SSL is also specified as SSL: port pair, for example, SSL:5000.
        
                    For HTTP/HTTPS, you must include a ping path in the string. HTTP is specified as a HTTP:port;/;PathToPing; grouping, for example \"HTTP:80/weather/us/wa/seattle\". In this case, a HTTP GET request is issued to the instance on the given port and path. Any answer other than \"200 OK\" within the timeout period is considered unhealthy.
        
                    The total length of the HTTP ping target must be 1024 16-bit Unicode characters or less.
        
                  - **Interval** *(integer) --* 
        
                    The approximate interval, in seconds, between health checks of an individual instance.
        
                  - **Timeout** *(integer) --* 
        
                    The amount of time, in seconds, during which no response means a failed health check.
        
                    This value must be less than the ``Interval`` value.
        
                  - **UnhealthyThreshold** *(integer) --* 
        
                    The number of consecutive health check failures required before moving the instance to the ``Unhealthy`` state.
        
                  - **HealthyThreshold** *(integer) --* 
        
                    The number of consecutive health checks successes required before moving the instance to the ``Healthy`` state.
        
                - **SourceSecurityGroup** *(dict) --* 
        
                  The security group for the load balancer, which you can use as part of your inbound rules for your registered instances. To only allow traffic from load balancers, add a security group rule that specifies this source security group as the inbound source.
        
                  - **OwnerAlias** *(string) --* 
        
                    The owner of the security group.
        
                  - **GroupName** *(string) --* 
        
                    The name of the security group.
        
                - **SecurityGroups** *(list) --* 
        
                  The security groups for the load balancer. Valid only for load balancers in a VPC.
        
                  - *(string) --* 
              
                - **CreatedTime** *(datetime) --* 
        
                  The date and time the load balancer was created.
        
                - **Scheme** *(string) --* 
        
                  The type of load balancer. Valid only for load balancers in a VPC.
        
                  If ``Scheme`` is ``internet-facing`` , the load balancer has a public DNS name that resolves to a public IP address.
        
                  If ``Scheme`` is ``internal`` , the load balancer has a public DNS name that resolves to a private IP address.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
