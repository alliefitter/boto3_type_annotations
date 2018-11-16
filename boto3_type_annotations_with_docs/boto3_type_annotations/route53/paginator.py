from typing import Dict
from botocore.paginate import Paginator


class ListHealthChecks(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListHealthChecks>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
                \'HealthChecks\': [
                    {
                        \'Id\': \'string\',
                        \'CallerReference\': \'string\',
                        \'LinkedService\': {
                            \'ServicePrincipal\': \'string\',
                            \'Description\': \'string\'
                        },
                        \'HealthCheckConfig\': {
                            \'IPAddress\': \'string\',
                            \'Port\': 123,
                            \'Type\': \'HTTP\'|\'HTTPS\'|\'HTTP_STR_MATCH\'|\'HTTPS_STR_MATCH\'|\'TCP\'|\'CALCULATED\'|\'CLOUDWATCH_METRIC\',
                            \'ResourcePath\': \'string\',
                            \'FullyQualifiedDomainName\': \'string\',
                            \'SearchString\': \'string\',
                            \'RequestInterval\': 123,
                            \'FailureThreshold\': 123,
                            \'MeasureLatency\': True|False,
                            \'Inverted\': True|False,
                            \'Disabled\': True|False,
                            \'HealthThreshold\': 123,
                            \'ChildHealthChecks\': [
                                \'string\',
                            ],
                            \'EnableSNI\': True|False,
                            \'Regions\': [
                                \'us-east-1\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'sa-east-1\',
                            ],
                            \'AlarmIdentifier\': {
                                \'Region\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'ca-central-1\'|\'eu-central-1\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'|\'ap-northeast-3\'|\'sa-east-1\',
                                \'Name\': \'string\'
                            },
                            \'InsufficientDataHealthStatus\': \'Healthy\'|\'Unhealthy\'|\'LastKnownStatus\'
                        },
                        \'HealthCheckVersion\': 123,
                        \'CloudWatchAlarmConfiguration\': {
                            \'EvaluationPeriods\': 123,
                            \'Threshold\': 123.0,
                            \'ComparisonOperator\': \'GreaterThanOrEqualToThreshold\'|\'GreaterThanThreshold\'|\'LessThanThreshold\'|\'LessThanOrEqualToThreshold\',
                            \'Period\': 123,
                            \'MetricName\': \'string\',
                            \'Namespace\': \'string\',
                            \'Statistic\': \'Average\'|\'Sum\'|\'SampleCount\'|\'Maximum\'|\'Minimum\',
                            \'Dimensions\': [
                                {
                                    \'Name\': \'string\',
                                    \'Value\': \'string\'
                                },
                            ]
                        }
                    },
                ],
                \'Marker\': \'string\',
                \'IsTruncated\': True|False,
                \'MaxItems\': \'string\',
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            A complex type that contains the response to a ``ListHealthChecks`` request.
        
            - **HealthChecks** *(list) --* 
        
              A complex type that contains one ``HealthCheck`` element for each health check that is associated with the current AWS account.
        
              - *(dict) --* 
        
                A complex type that contains information about one health check that is associated with the current AWS account.
        
                - **Id** *(string) --* 
        
                  The identifier that Amazon Route 53assigned to the health check when you created it. When you add or update a resource record set, you use this value to specify which health check to use. The value can be up to 64 characters long. 
        
                - **CallerReference** *(string) --* 
        
                  A unique string that you specified when you created the health check.
        
                - **LinkedService** *(dict) --* 
        
                  If the health check was created by another service, the service that created the health check. When a health check is created by another service, you can\'t edit or delete it using Amazon Route 53. 
        
                  - **ServicePrincipal** *(string) --* 
        
                    If the health check or hosted zone was created by another service, the service that created the resource. When a resource is created by another service, you can\'t edit or delete it using Amazon Route 53. 
        
                  - **Description** *(string) --* 
        
                    If the health check or hosted zone was created by another service, an optional description that can be provided by the other service. When a resource is created by another service, you can\'t edit or delete it using Amazon Route 53. 
        
                - **HealthCheckConfig** *(dict) --* 
        
                  A complex type that contains detailed information about one health check.
        
                  - **IPAddress** *(string) --* 
        
                    The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform health checks on. If you don\'t specify a value for ``IPAddress`` , Route 53 sends a DNS request to resolve the domain name that you specify in ``FullyQualifiedDomainName`` at the interval that you specify in ``RequestInterval`` . Using an IP address returned by DNS, Route 53 then checks the health of the endpoint.
        
                    Use one of the following formats for the value of ``IPAddress`` : 
        
                    * **IPv4 address** : four values between 0 and 255, separated by periods (.), for example, ``192.0.2.44`` . 
                     
                    * **IPv6 address** : eight groups of four hexadecimal values, separated by colons (:), for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . You can also shorten IPv6 addresses as described in RFC 5952, for example, ``2001:db8:85a3::abcd:1:2345`` . 
                     
                    If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address, associate it with your EC2 instance, and specify the Elastic IP address for ``IPAddress`` . This ensures that the IP address of your instance will never change.
        
                    For more information, see  HealthCheckConfig$FullyQualifiedDomainName .
        
                    Constraints: Route 53 can\'t check the health of endpoints for which the IP address is in local, private, non-routable, or multicast ranges. For more information about IP addresses for which you can\'t create health checks, see the following documents:
        
                    * `RFC 5735, Special Use IPv4 Addresses <https://tools.ietf.org/html/rfc5735>`__   
                     
                    * `RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space <https://tools.ietf.org/html/rfc6598>`__   
                     
                    * `RFC 5156, Special-Use IPv6 Addresses <https://tools.ietf.org/html/rfc5156>`__   
                     
                    When the value of ``Type`` is ``CALCULATED`` or ``CLOUDWATCH_METRIC`` , omit ``IPAddress`` .
        
                  - **Port** *(integer) --* 
        
                    The port on the endpoint on which you want Amazon Route 53 to perform health checks. Specify a value for ``Port`` only when you specify a value for ``IPAddress`` .
        
                  - **Type** *(string) --* 
        
                    The type of health check that you want to create, which indicates how Amazon Route 53 determines whether an endpoint is healthy.
        
                    .. warning::
        
                      You can\'t change the value of ``Type`` after you create a health check.
        
                    You can create the following types of health checks:
        
                    * **HTTP** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400. 
                     
                    * **HTTPS** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400. 
        
                    .. warning::
        
                       If you specify ``HTTPS`` for the value of ``Type`` , the endpoint must support TLS v1.0 or later. 
        
                    * **HTTP_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and searches the first 5,120 bytes of the response body for the string that you specify in ``SearchString`` . 
                     
                    * **HTTPS_STR_MATCH** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an ``HTTPS`` request and searches the first 5,120 bytes of the response body for the string that you specify in ``SearchString`` . 
                     
                    * **TCP** : Route 53 tries to establish a TCP connection. 
                     
                    * **CLOUDWATCH_METRIC** : The health check is associated with a CloudWatch alarm. If the state of the alarm is ``OK`` , the health check is considered healthy. If the state is ``ALARM`` , the health check is considered unhealthy. If CloudWatch doesn\'t have sufficient data to determine whether the state is ``OK`` or ``ALARM`` , the health check status depends on the setting for ``InsufficientDataHealthStatus`` : ``Healthy`` , ``Unhealthy`` , or ``LastKnownStatus`` .  
                     
                    * **CALCULATED** : For health checks that monitor the status of other health checks, Route 53 adds up the number of health checks that Route 53 health checkers consider to be healthy and compares that number with the value of ``HealthThreshold`` .  
                     
                    For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Amazon Route 53 Developer Guide* .
        
                  - **ResourcePath** *(string) --* 
        
                    The path, if any, that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example, the file /docs/route53-health-check.html. You can also include query string parameters, for example, ``/welcome.html?language=jp&login=y`` . 
        
                  - **FullyQualifiedDomainName** *(string) --* 
        
                    Amazon Route 53 behavior depends on whether you specify a value for ``IPAddress`` .
        
                     **If you specify a value for**  ``IPAddress`` :
        
                    Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header for all health checks except TCP health checks. This is typically the fully qualified DNS name of the endpoint on which you want Route 53 to perform health checks.
        
                    When Route 53 checks the health of an endpoint, here is how it constructs the ``Host`` header:
        
                    * If you specify a value of ``80`` for ``Port`` and ``HTTP`` or ``HTTP_STR_MATCH`` for ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in the Host header.  
                     
                    * If you specify a value of ``443`` for ``Port`` and ``HTTPS`` or ``HTTPS_STR_MATCH`` for ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in the ``Host`` header. 
                     
                    * If you specify another value for ``Port`` and any value except ``TCP`` for ``Type`` , Route 53 passes ``FullyQualifiedDomainName:Port`` to the endpoint in the ``Host`` header. 
                     
                    If you don\'t specify a value for ``FullyQualifiedDomainName`` , Route 53 substitutes the value of ``IPAddress`` in the ``Host`` header in each of the preceding cases.
        
                     **If you don\'t specify a value for ``IPAddress`` ** :
        
                    Route 53 sends a DNS request to the domain that you specify for ``FullyQualifiedDomainName`` at the interval that you specify for ``RequestInterval`` . Using an IPv4 address that DNS returns, Route 53 then checks the health of the endpoint.
        
                    .. note::
        
                      If you don\'t specify a value for ``IPAddress`` , Route 53 uses only IPv4 to send health checks to the endpoint. If there\'s no resource record set with a type of A for the name that you specify for ``FullyQualifiedDomainName`` , the health check fails with a \"DNS resolution failed\" error.
        
                    If you want to check the health of weighted, latency, or failover resource record sets and you choose to specify the endpoint only by ``FullyQualifiedDomainName`` , we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com. For the value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as us-east-2-www.example.com), not the name of the resource record sets (www.example.com).
        
                    .. warning::
        
                      In this configuration, if you create a health check for which the value of ``FullyQualifiedDomainName`` matches the name of the resource record sets and you then associate the health check with those resource record sets, health check results will be unpredictable.
        
                    In addition, if the value that you specify for ``Type`` is ``HTTP`` , ``HTTPS`` , ``HTTP_STR_MATCH`` , or ``HTTPS_STR_MATCH`` , Route 53 passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header, as it does when you specify a value for ``IPAddress`` . If the value of ``Type`` is ``TCP`` , Route 53 doesn\'t pass a ``Host`` header.
        
                  - **SearchString** *(string) --* 
        
                    If the value of Type is ``HTTP_STR_MATCH`` or ``HTTP_STR_MATCH`` , the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the response body, Route 53 considers the resource healthy.
        
                    Route 53 considers case when searching for ``SearchString`` in the response body. 
        
                  - **RequestInterval** *(integer) --* 
        
                    The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health check request. Each Route 53 health checker makes requests at this interval.
        
                    .. warning::
        
                      You can\'t change the value of ``RequestInterval`` after you create a health check.
        
                    If you don\'t specify a value for ``RequestInterval`` , the default value is ``30`` seconds.
        
                  - **FailureThreshold** *(integer) --* 
        
                    The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Amazon Route 53 Developer Guide* .
        
                    If you don\'t specify a value for ``FailureThreshold`` , the default value is three health checks.
        
                  - **MeasureLatency** *(boolean) --* 
        
                    Specify whether you want Amazon Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on the **Health Checks** page in the Route 53 console.
        
                    .. warning::
        
                      You can\'t change the value of ``MeasureLatency`` after you create a health check.
        
                  - **Inverted** *(boolean) --* 
        
                    Specify whether you want Amazon Route 53 to invert the status of a health check, for example, to consider a health check unhealthy when it otherwise would be considered healthy.
        
                  - **Disabled** *(boolean) --* 
        
                    Stops Route 53 from performing health checks. When you disable a health check, here\'s what happens:
        
                    * **Health checks that check the health of endpoints:** Route 53 stops submitting requests to your application, server, or other resource. 
                     
                    * **Calculated health checks:** Route 53 stops aggregating the status of the referenced health checks. 
                     
                    * **Health checks that monitor CloudWatch alarms:** Route 53 stops monitoring the corresponding CloudWatch metrics. 
                     
                    After you disable a health check, Route 53 considers the status of the health check to always be healthy. If you configured DNS failover, Route 53 continues to route traffic to the corresponding resources. If you want to stop routing traffic to a resource, change the value of  UpdateHealthCheckRequest$Inverted .
        
                    Charges for a health check still apply when the health check is disabled. For more information, see `Amazon Route 53 Pricing <http://aws.amazon.com/route53/pricing/>`__ .
        
                  - **HealthThreshold** *(integer) --* 
        
                    The number of child health checks that are associated with a ``CALCULATED`` health that Amazon Route 53 must consider healthy for the ``CALCULATED`` health check to be considered healthy. To specify the child health checks that you want to associate with a ``CALCULATED`` health check, use the  HealthCheckConfig$ChildHealthChecks and  HealthCheckConfig$ChildHealthChecks elements.
        
                    Note the following:
        
                    * If you specify a number greater than the number of child health checks, Route 53 always considers this health check to be unhealthy. 
                     
                    * If you specify ``0`` , Route 53 always considers this health check to be healthy. 
                     
                  - **ChildHealthChecks** *(list) --* 
        
                    (CALCULATED Health Checks Only) A complex type that contains one ``ChildHealthCheck`` element for each health check that you want to associate with a ``CALCULATED`` health check.
        
                    - *(string) --* 
                
                  - **EnableSNI** *(boolean) --* 
        
                    Specify whether you want Amazon Route 53 to send the value of ``FullyQualifiedDomainName`` to the endpoint in the ``client_hello`` message during TLS negotiation. This allows the endpoint to respond to ``HTTPS`` health check requests with the applicable SSL/TLS certificate.
        
                    Some endpoints require that ``HTTPS`` requests include the host name in the ``client_hello`` message. If you don\'t enable SNI, the status of the health check will be ``SSL alert handshake_failure`` . A health check can also have that status for other reasons. If SNI is enabled and you\'re still getting the error, check the SSL/TLS configuration on your endpoint and confirm that your certificate is valid.
        
                    The SSL/TLS certificate on your endpoint includes a domain name in the ``Common Name`` field and possibly several more in the ``Subject Alternative Names`` field. One of the domain names in the certificate should match the value that you specify for ``FullyQualifiedDomainName`` . If the endpoint responds to the ``client_hello`` message with a certificate that does not include the domain name that you specified in ``FullyQualifiedDomainName`` , a health checker will retry the handshake. In the second attempt, the health checker will omit ``FullyQualifiedDomainName`` from the ``client_hello`` message.
        
                  - **Regions** *(list) --* 
        
                    A complex type that contains one ``Region`` element for each region from which you want Amazon Route 53 health checkers to check the specified endpoint.
        
                    If you don\'t specify any regions, Route 53 health checkers automatically performs checks from all of the regions that are listed under **Valid Values** .
        
                    If you update a health check to remove a region that has been performing health checks, Route 53 will briefly continue to perform checks from that region to ensure that some health checkers are always checking the endpoint (for example, if you replace three regions with four different regions). 
        
                    - *(string) --* 
                
                  - **AlarmIdentifier** *(dict) --* 
        
                    A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether the specified health check is healthy.
        
                    - **Region** *(string) --* 
        
                      For the CloudWatch alarm that you want Route 53 health checkers to use to determine whether this health check is healthy, the region that the alarm was created in.
        
                      For the current list of CloudWatch regions, see `Amazon CloudWatch <http://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region>`__ in the *AWS Regions and Endpoints* chapter of the *Amazon Web Services General Reference* .
        
                    - **Name** *(string) --* 
        
                      The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.
        
                      .. note::
        
                        Route 53 supports CloudWatch alarms with the following features:
        
                        * Standard-resolution metrics. High-resolution metrics aren\'t supported. For more information, see `High-Resolution Metrics <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`__ in the *Amazon CloudWatch User Guide* . 
                         
                        * Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics aren\'t supported. 
                         
                  - **InsufficientDataHealthStatus** *(string) --* 
        
                    When CloudWatch has insufficient data about the metric to determine the alarm state, the status that you want Amazon Route 53 to assign to the health check:
        
                    * ``Healthy`` : Route 53 considers the health check to be healthy. 
                     
                    * ``Unhealthy`` : Route 53 considers the health check to be unhealthy. 
                     
                    * ``LastKnownStatus`` : Route 53 uses the status of the health check from the last time that CloudWatch had sufficient data to determine the alarm state. For new health checks that have no last known status, the default status for the health check is healthy. 
                     
                - **HealthCheckVersion** *(integer) --* 
        
                  The version of the health check. You can optionally pass this value in a call to ``UpdateHealthCheck`` to prevent overwriting another change to the health check.
        
                - **CloudWatchAlarmConfiguration** *(dict) --* 
        
                  A complex type that contains information about the CloudWatch alarm that Amazon Route 53 is monitoring for this health check.
        
                  - **EvaluationPeriods** *(integer) --* 
        
                    For the metric that the CloudWatch alarm is associated with, the number of periods that the metric is compared to the threshold.
        
                  - **Threshold** *(float) --* 
        
                    For the metric that the CloudWatch alarm is associated with, the value the metric is compared with.
        
                  - **ComparisonOperator** *(string) --* 
        
                    For the metric that the CloudWatch alarm is associated with, the arithmetic operation that is used for the comparison.
        
                  - **Period** *(integer) --* 
        
                    For the metric that the CloudWatch alarm is associated with, the duration of one evaluation period in seconds.
        
                  - **MetricName** *(string) --* 
        
                    The name of the CloudWatch metric that the alarm is associated with.
        
                  - **Namespace** *(string) --* 
        
                    The namespace of the metric that the alarm is associated with. For more information, see `Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__ in the *Amazon CloudWatch User Guide* .
        
                  - **Statistic** *(string) --* 
        
                    For the metric that the CloudWatch alarm is associated with, the statistic that is applied to the metric.
        
                  - **Dimensions** *(list) --* 
        
                    For the metric that the CloudWatch alarm is associated with, a complex type that contains information about the dimensions for the metric. For information, see `Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html>`__ in the *Amazon CloudWatch User Guide* .
        
                    - *(dict) --* 
        
                      For the metric that the CloudWatch alarm is associated with, a complex type that contains information about one dimension.
        
                      - **Name** *(string) --* 
        
                        For the metric that the CloudWatch alarm is associated with, the name of one dimension.
        
                      - **Value** *(string) --* 
        
                        For the metric that the CloudWatch alarm is associated with, the value of one dimension.
        
            - **Marker** *(string) --* 
        
              For the second and subsequent calls to ``ListHealthChecks`` , ``Marker`` is the value that you specified for the ``marker`` parameter in the previous request.
        
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether there are more health checks to be listed. If the response was truncated, you can get the next group of health checks by submitting another ``ListHealthChecks`` request and specifying the value of ``NextMarker`` in the ``marker`` parameter.
        
            - **MaxItems** *(string) --* 
        
              The value that you specified for the ``maxitems`` parameter in the call to ``ListHealthChecks`` that produced the current response.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListHostedZones(Paginator):
    def paginate(self, DelegationSetId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListHostedZones>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DelegationSetId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type DelegationSetId: string
        :param DelegationSetId: 
        
          If you\'re using reusable delegation sets and you want to list all of the hosted zones that are associated with a reusable delegation set, specify the ID of that reusable delegation set. 
        
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
                \'HostedZones\': [
                    {
                        \'Id\': \'string\',
                        \'Name\': \'string\',
                        \'CallerReference\': \'string\',
                        \'Config\': {
                            \'Comment\': \'string\',
                            \'PrivateZone\': True|False
                        },
                        \'ResourceRecordSetCount\': 123,
                        \'LinkedService\': {
                            \'ServicePrincipal\': \'string\',
                            \'Description\': \'string\'
                        }
                    },
                ],
                \'Marker\': \'string\',
                \'IsTruncated\': True|False,
                \'MaxItems\': \'string\',
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **HostedZones** *(list) --* 
        
              A complex type that contains general information about the hosted zone.
        
              - *(dict) --* 
        
                A complex type that contains general information about the hosted zone.
        
                - **Id** *(string) --* 
        
                  The ID that Amazon Route 53 assigned to the hosted zone when you created it.
        
                - **Name** *(string) --* 
        
                  The name of the domain. For public hosted zones, this is the name that you have registered with your DNS registrar.
        
                  For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-`` (hyphen) and how to specify internationalized domain names, see  CreateHostedZone .
        
                - **CallerReference** *(string) --* 
        
                  The value that you specified for ``CallerReference`` when you created the hosted zone.
        
                - **Config** *(dict) --* 
        
                  A complex type that includes the ``Comment`` and ``PrivateZone`` elements. If you omitted the ``HostedZoneConfig`` and ``Comment`` elements from the request, the ``Config`` and ``Comment`` elements don\'t appear in the response.
        
                  - **Comment** *(string) --* 
        
                    Any comments that you want to include about the hosted zone.
        
                  - **PrivateZone** *(boolean) --* 
        
                    A value that indicates whether this is a private hosted zone.
        
                - **ResourceRecordSetCount** *(integer) --* 
        
                  The number of resource record sets in the hosted zone.
        
                - **LinkedService** *(dict) --* 
        
                  If the hosted zone was created by another service, the service that created the hosted zone. When a hosted zone is created by another service, you can\'t edit or delete it using Route 53. 
        
                  - **ServicePrincipal** *(string) --* 
        
                    If the health check or hosted zone was created by another service, the service that created the resource. When a resource is created by another service, you can\'t edit or delete it using Amazon Route 53. 
        
                  - **Description** *(string) --* 
        
                    If the health check or hosted zone was created by another service, an optional description that can be provided by the other service. When a resource is created by another service, you can\'t edit or delete it using Amazon Route 53. 
        
            - **Marker** *(string) --* 
        
              For the second and subsequent calls to ``ListHostedZones`` , ``Marker`` is the value that you specified for the ``marker`` parameter in the request that produced the current response.
        
            - **IsTruncated** *(boolean) --* 
        
              A flag indicating whether there are more hosted zones to be listed. If the response was truncated, you can get more hosted zones by submitting another ``ListHostedZones`` request and specifying the value of ``NextMarker`` in the ``marker`` parameter.
        
            - **MaxItems** *(string) --* 
        
              The value that you specified for the ``maxitems`` parameter in the call to ``ListHostedZones`` that produced the current response.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListResourceRecordSets(Paginator):
    def paginate(self, HostedZoneId: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListResourceRecordSets>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              HostedZoneId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type HostedZoneId: string
        :param HostedZoneId: **[REQUIRED]** 
        
          The ID of the hosted zone that contains the resource record sets that you want to list.
        
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
                \'ResourceRecordSets\': [
                    {
                        \'Name\': \'string\',
                        \'Type\': \'SOA\'|\'A\'|\'TXT\'|\'NS\'|\'CNAME\'|\'MX\'|\'NAPTR\'|\'PTR\'|\'SRV\'|\'SPF\'|\'AAAA\'|\'CAA\',
                        \'SetIdentifier\': \'string\',
                        \'Weight\': 123,
                        \'Region\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'ca-central-1\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'|\'ap-northeast-3\'|\'sa-east-1\'|\'cn-north-1\'|\'cn-northwest-1\'|\'ap-south-1\',
                        \'GeoLocation\': {
                            \'ContinentCode\': \'string\',
                            \'CountryCode\': \'string\',
                            \'SubdivisionCode\': \'string\'
                        },
                        \'Failover\': \'PRIMARY\'|\'SECONDARY\',
                        \'MultiValueAnswer\': True|False,
                        \'TTL\': 123,
                        \'ResourceRecords\': [
                            {
                                \'Value\': \'string\'
                            },
                        ],
                        \'AliasTarget\': {
                            \'HostedZoneId\': \'string\',
                            \'DNSName\': \'string\',
                            \'EvaluateTargetHealth\': True|False
                        },
                        \'HealthCheckId\': \'string\',
                        \'TrafficPolicyInstanceId\': \'string\'
                    },
                ],
                \'IsTruncated\': True|False,
                \'MaxItems\': \'string\',
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            A complex type that contains list information for the resource record set.
        
            - **ResourceRecordSets** *(list) --* 
        
              Information about multiple resource record sets.
        
              - *(dict) --* 
        
                Information about the resource record set to create or delete.
        
                - **Name** *(string) --* 
        
                  For ``ChangeResourceRecordSets`` requests, the name of the record that you want to create, update, or delete. For ``ListResourceRecordSets`` responses, the name of a record in the specified hosted zone.
        
                   **ChangeResourceRecordSets Only**  
        
                  Enter a fully qualified domain name, for example, ``www.example.com`` . You can optionally include a trailing dot. If you omit the trailing dot, Amazon Route 53 assumes that the domain name that you specify is fully qualified. This means that Route 53 treats ``www.example.com`` (without a trailing dot) and ``www.example.com.`` (with a trailing dot) as identical.
        
                  For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-`` (hyphen) and how to specify internationalized domain names, see `DNS Domain Name Format <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html>`__ in the *Amazon Route 53 Developer Guide* .
        
                  You can use the asterisk (*) wildcard to replace the leftmost label in a domain name, for example, ``*.example.com`` . Note the following:
        
                  * The * must replace the entire label. For example, you can\'t specify ``*prod.example.com`` or ``prod*.example.com`` . 
                   
                  * The * can\'t replace any of the middle labels, for example, marketing.*.example.com. 
                   
                  * If you include * in any position other than the leftmost label in a domain name, DNS treats it as an * character (ASCII 42), not as a wildcard. 
        
                  .. warning::
        
                     You can\'t use the * wildcard for resource records sets that have a type of NS. 
        
                  You can use the * wildcard as the leftmost label in a domain name, for example, ``*.example.com`` . You can\'t use an * for one of the middle labels, for example, ``marketing.*.example.com`` . In addition, the * must replace the entire label; for example, you can\'t specify ``prod*.example.com`` .
        
                - **Type** *(string) --* 
        
                  The DNS record type. For information about different record types and how data is encoded for them, see `Supported DNS Resource Record Types <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html>`__ in the *Amazon Route 53 Developer Guide* .
        
                  Valid values for basic resource record sets: ``A`` | ``AAAA`` | ``CAA`` | ``CNAME`` | ``MX`` | ``NAPTR`` | ``NS`` | ``PTR`` | ``SOA`` | ``SPF`` | ``SRV`` | ``TXT``  
        
                  Values for weighted, latency, geolocation, and failover resource record sets: ``A`` | ``AAAA`` | ``CAA`` | ``CNAME`` | ``MX`` | ``NAPTR`` | ``PTR`` | ``SPF`` | ``SRV`` | ``TXT`` . When creating a group of weighted, latency, geolocation, or failover resource record sets, specify the same value for all of the resource record sets in the group.
        
                  Valid values for multivalue answer resource record sets: ``A`` | ``AAAA`` | ``MX`` | ``NAPTR`` | ``PTR`` | ``SPF`` | ``SRV`` | ``TXT``  
        
                  .. note::
        
                    SPF records were formerly used to verify the identity of the sender of email messages. However, we no longer recommend that you create resource record sets for which the value of ``Type`` is ``SPF`` . RFC 7208, *Sender Policy Framework (SPF) for Authorizing Use of Domains in Email, Version 1* , has been updated to say, \"...[I]ts existence and mechanism defined in [RFC4408] have led to some interoperability issues. Accordingly, its use is no longer appropriate for SPF version 1; implementations are not to use it.\" In RFC 7208, see section 14.1, `The SPF DNS Record Type <http://tools.ietf.org/html/rfc7208#section-14.1>`__ .
        
                  Values for alias resource record sets:
        
                  * **CloudFront distributions:**  ``A``   If IPv6 is enabled for the distribution, create two resource record sets to route traffic to your distribution, one with a value of ``A`` and one with a value of ``AAAA`` .  
                   
                  * **AWS Elastic Beanstalk environment that has a regionalized subdomain** : ``A``   
                   
                  * **ELB load balancers:**  ``A`` | ``AAAA``   
                   
                  * **Amazon S3 buckets:**  ``A``   
                   
                  * **Another resource record set in this hosted zone:** Specify the type of the resource record set that you\'re creating the alias for. All values are supported except ``NS`` and ``SOA`` . 
        
                  .. note::
        
                     If you\'re creating an alias record that has the same name as the hosted zone (known as the zone apex), you can\'t route traffic to a record for which the value of ``Type`` is ``CNAME`` . This is because the alias record must have the same type as the record you\'re routing traffic to, and creating a CNAME record for the zone apex isn\'t supported even for an alias record. 
        
                - **SetIdentifier** *(string) --* 
        
                   *Resource record sets that have a routing policy other than simple:* An identifier that differentiates among multiple resource record sets that have the same combination of name and type, such as multiple weighted resource record sets named acme.example.com that have a type of A. In a group of resource record sets that have the same name and type, the value of ``SetIdentifier`` must be unique for each resource record set. 
        
                  For information about routing policies, see `Choosing a Routing Policy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html>`__ in the *Amazon Route 53 Developer Guide* .
        
                - **Weight** *(integer) --* 
        
                   *Weighted resource record sets only:* Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource\'s weight to the total. Note the following:
        
                  * You must specify a value for the ``Weight`` element for every weighted resource record set. 
                   
                  * You can only specify one ``ResourceRecord`` per weighted resource record set. 
                   
                  * You can\'t create latency, failover, or geolocation resource record sets that have the same values for the ``Name`` and ``Type`` elements as weighted resource record sets. 
                   
                  * You can create a maximum of 100 weighted resource record sets that have the same values for the ``Name`` and ``Type`` elements. 
                   
                  * For weighted (but not weighted alias) resource record sets, if you set ``Weight`` to ``0`` for a resource record set, Route 53 never responds to queries with the applicable value for that resource record set. However, if you set ``Weight`` to ``0`` for all resource record sets that have the same combination of DNS name and type, traffic is routed to all resources with equal probability. The effect of setting ``Weight`` to ``0`` is different when you associate health checks with weighted resource record sets. For more information, see `Options for Configuring Route 53 Active-Active and Active-Passive Failover <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html>`__ in the *Amazon Route 53 Developer Guide* . 
                   
                - **Region** *(string) --* 
        
                   *Latency-based resource record sets only:* The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type.
        
                  .. note::
        
                    Creating latency and latency alias resource record sets in private hosted zones is not supported.
        
                  When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set.
        
                  Note the following:
        
                  * You can only specify one ``ResourceRecord`` per latency resource record set. 
                   
                  * You can only create one latency resource record set for each Amazon EC2 Region. 
                   
                  * You aren\'t required to create latency resource record sets for all Amazon EC2 Regions. Route 53 will choose the region with the best latency from among the regions that you create latency resource record sets for. 
                   
                  * You can\'t create non-latency resource record sets that have the same values for the ``Name`` and ``Type`` elements as latency resource record sets. 
                   
                - **GeoLocation** *(dict) --* 
        
                   *Geolocation resource record sets only:* A complex type that lets you control how Amazon Route 53 responds to DNS queries based on the geographic origin of the query. For example, if you want all queries from Africa to be routed to a web server with an IP address of ``192.0.2.111`` , create a resource record set with a ``Type`` of ``A`` and a ``ContinentCode`` of ``AF`` .
        
                  .. note::
        
                    Creating geolocation and geolocation alias resource record sets in private hosted zones is not supported.
        
                  If you create separate resource record sets for overlapping geographic regions (for example, one resource record set for a continent and one for a country on the same continent), priority goes to the smallest geographic region. This allows you to route most queries for a continent to one resource and to route queries for a country on that continent to a different resource.
        
                  You can\'t create two geolocation resource record sets that specify the same geographic location.
        
                  The value ``*`` in the ``CountryCode`` element matches all geographic locations that aren\'t specified in other geolocation resource record sets that have the same values for the ``Name`` and ``Type`` elements.
        
                  .. warning::
        
                    Geolocation works by mapping IP addresses to locations. However, some IP addresses aren\'t mapped to geographic locations, so even if you create geolocation resource record sets that cover all seven continents, Route 53 will receive some DNS queries from locations that it can\'t identify. We recommend that you create a resource record set for which the value of ``CountryCode`` is ``*`` , which handles both queries that come from locations for which you haven\'t created geolocation resource record sets and queries from IP addresses that aren\'t mapped to a location. If you don\'t create a ``*`` resource record set, Route 53 returns a \"no answer\" response for queries from those locations.
        
                  You can\'t create non-geolocation resource record sets that have the same values for the ``Name`` and ``Type`` elements as geolocation resource record sets.
        
                  - **ContinentCode** *(string) --* 
        
                    The two-letter code for the continent.
        
                    Valid values: ``AF`` | ``AN`` | ``AS`` | ``EU`` | ``OC`` | ``NA`` | ``SA``  
        
                    Constraint: Specifying ``ContinentCode`` with either ``CountryCode`` or ``SubdivisionCode`` returns an ``InvalidInput`` error.
        
                  - **CountryCode** *(string) --* 
        
                    The two-letter code for the country.
        
                  - **SubdivisionCode** *(string) --* 
        
                    The code for the subdivision. Route 53 currently supports only states in the United States.
        
                - **Failover** *(string) --* 
        
                   *Failover resource record sets only:* To configure failover, you add the ``Failover`` element to two resource record sets. For one resource record set, you specify ``PRIMARY`` as the value for ``Failover`` ; for the other resource record set, you specify ``SECONDARY`` . In addition, you include the ``HealthCheckId`` element and specify the health check that you want Amazon Route 53 to perform for each resource record set.
        
                  Except where noted, the following failover behaviors assume that you have included the ``HealthCheckId`` element in both resource record sets:
        
                  * When the primary resource record set is healthy, Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the secondary resource record set. 
                   
                  * When the primary resource record set is unhealthy and the secondary resource record set is healthy, Route 53 responds to DNS queries with the applicable value from the secondary resource record set. 
                   
                  * When the secondary resource record set is unhealthy, Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the primary resource record set. 
                   
                  * If you omit the ``HealthCheckId`` element for the secondary resource record set, and if the primary resource record set is unhealthy, Route 53 always responds to DNS queries with the applicable value from the secondary resource record set. This is true regardless of the health of the associated endpoint. 
                   
                  You can\'t create non-failover resource record sets that have the same values for the ``Name`` and ``Type`` elements as failover resource record sets.
        
                  For failover alias resource record sets, you must also include the ``EvaluateTargetHealth`` element and set the value to true.
        
                  For more information about configuring failover for Route 53, see the following topics in the *Amazon Route 53 Developer Guide* : 
        
                  * `Route 53 Health Checks and DNS Failover <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`__   
                   
                  * `Configuring Failover in a Private Hosted Zone <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`__   
                   
                - **MultiValueAnswer** *(boolean) --* 
        
                   *Multivalue answer resource record sets only* : To route traffic approximately randomly to multiple resources, such as web servers, create one multivalue answer record for each resource and specify ``true`` for ``MultiValueAnswer`` . Note the following:
        
                  * If you associate a health check with a multivalue answer resource record set, Amazon Route 53 responds to DNS queries with the corresponding IP address only when the health check is healthy. 
                   
                  * If you don\'t associate a health check with a multivalue answer record, Route 53 always considers the record to be healthy. 
                   
                  * Route 53 responds to DNS queries with up to eight healthy records; if you have eight or fewer healthy records, Route 53 responds to all DNS queries with all the healthy records. 
                   
                  * If you have more than eight healthy records, Route 53 responds to different DNS resolvers with different combinations of healthy records. 
                   
                  * When all records are unhealthy, Route 53 responds to DNS queries with up to eight unhealthy records. 
                   
                  * If a resource becomes unavailable after a resolver caches a response, client software typically tries another of the IP addresses in the response. 
                   
                  You can\'t create multivalue answer alias records.
        
                - **TTL** *(integer) --* 
        
                  The resource record cache time to live (TTL), in seconds. Note the following:
        
                  * If you\'re creating or updating an alias resource record set, omit ``TTL`` . Amazon Route 53 uses the value of ``TTL`` for the alias target.  
                   
                  * If you\'re associating this resource record set with a health check (if you\'re adding a ``HealthCheckId`` element), we recommend that you specify a ``TTL`` of 60 seconds or less so clients respond quickly to changes in health status. 
                   
                  * All of the resource record sets in a group of weighted resource record sets must have the same value for ``TTL`` . 
                   
                  * If a group of weighted resource record sets includes one or more weighted alias resource record sets for which the alias target is an ELB load balancer, we recommend that you specify a ``TTL`` of 60 seconds for all of the non-alias weighted resource record sets that have the same name and type. Values other than 60 seconds (the TTL for load balancers) will change the effect of the values that you specify for ``Weight`` . 
                   
                - **ResourceRecords** *(list) --* 
        
                  Information about the resource records to act upon.
        
                  .. note::
        
                    If you\'re creating an alias resource record set, omit ``ResourceRecords`` .
        
                  - *(dict) --* 
        
                    Information specific to the resource record.
        
                    .. note::
        
                      If you\'re creating an alias resource record set, omit ``ResourceRecord`` .
        
                    - **Value** *(string) --* 
        
                      The current or new DNS record value, not to exceed 4,000 characters. In the case of a ``DELETE`` action, if the current value does not match the actual value, an error is returned. For descriptions about how to format ``Value`` for different record types, see `Supported DNS Resource Record Types <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html>`__ in the *Amazon Route 53 Developer Guide* .
        
                      You can specify more than one value for all record types except ``CNAME`` and ``SOA`` . 
        
                      .. note::
        
                        If you\'re creating an alias resource record set, omit ``Value`` .
        
                - **AliasTarget** *(dict) --* 
        
                   *Alias resource record sets only:* Information about the CloudFront distribution, AWS Elastic Beanstalk environment, ELB load balancer, Amazon S3 bucket, or Amazon Route 53 resource record set to which you\'re redirecting queries. The AWS Elastic Beanstalk environment must have a regionalized subdomain.
        
                  If you\'re creating resource records sets for a private hosted zone, note the following:
        
                  * You can\'t create alias resource record sets for CloudFront distributions in a private hosted zone. 
                   
                  * Creating geolocation alias resource record sets or latency alias resource record sets in a private hosted zone is unsupported. 
                   
                  * For information about creating failover resource record sets in a private hosted zone, see `Configuring Failover in a Private Hosted Zone <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`__ in the *Amazon Route 53 Developer Guide* . 
                   
                  - **HostedZoneId** *(string) --* 
        
                     *Alias resource records sets only* : The value used depends on where you want to route traffic:
        
                      CloudFront distribution  
        
                    Specify ``Z2FDTNDATAQYW2`` .
        
                    .. note::
        
                      Alias resource record sets for CloudFront can\'t be created in a private zone.
        
                      Elastic Beanstalk environment  
        
                    Specify the hosted zone ID for the region that you created the environment in. The environment must have a regionalized subdomain. For a list of regions and the corresponding hosted zone IDs, see `AWS Elastic Beanstalk <http://docs.aws.amazon.com/general/latest/gr/rande.html#elasticbeanstalk_region>`__ in the \"AWS Regions and Endpoints\" chapter of the *Amazon Web Services General Reference* .
        
                      ELB load balancer  
        
                    Specify the value of the hosted zone ID for the load balancer. Use the following methods to get the hosted zone ID:
        
                    * `Elastic Load Balancing <http://docs.aws.amazon.com/general/latest/gr/rande.html#elb_region>`__ table in the \"AWS Regions and Endpoints\" chapter of the *Amazon Web Services General Reference* : Use the value that corresponds with the region that you created your load balancer in. Note that there are separate columns for Application and Classic Load Balancers and for Network Load Balancers. 
                     
                    * **AWS Management Console** : Go to the Amazon EC2 page, choose **Load Balancers** in the navigation pane, select the load balancer, and get the value of the **Hosted zone** field on the **Description** tab. 
                     
                    * **Elastic Load Balancing API** : Use ``DescribeLoadBalancers`` to get the applicable value. For more information, see the applicable guide: 
        
                      * Classic Load Balancers: Use `DescribeLoadBalancers <http://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancers.html>`__ to get the value of ``CanonicalHostedZoneNameId`` . 
                       
                      * Application and Network Load Balancers: Use `DescribeLoadBalancers <http://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html>`__ to get the value of ``CanonicalHostedZoneId`` . 
                       
                    * **AWS CLI** : Use ``describe-load-balancers`` to get the applicable value. For more information, see the applicable guide: 
        
                      * Classic Load Balancers: Use `describe-load-balancers <http://docs.aws.amazon.com/cli/latest/reference/elb/describe-load-balancers.html>`__ to get the value of ``CanonicalHostedZoneNameId`` . 
                       
                      * Application and Network Load Balancers: Use `describe-load-balancers <http://docs.aws.amazon.com/cli/latest/reference/elbv2/describe-load-balancers.html>`__ to get the value of ``CanonicalHostedZoneId`` . 
                       
                      An Amazon S3 bucket configured as a static website  
        
                    Specify the hosted zone ID for the region that you created the bucket in. For more information about valid values, see the `Amazon Simple Storage Service Website Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region>`__ table in the \"AWS Regions and Endpoints\" chapter of the *Amazon Web Services General Reference* .
        
                      Another Route 53 resource record set in your hosted zone  
        
                    Specify the hosted zone ID of your hosted zone. (An alias resource record set can\'t reference a resource record set in a different hosted zone.)
        
                  - **DNSName** *(string) --* 
        
                     *Alias resource record sets only:* The value that you specify depends on where you want to route queries:
        
                      CloudFront distribution  
        
                    Specify the domain name that CloudFront assigned when you created your distribution.
        
                    Your CloudFront distribution must include an alternate domain name that matches the name of the resource record set. For example, if the name of the resource record set is *acme.example.com* , your CloudFront distribution must include *acme.example.com* as one of the alternate domain names. For more information, see `Using Alternate Domain Names (CNAMEs) <http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html>`__ in the *Amazon CloudFront Developer Guide* .
        
                    .. note::
        
                      For failover alias records, you can\'t specify a CloudFront distribution for both the primary and secondary records. A distribution must include an alternate domain name that matches the name of the record. However, the primary and secondary records have the same name, and you can\'t include the same alternate domain name in more than one distribution. 
        
                      Elastic Beanstalk environment  
        
                    If the domain name for your Elastic Beanstalk environment includes the region that you deployed the environment in, you can create an alias record that routes traffic to the environment. For example, the domain name ``my-environment.*us-west-2* .elasticbeanstalk.com`` is a regionalized domain name. 
        
                    .. warning::
        
                      For environments that were created before early 2016, the domain name doesn\'t include the region. To route traffic to these environments, you must create a CNAME record instead of an alias record. Note that you can\'t create a CNAME record for the root domain name. For example, if your domain name is example.com, you can create a record that routes traffic for acme.example.com to your Elastic Beanstalk environment, but you can\'t create a record that routes traffic for example.com to your Elastic Beanstalk environment.
        
                    For Elastic Beanstalk environments that have regionalized subdomains, specify the ``CNAME`` attribute for the environment. You can use the following methods to get the value of the CNAME attribute:
        
                    * *AWS Management Console* : For information about how to get the value by using the console, see `Using Custom Domains with AWS Elastic Beanstalk <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customdomains.html>`__ in the *AWS Elastic Beanstalk Developer Guide* . 
                     
                    * *Elastic Beanstalk API* : Use the ``DescribeEnvironments`` action to get the value of the ``CNAME`` attribute. For more information, see `DescribeEnvironments <http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironments.html>`__ in the *AWS Elastic Beanstalk API Reference* . 
                     
                    * *AWS CLI* : Use the ``describe-environments`` command to get the value of the ``CNAME`` attribute. For more information, see `describe-environments <http://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/describe-environments.html>`__ in the *AWS Command Line Interface Reference* . 
                     
                      ELB load balancer  
        
                    Specify the DNS name that is associated with the load balancer. Get the DNS name by using the AWS Management Console, the ELB API, or the AWS CLI. 
        
                    * **AWS Management Console** : Go to the EC2 page, choose **Load Balancers** in the navigation pane, choose the load balancer, choose the **Description** tab, and get the value of the **DNS name** field. (If you\'re routing traffic to a Classic Load Balancer, get the value that begins with **dualstack** .)  
                     
                    * **Elastic Load Balancing API** : Use ``DescribeLoadBalancers`` to get the value of ``DNSName`` . For more information, see the applicable guide: 
        
                      * Classic Load Balancers: `DescribeLoadBalancers <http://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancers.html>`__   
                       
                      * Application and Network Load Balancers: `DescribeLoadBalancers <http://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html>`__   
                       
                    * **AWS CLI** : Use ``describe-load-balancers`` to get the value of ``DNSName`` . For more information, see the applicable guide: 
        
                      * Classic Load Balancers: `describe-load-balancers <http://docs.aws.amazon.com/cli/latest/reference/elb/describe-load-balancers.html>`__   
                       
                      * Application and Network Load Balancers: `describe-load-balancers <http://docs.aws.amazon.com/cli/latest/reference/elbv2/describe-load-balancers.html>`__   
                       
                      Amazon S3 bucket that is configured as a static website  
        
                    Specify the domain name of the Amazon S3 website endpoint that you created the bucket in, for example, ``s3-website-us-east-2.amazonaws.com`` . For more information about valid values, see the table `Amazon Simple Storage Service (S3) Website Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region>`__ in the *Amazon Web Services General Reference* . For more information about using S3 buckets for websites, see `Getting Started with Amazon Route 53 <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/getting-started.html>`__ in the *Amazon Route 53 Developer Guide.*  
        
                      Another Route 53 resource record set  
        
                    Specify the value of the ``Name`` element for a resource record set in the current hosted zone.
        
                    .. note::
        
                      If you\'re creating an alias record that has the same name as the hosted zone (known as the zone apex), you can\'t specify the domain name for a record for which the value of ``Type`` is ``CNAME`` . This is because the alias record must have the same type as the record that you\'re routing traffic to, and creating a CNAME record for the zone apex isn\'t supported even for an alias record.
        
                  - **EvaluateTargetHealth** *(boolean) --* 
        
                     *Applies only to alias, failover alias, geolocation alias, latency alias, and weighted alias resource record sets:* When ``EvaluateTargetHealth`` is ``true`` , an alias resource record set inherits the health of the referenced AWS resource, such as an ELB load balancer or another resource record set in the hosted zone.
        
                    Note the following:
        
                      CloudFront distributions  
        
                    You can\'t set ``EvaluateTargetHealth`` to ``true`` when the alias target is a CloudFront distribution.
        
                      Elastic Beanstalk environments that have regionalized subdomains  
        
                    If you specify an Elastic Beanstalk environment in ``DNSName`` and the environment contains an ELB load balancer, Elastic Load Balancing routes queries only to the healthy Amazon EC2 instances that are registered with the load balancer. (An environment automatically contains an ELB load balancer if it includes more than one Amazon EC2 instance.) If you set ``EvaluateTargetHealth`` to ``true`` and either no Amazon EC2 instances are healthy or the load balancer itself is unhealthy, Route 53 routes queries to other available resources that are healthy, if any. 
        
                    If the environment contains a single Amazon EC2 instance, there are no special requirements.
        
                      ELB load balancers  
        
                    Health checking behavior depends on the type of load balancer:
        
                    * **Classic Load Balancers** : If you specify an ELB Classic Load Balancer in ``DNSName`` , Elastic Load Balancing routes queries only to the healthy Amazon EC2 instances that are registered with the load balancer. If you set ``EvaluateTargetHealth`` to ``true`` and either no EC2 instances are healthy or the load balancer itself is unhealthy, Route 53 routes queries to other resources. 
                     
                    * **Application and Network Load Balancers** : If you specify an ELB Application or Network Load Balancer and you set ``EvaluateTargetHealth`` to ``true`` , Route 53 routes queries to the load balancer based on the health of the target groups that are associated with the load balancer: 
        
                      * For an Application or Network Load Balancer to be considered healthy, every target group that contains targets must contain at least one healthy target. If any target group contains only unhealthy targets, the load balancer is considered unhealthy, and Route 53 routes queries to other resources. 
                       
                      * A target group that has no registered targets is considered healthy. 
                       
                    .. note::
        
                      When you create a load balancer, you configure settings for Elastic Load Balancing health checks; they\'re not Route 53 health checks, but they perform a similar function. Do not create Route 53 health checks for the EC2 instances that you register with an ELB load balancer. 
        
                      S3 buckets  
        
                    There are no special requirements for setting ``EvaluateTargetHealth`` to ``true`` when the alias target is an S3 bucket.
        
                      Other records in the same hosted zone  
        
                    If the AWS resource that you specify in ``DNSName`` is a record or a group of records (for example, a group of weighted records) but is not another alias record, we recommend that you associate a health check with all of the records in the alias target. For more information, see `What Happens When You Omit Health Checks? <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-complex-configs.html#dns-failover-complex-configs-hc-omitting>`__ in the *Amazon Route 53 Developer Guide* .
        
                    For more information and examples, see `Amazon Route 53 Health Checks and DNS Failover <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`__ in the *Amazon Route 53 Developer Guide* .
        
                - **HealthCheckId** *(string) --* 
        
                  If you want Amazon Route 53 to return this resource record set in response to a DNS query only when the status of a health check is healthy, include the ``HealthCheckId`` element and specify the ID of the applicable health check.
        
                  Route 53 determines whether a resource record set is healthy based on one of the following:
        
                  * By periodically sending a request to the endpoint that is specified in the health check 
                   
                  * By aggregating the status of a specified group of health checks (calculated health checks) 
                   
                  * By determining the current state of a CloudWatch alarm (CloudWatch metric health checks) 
                   
                  .. warning::
        
                    Route 53 doesn\'t check the health of the endpoint that is specified in the resource record set, for example, the endpoint specified by the IP address in the ``Value`` element. When you add a ``HealthCheckId`` element to a resource record set, Route 53 checks the health of the endpoint that you specified in the health check. 
        
                  For more information, see the following topics in the *Amazon Route 53 Developer Guide* :
        
                  * `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__   
                   
                  * `Route 53 Health Checks and DNS Failover <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`__   
                   
                  * `Configuring Failover in a Private Hosted Zone <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`__   
                   
                   **When to Specify HealthCheckId**  
        
                  Specifying a value for ``HealthCheckId`` is useful only when Route 53 is choosing between two or more resource record sets to respond to a DNS query, and you want Route 53 to base the choice in part on the status of a health check. Configuring health checks makes sense only in the following configurations:
        
                  * **Non-alias resource record sets** : You\'re checking the health of a group of non-alias resource record sets that have the same routing policy, name, and type (such as multiple weighted records named www.example.com with a type of A) and you specify health check IDs for all the resource record sets.  If the health check status for a resource record set is healthy, Route 53 includes the record among the records that it responds to DNS queries with. If the health check status for a resource record set is unhealthy, Route 53 stops responding to DNS queries using the value for that resource record set. If the health check status for all resource record sets in the group is unhealthy, Route 53 considers all resource record sets in the group healthy and responds to DNS queries accordingly.  
                   
                  * **Alias resource record sets** : You specify the following settings: 
        
                    * You set ``EvaluateTargetHealth`` to true for an alias resource record set in a group of resource record sets that have the same routing policy, name, and type (such as multiple weighted records named www.example.com with a type of A).  
                     
                    * You configure the alias resource record set to route traffic to a non-alias resource record set in the same hosted zone. 
                     
                    * You specify a health check ID for the non-alias resource record set.  
                     
                  If the health check status is healthy, Route 53 considers the alias resource record set to be healthy and includes the alias record among the records that it responds to DNS queries with.
        
                  If the health check status is unhealthy, Route 53 stops responding to DNS queries using the alias resource record set.
        
                  .. note::
        
                    The alias resource record set can also route traffic to a *group* of non-alias resource record sets that have the same routing policy, name, and type. In that configuration, associate health checks with all of the resource record sets in the group of non-alias resource record sets.
        
                   **Geolocation Routing**  
        
                  For geolocation resource record sets, if an endpoint is unhealthy, Route 53 looks for a resource record set for the larger, associated geographic region. For example, suppose you have resource record sets for a state in the United States, for the entire United States, for North America, and a resource record set that has ``*`` for ``CountryCode`` is ``*`` , which applies to all locations. If the endpoint for the state resource record set is unhealthy, Route 53 checks for healthy resource record sets in the following order until it finds a resource record set for which the endpoint is healthy:
        
                  * The United States 
                   
                  * North America 
                   
                  * The default resource record set 
                   
                   **Specifying the Health Check Endpoint by Domain Name**  
        
                  If your health checks specify the endpoint only by domain name, we recommend that you create a separate health check for each endpoint. For example, create a health check for each ``HTTP`` server that is serving content for ``www.example.com`` . For the value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as ``us-east-2-www.example.com`` ), not the name of the resource record sets (``www.example.com`` ).
        
                  .. warning::
        
                    Health check results will be unpredictable if you do the following:
        
                    * Create a health check that has the same value for ``FullyQualifiedDomainName`` as the name of a resource record set. 
                     
                    * Associate that health check with the resource record set. 
                     
                - **TrafficPolicyInstanceId** *(string) --* 
        
                  When you create a traffic policy instance, Amazon Route 53 automatically creates a resource record set. ``TrafficPolicyInstanceId`` is the ID of the traffic policy instance that Route 53 created this resource record set for.
        
                  .. warning::
        
                    To delete the resource record set that is associated with a traffic policy instance, use ``DeleteTrafficPolicyInstance`` . Route 53 will delete the resource record set automatically. If you delete the resource record set by using ``ChangeResourceRecordSets`` , Route 53 doesn\'t automatically delete the traffic policy instance, and you\'ll continue to be charged for it even though it\'s no longer in use. 
        
            - **IsTruncated** *(boolean) --* 
        
              A flag that indicates whether more resource record sets remain to be listed. If your results were truncated, you can make a follow-up pagination request by using the ``NextRecordName`` element.
        
            - **MaxItems** *(string) --* 
        
              The maximum number of records you requested.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
