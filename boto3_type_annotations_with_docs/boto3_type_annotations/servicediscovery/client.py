from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
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

    def create_private_dns_namespace(self, Name: str, Vpc: str, CreatorRequestId: str = None, Description: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/CreatePrivateDnsNamespace>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_private_dns_namespace(
              Name=\'string\',
              CreatorRequestId=\'string\',
              Description=\'string\',
              Vpc=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name that you want to assign to this namespace. When you create a namespace, Amazon Route 53 automatically creates a hosted zone that has the same name as the namespace.
        
        :type CreatorRequestId: string
        :param CreatorRequestId: 
        
          A unique string that identifies the request and that allows failed ``CreatePrivateDnsNamespace`` requests to be retried without the risk of executing the operation twice. ``CreatorRequestId`` can be any unique string, for example, a date/time stamp.
        
          This field is autopopulated if not provided.
        
        :type Description: string
        :param Description: 
        
          A description for the namespace.
        
        :type Vpc: string
        :param Vpc: **[REQUIRED]** 
        
          The ID of the Amazon VPC that you want to associate the namespace with.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'OperationId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **OperationId** *(string) --* 
        
              A value that you can use to determine whether the request completed successfully. To get the status of the operation, see  GetOperation .
        
        """
        pass

    def create_public_dns_namespace(self, Name: str, CreatorRequestId: str = None, Description: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/CreatePublicDnsNamespace>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_public_dns_namespace(
              Name=\'string\',
              CreatorRequestId=\'string\',
              Description=\'string\'
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name that you want to assign to this namespace.
        
        :type CreatorRequestId: string
        :param CreatorRequestId: 
        
          A unique string that identifies the request and that allows failed ``CreatePublicDnsNamespace`` requests to be retried without the risk of executing the operation twice. ``CreatorRequestId`` can be any unique string, for example, a date/time stamp.
        
          This field is autopopulated if not provided.
        
        :type Description: string
        :param Description: 
        
          A description for the namespace.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'OperationId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **OperationId** *(string) --* 
        
              A value that you can use to determine whether the request completed successfully. To get the status of the operation, see  GetOperation .
        
        """
        pass

    def create_service(self, Name: str, DnsConfig: Dict, CreatorRequestId: str = None, Description: str = None, HealthCheckConfig: Dict = None, HealthCheckCustomConfig: Dict = None) -> Dict:
        """
        Creates a service, which defines the configuration for the following entities:
        
        * Up to three records (A, AAAA, and SRV) or one CNAME record 
         
        * Optionally, a health check 
         
        After you create the service, you can submit a  RegisterInstance request, and Amazon Route 53 uses the values in the configuration to create the specified entities.
        
        For the current limit on the number of instances that you can register using the same namespace and using the same service, see `Limits on Auto Naming <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html#limits-api-entities-autonaming>`__ in the *Route 53 Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/CreateService>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_service(
              Name=\'string\',
              CreatorRequestId=\'string\',
              Description=\'string\',
              DnsConfig={
                  \'NamespaceId\': \'string\',
                  \'RoutingPolicy\': \'MULTIVALUE\'|\'WEIGHTED\',
                  \'DnsRecords\': [
                      {
                          \'Type\': \'SRV\'|\'A\'|\'AAAA\'|\'CNAME\',
                          \'TTL\': 123
                      },
                  ]
              },
              HealthCheckConfig={
                  \'Type\': \'HTTP\'|\'HTTPS\'|\'TCP\',
                  \'ResourcePath\': \'string\',
                  \'FailureThreshold\': 123
              },
              HealthCheckCustomConfig={
                  \'FailureThreshold\': 123
              }
          )
        :type Name: string
        :param Name: **[REQUIRED]** 
        
          The name that you want to assign to the service.
        
        :type CreatorRequestId: string
        :param CreatorRequestId: 
        
          A unique string that identifies the request and that allows failed ``CreateService`` requests to be retried without the risk of executing the operation twice. ``CreatorRequestId`` can be any unique string, for example, a date/time stamp.
        
          This field is autopopulated if not provided.
        
        :type Description: string
        :param Description: 
        
          A description for the service.
        
        :type DnsConfig: dict
        :param DnsConfig: **[REQUIRED]** 
        
          A complex type that contains information about the records that you want Route 53 to create when you register an instance. 
        
          - **NamespaceId** *(string) --* **[REQUIRED]** 
        
            The ID of the namespace to use for DNS configuration.
        
          - **RoutingPolicy** *(string) --* 
        
            The routing policy that you want to apply to all records that Route 53 creates when you register an instance and specify this service.
        
            .. note::
        
              If you want to use this service to register instances that create alias records, specify ``WEIGHTED`` for the routing policy.
        
            You can specify the following values:
        
             **MULTIVALUE**  
        
            If you define a health check for the service and the health check is healthy, Route 53 returns the applicable value for up to eight instances.
        
            For example, suppose the service includes configurations for one A record and a health check, and you use the service to register 10 instances. Route 53 responds to DNS queries with IP addresses for up to eight healthy instances. If fewer than eight instances are healthy, Route 53 responds to every DNS query with the IP addresses for all of the healthy instances.
        
            If you don\'t define a health check for the service, Route 53 assumes that all instances are healthy and returns the values for up to eight instances.
        
            For more information about the multivalue routing policy, see `Multivalue Answer Routing <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-multivalue>`__ in the *Route 53 Developer Guide* .
        
             **WEIGHTED**  
        
            Route 53 returns the applicable value from one randomly selected instance from among the instances that you registered using the same service. Currently, all records have the same weight, so you can\'t route more or less traffic to any instances.
        
            For example, suppose the service includes configurations for one A record and a health check, and you use the service to register 10 instances. Route 53 responds to DNS queries with the IP address for one randomly selected instance from among the healthy instances. If no instances are healthy, Route 53 responds to DNS queries as if all of the instances were healthy.
        
            If you don\'t define a health check for the service, Route 53 assumes that all instances are healthy and returns the applicable value for one randomly selected instance.
        
            For more information about the weighted routing policy, see `Weighted Routing <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted>`__ in the *Route 53 Developer Guide* .
        
          - **DnsRecords** *(list) --* **[REQUIRED]** 
        
            An array that contains one ``DnsRecord`` object for each record that you want Route 53 to create when you register an instance.
        
            - *(dict) --* 
        
              A complex type that contains information about the records that you want Route 53 to create when you register an instance.
        
              - **Type** *(string) --* **[REQUIRED]** 
        
                The type of the resource, which indicates the type of value that Route 53 returns in response to DNS queries.
        
                Note the following:
        
                * **A, AAAA, and SRV records: You can specify settings for a maximum of one A, one AAAA, and one SRV record. You can specify them in any combination.**   
                 
                * **CNAME records:** If you specify ``CNAME`` for ``Type`` , you can\'t define any other records. This is a limitation of DNS—you can\'t create a CNAME record and any other type of record that has the same name as a CNAME record. 
                 
                * **Alias records:** If you want Route 53 to create an alias record when you register an instance, specify ``A`` or ``AAAA`` for ``Type`` . 
                 
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
                 
                * You can\'t specify both ``CNAME`` for ``Type`` and settings for ``HealthCheckConfig`` . If you do, the request will fail with an ``InvalidInput`` error. 
                 
                 **SRV**  
        
                Route 53 returns the value for an SRV record. The value for an SRV record uses the following values:
        
                 ``priority weight port service-hostname``  
        
                Note the following about the values:
        
                * The values of ``priority`` and ``weight`` are both set to ``1`` and can\'t be changed.  
                 
                * The value of ``port`` comes from the value that you specify for the ``AWS_INSTANCE_PORT`` attribute when you submit a  RegisterInstance request.  
                 
                * The value of ``service-hostname`` is a concatenation of the following values: 
        
                  * The value that you specify for ``InstanceId`` when you register an instance. 
                   
                  * The name of the service. 
                   
                  * The name of the namespace.  
                   
                For example, if the value of ``InstanceId`` is ``test`` , the name of the service is ``backend`` , and the name of the namespace is ``example.com`` , the value of ``service-hostname`` is:
        
                 ``test.backend.example.com``  
        
                If you specify settings for an SRV record and if you specify values for ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both in the ``RegisterInstance`` request, Route 53 automatically creates ``A`` and/or ``AAAA`` records that have the same name as the value of ``service-hostname`` in the SRV record. You can ignore these records.
        
              - **TTL** *(integer) --* **[REQUIRED]** 
        
                The amount of time, in seconds, that you want DNS resolvers to cache the settings for this record.
        
                .. note::
        
                  Alias records don\'t include a TTL because Route 53 uses the TTL for the AWS resource that an alias record routes traffic to. If you include the ``AWS_ALIAS_DNS_NAME`` attribute when you submit a  RegisterInstance request, the ``TTL`` value is ignored. Always specify a TTL for the service; you can use a service to register instances that create either alias or non-alias records.
        
        :type HealthCheckConfig: dict
        :param HealthCheckConfig: 
        
           *Public DNS namespaces only.* A complex type that contains settings for an optional health check. If you specify settings for a health check, Route 53 associates the health check with all the records that you specify in ``DnsConfig`` .
        
          For information about the charges for health checks, see `Route 53 Pricing <http://aws.amazon.com/route53/pricing>`__ .
        
          - **Type** *(string) --* 
        
            The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy.
        
            .. warning::
        
              You can\'t change the value of ``Type`` after you create a health check.
        
            You can create the following types of health checks:
        
            * **HTTP** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400. 
             
            * **HTTPS** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400. 
        
            .. warning::
        
               If you specify HTTPS for the value of ``Type`` , the endpoint must support TLS v1.0 or later. 
        
            * **TCP** : Route 53 tries to establish a TCP connection. 
             
            For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Route 53 Developer Guide* .
        
          - **ResourcePath** *(string) --* 
        
            The path that you want Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, such as the file ``/docs/route53-health-check.html`` . Route 53 automatically adds the DNS name for the service and a leading forward slash (``/`` ) character. 
        
          - **FailureThreshold** *(integer) --* 
        
            The number of consecutive health checks that an endpoint must pass or fail for Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Route 53 Developer Guide* .
        
        :type HealthCheckCustomConfig: dict
        :param HealthCheckCustomConfig: 
        
          - **FailureThreshold** *(integer) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Service\': {
                    \'Id\': \'string\',
                    \'Arn\': \'string\',
                    \'Name\': \'string\',
                    \'Description\': \'string\',
                    \'InstanceCount\': 123,
                    \'DnsConfig\': {
                        \'NamespaceId\': \'string\',
                        \'RoutingPolicy\': \'MULTIVALUE\'|\'WEIGHTED\',
                        \'DnsRecords\': [
                            {
                                \'Type\': \'SRV\'|\'A\'|\'AAAA\'|\'CNAME\',
                                \'TTL\': 123
                            },
                        ]
                    },
                    \'HealthCheckConfig\': {
                        \'Type\': \'HTTP\'|\'HTTPS\'|\'TCP\',
                        \'ResourcePath\': \'string\',
                        \'FailureThreshold\': 123
                    },
                    \'HealthCheckCustomConfig\': {
                        \'FailureThreshold\': 123
                    },
                    \'CreateDate\': datetime(2015, 1, 1),
                    \'CreatorRequestId\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Service** *(dict) --* 
        
              A complex type that contains information about the new service.
        
              - **Id** *(string) --* 
        
                The ID that Route 53 assigned to the service when you created it.
        
              - **Arn** *(string) --* 
        
                The Amazon Resource Name (ARN) that Route 53 assigns to the service when you create it.
        
              - **Name** *(string) --* 
        
                The name of the service.
        
              - **Description** *(string) --* 
        
                The description of the service.
        
              - **InstanceCount** *(integer) --* 
        
                The number of instances that are currently associated with the service. Instances that were previously associated with the service but that have been deleted are not included in the count.
        
              - **DnsConfig** *(dict) --* 
        
                A complex type that contains information about the records that you want Route 53 to create when you register an instance.
        
                - **NamespaceId** *(string) --* 
        
                  The ID of the namespace to use for DNS configuration.
        
                - **RoutingPolicy** *(string) --* 
        
                  The routing policy that you want to apply to all records that Route 53 creates when you register an instance and specify this service.
        
                  .. note::
        
                    If you want to use this service to register instances that create alias records, specify ``WEIGHTED`` for the routing policy.
        
                  You can specify the following values:
        
                   **MULTIVALUE**  
        
                  If you define a health check for the service and the health check is healthy, Route 53 returns the applicable value for up to eight instances.
        
                  For example, suppose the service includes configurations for one A record and a health check, and you use the service to register 10 instances. Route 53 responds to DNS queries with IP addresses for up to eight healthy instances. If fewer than eight instances are healthy, Route 53 responds to every DNS query with the IP addresses for all of the healthy instances.
        
                  If you don\'t define a health check for the service, Route 53 assumes that all instances are healthy and returns the values for up to eight instances.
        
                  For more information about the multivalue routing policy, see `Multivalue Answer Routing <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-multivalue>`__ in the *Route 53 Developer Guide* .
        
                   **WEIGHTED**  
        
                  Route 53 returns the applicable value from one randomly selected instance from among the instances that you registered using the same service. Currently, all records have the same weight, so you can\'t route more or less traffic to any instances.
        
                  For example, suppose the service includes configurations for one A record and a health check, and you use the service to register 10 instances. Route 53 responds to DNS queries with the IP address for one randomly selected instance from among the healthy instances. If no instances are healthy, Route 53 responds to DNS queries as if all of the instances were healthy.
        
                  If you don\'t define a health check for the service, Route 53 assumes that all instances are healthy and returns the applicable value for one randomly selected instance.
        
                  For more information about the weighted routing policy, see `Weighted Routing <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted>`__ in the *Route 53 Developer Guide* .
        
                - **DnsRecords** *(list) --* 
        
                  An array that contains one ``DnsRecord`` object for each record that you want Route 53 to create when you register an instance.
        
                  - *(dict) --* 
        
                    A complex type that contains information about the records that you want Route 53 to create when you register an instance.
        
                    - **Type** *(string) --* 
        
                      The type of the resource, which indicates the type of value that Route 53 returns in response to DNS queries.
        
                      Note the following:
        
                      * **A, AAAA, and SRV records: You can specify settings for a maximum of one A, one AAAA, and one SRV record. You can specify them in any combination.**   
                       
                      * **CNAME records:** If you specify ``CNAME`` for ``Type`` , you can\'t define any other records. This is a limitation of DNS—you can\'t create a CNAME record and any other type of record that has the same name as a CNAME record. 
                       
                      * **Alias records:** If you want Route 53 to create an alias record when you register an instance, specify ``A`` or ``AAAA`` for ``Type`` . 
                       
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
                       
                      * You can\'t specify both ``CNAME`` for ``Type`` and settings for ``HealthCheckConfig`` . If you do, the request will fail with an ``InvalidInput`` error. 
                       
                       **SRV**  
        
                      Route 53 returns the value for an SRV record. The value for an SRV record uses the following values:
        
                       ``priority weight port service-hostname``  
        
                      Note the following about the values:
        
                      * The values of ``priority`` and ``weight`` are both set to ``1`` and can\'t be changed.  
                       
                      * The value of ``port`` comes from the value that you specify for the ``AWS_INSTANCE_PORT`` attribute when you submit a  RegisterInstance request.  
                       
                      * The value of ``service-hostname`` is a concatenation of the following values: 
        
                        * The value that you specify for ``InstanceId`` when you register an instance. 
                         
                        * The name of the service. 
                         
                        * The name of the namespace.  
                         
                      For example, if the value of ``InstanceId`` is ``test`` , the name of the service is ``backend`` , and the name of the namespace is ``example.com`` , the value of ``service-hostname`` is:
        
                       ``test.backend.example.com``  
        
                      If you specify settings for an SRV record and if you specify values for ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both in the ``RegisterInstance`` request, Route 53 automatically creates ``A`` and/or ``AAAA`` records that have the same name as the value of ``service-hostname`` in the SRV record. You can ignore these records.
        
                    - **TTL** *(integer) --* 
        
                      The amount of time, in seconds, that you want DNS resolvers to cache the settings for this record.
        
                      .. note::
        
                        Alias records don\'t include a TTL because Route 53 uses the TTL for the AWS resource that an alias record routes traffic to. If you include the ``AWS_ALIAS_DNS_NAME`` attribute when you submit a  RegisterInstance request, the ``TTL`` value is ignored. Always specify a TTL for the service; you can use a service to register instances that create either alias or non-alias records.
        
              - **HealthCheckConfig** *(dict) --* 
        
                 *Public DNS namespaces only.* A complex type that contains settings for an optional health check. If you specify settings for a health check, Route 53 associates the health check with all the records that you specify in ``DnsConfig`` .
        
                For information about the charges for health checks, see `Route 53 Pricing <http://aws.amazon.com/route53/pricing>`__ .
        
                - **Type** *(string) --* 
        
                  The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy.
        
                  .. warning::
        
                    You can\'t change the value of ``Type`` after you create a health check.
        
                  You can create the following types of health checks:
        
                  * **HTTP** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400. 
                   
                  * **HTTPS** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400. 
        
                  .. warning::
        
                     If you specify HTTPS for the value of ``Type`` , the endpoint must support TLS v1.0 or later. 
        
                  * **TCP** : Route 53 tries to establish a TCP connection. 
                   
                  For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Route 53 Developer Guide* .
        
                - **ResourcePath** *(string) --* 
        
                  The path that you want Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, such as the file ``/docs/route53-health-check.html`` . Route 53 automatically adds the DNS name for the service and a leading forward slash (``/`` ) character. 
        
                - **FailureThreshold** *(integer) --* 
        
                  The number of consecutive health checks that an endpoint must pass or fail for Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Route 53 Developer Guide* .
        
              - **HealthCheckCustomConfig** *(dict) --* 
                
                - **FailureThreshold** *(integer) --* 
            
              - **CreateDate** *(datetime) --* 
        
                The date and time that the service was created, in Unix format and Coordinated Universal Time (UTC). The value of ``CreateDate`` is accurate to milliseconds. For example, the value ``1516925490.087`` represents Friday, January 26, 2018 12:11:30.087 AM.
        
              - **CreatorRequestId** *(string) --* 
        
                A unique string that identifies the request and that allows failed requests to be retried without the risk of executing the operation twice. ``CreatorRequestId`` can be any unique string, for example, a date/time stamp.
        
        """
        pass

    def delete_namespace(self, Id: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/DeleteNamespace>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_namespace(
              Id=\'string\'
          )
        :type Id: string
        :param Id: **[REQUIRED]** 
        
          The ID of the namespace that you want to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'OperationId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **OperationId** *(string) --* 
        
              A value that you can use to determine whether the request completed successfully. To get the status of the operation, see  GetOperation .
        
        """
        pass

    def delete_service(self, Id: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/DeleteService>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_service(
              Id=\'string\'
          )
        :type Id: string
        :param Id: **[REQUIRED]** 
        
          The ID of the service that you want to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def deregister_instance(self, ServiceId: str, InstanceId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/DeregisterInstance>`_
        
        **Request Syntax** 
        ::
        
          response = client.deregister_instance(
              ServiceId=\'string\',
              InstanceId=\'string\'
          )
        :type ServiceId: string
        :param ServiceId: **[REQUIRED]** 
        
          The ID of the service that the instance is associated with.
        
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The value that you specified for ``Id`` in the  RegisterInstance request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'OperationId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **OperationId** *(string) --* 
        
              A value that you can use to determine whether the request completed successfully. For more information, see  GetOperation .
        
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

    def get_instance(self, ServiceId: str, InstanceId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/GetInstance>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_instance(
              ServiceId=\'string\',
              InstanceId=\'string\'
          )
        :type ServiceId: string
        :param ServiceId: **[REQUIRED]** 
        
          The ID of the service that the instance is associated with.
        
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The ID of the instance that you want to get information about.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Instance\': {
                    \'Id\': \'string\',
                    \'CreatorRequestId\': \'string\',
                    \'Attributes\': {
                        \'string\': \'string\'
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Instance** *(dict) --* 
        
              A complex type that contains information about a specified instance.
        
              - **Id** *(string) --* 
        
                An identifier that you want to associate with the instance. Note the following:
        
                * If the service that is specified by ``ServiceId`` includes settings for an SRV record, the value of ``InstanceId`` is automatically included as part of the value for the SRV record. For more information, see  DnsRecord$Type . 
                 
                * You can use this value to update an existing instance. 
                 
                * To register a new instance, you must specify a value that is unique among instances that you register by using the same service.  
                 
                * If you specify an existing ``InstanceId`` and ``ServiceId`` , Route 53 updates the existing records. If there\'s also an existing health check, Route 53 deletes the old health check and creates a new one.  
        
                .. note::
        
                   The health check isn\'t deleted immediately, so it will still appear for a while if you submit a ``ListHealthChecks`` request, for example. 
        
              - **CreatorRequestId** *(string) --* 
        
                A unique string that identifies the request and that allows failed ``RegisterInstance`` requests to be retried without the risk of executing the operation twice. You must use a unique ``CreatorRequestId`` string every time you submit a ``RegisterInstance`` request if you\'re registering additional instances for the same namespace and service. ``CreatorRequestId`` can be any unique string, for example, a date/time stamp.
        
              - **Attributes** *(dict) --* 
        
                A string map that contains the following information for the service that you specify in ``ServiceId`` :
        
                * The attributes that apply to the records that are defined in the service.  
                 
                * For each attribute, the applicable value. 
                 
                Supported attribute keys include the following:
        
                 **AWS_ALIAS_DNS_NAME**  
        
                If you want Route 53 to create an alias record that routes traffic to an Elastic Load Balancing load balancer, specify the DNS name that is associated with the load balancer. For information about how to get the DNS name, see \"DNSName\" in the topic `AliasTarget <http://docs.aws.amazon.com/http:/docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html>`__ .
        
                Note the following:
        
                * The configuration for the service that is specified by ``ServiceId`` must include settings for an A record, an AAAA record, or both. 
                 
                * In the service that is specified by ``ServiceId`` , the value of ``RoutingPolicy`` must be ``WEIGHTED`` . 
                 
                * If the service that is specified by ``ServiceId`` includes ``HealthCheckConfig`` settings, Route 53 will create the health check, but it won\'t associate the health check with the alias record. 
                 
                * Auto naming currently doesn\'t support creating alias records that route traffic to AWS resources other than ELB load balancers. 
                 
                * If you specify a value for ``AWS_ALIAS_DNS_NAME`` , don\'t specify values for any of the ``AWS_INSTANCE`` attributes. 
                 
                 **AWS_INSTANCE_CNAME**  
        
                If the service configuration includes a CNAME record, the domain name that you want Route 53 to return in response to DNS queries, for example, ``example.com`` .
        
                This value is required if the service specified by ``ServiceId`` includes settings for an CNAME record.
        
                 **AWS_INSTANCE_IPV4**  
        
                If the service configuration includes an A record, the IPv4 address that you want Route 53 to return in response to DNS queries, for example, ``192.0.2.44`` .
        
                This value is required if the service specified by ``ServiceId`` includes settings for an A record. If the service includes settings for an SRV record, you must specify a value for ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both.
        
                 **AWS_INSTANCE_IPV6**  
        
                If the service configuration includes an AAAA record, the IPv6 address that you want Route 53 to return in response to DNS queries, for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` .
        
                This value is required if the service specified by ``ServiceId`` includes settings for an AAAA record. If the service includes settings for an SRV record, you must specify a value for ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both.
        
                 **AWS_INSTANCE_PORT**  
        
                If the service includes an SRV record, the value that you want Route 53 to return for the port.
        
                If the service includes ``HealthCheckConfig`` , the port on the endpoint that you want Route 53 to send requests to. 
        
                This value is required if you specified settings for an SRV record when you created the service.
        
                - *(string) --* 
                  
                  - *(string) --* 
            
        """
        pass

    def get_instances_health_status(self, ServiceId: str, Instances: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        .. note::
        
          There is a brief delay between when you register an instance and when the health status for the instance is available. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/GetInstancesHealthStatus>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_instances_health_status(
              ServiceId=\'string\',
              Instances=[
                  \'string\',
              ],
              MaxResults=123,
              NextToken=\'string\'
          )
        :type ServiceId: string
        :param ServiceId: **[REQUIRED]** 
        
          The ID of the service that the instance is associated with.
        
        :type Instances: list
        :param Instances: 
        
          An array that contains the IDs of all the instances that you want to get the health status for.
        
          If you omit ``Instances`` , Amazon Route 53 returns the health status for all the instances that are associated with the specified service.
        
          .. note::
        
            To get the IDs for the instances that you\'ve registered by using a specified service, submit a  ListInstances request.
        
          - *(string) --* 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of instances that you want Route 53 to return in the response to a ``GetInstancesHealthStatus`` request. If you don\'t specify a value for ``MaxResults`` , Route 53 returns up to 100 instances.
        
        :type NextToken: string
        :param NextToken: 
        
          For the first ``GetInstancesHealthStatus`` request, omit this value.
        
          If more than ``MaxResults`` instances match the specified criteria, you can submit another ``GetInstancesHealthStatus`` request to get the next group of results. Specify the value of ``NextToken`` from the previous response in the next request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Status\': {
                    \'string\': \'HEALTHY\'|\'UNHEALTHY\'|\'UNKNOWN\'
                },
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Status** *(dict) --* 
        
              A complex type that contains the IDs and the health status of the instances that you specified in the ``GetInstancesHealthStatus`` request.
        
              - *(string) --* 
                
                - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              If more than ``MaxResults`` instances match the specified criteria, you can submit another ``GetInstancesHealthStatus`` request to get the next group of results. Specify the value of ``NextToken`` from the previous response in the next request.
        
        """
        pass

    def get_namespace(self, Id: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/GetNamespace>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_namespace(
              Id=\'string\'
          )
        :type Id: string
        :param Id: **[REQUIRED]** 
        
          The ID of the namespace that you want to get information about.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Namespace\': {
                    \'Id\': \'string\',
                    \'Arn\': \'string\',
                    \'Name\': \'string\',
                    \'Type\': \'DNS_PUBLIC\'|\'DNS_PRIVATE\',
                    \'Description\': \'string\',
                    \'ServiceCount\': 123,
                    \'Properties\': {
                        \'DnsProperties\': {
                            \'HostedZoneId\': \'string\'
                        }
                    },
                    \'CreateDate\': datetime(2015, 1, 1),
                    \'CreatorRequestId\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Namespace** *(dict) --* 
        
              A complex type that contains information about the specified namespace.
        
              - **Id** *(string) --* 
        
                The ID of a namespace.
        
              - **Arn** *(string) --* 
        
                The Amazon Resource Name (ARN) that Route 53 assigns to the namespace when you create it.
        
              - **Name** *(string) --* 
        
                The name of the namespace, such as ``example.com`` .
        
              - **Type** *(string) --* 
        
                The type of the namespace. Valid values are ``DNS_PUBLIC`` and ``DNS_PRIVATE`` .
        
              - **Description** *(string) --* 
        
                The description that you specify for the namespace when you create it.
        
              - **ServiceCount** *(integer) --* 
        
                The number of services that are associated with the namespace.
        
              - **Properties** *(dict) --* 
        
                A complex type that contains information that\'s specific to the type of the namespace.
        
                - **DnsProperties** *(dict) --* 
        
                  A complex type that contains the ID for the hosted zone that Route 53 creates when you create a namespace.
        
                  - **HostedZoneId** *(string) --* 
        
                    The ID for the hosted zone that Route 53 creates when you create a namespace.
        
              - **CreateDate** *(datetime) --* 
        
                The date that the namespace was created, in Unix date/time format and Coordinated Universal Time (UTC). The value of ``CreateDate`` is accurate to milliseconds. For example, the value ``1516925490.087`` represents Friday, January 26, 2018 12:11:30.087 AM.
        
              - **CreatorRequestId** *(string) --* 
        
                A unique string that identifies the request and that allows failed requests to be retried without the risk of executing an operation twice. 
        
        """
        pass

    def get_operation(self, OperationId: str) -> Dict:
        """
        
        .. note::
        
          To get a list of operations that match specified criteria, see  ListOperations .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/GetOperation>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_operation(
              OperationId=\'string\'
          )
        :type OperationId: string
        :param OperationId: **[REQUIRED]** 
        
          The ID of the operation that you want to get more information about.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Operation\': {
                    \'Id\': \'string\',
                    \'Type\': \'CREATE_NAMESPACE\'|\'DELETE_NAMESPACE\'|\'UPDATE_SERVICE\'|\'REGISTER_INSTANCE\'|\'DEREGISTER_INSTANCE\',
                    \'Status\': \'SUBMITTED\'|\'PENDING\'|\'SUCCESS\'|\'FAIL\',
                    \'ErrorMessage\': \'string\',
                    \'ErrorCode\': \'string\',
                    \'CreateDate\': datetime(2015, 1, 1),
                    \'UpdateDate\': datetime(2015, 1, 1),
                    \'Targets\': {
                        \'string\': \'string\'
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Operation** *(dict) --* 
        
              A complex type that contains information about the operation.
        
              - **Id** *(string) --* 
        
                The ID of the operation that you want to get information about.
        
              - **Type** *(string) --* 
        
                The name of the operation that is associated with the specified ID.
        
              - **Status** *(string) --* 
        
                The status of the operation. Values include the following:
        
                * **SUBMITTED** : This is the initial state immediately after you submit a request. 
                 
                * **PENDING** : Route 53 is performing the operation. 
                 
                * **SUCCESS** : The operation succeeded. 
                 
                * **FAIL** : The operation failed. For the failure reason, see ``ErrorMessage`` . 
                 
              - **ErrorMessage** *(string) --* 
        
                If the value of ``Status`` is ``FAIL`` , the reason that the operation failed.
        
              - **ErrorCode** *(string) --* 
        
                The code associated with ``ErrorMessage`` . Values for ``ErrorCode`` include the following:
        
                * ``ACCESS_DENIED``   
                 
                * ``CANNOT_CREATE_HOSTED_ZONE``   
                 
                * ``EXPIRED_TOKEN``   
                 
                * ``HOSTED_ZONE_NOT_FOUND``   
                 
                * ``INTERNAL_FAILURE``   
                 
                * ``INVALID_CHANGE_BATCH``   
                 
                * ``THROTTLED_REQUEST``   
                 
              - **CreateDate** *(datetime) --* 
        
                The date and time that the request was submitted, in Unix date/time format and Coordinated Universal Time (UTC). The value of ``CreateDate`` is accurate to milliseconds. For example, the value ``1516925490.087`` represents Friday, January 26, 2018 12:11:30.087 AM.
        
              - **UpdateDate** *(datetime) --* 
        
                The date and time that the value of ``Status`` changed to the current value, in Unix date/time format and Coordinated Universal Time (UTC). The value of ``UpdateDate`` is accurate to milliseconds. For example, the value ``1516925490.087`` represents Friday, January 26, 2018 12:11:30.087 AM.
        
              - **Targets** *(dict) --* 
        
                The name of the target entity that is associated with the operation:
        
                * **NAMESPACE** : The namespace ID is returned in the ``ResourceId`` property. 
                 
                * **SERVICE** : The service ID is returned in the ``ResourceId`` property. 
                 
                * **INSTANCE** : The instance ID is returned in the ``ResourceId`` property. 
                 
                - *(string) --* 
                  
                  - *(string) --* 
            
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

    def get_service(self, Id: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/GetService>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_service(
              Id=\'string\'
          )
        :type Id: string
        :param Id: **[REQUIRED]** 
        
          The ID of the service that you want to get settings for.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Service\': {
                    \'Id\': \'string\',
                    \'Arn\': \'string\',
                    \'Name\': \'string\',
                    \'Description\': \'string\',
                    \'InstanceCount\': 123,
                    \'DnsConfig\': {
                        \'NamespaceId\': \'string\',
                        \'RoutingPolicy\': \'MULTIVALUE\'|\'WEIGHTED\',
                        \'DnsRecords\': [
                            {
                                \'Type\': \'SRV\'|\'A\'|\'AAAA\'|\'CNAME\',
                                \'TTL\': 123
                            },
                        ]
                    },
                    \'HealthCheckConfig\': {
                        \'Type\': \'HTTP\'|\'HTTPS\'|\'TCP\',
                        \'ResourcePath\': \'string\',
                        \'FailureThreshold\': 123
                    },
                    \'HealthCheckCustomConfig\': {
                        \'FailureThreshold\': 123
                    },
                    \'CreateDate\': datetime(2015, 1, 1),
                    \'CreatorRequestId\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Service** *(dict) --* 
        
              A complex type that contains information about the service.
        
              - **Id** *(string) --* 
        
                The ID that Route 53 assigned to the service when you created it.
        
              - **Arn** *(string) --* 
        
                The Amazon Resource Name (ARN) that Route 53 assigns to the service when you create it.
        
              - **Name** *(string) --* 
        
                The name of the service.
        
              - **Description** *(string) --* 
        
                The description of the service.
        
              - **InstanceCount** *(integer) --* 
        
                The number of instances that are currently associated with the service. Instances that were previously associated with the service but that have been deleted are not included in the count.
        
              - **DnsConfig** *(dict) --* 
        
                A complex type that contains information about the records that you want Route 53 to create when you register an instance.
        
                - **NamespaceId** *(string) --* 
        
                  The ID of the namespace to use for DNS configuration.
        
                - **RoutingPolicy** *(string) --* 
        
                  The routing policy that you want to apply to all records that Route 53 creates when you register an instance and specify this service.
        
                  .. note::
        
                    If you want to use this service to register instances that create alias records, specify ``WEIGHTED`` for the routing policy.
        
                  You can specify the following values:
        
                   **MULTIVALUE**  
        
                  If you define a health check for the service and the health check is healthy, Route 53 returns the applicable value for up to eight instances.
        
                  For example, suppose the service includes configurations for one A record and a health check, and you use the service to register 10 instances. Route 53 responds to DNS queries with IP addresses for up to eight healthy instances. If fewer than eight instances are healthy, Route 53 responds to every DNS query with the IP addresses for all of the healthy instances.
        
                  If you don\'t define a health check for the service, Route 53 assumes that all instances are healthy and returns the values for up to eight instances.
        
                  For more information about the multivalue routing policy, see `Multivalue Answer Routing <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-multivalue>`__ in the *Route 53 Developer Guide* .
        
                   **WEIGHTED**  
        
                  Route 53 returns the applicable value from one randomly selected instance from among the instances that you registered using the same service. Currently, all records have the same weight, so you can\'t route more or less traffic to any instances.
        
                  For example, suppose the service includes configurations for one A record and a health check, and you use the service to register 10 instances. Route 53 responds to DNS queries with the IP address for one randomly selected instance from among the healthy instances. If no instances are healthy, Route 53 responds to DNS queries as if all of the instances were healthy.
        
                  If you don\'t define a health check for the service, Route 53 assumes that all instances are healthy and returns the applicable value for one randomly selected instance.
        
                  For more information about the weighted routing policy, see `Weighted Routing <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted>`__ in the *Route 53 Developer Guide* .
        
                - **DnsRecords** *(list) --* 
        
                  An array that contains one ``DnsRecord`` object for each record that you want Route 53 to create when you register an instance.
        
                  - *(dict) --* 
        
                    A complex type that contains information about the records that you want Route 53 to create when you register an instance.
        
                    - **Type** *(string) --* 
        
                      The type of the resource, which indicates the type of value that Route 53 returns in response to DNS queries.
        
                      Note the following:
        
                      * **A, AAAA, and SRV records: You can specify settings for a maximum of one A, one AAAA, and one SRV record. You can specify them in any combination.**   
                       
                      * **CNAME records:** If you specify ``CNAME`` for ``Type`` , you can\'t define any other records. This is a limitation of DNS—you can\'t create a CNAME record and any other type of record that has the same name as a CNAME record. 
                       
                      * **Alias records:** If you want Route 53 to create an alias record when you register an instance, specify ``A`` or ``AAAA`` for ``Type`` . 
                       
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
                       
                      * You can\'t specify both ``CNAME`` for ``Type`` and settings for ``HealthCheckConfig`` . If you do, the request will fail with an ``InvalidInput`` error. 
                       
                       **SRV**  
        
                      Route 53 returns the value for an SRV record. The value for an SRV record uses the following values:
        
                       ``priority weight port service-hostname``  
        
                      Note the following about the values:
        
                      * The values of ``priority`` and ``weight`` are both set to ``1`` and can\'t be changed.  
                       
                      * The value of ``port`` comes from the value that you specify for the ``AWS_INSTANCE_PORT`` attribute when you submit a  RegisterInstance request.  
                       
                      * The value of ``service-hostname`` is a concatenation of the following values: 
        
                        * The value that you specify for ``InstanceId`` when you register an instance. 
                         
                        * The name of the service. 
                         
                        * The name of the namespace.  
                         
                      For example, if the value of ``InstanceId`` is ``test`` , the name of the service is ``backend`` , and the name of the namespace is ``example.com`` , the value of ``service-hostname`` is:
        
                       ``test.backend.example.com``  
        
                      If you specify settings for an SRV record and if you specify values for ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both in the ``RegisterInstance`` request, Route 53 automatically creates ``A`` and/or ``AAAA`` records that have the same name as the value of ``service-hostname`` in the SRV record. You can ignore these records.
        
                    - **TTL** *(integer) --* 
        
                      The amount of time, in seconds, that you want DNS resolvers to cache the settings for this record.
        
                      .. note::
        
                        Alias records don\'t include a TTL because Route 53 uses the TTL for the AWS resource that an alias record routes traffic to. If you include the ``AWS_ALIAS_DNS_NAME`` attribute when you submit a  RegisterInstance request, the ``TTL`` value is ignored. Always specify a TTL for the service; you can use a service to register instances that create either alias or non-alias records.
        
              - **HealthCheckConfig** *(dict) --* 
        
                 *Public DNS namespaces only.* A complex type that contains settings for an optional health check. If you specify settings for a health check, Route 53 associates the health check with all the records that you specify in ``DnsConfig`` .
        
                For information about the charges for health checks, see `Route 53 Pricing <http://aws.amazon.com/route53/pricing>`__ .
        
                - **Type** *(string) --* 
        
                  The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy.
        
                  .. warning::
        
                    You can\'t change the value of ``Type`` after you create a health check.
        
                  You can create the following types of health checks:
        
                  * **HTTP** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400. 
                   
                  * **HTTPS** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400. 
        
                  .. warning::
        
                     If you specify HTTPS for the value of ``Type`` , the endpoint must support TLS v1.0 or later. 
        
                  * **TCP** : Route 53 tries to establish a TCP connection. 
                   
                  For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Route 53 Developer Guide* .
        
                - **ResourcePath** *(string) --* 
        
                  The path that you want Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, such as the file ``/docs/route53-health-check.html`` . Route 53 automatically adds the DNS name for the service and a leading forward slash (``/`` ) character. 
        
                - **FailureThreshold** *(integer) --* 
        
                  The number of consecutive health checks that an endpoint must pass or fail for Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Route 53 Developer Guide* .
        
              - **HealthCheckCustomConfig** *(dict) --* 
                
                - **FailureThreshold** *(integer) --* 
            
              - **CreateDate** *(datetime) --* 
        
                The date and time that the service was created, in Unix format and Coordinated Universal Time (UTC). The value of ``CreateDate`` is accurate to milliseconds. For example, the value ``1516925490.087`` represents Friday, January 26, 2018 12:11:30.087 AM.
        
              - **CreatorRequestId** *(string) --* 
        
                A unique string that identifies the request and that allows failed requests to be retried without the risk of executing the operation twice. ``CreatorRequestId`` can be any unique string, for example, a date/time stamp.
        
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

    def list_instances(self, ServiceId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/ListInstances>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_instances(
              ServiceId=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type ServiceId: string
        :param ServiceId: **[REQUIRED]** 
        
          The ID of the service that you want to list instances for.
        
        :type NextToken: string
        :param NextToken: 
        
          For the first ``ListInstances`` request, omit this value.
        
          If more than ``MaxResults`` instances match the specified criteria, you can submit another ``ListInstances`` request to get the next group of results. Specify the value of ``NextToken`` from the previous response in the next request.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of instances that you want Amazon Route 53 to return in the response to a ``ListInstances`` request. If you don\'t specify a value for ``MaxResults`` , Route 53 returns up to 100 instances.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Instances\': [
                    {
                        \'Id\': \'string\',
                        \'Attributes\': {
                            \'string\': \'string\'
                        }
                    },
                ],
                \'NextToken\': \'string\'
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
              
            - **NextToken** *(string) --* 
        
              If more than ``MaxResults`` instances match the specified criteria, you can submit another ``ListInstances`` request to get the next group of results. Specify the value of ``NextToken`` from the previous response in the next request.
        
        """
        pass

    def list_namespaces(self, NextToken: str = None, MaxResults: int = None, Filters: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/ListNamespaces>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_namespaces(
              NextToken=\'string\',
              MaxResults=123,
              Filters=[
                  {
                      \'Name\': \'TYPE\',
                      \'Values\': [
                          \'string\',
                      ],
                      \'Condition\': \'EQ\'|\'IN\'|\'BETWEEN\'
                  },
              ]
          )
        :type NextToken: string
        :param NextToken: 
        
          For the first ``ListNamespaces`` request, omit this value.
        
          If the response contains ``NextToken`` , submit another ``ListNamespaces`` request to get the next group of results. Specify the value of ``NextToken`` from the previous response in the next request.
        
          .. note::
        
            Route 53 gets ``MaxResults`` namespaces and then filters them based on the specified criteria. It\'s possible that no namespaces in the first ``MaxResults`` namespaces matched the specified criteria but that subsequent groups of ``MaxResults`` namespaces do contain namespaces that match the criteria.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of namespaces that you want Amazon Route 53 to return in the response to a ``ListNamespaces`` request. If you don\'t specify a value for ``MaxResults`` , Route 53 returns up to 100 namespaces.
        
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
               
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Namespaces\': [
                    {
                        \'Id\': \'string\',
                        \'Arn\': \'string\',
                        \'Name\': \'string\',
                        \'Type\': \'DNS_PUBLIC\'|\'DNS_PRIVATE\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
                  The Amazon Resource Name (ARN) that Route 53 assigns to the namespace when you create it.
        
                - **Name** *(string) --* 
        
                  The name of the namespace. When you create a namespace, Route 53 automatically creates a hosted zone that has the same name as the namespace.
        
                - **Type** *(string) --* 
        
                  The type of the namespace, either public or private.
        
            - **NextToken** *(string) --* 
        
              If the response contains ``NextToken`` , submit another ``ListNamespaces`` request to get the next group of results. Specify the value of ``NextToken`` from the previous response in the next request.
        
              .. note::
        
                Route 53 gets ``MaxResults`` namespaces and then filters them based on the specified criteria. It\'s possible that no namespaces in the first ``MaxResults`` namespaces matched the specified criteria but that subsequent groups of ``MaxResults`` namespaces do contain namespaces that match the criteria.
        
        """
        pass

    def list_operations(self, NextToken: str = None, MaxResults: int = None, Filters: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/ListOperations>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_operations(
              NextToken=\'string\',
              MaxResults=123,
              Filters=[
                  {
                      \'Name\': \'NAMESPACE_ID\'|\'SERVICE_ID\'|\'STATUS\'|\'TYPE\'|\'UPDATE_DATE\',
                      \'Values\': [
                          \'string\',
                      ],
                      \'Condition\': \'EQ\'|\'IN\'|\'BETWEEN\'
                  },
              ]
          )
        :type NextToken: string
        :param NextToken: 
        
          For the first ``ListOperations`` request, omit this value.
        
          If the response contains ``NextToken`` , submit another ``ListOperations`` request to get the next group of results. Specify the value of ``NextToken`` from the previous response in the next request.
        
          .. note::
        
            Route 53 gets ``MaxResults`` operations and then filters them based on the specified criteria. It\'s possible that no operations in the first ``MaxResults`` operations matched the specified criteria but that subsequent groups of ``MaxResults`` operations do contain operations that match the criteria.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items that you want Amazon Route 53 to return in the response to a ``ListOperations`` request. If you don\'t specify a value for ``MaxResults`` , Route 53 returns up to 100 operations.
        
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
               
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Operations\': [
                    {
                        \'Id\': \'string\',
                        \'Status\': \'SUBMITTED\'|\'PENDING\'|\'SUCCESS\'|\'FAIL\'
                    },
                ],
                \'NextToken\': \'string\'
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
                   
                  * **PENDING** : Route 53 is performing the operation. 
                   
                  * **SUCCESS** : The operation succeeded. 
                   
                  * **FAIL** : The operation failed. For the failure reason, see ``ErrorMessage`` . 
                   
            - **NextToken** *(string) --* 
        
              If the response contains ``NextToken`` , submit another ``ListOperations`` request to get the next group of results. Specify the value of ``NextToken`` from the previous response in the next request.
        
              .. note::
        
                Route 53 gets ``MaxResults`` operations and then filters them based on the specified criteria. It\'s possible that no operations in the first ``MaxResults`` operations matched the specified criteria but that subsequent groups of ``MaxResults`` operations do contain operations that match the criteria.
        
        """
        pass

    def list_services(self, NextToken: str = None, MaxResults: int = None, Filters: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/ListServices>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_services(
              NextToken=\'string\',
              MaxResults=123,
              Filters=[
                  {
                      \'Name\': \'NAMESPACE_ID\',
                      \'Values\': [
                          \'string\',
                      ],
                      \'Condition\': \'EQ\'|\'IN\'|\'BETWEEN\'
                  },
              ]
          )
        :type NextToken: string
        :param NextToken: 
        
          For the first ``ListServices`` request, omit this value.
        
          If the response contains ``NextToken`` , submit another ``ListServices`` request to get the next group of results. Specify the value of ``NextToken`` from the previous response in the next request.
        
          .. note::
        
            Route 53 gets ``MaxResults`` services and then filters them based on the specified criteria. It\'s possible that no services in the first ``MaxResults`` services matched the specified criteria but that subsequent groups of ``MaxResults`` services do contain services that match the criteria.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of services that you want Amazon Route 53 to return in the response to a ``ListServices`` request. If you don\'t specify a value for ``MaxResults`` , Route 53 returns up to 100 services.
        
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
               
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Services\': [
                    {
                        \'Id\': \'string\',
                        \'Arn\': \'string\',
                        \'Name\': \'string\',
                        \'Description\': \'string\',
                        \'InstanceCount\': 123
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Services** *(list) --* 
        
              An array that contains one ``ServiceSummary`` object for each service that matches the specified filter criteria.
        
              - *(dict) --* 
        
                A complex type that contains information about a specified service.
        
                - **Id** *(string) --* 
        
                  The ID that Route 53 assigned to the service when you created it.
        
                - **Arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) that Route 53 assigns to the service when you create it.
        
                - **Name** *(string) --* 
        
                  The name of the service.
        
                - **Description** *(string) --* 
        
                  The description that you specify when you create the service.
        
                - **InstanceCount** *(integer) --* 
        
                  The number of instances that are currently associated with the service. Instances that were previously associated with the service but that have been deleted are not included in the count.
        
            - **NextToken** *(string) --* 
        
              If the response contains ``NextToken`` , submit another ``ListServices`` request to get the next group of results. Specify the value of ``NextToken`` from the previous response in the next request.
        
              .. note::
        
                Route 53 gets ``MaxResults`` services and then filters them based on the specified criteria. It\'s possible that no services in the first ``MaxResults`` services matched the specified criteria but that subsequent groups of ``MaxResults`` services do contain services that match the criteria.
        
        """
        pass

    def register_instance(self, ServiceId: str, InstanceId: str, Attributes: Dict, CreatorRequestId: str = None) -> Dict:
        """
        Creates or updates one or more records and optionally a health check based on the settings in a specified service. When you submit a ``RegisterInstance`` request, Amazon Route 53 does the following:
        
        * For each DNS record that you define in the service specified by ``ServiceId`` , creates or updates a record in the hosted zone that is associated with the corresponding namespace 
         
        * If the service includes ``HealthCheckConfig`` , creates or updates a health check based on the settings in the health check configuration 
         
        * Associates the health check, if any, with each of the records 
         
        .. warning::
        
          One ``RegisterInstance`` request must complete before you can submit another request and specify the same service ID and instance ID.
        
        For more information, see  CreateService .
        
        When Route 53 receives a DNS query for the specified DNS name, it returns the applicable value:
        
        * **If the health check is healthy** : returns all the records 
         
        * **If the health check is unhealthy** : returns the applicable value for the last healthy instance 
         
        * **If you didn\'t specify a health check configuration** : returns all the records 
         
        For the current limit on the number of instances that you can register using the same namespace and using the same service, see `Limits on Auto Naming <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html#limits-api-entities-autonaming>`__ in the *Route 53 Developer Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/RegisterInstance>`_
        
        **Request Syntax** 
        ::
        
          response = client.register_instance(
              ServiceId=\'string\',
              InstanceId=\'string\',
              CreatorRequestId=\'string\',
              Attributes={
                  \'string\': \'string\'
              }
          )
        :type ServiceId: string
        :param ServiceId: **[REQUIRED]** 
        
          The ID of the service that you want to use for settings for the records and health check that Route 53 will create.
        
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          An identifier that you want to associate with the instance. Note the following:
        
          * If the service that is specified by ``ServiceId`` includes settings for an SRV record, the value of ``InstanceId`` is automatically included as part of the value for the SRV record. For more information, see  DnsRecord$Type . 
           
          * You can use this value to update an existing instance. 
           
          * To register a new instance, you must specify a value that is unique among instances that you register by using the same service.  
           
          * If you specify an existing ``InstanceId`` and ``ServiceId`` , Route 53 updates the existing records. If there\'s also an existing health check, Route 53 deletes the old health check and creates a new one.  
        
          .. note::
        
             The health check isn\'t deleted immediately, so it will still appear for a while if you submit a ``ListHealthChecks`` request, for example. 
        
        :type CreatorRequestId: string
        :param CreatorRequestId: 
        
          A unique string that identifies the request and that allows failed ``RegisterInstance`` requests to be retried without the risk of executing the operation twice. You must use a unique ``CreatorRequestId`` string every time you submit a ``RegisterInstance`` request if you\'re registering additional instances for the same namespace and service. ``CreatorRequestId`` can be any unique string, for example, a date/time stamp.
        
          This field is autopopulated if not provided.
        
        :type Attributes: dict
        :param Attributes: **[REQUIRED]** 
        
          A string map that contains the following information for the service that you specify in ``ServiceId`` :
        
          * The attributes that apply to the records that are defined in the service.  
           
          * For each attribute, the applicable value. 
           
          Supported attribute keys include the following:
        
           **AWS_ALIAS_DNS_NAME**  
        
          If you want Route 53 to create an alias record that routes traffic to an Elastic Load Balancing load balancer, specify the DNS name that is associated with the load balancer. For information about how to get the DNS name, see \"DNSName\" in the topic `AliasTarget <http://docs.aws.amazon.com/http:/docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html>`__ .
        
          Note the following:
        
          * The configuration for the service that is specified by ``ServiceId`` must include settings for an A record, an AAAA record, or both. 
           
          * In the service that is specified by ``ServiceId`` , the value of ``RoutingPolicy`` must be ``WEIGHTED`` . 
           
          * If the service that is specified by ``ServiceId`` includes ``HealthCheckConfig`` settings, Route 53 will create the health check, but it won\'t associate the health check with the alias record. 
           
          * Auto naming currently doesn\'t support creating alias records that route traffic to AWS resources other than ELB load balancers. 
           
          * If you specify a value for ``AWS_ALIAS_DNS_NAME`` , don\'t specify values for any of the ``AWS_INSTANCE`` attributes. 
           
           **AWS_INSTANCE_CNAME**  
        
          If the service configuration includes a CNAME record, the domain name that you want Route 53 to return in response to DNS queries, for example, ``example.com`` .
        
          This value is required if the service specified by ``ServiceId`` includes settings for an CNAME record.
        
           **AWS_INSTANCE_IPV4**  
        
          If the service configuration includes an A record, the IPv4 address that you want Route 53 to return in response to DNS queries, for example, ``192.0.2.44`` .
        
          This value is required if the service specified by ``ServiceId`` includes settings for an A record. If the service includes settings for an SRV record, you must specify a value for ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both.
        
           **AWS_INSTANCE_IPV6**  
        
          If the service configuration includes an AAAA record, the IPv6 address that you want Route 53 to return in response to DNS queries, for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` .
        
          This value is required if the service specified by ``ServiceId`` includes settings for an AAAA record. If the service includes settings for an SRV record, you must specify a value for ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both.
        
           **AWS_INSTANCE_PORT**  
        
          If the service includes an SRV record, the value that you want Route 53 to return for the port.
        
          If the service includes ``HealthCheckConfig`` , the port on the endpoint that you want Route 53 to send requests to. 
        
          This value is required if you specified settings for an SRV record when you created the service.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'OperationId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **OperationId** *(string) --* 
        
              A value that you can use to determine whether the request completed successfully. To get the status of the operation, see  GetOperation .
        
        """
        pass

    def update_instance_custom_health_status(self, ServiceId: str, InstanceId: str, Status: str):
        """
        
        **Request Syntax** 
        ::
        
          response = client.update_instance_custom_health_status(
              ServiceId=\'string\',
              InstanceId=\'string\',
              Status=\'HEALTHY\'|\'UNHEALTHY\'
          )
        :type ServiceId: string
        :param ServiceId: **[REQUIRED]** 
        
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
        :type Status: string
        :param Status: **[REQUIRED]** 
        
        :returns: None
        """
        pass

    def update_service(self, Id: str, Service: Dict) -> Dict:
        """
        Submits a request to perform the following operations:
        
        * Add or delete ``DnsRecords`` configurations 
         
        * Update the TTL setting for existing ``DnsRecords`` configurations 
         
        * Add, update, or delete ``HealthCheckConfig`` for a specified service 
         
        You must specify all ``DnsRecords`` configurations (and, optionally, ``HealthCheckConfig`` ) that you want to appear in the updated service. Any current configurations that don\'t appear in an ``UpdateService`` request are deleted.
        
        When you update the TTL setting for a service, Amazon Route 53 also updates the corresponding settings in all the records and health checks that were created by using the specified service.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicediscovery-2017-03-14/UpdateService>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_service(
              Id=\'string\',
              Service={
                  \'Description\': \'string\',
                  \'DnsConfig\': {
                      \'DnsRecords\': [
                          {
                              \'Type\': \'SRV\'|\'A\'|\'AAAA\'|\'CNAME\',
                              \'TTL\': 123
                          },
                      ]
                  },
                  \'HealthCheckConfig\': {
                      \'Type\': \'HTTP\'|\'HTTPS\'|\'TCP\',
                      \'ResourcePath\': \'string\',
                      \'FailureThreshold\': 123
                  }
              }
          )
        :type Id: string
        :param Id: **[REQUIRED]** 
        
          The ID of the service that you want to update.
        
        :type Service: dict
        :param Service: **[REQUIRED]** 
        
          A complex type that contains the new settings for the service.
        
          - **Description** *(string) --* 
        
            A description for the service.
        
          - **DnsConfig** *(dict) --* **[REQUIRED]** 
        
            A complex type that contains information about the records that you want Route 53 to create when you register an instance.
        
            - **DnsRecords** *(list) --* **[REQUIRED]** 
        
              An array that contains one ``DnsRecord`` object for each record that you want Route 53 to create when you register an instance.
        
              - *(dict) --* 
        
                A complex type that contains information about the records that you want Route 53 to create when you register an instance.
        
                - **Type** *(string) --* **[REQUIRED]** 
        
                  The type of the resource, which indicates the type of value that Route 53 returns in response to DNS queries.
        
                  Note the following:
        
                  * **A, AAAA, and SRV records: You can specify settings for a maximum of one A, one AAAA, and one SRV record. You can specify them in any combination.**   
                   
                  * **CNAME records:** If you specify ``CNAME`` for ``Type`` , you can\'t define any other records. This is a limitation of DNS—you can\'t create a CNAME record and any other type of record that has the same name as a CNAME record. 
                   
                  * **Alias records:** If you want Route 53 to create an alias record when you register an instance, specify ``A`` or ``AAAA`` for ``Type`` . 
                   
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
                   
                  * You can\'t specify both ``CNAME`` for ``Type`` and settings for ``HealthCheckConfig`` . If you do, the request will fail with an ``InvalidInput`` error. 
                   
                   **SRV**  
        
                  Route 53 returns the value for an SRV record. The value for an SRV record uses the following values:
        
                   ``priority weight port service-hostname``  
        
                  Note the following about the values:
        
                  * The values of ``priority`` and ``weight`` are both set to ``1`` and can\'t be changed.  
                   
                  * The value of ``port`` comes from the value that you specify for the ``AWS_INSTANCE_PORT`` attribute when you submit a  RegisterInstance request.  
                   
                  * The value of ``service-hostname`` is a concatenation of the following values: 
        
                    * The value that you specify for ``InstanceId`` when you register an instance. 
                     
                    * The name of the service. 
                     
                    * The name of the namespace.  
                     
                  For example, if the value of ``InstanceId`` is ``test`` , the name of the service is ``backend`` , and the name of the namespace is ``example.com`` , the value of ``service-hostname`` is:
        
                   ``test.backend.example.com``  
        
                  If you specify settings for an SRV record and if you specify values for ``AWS_INSTANCE_IPV4`` , ``AWS_INSTANCE_IPV6`` , or both in the ``RegisterInstance`` request, Route 53 automatically creates ``A`` and/or ``AAAA`` records that have the same name as the value of ``service-hostname`` in the SRV record. You can ignore these records.
        
                - **TTL** *(integer) --* **[REQUIRED]** 
        
                  The amount of time, in seconds, that you want DNS resolvers to cache the settings for this record.
        
                  .. note::
        
                    Alias records don\'t include a TTL because Route 53 uses the TTL for the AWS resource that an alias record routes traffic to. If you include the ``AWS_ALIAS_DNS_NAME`` attribute when you submit a  RegisterInstance request, the ``TTL`` value is ignored. Always specify a TTL for the service; you can use a service to register instances that create either alias or non-alias records.
        
          - **HealthCheckConfig** *(dict) --* 
        
             *Public DNS namespaces only.* A complex type that contains settings for an optional health check. If you specify settings for a health check, Amazon Route 53 associates the health check with all the records that you specify in ``DnsConfig`` .
        
             **A and AAAA records**  
        
            If ``DnsConfig`` includes configurations for both A and AAAA records, Route 53 creates a health check that uses the IPv4 address to check the health of the resource. If the endpoint that is specified by the IPv4 address is unhealthy, Route 53 considers both the A and AAAA records to be unhealthy. 
        
             **CNAME records**  
        
            You can\'t specify settings for ``HealthCheckConfig`` when the ``DNSConfig`` includes ``CNAME`` for the value of ``Type`` . If you do, the ``CreateService`` request will fail with an ``InvalidInput`` error.
        
             **Request interval**  
        
            The health check uses 30 seconds as the request interval. This is the number of seconds between the time that each Route 53 health checker gets a response from your endpoint and the time that it sends the next health check request. A health checker in each data center around the world sends your endpoint a health check request every 30 seconds. On average, your endpoint receives a health check request about every two seconds. Health checkers in different data centers don\'t coordinate with one another, so you\'ll sometimes see several requests per second followed by a few seconds with no health checks at all.
        
             **Health checking regions**  
        
            Health checkers perform checks from all Route 53 health-checking regions. For a list of the current regions, see `Regions <http://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckConfig.html#Route53-Type-HealthCheckConfig-Regions>`__ .
        
             **Alias records**  
        
            When you register an instance, if you include the ``AWS_ALIAS_DNS_NAME`` attribute, Route 53 creates an alias record. Note the following:
        
            * Route 53 automatically sets ``EvaluateTargetHealth`` to true for alias records. When ``EvaluateTargetHealth`` is true, the alias record inherits the health of the referenced AWS resource. such as an ELB load balancer. For more information, see `EvaluateTargetHealth <http://docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html#Route53-Type-AliasTarget-EvaluateTargetHealth>`__ . 
             
            * If you include ``HealthCheckConfig`` and then use the service to register an instance that creates an alias record, Route 53 doesn\'t create the health check. 
             
            For information about the charges for health checks, see `Route 53 Pricing <http://aws.amazon.com/route53/pricing>`__ .
        
            - **Type** *(string) --* 
        
              The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy.
        
              .. warning::
        
                You can\'t change the value of ``Type`` after you create a health check.
        
              You can create the following types of health checks:
        
              * **HTTP** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400. 
               
              * **HTTPS** : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400. 
        
              .. warning::
        
                 If you specify HTTPS for the value of ``Type`` , the endpoint must support TLS v1.0 or later. 
        
              * **TCP** : Route 53 tries to establish a TCP connection. 
               
              For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Route 53 Developer Guide* .
        
            - **ResourcePath** *(string) --* 
        
              The path that you want Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, such as the file ``/docs/route53-health-check.html`` . Route 53 automatically adds the DNS name for the service and a leading forward slash (``/`` ) character. 
        
            - **FailureThreshold** *(integer) --* 
        
              The number of consecutive health checks that an endpoint must pass or fail for Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`__ in the *Route 53 Developer Guide* .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'OperationId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **OperationId** *(string) --* 
        
              A value that you can use to determine whether the request completed successfully. To get the status of the operation, see  GetOperation .
        
        """
        pass
