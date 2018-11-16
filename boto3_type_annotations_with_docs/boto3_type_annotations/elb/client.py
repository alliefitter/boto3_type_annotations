from typing import Optional
from typing import Union
from typing import List
from botocore.waiter import Waiter
from botocore.paginate import Paginator
from typing import Dict
from botocore.client import BaseClient


class Client(BaseClient):
    def add_tags(self, LoadBalancerNames: List, Tags: List) -> Dict:
        """
        
        Each tag consists of a key and an optional value. If a tag with the same key is already associated with the load balancer, ``AddTags`` updates its value.
        
        For more information, see `Tag Your Classic Load Balancer <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/add-remove-tags.html>`__ in the *Classic Load Balancers Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/AddTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.add_tags(
              LoadBalancerNames=[
                  \'string\',
              ],
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type LoadBalancerNames: list
        :param LoadBalancerNames: **[REQUIRED]** 
        
          The name of the load balancer. You can specify one load balancer only.
        
          - *(string) --* 
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          The tags.
        
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
        
            Contains the output of AddTags.
        
        """
        pass

    def apply_security_groups_to_load_balancer(self, LoadBalancerName: str, SecurityGroups: List) -> Dict:
        """
        
        For more information, see `Security Groups for Load Balancers in a VPC <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-groups.html#elb-vpc-security-groups>`__ in the *Classic Load Balancers Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/ApplySecurityGroupsToLoadBalancer>`_
        
        **Request Syntax** 
        ::
        
          response = client.apply_security_groups_to_load_balancer(
              LoadBalancerName=\'string\',
              SecurityGroups=[
                  \'string\',
              ]
          )
        :type LoadBalancerName: string
        :param LoadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
        :type SecurityGroups: list
        :param SecurityGroups: **[REQUIRED]** 
        
          The IDs of the security groups to associate with the load balancer. Note that you cannot specify the name of the security group.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SecurityGroups\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of ApplySecurityGroupsToLoadBalancer.
        
            - **SecurityGroups** *(list) --* 
        
              The IDs of the security groups associated with the load balancer.
        
              - *(string) --* 
          
        """
        pass

    def attach_load_balancer_to_subnets(self, LoadBalancerName: str, Subnets: List) -> Dict:
        """
        
        The load balancer evenly distributes requests across all registered subnets. For more information, see `Add or Remove Subnets for Your Load Balancer in a VPC <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-manage-subnets.html>`__ in the *Classic Load Balancers Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/AttachLoadBalancerToSubnets>`_
        
        **Request Syntax** 
        ::
        
          response = client.attach_load_balancer_to_subnets(
              LoadBalancerName=\'string\',
              Subnets=[
                  \'string\',
              ]
          )
        :type LoadBalancerName: string
        :param LoadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
        :type Subnets: list
        :param Subnets: **[REQUIRED]** 
        
          The IDs of the subnets to add. You can add only one subnet per Availability Zone.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Subnets\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of AttachLoadBalancerToSubnets.
        
            - **Subnets** *(list) --* 
        
              The IDs of the subnets attached to the load balancer.
        
              - *(string) --* 
          
        """
        pass

    def can_paginate(self, operation_name: str = None):
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

    def configure_health_check(self, LoadBalancerName: str, HealthCheck: Dict) -> Dict:
        """
        
        For more information, see `Configure Health Checks for Your Load Balancer <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-healthchecks.html>`__ in the *Classic Load Balancers Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/ConfigureHealthCheck>`_
        
        **Request Syntax** 
        ::
        
          response = client.configure_health_check(
              LoadBalancerName=\'string\',
              HealthCheck={
                  \'Target\': \'string\',
                  \'Interval\': 123,
                  \'Timeout\': 123,
                  \'UnhealthyThreshold\': 123,
                  \'HealthyThreshold\': 123
              }
          )
        :type LoadBalancerName: string
        :param LoadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
        :type HealthCheck: dict
        :param HealthCheck: **[REQUIRED]** 
        
          The configuration information.
        
          - **Target** *(string) --* **[REQUIRED]** 
        
            The instance being checked. The protocol is either TCP, HTTP, HTTPS, or SSL. The range of valid ports is one (1) through 65535.
        
            TCP is the default, specified as a TCP: port pair, for example \"TCP:5000\". In this case, a health check simply attempts to open a TCP connection to the instance on the specified port. Failure to connect within the configured timeout is considered unhealthy.
        
            SSL is also specified as SSL: port pair, for example, SSL:5000.
        
            For HTTP/HTTPS, you must include a ping path in the string. HTTP is specified as a HTTP:port;/;PathToPing; grouping, for example \"HTTP:80/weather/us/wa/seattle\". In this case, a HTTP GET request is issued to the instance on the given port and path. Any answer other than \"200 OK\" within the timeout period is considered unhealthy.
        
            The total length of the HTTP ping target must be 1024 16-bit Unicode characters or less.
        
          - **Interval** *(integer) --* **[REQUIRED]** 
        
            The approximate interval, in seconds, between health checks of an individual instance.
        
          - **Timeout** *(integer) --* **[REQUIRED]** 
        
            The amount of time, in seconds, during which no response means a failed health check.
        
            This value must be less than the ``Interval`` value.
        
          - **UnhealthyThreshold** *(integer) --* **[REQUIRED]** 
        
            The number of consecutive health check failures required before moving the instance to the ``Unhealthy`` state.
        
          - **HealthyThreshold** *(integer) --* **[REQUIRED]** 
        
            The number of consecutive health checks successes required before moving the instance to the ``Healthy`` state.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'HealthCheck\': {
                    \'Target\': \'string\',
                    \'Interval\': 123,
                    \'Timeout\': 123,
                    \'UnhealthyThreshold\': 123,
                    \'HealthyThreshold\': 123
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of ConfigureHealthCheck.
        
            - **HealthCheck** *(dict) --* 
        
              The updated health check.
        
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
        
        """
        pass

    def create_app_cookie_stickiness_policy(self, LoadBalancerName: str, PolicyName: str, CookieName: str) -> Dict:
        """
        
        This policy is similar to the policy created by  CreateLBCookieStickinessPolicy , except that the lifetime of the special Elastic Load Balancing cookie, ``AWSELB`` , follows the lifetime of the application-generated cookie specified in the policy configuration. The load balancer only inserts a new stickiness cookie when the application response includes a new application cookie.
        
        If the application cookie is explicitly removed or expires, the session stops being sticky until a new application cookie is issued.
        
        For more information, see `Application-Controlled Session Stickiness <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-sticky-sessions.html#enable-sticky-sessions-application>`__ in the *Classic Load Balancers Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/CreateAppCookieStickinessPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_app_cookie_stickiness_policy(
              LoadBalancerName=\'string\',
              PolicyName=\'string\',
              CookieName=\'string\'
          )
        :type LoadBalancerName: string
        :param LoadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
        :type PolicyName: string
        :param PolicyName: **[REQUIRED]** 
        
          The name of the policy being created. Policy names must consist of alphanumeric characters and dashes (-). This name must be unique within the set of policies for this load balancer.
        
        :type CookieName: string
        :param CookieName: **[REQUIRED]** 
        
          The name of the application cookie used for stickiness.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output for CreateAppCookieStickinessPolicy.
        
        """
        pass

    def create_lb_cookie_stickiness_policy(self, LoadBalancerName: str, PolicyName: str, CookieExpirationPeriod: int = None) -> Dict:
        """
        
        When a load balancer implements this policy, the load balancer uses a special cookie to track the instance for each request. When the load balancer receives a request, it first checks to see if this cookie is present in the request. If so, the load balancer sends the request to the application server specified in the cookie. If not, the load balancer sends the request to a server that is chosen based on the existing load-balancing algorithm.
        
        A cookie is inserted into the response for binding subsequent requests from the same user to that server. The validity of the cookie is based on the cookie expiration time, which is specified in the policy configuration.
        
        For more information, see `Duration-Based Session Stickiness <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-sticky-sessions.html#enable-sticky-sessions-duration>`__ in the *Classic Load Balancers Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/CreateLBCookieStickinessPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_lb_cookie_stickiness_policy(
              LoadBalancerName=\'string\',
              PolicyName=\'string\',
              CookieExpirationPeriod=123
          )
        :type LoadBalancerName: string
        :param LoadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
        :type PolicyName: string
        :param PolicyName: **[REQUIRED]** 
        
          The name of the policy being created. Policy names must consist of alphanumeric characters and dashes (-). This name must be unique within the set of policies for this load balancer.
        
        :type CookieExpirationPeriod: integer
        :param CookieExpirationPeriod: 
        
          The time period, in seconds, after which the cookie should be considered stale. If you do not specify this parameter, the default value is 0, which indicates that the sticky session should last for the duration of the browser session.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output for CreateLBCookieStickinessPolicy.
        
        """
        pass

    def create_load_balancer(self, LoadBalancerName: str, Listeners: List, AvailabilityZones: List = None, Subnets: List = None, SecurityGroups: List = None, Scheme: str = None, Tags: List = None) -> Dict:
        """
        
        You can add listeners, security groups, subnets, and tags when you create your load balancer, or you can add them later using  CreateLoadBalancerListeners ,  ApplySecurityGroupsToLoadBalancer ,  AttachLoadBalancerToSubnets , and  AddTags .
        
        To describe your current load balancers, see  DescribeLoadBalancers . When you are finished with a load balancer, you can delete it using  DeleteLoadBalancer .
        
        You can create up to 20 load balancers per region per account. You can request an increase for the number of load balancers for your account. For more information, see `Limits for Your Classic Load Balancer <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-limits.html>`__ in the *Classic Load Balancers Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/CreateLoadBalancer>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_load_balancer(
              LoadBalancerName=\'string\',
              Listeners=[
                  {
                      \'Protocol\': \'string\',
                      \'LoadBalancerPort\': 123,
                      \'InstanceProtocol\': \'string\',
                      \'InstancePort\': 123,
                      \'SSLCertificateId\': \'string\'
                  },
              ],
              AvailabilityZones=[
                  \'string\',
              ],
              Subnets=[
                  \'string\',
              ],
              SecurityGroups=[
                  \'string\',
              ],
              Scheme=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type LoadBalancerName: string
        :param LoadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
          This name must be unique within your set of load balancers for the region, must have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and cannot begin or end with a hyphen.
        
        :type Listeners: list
        :param Listeners: **[REQUIRED]** 
        
          The listeners.
        
          For more information, see `Listeners for Your Classic Load Balancer <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-listener-config.html>`__ in the *Classic Load Balancers Guide* .
        
          - *(dict) --* 
        
            Information about a listener.
        
            For information about the protocols and the ports supported by Elastic Load Balancing, see `Listeners for Your Classic Load Balancer <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-listener-config.html>`__ in the *Classic Load Balancers Guide* .
        
            - **Protocol** *(string) --* **[REQUIRED]** 
        
              The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP, or SSL.
        
            - **LoadBalancerPort** *(integer) --* **[REQUIRED]** 
        
              The port on which the load balancer is listening. On EC2-VPC, you can specify any port from the range 1-65535. On EC2-Classic, you can specify any port from the following list: 25, 80, 443, 465, 587, 1024-65535.
        
            - **InstanceProtocol** *(string) --* 
        
              The protocol to use for routing traffic to instances: HTTP, HTTPS, TCP, or SSL.
        
              If the front-end protocol is HTTP, HTTPS, TCP, or SSL, ``InstanceProtocol`` must be at the same protocol.
        
              If there is another listener with the same ``InstancePort`` whose ``InstanceProtocol`` is secure, (HTTPS or SSL), the listener\'s ``InstanceProtocol`` must also be secure.
        
              If there is another listener with the same ``InstancePort`` whose ``InstanceProtocol`` is HTTP or TCP, the listener\'s ``InstanceProtocol`` must be HTTP or TCP.
        
            - **InstancePort** *(integer) --* **[REQUIRED]** 
        
              The port on which the instance is listening.
        
            - **SSLCertificateId** *(string) --* 
        
              The Amazon Resource Name (ARN) of the server certificate.
        
        :type AvailabilityZones: list
        :param AvailabilityZones: 
        
          One or more Availability Zones from the same region as the load balancer.
        
          You must specify at least one Availability Zone.
        
          You can add more Availability Zones after you create the load balancer using  EnableAvailabilityZonesForLoadBalancer .
        
          - *(string) --* 
        
        :type Subnets: list
        :param Subnets: 
        
          The IDs of the subnets in your VPC to attach to the load balancer. Specify one subnet per Availability Zone specified in ``AvailabilityZones`` .
        
          - *(string) --* 
        
        :type SecurityGroups: list
        :param SecurityGroups: 
        
          The IDs of the security groups to assign to the load balancer.
        
          - *(string) --* 
        
        :type Scheme: string
        :param Scheme: 
        
          The type of a load balancer. Valid only for load balancers in a VPC.
        
          By default, Elastic Load Balancing creates an Internet-facing load balancer with a DNS name that resolves to public IP addresses. For more information about Internet-facing and Internal load balancers, see `Load Balancer Scheme <http://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html#load-balancer-scheme>`__ in the *Elastic Load Balancing User Guide* .
        
          Specify ``internal`` to create a load balancer with a DNS name that resolves to private IP addresses.
        
        :type Tags: list
        :param Tags: 
        
          A list of tags to assign to the load balancer.
        
          For more information about tagging your load balancer, see `Tag Your Classic Load Balancer <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/add-remove-tags.html>`__ in the *Classic Load Balancers Guide* .
        
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
        
            {
                \'DNSName\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output for CreateLoadBalancer.
        
            - **DNSName** *(string) --* 
        
              The DNS name of the load balancer.
        
        """
        pass

    def create_load_balancer_listeners(self, LoadBalancerName: str, Listeners: List) -> Dict:
        """
        
        For more information, see `Listeners for Your Classic Load Balancer <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-listener-config.html>`__ in the *Classic Load Balancers Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/CreateLoadBalancerListeners>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_load_balancer_listeners(
              LoadBalancerName=\'string\',
              Listeners=[
                  {
                      \'Protocol\': \'string\',
                      \'LoadBalancerPort\': 123,
                      \'InstanceProtocol\': \'string\',
                      \'InstancePort\': 123,
                      \'SSLCertificateId\': \'string\'
                  },
              ]
          )
        :type LoadBalancerName: string
        :param LoadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
        :type Listeners: list
        :param Listeners: **[REQUIRED]** 
        
          The listeners.
        
          - *(dict) --* 
        
            Information about a listener.
        
            For information about the protocols and the ports supported by Elastic Load Balancing, see `Listeners for Your Classic Load Balancer <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-listener-config.html>`__ in the *Classic Load Balancers Guide* .
        
            - **Protocol** *(string) --* **[REQUIRED]** 
        
              The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP, or SSL.
        
            - **LoadBalancerPort** *(integer) --* **[REQUIRED]** 
        
              The port on which the load balancer is listening. On EC2-VPC, you can specify any port from the range 1-65535. On EC2-Classic, you can specify any port from the following list: 25, 80, 443, 465, 587, 1024-65535.
        
            - **InstanceProtocol** *(string) --* 
        
              The protocol to use for routing traffic to instances: HTTP, HTTPS, TCP, or SSL.
        
              If the front-end protocol is HTTP, HTTPS, TCP, or SSL, ``InstanceProtocol`` must be at the same protocol.
        
              If there is another listener with the same ``InstancePort`` whose ``InstanceProtocol`` is secure, (HTTPS or SSL), the listener\'s ``InstanceProtocol`` must also be secure.
        
              If there is another listener with the same ``InstancePort`` whose ``InstanceProtocol`` is HTTP or TCP, the listener\'s ``InstanceProtocol`` must be HTTP or TCP.
        
            - **InstancePort** *(integer) --* **[REQUIRED]** 
        
              The port on which the instance is listening.
        
            - **SSLCertificateId** *(string) --* 
        
              The Amazon Resource Name (ARN) of the server certificate.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the parameters for CreateLoadBalancerListener.
        
        """
        pass

    def create_load_balancer_policy(self, LoadBalancerName: str, PolicyName: str, PolicyTypeName: str, PolicyAttributes: List = None) -> Dict:
        """
        
        Policies are settings that are saved for your load balancer and that can be applied to the listener or the application server, depending on the policy type.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/CreateLoadBalancerPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_load_balancer_policy(
              LoadBalancerName=\'string\',
              PolicyName=\'string\',
              PolicyTypeName=\'string\',
              PolicyAttributes=[
                  {
                      \'AttributeName\': \'string\',
                      \'AttributeValue\': \'string\'
                  },
              ]
          )
        :type LoadBalancerName: string
        :param LoadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
        :type PolicyName: string
        :param PolicyName: **[REQUIRED]** 
        
          The name of the load balancer policy to be created. This name must be unique within the set of policies for this load balancer.
        
        :type PolicyTypeName: string
        :param PolicyTypeName: **[REQUIRED]** 
        
          The name of the base policy type. To get the list of policy types, use  DescribeLoadBalancerPolicyTypes .
        
        :type PolicyAttributes: list
        :param PolicyAttributes: 
        
          The policy attributes.
        
          - *(dict) --* 
        
            Information about a policy attribute.
        
            - **AttributeName** *(string) --* 
        
              The name of the attribute.
        
            - **AttributeValue** *(string) --* 
        
              The value of the attribute.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of CreateLoadBalancerPolicy.
        
        """
        pass

    def delete_load_balancer(self, LoadBalancerName: str) -> Dict:
        """
        
        If you are attempting to recreate a load balancer, you must reconfigure all settings. The DNS name associated with a deleted load balancer are no longer usable. The name and associated DNS record of the deleted load balancer no longer exist and traffic sent to any of its IP addresses is no longer delivered to your instances.
        
        If the load balancer does not exist or has already been deleted, the call to ``DeleteLoadBalancer`` still succeeds.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/DeleteLoadBalancer>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_load_balancer(
              LoadBalancerName=\'string\'
          )
        :type LoadBalancerName: string
        :param LoadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of DeleteLoadBalancer.
        
        """
        pass

    def delete_load_balancer_listeners(self, LoadBalancerName: str, LoadBalancerPorts: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/DeleteLoadBalancerListeners>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_load_balancer_listeners(
              LoadBalancerName=\'string\',
              LoadBalancerPorts=[
                  123,
              ]
          )
        :type LoadBalancerName: string
        :param LoadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
        :type LoadBalancerPorts: list
        :param LoadBalancerPorts: **[REQUIRED]** 
        
          The client port numbers of the listeners.
        
          - *(integer) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of DeleteLoadBalancerListeners.
        
        """
        pass

    def delete_load_balancer_policy(self, LoadBalancerName: str, PolicyName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/DeleteLoadBalancerPolicy>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_load_balancer_policy(
              LoadBalancerName=\'string\',
              PolicyName=\'string\'
          )
        :type LoadBalancerName: string
        :param LoadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
        :type PolicyName: string
        :param PolicyName: **[REQUIRED]** 
        
          The name of the policy.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of DeleteLoadBalancerPolicy.
        
        """
        pass

    def deregister_instances_from_load_balancer(self, LoadBalancerName: str, Instances: List) -> Dict:
        """
        
        You can use  DescribeLoadBalancers to verify that the instance is deregistered from the load balancer.
        
        For more information, see `Register or De-Register EC2 Instances <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-deregister-register-instances.html>`__ in the *Classic Load Balancers Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/DeregisterInstancesFromLoadBalancer>`_
        
        **Request Syntax** 
        ::
        
          response = client.deregister_instances_from_load_balancer(
              LoadBalancerName=\'string\',
              Instances=[
                  {
                      \'InstanceId\': \'string\'
                  },
              ]
          )
        :type LoadBalancerName: string
        :param LoadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
        :type Instances: list
        :param Instances: **[REQUIRED]** 
        
          The IDs of the instances.
        
          - *(dict) --* 
        
            The ID of an EC2 instance.
        
            - **InstanceId** *(string) --* 
        
              The instance ID.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Instances\': [
                    {
                        \'InstanceId\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of DeregisterInstancesFromLoadBalancer.
        
            - **Instances** *(list) --* 
        
              The remaining instances registered with the load balancer.
        
              - *(dict) --* 
        
                The ID of an EC2 instance.
        
                - **InstanceId** *(string) --* 
        
                  The instance ID.
        
        """
        pass

    def describe_account_limits(self, Marker: str = None, PageSize: int = None) -> Dict:
        """
        
        For more information, see `Limits for Your Classic Load Balancer <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-limits.html>`__ in the *Classic Load Balancers Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/DescribeAccountLimits>`_
        
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
        
                  * classic-listeners 
                   
                  * classic-load-balancers 
                   
                  * classic-registered-instances 
                   
                - **Max** *(string) --* 
        
                  The maximum value of the limit.
        
            - **NextMarker** *(string) --* 
        
              The marker to use when requesting the next set of results. If there are no additional results, the string is empty.
        
        """
        pass

    def describe_instance_health(self, LoadBalancerName: str, Instances: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/DescribeInstanceHealth>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_instance_health(
              LoadBalancerName=\'string\',
              Instances=[
                  {
                      \'InstanceId\': \'string\'
                  },
              ]
          )
        :type LoadBalancerName: string
        :param LoadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
        :type Instances: list
        :param Instances: 
        
          The IDs of the instances.
        
          - *(dict) --* 
        
            The ID of an EC2 instance.
        
            - **InstanceId** *(string) --* 
        
              The instance ID.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'InstanceStates\': [
                    {
                        \'InstanceId\': \'string\',
                        \'State\': \'string\',
                        \'ReasonCode\': \'string\',
                        \'Description\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output for DescribeInstanceHealth.
        
            - **InstanceStates** *(list) --* 
        
              Information about the health of the instances.
        
              - *(dict) --* 
        
                Information about the state of an EC2 instance.
        
                - **InstanceId** *(string) --* 
        
                  The ID of the instance.
        
                - **State** *(string) --* 
        
                  The current state of the instance.
        
                  Valid values: ``InService`` | ``OutOfService`` | ``Unknown``  
        
                - **ReasonCode** *(string) --* 
        
                  Information about the cause of ``OutOfService`` instances. Specifically, whether the cause is Elastic Load Balancing or the instance.
        
                  Valid values: ``ELB`` | ``Instance`` | ``N/A``  
        
                - **Description** *(string) --* 
        
                  A description of the instance state. This string can contain one or more of the following messages.
        
                  * ``N/A``   
                   
                  * ``A transient error occurred. Please try again later.``   
                   
                  * ``Instance has failed at least the UnhealthyThreshold number of health checks consecutively.``   
                   
                  * ``Instance has not passed the configured HealthyThreshold number of health checks consecutively.``   
                   
                  * ``Instance registration is still in progress.``   
                   
                  * ``Instance is in the EC2 Availability Zone for which LoadBalancer is not configured to route traffic to.``   
                   
                  * ``Instance is not currently registered with the LoadBalancer.``   
                   
                  * ``Instance deregistration currently in progress.``   
                   
                  * ``Disable Availability Zone is currently in progress.``   
                   
                  * ``Instance is in pending state.``   
                   
                  * ``Instance is in stopped state.``   
                   
                  * ``Instance is in terminated state.``   
                   
        """
        pass

    def describe_load_balancer_attributes(self, LoadBalancerName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/DescribeLoadBalancerAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_load_balancer_attributes(
              LoadBalancerName=\'string\'
          )
        :type LoadBalancerName: string
        :param LoadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'LoadBalancerAttributes\': {
                    \'CrossZoneLoadBalancing\': {
                        \'Enabled\': True|False
                    },
                    \'AccessLog\': {
                        \'Enabled\': True|False,
                        \'S3BucketName\': \'string\',
                        \'EmitInterval\': 123,
                        \'S3BucketPrefix\': \'string\'
                    },
                    \'ConnectionDraining\': {
                        \'Enabled\': True|False,
                        \'Timeout\': 123
                    },
                    \'ConnectionSettings\': {
                        \'IdleTimeout\': 123
                    },
                    \'AdditionalAttributes\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ]
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of DescribeLoadBalancerAttributes.
        
            - **LoadBalancerAttributes** *(dict) --* 
        
              Information about the load balancer attributes.
        
              - **CrossZoneLoadBalancing** *(dict) --* 
        
                If enabled, the load balancer routes the request traffic evenly across all instances regardless of the Availability Zones.
        
                For more information, see `Configure Cross-Zone Load Balancing <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html>`__ in the *Classic Load Balancers Guide* .
        
                - **Enabled** *(boolean) --* 
        
                  Specifies whether cross-zone load balancing is enabled for the load balancer.
        
              - **AccessLog** *(dict) --* 
        
                If enabled, the load balancer captures detailed information of all requests and delivers the information to the Amazon S3 bucket that you specify.
        
                For more information, see `Enable Access Logs <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-access-logs.html>`__ in the *Classic Load Balancers Guide* .
        
                - **Enabled** *(boolean) --* 
        
                  Specifies whether access logs are enabled for the load balancer.
        
                - **S3BucketName** *(string) --* 
        
                  The name of the Amazon S3 bucket where the access logs are stored.
        
                - **EmitInterval** *(integer) --* 
        
                  The interval for publishing the access logs. You can specify an interval of either 5 minutes or 60 minutes.
        
                  Default: 60 minutes
        
                - **S3BucketPrefix** *(string) --* 
        
                  The logical hierarchy you created for your Amazon S3 bucket, for example ``my-bucket-prefix/prod`` . If the prefix is not provided, the log is placed at the root level of the bucket.
        
              - **ConnectionDraining** *(dict) --* 
        
                If enabled, the load balancer allows existing requests to complete before the load balancer shifts traffic away from a deregistered or unhealthy instance.
        
                For more information, see `Configure Connection Draining <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-conn-drain.html>`__ in the *Classic Load Balancers Guide* .
        
                - **Enabled** *(boolean) --* 
        
                  Specifies whether connection draining is enabled for the load balancer.
        
                - **Timeout** *(integer) --* 
        
                  The maximum time, in seconds, to keep the existing connections open before deregistering the instances.
        
              - **ConnectionSettings** *(dict) --* 
        
                If enabled, the load balancer allows the connections to remain idle (no data is sent over the connection) for the specified duration.
        
                By default, Elastic Load Balancing maintains a 60-second idle connection timeout for both front-end and back-end connections of your load balancer. For more information, see `Configure Idle Connection Timeout <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-idle-timeout.html>`__ in the *Classic Load Balancers Guide* .
        
                - **IdleTimeout** *(integer) --* 
        
                  The time, in seconds, that the connection is allowed to be idle (no data has been sent over the connection) before it is closed by the load balancer.
        
              - **AdditionalAttributes** *(list) --* 
        
                This parameter is reserved.
        
                - *(dict) --* 
        
                  This data type is reserved.
        
                  - **Key** *(string) --* 
        
                    This parameter is reserved.
        
                  - **Value** *(string) --* 
        
                    This parameter is reserved.
        
        """
        pass

    def describe_load_balancer_policies(self, LoadBalancerName: str = None, PolicyNames: List = None) -> Dict:
        """
        
        If you specify a load balancer name, the action returns the descriptions of all policies created for the load balancer. If you specify a policy name associated with your load balancer, the action returns the description of that policy. If you don\'t specify a load balancer name, the action returns descriptions of the specified sample policies, or descriptions of all sample policies. The names of the sample policies have the ``ELBSample-`` prefix.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/DescribeLoadBalancerPolicies>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_load_balancer_policies(
              LoadBalancerName=\'string\',
              PolicyNames=[
                  \'string\',
              ]
          )
        :type LoadBalancerName: string
        :param LoadBalancerName: 
        
          The name of the load balancer.
        
        :type PolicyNames: list
        :param PolicyNames: 
        
          The names of the policies.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'PolicyDescriptions\': [
                    {
                        \'PolicyName\': \'string\',
                        \'PolicyTypeName\': \'string\',
                        \'PolicyAttributeDescriptions\': [
                            {
                                \'AttributeName\': \'string\',
                                \'AttributeValue\': \'string\'
                            },
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of DescribeLoadBalancerPolicies.
        
            - **PolicyDescriptions** *(list) --* 
        
              Information about the policies.
        
              - *(dict) --* 
        
                Information about a policy.
        
                - **PolicyName** *(string) --* 
        
                  The name of the policy.
        
                - **PolicyTypeName** *(string) --* 
        
                  The name of the policy type.
        
                - **PolicyAttributeDescriptions** *(list) --* 
        
                  The policy attributes.
        
                  - *(dict) --* 
        
                    Information about a policy attribute.
        
                    - **AttributeName** *(string) --* 
        
                      The name of the attribute.
        
                    - **AttributeValue** *(string) --* 
        
                      The value of the attribute.
        
        """
        pass

    def describe_load_balancer_policy_types(self, PolicyTypeNames: List = None) -> Dict:
        """
        
        The description of each type indicates how it can be used. For example, some policies can be used only with layer 7 listeners, some policies can be used only with layer 4 listeners, and some policies can be used only with your EC2 instances.
        
        You can use  CreateLoadBalancerPolicy to create a policy configuration for any of these policy types. Then, depending on the policy type, use either  SetLoadBalancerPoliciesOfListener or  SetLoadBalancerPoliciesForBackendServer to set the policy.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/DescribeLoadBalancerPolicyTypes>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_load_balancer_policy_types(
              PolicyTypeNames=[
                  \'string\',
              ]
          )
        :type PolicyTypeNames: list
        :param PolicyTypeNames: 
        
          The names of the policy types. If no names are specified, describes all policy types defined by Elastic Load Balancing.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'PolicyTypeDescriptions\': [
                    {
                        \'PolicyTypeName\': \'string\',
                        \'Description\': \'string\',
                        \'PolicyAttributeTypeDescriptions\': [
                            {
                                \'AttributeName\': \'string\',
                                \'AttributeType\': \'string\',
                                \'Description\': \'string\',
                                \'DefaultValue\': \'string\',
                                \'Cardinality\': \'string\'
                            },
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of DescribeLoadBalancerPolicyTypes.
        
            - **PolicyTypeDescriptions** *(list) --* 
        
              Information about the policy types.
        
              - *(dict) --* 
        
                Information about a policy type.
        
                - **PolicyTypeName** *(string) --* 
        
                  The name of the policy type.
        
                - **Description** *(string) --* 
        
                  A description of the policy type.
        
                - **PolicyAttributeTypeDescriptions** *(list) --* 
        
                  The description of the policy attributes associated with the policies defined by Elastic Load Balancing.
        
                  - *(dict) --* 
        
                    Information about a policy attribute type.
        
                    - **AttributeName** *(string) --* 
        
                      The name of the attribute.
        
                    - **AttributeType** *(string) --* 
        
                      The type of the attribute. For example, ``Boolean`` or ``Integer`` .
        
                    - **Description** *(string) --* 
        
                      A description of the attribute.
        
                    - **DefaultValue** *(string) --* 
        
                      The default value of the attribute, if applicable.
        
                    - **Cardinality** *(string) --* 
        
                      The cardinality of the attribute.
        
                      Valid values:
        
                      * ONE(1) : Single value required 
                       
                      * ZERO_OR_ONE(0..1) : Up to one value is allowed 
                       
                      * ZERO_OR_MORE(0..*) : Optional. Multiple values are allowed 
                       
                      * ONE_OR_MORE(1..*0) : Required. Multiple values are allowed 
                       
        """
        pass

    def describe_load_balancers(self, LoadBalancerNames: List = None, Marker: str = None, PageSize: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/DescribeLoadBalancers>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_load_balancers(
              LoadBalancerNames=[
                  \'string\',
              ],
              Marker=\'string\',
              PageSize=123
          )
        :type LoadBalancerNames: list
        :param LoadBalancerNames: 
        
          The names of the load balancers.
        
          - *(string) --* 
        
        :type Marker: string
        :param Marker: 
        
          The marker for the next set of results. (You received this marker from a previous call.)
        
        :type PageSize: integer
        :param PageSize: 
        
          The maximum number of results to return with this call (a number from 1 to 400). The default is 400.
        
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
                \'NextMarker\': \'string\'
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
        
            - **NextMarker** *(string) --* 
        
              The marker to use when requesting the next set of results. If there are no additional results, the string is empty.
        
        """
        pass

    def describe_tags(self, LoadBalancerNames: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/DescribeTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_tags(
              LoadBalancerNames=[
                  \'string\',
              ]
          )
        :type LoadBalancerNames: list
        :param LoadBalancerNames: **[REQUIRED]** 
        
          The names of the load balancers.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TagDescriptions\': [
                    {
                        \'LoadBalancerName\': \'string\',
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
        
            Contains the output for DescribeTags.
        
            - **TagDescriptions** *(list) --* 
        
              Information about the tags.
        
              - *(dict) --* 
        
                The tags associated with a load balancer.
        
                - **LoadBalancerName** *(string) --* 
        
                  The name of the load balancer.
        
                - **Tags** *(list) --* 
        
                  The tags.
        
                  - *(dict) --* 
        
                    Information about a tag.
        
                    - **Key** *(string) --* 
        
                      The key of the tag.
        
                    - **Value** *(string) --* 
        
                      The value of the tag.
        
        """
        pass

    def detach_load_balancer_from_subnets(self, LoadBalancerName: str, Subnets: List) -> Dict:
        """
        
        After a subnet is removed, all EC2 instances registered with the load balancer in the removed subnet go into the ``OutOfService`` state. Then, the load balancer balances the traffic among the remaining routable subnets.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/DetachLoadBalancerFromSubnets>`_
        
        **Request Syntax** 
        ::
        
          response = client.detach_load_balancer_from_subnets(
              LoadBalancerName=\'string\',
              Subnets=[
                  \'string\',
              ]
          )
        :type LoadBalancerName: string
        :param LoadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
        :type Subnets: list
        :param Subnets: **[REQUIRED]** 
        
          The IDs of the subnets.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Subnets\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of DetachLoadBalancerFromSubnets.
        
            - **Subnets** *(list) --* 
        
              The IDs of the remaining subnets for the load balancer.
        
              - *(string) --* 
          
        """
        pass

    def disable_availability_zones_for_load_balancer(self, LoadBalancerName: str, AvailabilityZones: List) -> Dict:
        """
        
        For load balancers in a non-default VPC, use  DetachLoadBalancerFromSubnets .
        
        There must be at least one Availability Zone registered with a load balancer at all times. After an Availability Zone is removed, all instances registered with the load balancer that are in the removed Availability Zone go into the ``OutOfService`` state. Then, the load balancer attempts to equally balance the traffic among its remaining Availability Zones.
        
        For more information, see `Add or Remove Availability Zones <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-az.html>`__ in the *Classic Load Balancers Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/DisableAvailabilityZonesForLoadBalancer>`_
        
        **Request Syntax** 
        ::
        
          response = client.disable_availability_zones_for_load_balancer(
              LoadBalancerName=\'string\',
              AvailabilityZones=[
                  \'string\',
              ]
          )
        :type LoadBalancerName: string
        :param LoadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
        :type AvailabilityZones: list
        :param AvailabilityZones: **[REQUIRED]** 
        
          The Availability Zones.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AvailabilityZones\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output for DisableAvailabilityZonesForLoadBalancer.
        
            - **AvailabilityZones** *(list) --* 
        
              The remaining Availability Zones for the load balancer.
        
              - *(string) --* 
          
        """
        pass

    def enable_availability_zones_for_load_balancer(self, LoadBalancerName: str, AvailabilityZones: List) -> Dict:
        """
        
        For load balancers in a non-default VPC, use  AttachLoadBalancerToSubnets .
        
        The load balancer evenly distributes requests across all its registered Availability Zones that contain instances. For more information, see `Add or Remove Availability Zones <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-az.html>`__ in the *Classic Load Balancers Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/EnableAvailabilityZonesForLoadBalancer>`_
        
        **Request Syntax** 
        ::
        
          response = client.enable_availability_zones_for_load_balancer(
              LoadBalancerName=\'string\',
              AvailabilityZones=[
                  \'string\',
              ]
          )
        :type LoadBalancerName: string
        :param LoadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
        :type AvailabilityZones: list
        :param AvailabilityZones: **[REQUIRED]** 
        
          The Availability Zones. These must be in the same region as the load balancer.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AvailabilityZones\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of EnableAvailabilityZonesForLoadBalancer.
        
            - **AvailabilityZones** *(list) --* 
        
              The updated list of Availability Zones for the load balancer.
        
              - *(string) --* 
          
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
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

    def modify_load_balancer_attributes(self, LoadBalancerName: str, LoadBalancerAttributes: Dict) -> Dict:
        """
        
        You can modify the load balancer attributes, such as ``AccessLogs`` , ``ConnectionDraining`` , and ``CrossZoneLoadBalancing`` by either enabling or disabling them. Or, you can modify the load balancer attribute ``ConnectionSettings`` by specifying an idle connection timeout value for your load balancer.
        
        For more information, see the following in the *Classic Load Balancers Guide* :
        
        * `Cross-Zone Load Balancing <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html>`__   
         
        * `Connection Draining <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-conn-drain.html>`__   
         
        * `Access Logs <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/access-log-collection.html>`__   
         
        * `Idle Connection Timeout <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-idle-timeout.html>`__   
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/ModifyLoadBalancerAttributes>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_load_balancer_attributes(
              LoadBalancerName=\'string\',
              LoadBalancerAttributes={
                  \'CrossZoneLoadBalancing\': {
                      \'Enabled\': True|False
                  },
                  \'AccessLog\': {
                      \'Enabled\': True|False,
                      \'S3BucketName\': \'string\',
                      \'EmitInterval\': 123,
                      \'S3BucketPrefix\': \'string\'
                  },
                  \'ConnectionDraining\': {
                      \'Enabled\': True|False,
                      \'Timeout\': 123
                  },
                  \'ConnectionSettings\': {
                      \'IdleTimeout\': 123
                  },
                  \'AdditionalAttributes\': [
                      {
                          \'Key\': \'string\',
                          \'Value\': \'string\'
                      },
                  ]
              }
          )
        :type LoadBalancerName: string
        :param LoadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
        :type LoadBalancerAttributes: dict
        :param LoadBalancerAttributes: **[REQUIRED]** 
        
          The attributes for the load balancer.
        
          - **CrossZoneLoadBalancing** *(dict) --* 
        
            If enabled, the load balancer routes the request traffic evenly across all instances regardless of the Availability Zones.
        
            For more information, see `Configure Cross-Zone Load Balancing <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html>`__ in the *Classic Load Balancers Guide* .
        
            - **Enabled** *(boolean) --* **[REQUIRED]** 
        
              Specifies whether cross-zone load balancing is enabled for the load balancer.
        
          - **AccessLog** *(dict) --* 
        
            If enabled, the load balancer captures detailed information of all requests and delivers the information to the Amazon S3 bucket that you specify.
        
            For more information, see `Enable Access Logs <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-access-logs.html>`__ in the *Classic Load Balancers Guide* .
        
            - **Enabled** *(boolean) --* **[REQUIRED]** 
        
              Specifies whether access logs are enabled for the load balancer.
        
            - **S3BucketName** *(string) --* 
        
              The name of the Amazon S3 bucket where the access logs are stored.
        
            - **EmitInterval** *(integer) --* 
        
              The interval for publishing the access logs. You can specify an interval of either 5 minutes or 60 minutes.
        
              Default: 60 minutes
        
            - **S3BucketPrefix** *(string) --* 
        
              The logical hierarchy you created for your Amazon S3 bucket, for example ``my-bucket-prefix/prod`` . If the prefix is not provided, the log is placed at the root level of the bucket.
        
          - **ConnectionDraining** *(dict) --* 
        
            If enabled, the load balancer allows existing requests to complete before the load balancer shifts traffic away from a deregistered or unhealthy instance.
        
            For more information, see `Configure Connection Draining <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-conn-drain.html>`__ in the *Classic Load Balancers Guide* .
        
            - **Enabled** *(boolean) --* **[REQUIRED]** 
        
              Specifies whether connection draining is enabled for the load balancer.
        
            - **Timeout** *(integer) --* 
        
              The maximum time, in seconds, to keep the existing connections open before deregistering the instances.
        
          - **ConnectionSettings** *(dict) --* 
        
            If enabled, the load balancer allows the connections to remain idle (no data is sent over the connection) for the specified duration.
        
            By default, Elastic Load Balancing maintains a 60-second idle connection timeout for both front-end and back-end connections of your load balancer. For more information, see `Configure Idle Connection Timeout <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-idle-timeout.html>`__ in the *Classic Load Balancers Guide* .
        
            - **IdleTimeout** *(integer) --* **[REQUIRED]** 
        
              The time, in seconds, that the connection is allowed to be idle (no data has been sent over the connection) before it is closed by the load balancer.
        
          - **AdditionalAttributes** *(list) --* 
        
            This parameter is reserved.
        
            - *(dict) --* 
        
              This data type is reserved.
        
              - **Key** *(string) --* 
        
                This parameter is reserved.
        
              - **Value** *(string) --* 
        
                This parameter is reserved.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'LoadBalancerName\': \'string\',
                \'LoadBalancerAttributes\': {
                    \'CrossZoneLoadBalancing\': {
                        \'Enabled\': True|False
                    },
                    \'AccessLog\': {
                        \'Enabled\': True|False,
                        \'S3BucketName\': \'string\',
                        \'EmitInterval\': 123,
                        \'S3BucketPrefix\': \'string\'
                    },
                    \'ConnectionDraining\': {
                        \'Enabled\': True|False,
                        \'Timeout\': 123
                    },
                    \'ConnectionSettings\': {
                        \'IdleTimeout\': 123
                    },
                    \'AdditionalAttributes\': [
                        {
                            \'Key\': \'string\',
                            \'Value\': \'string\'
                        },
                    ]
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of ModifyLoadBalancerAttributes.
        
            - **LoadBalancerName** *(string) --* 
        
              The name of the load balancer.
        
            - **LoadBalancerAttributes** *(dict) --* 
        
              Information about the load balancer attributes.
        
              - **CrossZoneLoadBalancing** *(dict) --* 
        
                If enabled, the load balancer routes the request traffic evenly across all instances regardless of the Availability Zones.
        
                For more information, see `Configure Cross-Zone Load Balancing <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html>`__ in the *Classic Load Balancers Guide* .
        
                - **Enabled** *(boolean) --* 
        
                  Specifies whether cross-zone load balancing is enabled for the load balancer.
        
              - **AccessLog** *(dict) --* 
        
                If enabled, the load balancer captures detailed information of all requests and delivers the information to the Amazon S3 bucket that you specify.
        
                For more information, see `Enable Access Logs <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-access-logs.html>`__ in the *Classic Load Balancers Guide* .
        
                - **Enabled** *(boolean) --* 
        
                  Specifies whether access logs are enabled for the load balancer.
        
                - **S3BucketName** *(string) --* 
        
                  The name of the Amazon S3 bucket where the access logs are stored.
        
                - **EmitInterval** *(integer) --* 
        
                  The interval for publishing the access logs. You can specify an interval of either 5 minutes or 60 minutes.
        
                  Default: 60 minutes
        
                - **S3BucketPrefix** *(string) --* 
        
                  The logical hierarchy you created for your Amazon S3 bucket, for example ``my-bucket-prefix/prod`` . If the prefix is not provided, the log is placed at the root level of the bucket.
        
              - **ConnectionDraining** *(dict) --* 
        
                If enabled, the load balancer allows existing requests to complete before the load balancer shifts traffic away from a deregistered or unhealthy instance.
        
                For more information, see `Configure Connection Draining <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-conn-drain.html>`__ in the *Classic Load Balancers Guide* .
        
                - **Enabled** *(boolean) --* 
        
                  Specifies whether connection draining is enabled for the load balancer.
        
                - **Timeout** *(integer) --* 
        
                  The maximum time, in seconds, to keep the existing connections open before deregistering the instances.
        
              - **ConnectionSettings** *(dict) --* 
        
                If enabled, the load balancer allows the connections to remain idle (no data is sent over the connection) for the specified duration.
        
                By default, Elastic Load Balancing maintains a 60-second idle connection timeout for both front-end and back-end connections of your load balancer. For more information, see `Configure Idle Connection Timeout <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-idle-timeout.html>`__ in the *Classic Load Balancers Guide* .
        
                - **IdleTimeout** *(integer) --* 
        
                  The time, in seconds, that the connection is allowed to be idle (no data has been sent over the connection) before it is closed by the load balancer.
        
              - **AdditionalAttributes** *(list) --* 
        
                This parameter is reserved.
        
                - *(dict) --* 
        
                  This data type is reserved.
        
                  - **Key** *(string) --* 
        
                    This parameter is reserved.
        
                  - **Value** *(string) --* 
        
                    This parameter is reserved.
        
        """
        pass

    def register_instances_with_load_balancer(self, LoadBalancerName: str, Instances: List) -> Dict:
        """
        
        The instance must be a running instance in the same network as the load balancer (EC2-Classic or the same VPC). If you have EC2-Classic instances and a load balancer in a VPC with ClassicLink enabled, you can link the EC2-Classic instances to that VPC and then register the linked EC2-Classic instances with the load balancer in the VPC.
        
        Note that ``RegisterInstanceWithLoadBalancer`` completes when the request has been registered. Instance registration takes a little time to complete. To check the state of the registered instances, use  DescribeLoadBalancers or  DescribeInstanceHealth .
        
        After the instance is registered, it starts receiving traffic and requests from the load balancer. Any instance that is not in one of the Availability Zones registered for the load balancer is moved to the ``OutOfService`` state. If an Availability Zone is added to the load balancer later, any instances registered with the load balancer move to the ``InService`` state.
        
        To deregister instances from a load balancer, use  DeregisterInstancesFromLoadBalancer .
        
        For more information, see `Register or De-Register EC2 Instances <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-deregister-register-instances.html>`__ in the *Classic Load Balancers Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/RegisterInstancesWithLoadBalancer>`_
        
        **Request Syntax** 
        ::
        
          response = client.register_instances_with_load_balancer(
              LoadBalancerName=\'string\',
              Instances=[
                  {
                      \'InstanceId\': \'string\'
                  },
              ]
          )
        :type LoadBalancerName: string
        :param LoadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
        :type Instances: list
        :param Instances: **[REQUIRED]** 
        
          The IDs of the instances.
        
          - *(dict) --* 
        
            The ID of an EC2 instance.
        
            - **InstanceId** *(string) --* 
        
              The instance ID.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Instances\': [
                    {
                        \'InstanceId\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of RegisterInstancesWithLoadBalancer.
        
            - **Instances** *(list) --* 
        
              The updated list of instances for the load balancer.
        
              - *(dict) --* 
        
                The ID of an EC2 instance.
        
                - **InstanceId** *(string) --* 
        
                  The instance ID.
        
        """
        pass

    def remove_tags(self, LoadBalancerNames: List, Tags: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/RemoveTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.remove_tags(
              LoadBalancerNames=[
                  \'string\',
              ],
              Tags=[
                  {
                      \'Key\': \'string\'
                  },
              ]
          )
        :type LoadBalancerNames: list
        :param LoadBalancerNames: **[REQUIRED]** 
        
          The name of the load balancer. You can specify a maximum of one load balancer name.
        
          - *(string) --* 
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          The list of tag keys to remove.
        
          - *(dict) --* 
        
            The key of a tag.
        
            - **Key** *(string) --* 
        
              The name of the key.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of RemoveTags.
        
        """
        pass

    def set_load_balancer_listener_ssl_certificate(self, LoadBalancerName: str, LoadBalancerPort: int, SSLCertificateId: str) -> Dict:
        """
        
        For more information about updating your SSL certificate, see `Replace the SSL Certificate for Your Load Balancer <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-update-ssl-cert.html>`__ in the *Classic Load Balancers Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/SetLoadBalancerListenerSSLCertificate>`_
        
        **Request Syntax** 
        ::
        
          response = client.set_load_balancer_listener_ssl_certificate(
              LoadBalancerName=\'string\',
              LoadBalancerPort=123,
              SSLCertificateId=\'string\'
          )
        :type LoadBalancerName: string
        :param LoadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
        :type LoadBalancerPort: integer
        :param LoadBalancerPort: **[REQUIRED]** 
        
          The port that uses the specified SSL certificate.
        
        :type SSLCertificateId: string
        :param SSLCertificateId: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the SSL certificate.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of SetLoadBalancerListenerSSLCertificate.
        
        """
        pass

    def set_load_balancer_policies_for_backend_server(self, LoadBalancerName: str, InstancePort: int, PolicyNames: List) -> Dict:
        """
        
        Each time you use ``SetLoadBalancerPoliciesForBackendServer`` to enable the policies, use the ``PolicyNames`` parameter to list the policies that you want to enable.
        
        You can use  DescribeLoadBalancers or  DescribeLoadBalancerPolicies to verify that the policy is associated with the EC2 instance.
        
        For more information about enabling back-end instance authentication, see `Configure Back-end Instance Authentication <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-create-https-ssl-load-balancer.html#configure_backendauth_clt>`__ in the *Classic Load Balancers Guide* . For more information about Proxy Protocol, see `Configure Proxy Protocol Support <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-proxy-protocol.html>`__ in the *Classic Load Balancers Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/SetLoadBalancerPoliciesForBackendServer>`_
        
        **Request Syntax** 
        ::
        
          response = client.set_load_balancer_policies_for_backend_server(
              LoadBalancerName=\'string\',
              InstancePort=123,
              PolicyNames=[
                  \'string\',
              ]
          )
        :type LoadBalancerName: string
        :param LoadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
        :type InstancePort: integer
        :param InstancePort: **[REQUIRED]** 
        
          The port number associated with the EC2 instance.
        
        :type PolicyNames: list
        :param PolicyNames: **[REQUIRED]** 
        
          The names of the policies. If the list is empty, then all current polices are removed from the EC2 instance.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of SetLoadBalancerPoliciesForBackendServer.
        
        """
        pass

    def set_load_balancer_policies_of_listener(self, LoadBalancerName: str, LoadBalancerPort: int, PolicyNames: List) -> Dict:
        """
        
        To enable back-end server authentication, use  SetLoadBalancerPoliciesForBackendServer .
        
        For more information about setting policies, see `Update the SSL Negotiation Configuration <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/ssl-config-update.html>`__ , `Duration-Based Session Stickiness <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-sticky-sessions.html#enable-sticky-sessions-duration>`__ , and `Application-Controlled Session Stickiness <http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-sticky-sessions.html#enable-sticky-sessions-application>`__ in the *Classic Load Balancers Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancing-2012-06-01/SetLoadBalancerPoliciesOfListener>`_
        
        **Request Syntax** 
        ::
        
          response = client.set_load_balancer_policies_of_listener(
              LoadBalancerName=\'string\',
              LoadBalancerPort=123,
              PolicyNames=[
                  \'string\',
              ]
          )
        :type LoadBalancerName: string
        :param LoadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
        :type LoadBalancerPort: integer
        :param LoadBalancerPort: **[REQUIRED]** 
        
          The external port of the load balancer.
        
        :type PolicyNames: list
        :param PolicyNames: **[REQUIRED]** 
        
          The names of the policies. This list must include all policies to be enabled. If you omit a policy that is currently enabled, it is disabled. If the list is empty, all current policies are disabled.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of SetLoadBalancePoliciesOfListener.
        
        """
        pass
