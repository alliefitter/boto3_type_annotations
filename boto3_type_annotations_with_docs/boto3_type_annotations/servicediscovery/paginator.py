from typing import List
from typing import Dict
from botocore.paginate import Paginator


class ListInstances(Paginator):
    def paginate(self, ServiceId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ServiceDiscovery.Client.list_instances`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/ListInstances>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ServiceId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Instances': [
                    {
                        'Id': 'string',
                        'Attributes': {
                            'string': 'string'
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Instances** *(list) --* 
              Summary information about the instances that are associated with the specified service.
              - *(dict) --* 
                A complex type that contains information about the instances that you registered by using a specified service.
                - **Id** *(string) --* 
                  The ID for an instance that you created by using a specified service.
                - **Attributes** *(dict) --* 
                  A string map that contains the following information:
                  * The attributes that are associate with the instance.  
                  * For each attribute, the applicable value. 
                  Supported attribute keys include the following:
                  * ``AWS_ALIAS_DNS_NAME`` : For an alias record that routes traffic to an Elastic Load Balancing load balancer, the DNS name that is associated with the load balancer.  
                  * ``AWS_INSTANCE_CNAME`` : For a CNAME record, the domain name that Route 53 returns in response to DNS queries, for example, ``example.com`` . 
                  * ``AWS_INSTANCE_IPV4`` : For an A record, the IPv4 address that Route 53 returns in response to DNS queries, for example, ``192.0.2.44`` . 
                  * ``AWS_INSTANCE_IPV6`` : For an AAAA record, the IPv6 address that Route 53 returns in response to DNS queries, for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . 
                  * ``AWS_INSTANCE_PORT`` : For an SRV record, the value that Route 53 returns for the port. In addition, if the service includes ``HealthCheckConfig`` , the port on the endpoint that Route 53 sends requests to. 
                  - *(string) --* 
                    - *(string) --* 
        :type ServiceId: string
        :param ServiceId: **[REQUIRED]**
          The ID of the service that you want to list instances for.
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
        """
        pass


class ListNamespaces(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ServiceDiscovery.Client.list_namespaces`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/ListNamespaces>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'TYPE',
                      'Values': [
                          'string',
                      ],
                      'Condition': 'EQ'|'IN'|'BETWEEN'
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Namespaces': [
                    {
                        'Id': 'string',
                        'Arn': 'string',
                        'Name': 'string',
                        'Type': 'DNS_PUBLIC'|'DNS_PRIVATE'|'HTTP',
                        'Description': 'string',
                        'ServiceCount': 123,
                        'Properties': {
                            'DnsProperties': {
                                'HostedZoneId': 'string'
                            },
                            'HttpProperties': {
                                'HttpName': 'string'
                            }
                        },
                        'CreateDate': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Namespaces** *(list) --* 
              An array that contains one ``NamespaceSummary`` object for each namespace that matches the specified filter criteria.
              - *(dict) --* 
                A complex type that contains information about a namespace.
                - **Id** *(string) --* 
                  The ID of the namespace.
                - **Arn** *(string) --* 
                  The Amazon Resource Name (ARN) that AWS Cloud Map assigns to the namespace when you create it.
                - **Name** *(string) --* 
                  The name of the namespace. When you create a namespace, AWS Cloud Map automatically creates a Route 53 hosted zone that has the same name as the namespace.
                - **Type** *(string) --* 
                  The type of the namespace, either public or private.
                - **Description** *(string) --* 
                  A description for the namespace.
                - **ServiceCount** *(integer) --* 
                  The number of services that were created using the namespace.
                - **Properties** *(dict) --* 
                  A complex type that contains information that is specific to the namespace type.
                  - **DnsProperties** *(dict) --* 
                    A complex type that contains the ID for the Route 53 hosted zone that AWS Cloud Map creates when you create a namespace.
                    - **HostedZoneId** *(string) --* 
                      The ID for the Route 53 hosted zone that AWS Cloud Map creates when you create a namespace.
                  - **HttpProperties** *(dict) --* 
                    A complex type that contains the name of an HTTP namespace.
                    - **HttpName** *(string) --* 
                      The name of an HTTP namespace.
                - **CreateDate** *(datetime) --* 
                  The date and time that the namespace was created.
        :type Filters: list
        :param Filters:
          A complex type that contains specifications for the namespaces that you want to list.
          If you specify more than one filter, a namespace must match all filters to be returned by ``ListNamespaces`` .
          - *(dict) --*
            A complex type that identifies the namespaces that you want to list. You can choose to list public or private namespaces.
            - **Name** *(string) --* **[REQUIRED]**
              Specify ``TYPE`` .
            - **Values** *(list) --* **[REQUIRED]**
              If you specify ``EQ`` for ``Condition`` , specify either ``DNS_PUBLIC`` or ``DNS_PRIVATE`` .
              If you specify ``IN`` for ``Condition`` , you can specify ``DNS_PUBLIC`` , ``DNS_PRIVATE`` , or both.
              - *(string) --*
            - **Condition** *(string) --*
              The operator that you want to use to determine whether ``ListNamespaces`` returns a namespace. Valid values for ``condition`` include:
              * ``EQ`` : When you specify ``EQ`` for the condition, you can choose to list only public namespaces or private namespaces, but not both. ``EQ`` is the default condition and can be omitted.
              * ``IN`` : When you specify ``IN`` for the condition, you can choose to list public namespaces, private namespaces, or both.
              * ``BETWEEN`` : Not applicable
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
        """
        pass


class ListOperations(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ServiceDiscovery.Client.list_operations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/ListOperations>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'NAMESPACE_ID'|'SERVICE_ID'|'STATUS'|'TYPE'|'UPDATE_DATE',
                      'Values': [
                          'string',
                      ],
                      'Condition': 'EQ'|'IN'|'BETWEEN'
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Operations': [
                    {
                        'Id': 'string',
                        'Status': 'SUBMITTED'|'PENDING'|'SUCCESS'|'FAIL'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Operations** *(list) --* 
              Summary information about the operations that match the specified criteria.
              - *(dict) --* 
                A complex type that contains information about an operation that matches the criteria that you specified in a  ListOperations request.
                - **Id** *(string) --* 
                  The ID for an operation.
                - **Status** *(string) --* 
                  The status of the operation. Values include the following:
                  * **SUBMITTED** : This is the initial state immediately after you submit a request. 
                  * **PENDING** : AWS Cloud Map is performing the operation. 
                  * **SUCCESS** : The operation succeeded. 
                  * **FAIL** : The operation failed. For the failure reason, see ``ErrorMessage`` . 
        :type Filters: list
        :param Filters:
          A complex type that contains specifications for the operations that you want to list, for example, operations that you started between a specified start date and end date.
          If you specify more than one filter, an operation must match all filters to be returned by ``ListOperations`` .
          - *(dict) --*
            A complex type that lets you select the operations that you want to list.
            - **Name** *(string) --* **[REQUIRED]**
              Specify the operations that you want to get:
              * **NAMESPACE_ID** : Gets operations related to specified namespaces.
              * **SERVICE_ID** : Gets operations related to specified services.
              * **STATUS** : Gets operations based on the status of the operations: ``SUBMITTED`` , ``PENDING`` , ``SUCCEED`` , or ``FAIL`` .
              * **TYPE** : Gets specified types of operation.
              * **UPDATE_DATE** : Gets operations that changed status during a specified date/time range.
            - **Values** *(list) --* **[REQUIRED]**
              Specify values that are applicable to the value that you specify for ``Name`` :
              * **NAMESPACE_ID** : Specify one namespace ID.
              * **SERVICE_ID** : Specify one service ID.
              * **STATUS** : Specify one or more statuses: ``SUBMITTED`` , ``PENDING`` , ``SUCCEED`` , or ``FAIL`` .
              * **TYPE** : Specify one or more of the following types: ``CREATE_NAMESPACE`` , ``DELETE_NAMESPACE`` , ``UPDATE_SERVICE`` , ``REGISTER_INSTANCE`` , or ``DEREGISTER_INSTANCE`` .
              * **UPDATE_DATE** : Specify a start date and an end date in Unix date/time format and Coordinated Universal Time (UTC). The start date must be the first value.
              - *(string) --*
            - **Condition** *(string) --*
              The operator that you want to use to determine whether an operation matches the specified value. Valid values for condition include:
              * ``EQ`` : When you specify ``EQ`` for the condition, you can specify only one value. ``EQ`` is supported for ``NAMESPACE_ID`` , ``SERVICE_ID`` , ``STATUS`` , and ``TYPE`` . ``EQ`` is the default condition and can be omitted.
              * ``IN`` : When you specify ``IN`` for the condition, you can specify a list of one or more values. ``IN`` is supported for ``STATUS`` and ``TYPE`` . An operation must match one of the specified values to be returned in the response.
              * ``BETWEEN`` : Specify a start date and an end date in Unix date/time format and Coordinated Universal Time (UTC). The start date must be the first value. ``BETWEEN`` is supported for ``UPDATE_DATE`` .
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
        """
        pass


class ListServices(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`ServiceDiscovery.Client.list_services`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/ListServices>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'NAMESPACE_ID',
                      'Values': [
                          'string',
                      ],
                      'Condition': 'EQ'|'IN'|'BETWEEN'
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Services': [
                    {
                        'Id': 'string',
                        'Arn': 'string',
                        'Name': 'string',
                        'Description': 'string',
                        'InstanceCount': 123,
                        'DnsConfig': {
                            'NamespaceId': 'string',
                            'RoutingPolicy': 'MULTIVALUE'|'WEIGHTED',
                            'DnsRecords': [
                                {
                                    'Type': 'SRV'|'A'|'AAAA'|'CNAME',
                                    'TTL': 123
                                },
                            ]
                        },
                        'HealthCheckConfig': {
                            'Type': 'HTTP'|'HTTPS'|'TCP',
                            'ResourcePath': 'string',
                            'FailureThreshold': 123
                        },
                        'HealthCheckCustomConfig': {
                            'FailureThreshold': 123
                        },
                        'CreateDate': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Services** *(list) --* 
              An array that contains one ``ServiceSummary`` object for each service that matches the specified filter criteria.
              - *(dict) --* 
                A complex type that contains information about a specified service.
                - **Id** *(string) --* 
                  The ID that AWS Cloud Map assigned to the service when you created it.
                - **Arn** *(string) --* 
                  The Amazon Resource Name (ARN) that AWS Cloud Map assigns to the service when you create it.
                - **Name** *(string) --* 
                  The name of the service.
                - **Description** *(string) --* 
                  The description that you specify when you create the service.
                - **InstanceCount** *(integer) --* 
                  The number of instances that are currently associated with the service. Instances that were previously associated with the service but that have been deleted are not included in the count.
                - **DnsConfig** *(dict) --* 
                  A complex type that contains information about the Amazon Route 53 DNS records that you want AWS Cloud Map to create when you register an instance.
                  - **NamespaceId** *(string) --* 
                    The ID of the namespace to use for DNS configuration.
                  - **RoutingPolicy** *(string) --* 
                    The routing policy that you want to apply to all Route 53 DNS records that AWS Cloud Map creates when you register an instance and specify this service.
                    .. note::
                      If you want to use this service to register instances that create alias records, specify ``WEIGHTED`` for the routing policy.
                    You can specify the following values:
        
        **MULTIVALUE**
                    If you define a health check for the service and the health check is healthy, Route 53 returns the applicable value for up to eight instances.
                    For example, suppose the service includes configurations for one A record and a health check, and you use the service to register 10 instances. Route 53 responds to DNS queries with IP addresses for up to eight healthy instances. If fewer than eight instances are healthy, Route 53 responds to every DNS query with the IP addresses for all of the healthy instances.
                    If you don't define a health check for the service, Route 53 assumes that all instances are healthy and returns the values for up to eight instances.
                    For more information about the multivalue routing policy, see `Multivalue Answer Routing <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-multivalue>`__ in the *Route 53 Developer Guide* .
        
        **WEIGHTED**
                    Route 53 returns the applicable value from one randomly selected instance from among the instances that you registered using the same service. Currently, all records have the same weight, so you can't route more or less traffic to any instances.
                    For example, suppose the service includes configurations for one A record and a health check, and you use the service to register 10 instances. Route 53 responds to DNS queries with the IP address for one randomly selected instance from among the healthy instances. If no instances are healthy, Route 53 responds to DNS queries as if all of the instances were healthy.
                    If you don't define a health check for the service, Route 53 assumes that all instances are healthy and returns the applicable value for one randomly selected instance.
                    For more information about the weighted routing policy, see `Weighted Routing <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted>`__ in the *Route 53 Developer Guide* .
                  - **DnsRecords** *(list) --* 
                    An array that contains one ``DnsRecord`` object for each Route 53 DNS record that you want AWS Cloud Map to create when you register an instance.
                    - *(dict) --* 
                      A complex type that contains information about the Route 53 DNS records that you want AWS Cloud Map to create when you register an instance.
                      - **Type** *(string) --* 
                        The type of the resource, which indicates the type of value that Route 53 returns in response to DNS queries.
                        Note the following:
                        * **A, AAAA, and SRV records:** You can specify settings for a maximum of one A, one AAAA, and one SRV record. You can specify them in any combination. 
                        * **CNAME records:** If you specify ``CNAME`` for ``Type`` , you can't define any other records. This is a limitation of DNS: you can't create a CNAME record and any other type of record that has the same name as a CNAME record. 
                        * **Alias records:** If you want AWS Cloud Map to create a Route 53 alias record when you register an instance, specify ``A`` or ``AAAA`` for ``Type`` . 
                        * **All records:** You specify settings other than ``TTL`` and ``Type`` when you register an instance. 
                        The following values are supported:
        
        **A**
                        Route 53 returns the IP address of the resource in IPv4 format, such as 192.0.2.44.
        
        **AAAA**
                        Route 53 returns the IP address of the resource in IPv6 format, such as 2001:0db8:85a3:0000:0000:abcd:0001:2345.
        
        **CNAME**
                        Route 53 returns the domain name of the resource, such as www.example.com. Note the following:
                        * You specify the domain name that you want to route traffic to when you register an instance. For more information, see  RegisterInstanceRequest$Attributes . 
                        * You must specify ``WEIGHTED`` for the value of ``RoutingPolicy`` . 
                        * You can't specify both ``CNAME`` for ``Type`` and settings for ``HealthCheckConfig`` . If you do, the request will fail with an ``InvalidInput`` error. 
        
        **SRV**
                        Route 53 returns the value for an SRV record. The value for an SRV record uses the following values:
                         ``priority weight port service-hostname``  
                        Note the following about the values:
                        * The values of ``priority`` and ``weight`` are both set to ``1`` and can't be changed.  
                        * The value of ``port`` comes from the value that you specify for the ``AWS_INSTANCE_PORT`` attribute when you submit a  RegisterInstance request.  
                        * The value of ``service-hostname`` is a concatenation of the following values: 
                          * The value that you specify for ``InstanceId`` when you register an instance. 
                          * The name of the service. 
                          * The name of the namespace.  
                        For example, if the value of ``InstanceId`` is ``test`` , the name of the service is ``backend`` , and the name of the namespace is ``example.com`` , the value of ``service-hostname`` is:
                         ``test.backend.example.com``  
                        If you specify settings for an SRV record and if you specify values for ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both in the ``RegisterInstance`` request, AWS Cloud Map automatically creates ``A`` and/or ``AAAA`` records that have the same name as the value of ``service-hostname`` in the SRV record. You can ignore these records.
                      - **TTL** *(integer) --* 
                        The amount of time, in seconds, that you want DNS resolvers to cache the settings for this record.
                        .. note::
                          Alias records don't include a TTL because Route 53 uses the TTL for the AWS resource that an alias record routes traffic to. If you include the ``AWS_ALIAS_DNS_NAME`` attribute when you submit a  RegisterInstance request, the ``TTL`` value is ignored. Always specify a TTL for the service; you can use a service to register instances that create either alias or non-alias records.
                - **HealthCheckConfig** *(dict) --* 
                   *Public DNS namespaces only.* A complex type that contains settings for an optional health check. If you specify settings for a health check, AWS Cloud Map associates the health check with the records that you specify in ``DnsConfig`` .
                  .. warning::
                    If you specify a health check configuration, you can specify either ``HealthCheckCustomConfig`` or ``HealthCheckConfig`` but not both.
                  Health checks are basic Route 53 health checks that monitor an AWS endpoint. For information about pricing for health checks, see `Amazon Route 53 Pricing <http://aws.amazon.com/route53/pricing/>`__ .
                  Note the following about configuring health checks.
        
        **A and AAAA records**
                  If ``DnsConfig`` includes configurations for both A and AAAA records, AWS Cloud Map creates a health check that uses the IPv4 address to check the health of the resource. If the endpoint that is specified by the IPv4 address is unhealthy, Route 53 considers both the A and AAAA records to be unhealthy. 
        
        **CNAME records**
                  You can't specify settings for ``HealthCheckConfig`` when the ``DNSConfig`` includes ``CNAME`` for the value of ``Type`` . If you do, the ``CreateService`` request will fail with an ``InvalidInput`` error.
        
        **Request interval**
                  A Route 53 health checker in each health-checking region sends a health check request to an endpoint every 30 seconds. On average, your endpoint receives a health check request about every two seconds. However, health checkers don't coordinate with one another, so you'll sometimes see several requests per second followed by a few seconds with no health checks at all.
        
        **Health checking regions**
                  Health checkers perform checks from all Route 53 health-checking regions. For a list of the current regions, see `Regions <http://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckConfig.html#Route53-Type-HealthCheckConfig-Regions>`__ .
        
        **Alias records**
                  When you register an instance, if you include the ``AWS_ALIAS_DNS_NAME`` attribute, AWS Cloud Map creates a Route 53 alias record. Note the following:
                  * Route 53 automatically sets ``EvaluateTargetHealth`` to true for alias records. When ``EvaluateTargetHealth`` is true, the alias record inherits the health of the referenced AWS resource. such as an ELB load balancer. For more information, see `EvaluateTargetHealth <http://docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html#Route53-Type-AliasTarget-EvaluateTargetHealth>`__ . 
                  * If you include ``HealthCheckConfig`` and then use the service to register an instance that creates an alias record, Route 53 doesn't create the health check. 
        
        **Charges for health checks**
                  Health checks are basic Route 53 health checks that monitor an AWS endpoint. For information about pricing for health checks, see `Amazon Route 53 Pricing <http://aws.amazon.com/route53/pricing/>`__ .
                  - **Type** *(string) --* 
                    The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy.
                    .. warning::
                      You can't change the value of ``Type`` after you create a health check.
                    You can create the following types of health checks:
                    * **HTTP** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400. 
                    * **HTTPS** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400. 
                    .. warning::
                       If you specify HTTPS for the value of ``Type`` , the endpoint must support TLS v1.0 or later. 
                    * **TCP** : Route 53 tries to establish a TCP connection. If you specify ``TCP`` for ``Type`` , don't specify a value for ``ResourcePath`` . 
                    For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Route 53 Developer Guide* .
                  - **ResourcePath** *(string) --* 
                    The path that you want Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, such as the file ``/docs/route53-health-check.html`` . Route 53 automatically adds the DNS name for the service. If you don't specify a value for ``ResourcePath`` , the default value is ``/`` .
                    If you specify ``TCP`` for ``Type`` , you must *not* specify a value for ``ResourcePath`` .
                  - **FailureThreshold** *(integer) --* 
                    The number of consecutive health checks that an endpoint must pass or fail for Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Route 53 Developer Guide* .
                - **HealthCheckCustomConfig** *(dict) --* 
                  A complex type that contains information about an optional custom health check. A custom health check, which requires that you use a third-party health checker to evaluate the health of your resources, is useful in the following circumstances:
                  * You can't use a health check that is defined by ``HealthCheckConfig`` because the resource isn't available over the internet. For example, you can use a custom health check when the instance is in an Amazon VPC. (To check the health of resources in a VPC, the health checker must also be in the VPC.) 
                  * You want to use a third-party health checker regardless of where your resources are. 
                  .. warning::
                    If you specify a health check configuration, you can specify either ``HealthCheckCustomConfig`` or ``HealthCheckConfig`` but not both.
                  To change the status of a custom health check, submit an ``UpdateInstanceCustomHealthStatus`` request. Cloud Map doesn't monitor the status of the resource, it just keeps a record of the status specified in the most recent ``UpdateInstanceCustomHealthStatus`` request.
                  Here's how custom health checks work:
                  * You create a service and specify a value for ``FailureThreshold`` .  The failure threshold indicates the number of 30-second intervals you want AWS Cloud Map to wait between the time that your application sends an  UpdateInstanceCustomHealthStatus request and the time that AWS Cloud Map stops routing internet traffic to the corresponding resource. 
                  * You register an instance. 
                  * You configure a third-party health checker to monitor the resource that is associated with the new instance.  
                  .. note::
                     AWS Cloud Map doesn't check the health of the resource directly.  
                  * The third-party health-checker determines that the resource is unhealthy and notifies your application. 
                  * Your application submits an ``UpdateInstanceCustomHealthStatus`` request. 
                  * AWS Cloud Map waits for (``FailureThreshold`` x 30) seconds. 
                  * If another ``UpdateInstanceCustomHealthStatus`` request doesn't arrive during that time to change the status back to healthy, AWS Cloud Map stops routing traffic to the resource. 
                  Note the following about configuring custom health checks.
                  - **FailureThreshold** *(integer) --* 
                    The number of 30-second intervals that you want Cloud Map to wait after receiving an ``UpdateInstanceCustomHealthStatus`` request before it changes the health status of a service instance. For example, suppose you specify a value of ``2`` for ``FailureTheshold`` , and then your application sends an ``UpdateInstanceCustomHealthStatus`` request. Cloud Map waits for approximately 60 seconds (2 x 30) before changing the status of the service instance based on that request.
                    Sending a second or subsequent ``UpdateInstanceCustomHealthStatus`` request with the same value before ``FailureThreshold x 30`` seconds has passed doesn't accelerate the change. Cloud Map still waits ``FailureThreshold x 30`` seconds after the first request to make the change.
                - **CreateDate** *(datetime) --* 
                  The date and time that the service was created.
        :type Filters: list
        :param Filters:
          A complex type that contains specifications for the namespaces that you want to list services for.
          If you specify more than one filter, an operation must match all filters to be returned by ``ListServices`` .
          - *(dict) --*
            A complex type that lets you specify the namespaces that you want to list services for.
            - **Name** *(string) --* **[REQUIRED]**
              Specify ``NAMESPACE_ID`` .
            - **Values** *(list) --* **[REQUIRED]**
              The values that are applicable to the value that you specify for ``Condition`` to filter the list of services.
              - *(string) --*
            - **Condition** *(string) --*
              The operator that you want to use to determine whether a service is returned by ``ListServices`` . Valid values for ``Condition`` include the following:
              * ``EQ`` : When you specify ``EQ`` , specify one namespace ID for ``Values`` . ``EQ`` is the default condition and can be omitted.
              * ``IN`` : When you specify ``IN`` , specify a list of the IDs for the namespaces that you want ``ListServices`` to return a list of services for.
              * ``BETWEEN`` : Not applicable.
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
        """
        pass
