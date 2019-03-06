from typing import Dict
from botocore.paginate import Paginator


class ListAccelerators(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`GlobalAccelerator.Client.list_accelerators`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/globalaccelerator-2018-08-08/ListAccelerators>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Accelerators': [
                    {
                        'AcceleratorArn': 'string',
                        'Name': 'string',
                        'IpAddressType': 'IPV4',
                        'Enabled': True|False,
                        'IpSets': [
                            {
                                'IpFamily': 'string',
                                'IpAddresses': [
                                    'string',
                                ]
                            },
                        ],
                        'Status': 'DEPLOYED'|'IN_PROGRESS',
                        'CreatedTime': datetime(2015, 1, 1),
                        'LastModifiedTime': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Accelerators** *(list) --* 
              The list of accelerators for a customer account.
              - *(dict) --* 
                An accelerator is a complex type that includes one or more listeners that process inbound connections and then direct traffic to one or more endpoint groups, each of which includes endpoints, such as load balancers.
                - **AcceleratorArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the accelerator.
                - **Name** *(string) --* 
                  The name of the accelerator. The name can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens (-), and must not begin or end with a hyphen.
                - **IpAddressType** *(string) --* 
                  The value for the address type must be IPv4. 
                - **Enabled** *(boolean) --* 
                  Indicates whether theaccelerator is enabled. The value is true or false. The default value is true. 
                  If the value is set to true, the accelerator cannot be deleted. If set to false, accelerator can be deleted.
                - **IpSets** *(list) --* 
                  IP address set associated with the accelerator.
                  - *(dict) --* 
                    A complex type for the set of IP addresses for an accelerator.
                    - **IpFamily** *(string) --* 
                      The types of IP addresses included in this IP set.
                    - **IpAddresses** *(list) --* 
                      The array of IP addresses in the IP address set. An IP address set can have a maximum of two IP addresses.
                      - *(string) --* 
                - **Status** *(string) --* 
                  Describes the deployment status of the accelerator.
                - **CreatedTime** *(datetime) --* 
                  The date and time that the accelerator was created.
                - **LastModifiedTime** *(datetime) --* 
                  The date and time that the accelerator was last modified.
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


class ListEndpointGroups(Paginator):
    def paginate(self, ListenerArn: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`GlobalAccelerator.Client.list_endpoint_groups`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/globalaccelerator-2018-08-08/ListEndpointGroups>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ListenerArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'EndpointGroups': [
                    {
                        'EndpointGroupArn': 'string',
                        'EndpointGroupRegion': 'string',
                        'EndpointDescriptions': [
                            {
                                'EndpointId': 'string',
                                'Weight': 123,
                                'HealthState': 'INITIAL'|'HEALTHY'|'UNHEALTHY',
                                'HealthReason': 'string'
                            },
                        ],
                        'TrafficDialPercentage': ...,
                        'HealthCheckPort': 123,
                        'HealthCheckProtocol': 'TCP'|'HTTP'|'HTTPS',
                        'HealthCheckPath': 'string',
                        'HealthCheckIntervalSeconds': 123,
                        'ThresholdCount': 123
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **EndpointGroups** *(list) --* 
              The list of the endpoint groups associated with a listener.
              - *(dict) --* 
                A complex type for the endpoint group. An AWS Region can have only one endpoint group for a specific listener. 
                - **EndpointGroupArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the endpoint group.
                - **EndpointGroupRegion** *(string) --* 
                  The AWS Region that this endpoint group belongs.
                - **EndpointDescriptions** *(list) --* 
                  The list of endpoint objects.
                  - *(dict) --* 
                    A complex type for an endpoint. Each endpoint group can include one or more endpoints, such as load balancers.
                    - **EndpointId** *(string) --* 
                      An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an Elastic IP address, this is the Elastic IP address allocation ID.
                    - **Weight** *(integer) --* 
                      The weight associated with the endpoint. When you add weights to endpoints, you configure AWS Global Accelerator to route traffic based on proportions that you specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20). The result is that 4/20 of your traffic, on average, is routed to the first endpoint, 5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last endpoint. For more information, see `Endpoint Weights <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html>`__ in the *AWS Global Accelerator Developer Guide* . 
                    - **HealthState** *(string) --* 
                      The health status of the endpoint.
                    - **HealthReason** *(string) --* 
                      The reason code associated with why the endpoint is not healthy. If the endpoint state is healthy, a reason code is not provided.
                      If the endpoint state is **unhealthy** , the reason code can be one of the following values:
                      * **Timeout** : The health check requests to the endpoint are timing out before returning a status. 
                      * **Failed** : The health check failed, for example because the endpoint response was invalid (malformed). 
                      If the endpoint state is **initial** , the reason code can be one of the following values:
                      * **ProvisioningInProgress** : The endpoint is in the process of being provisioned. 
                      * **InitialHealthChecking** : Global Accelerator is still setting up the minimum number of health checks for the endpoint that are required to determine its health status. 
                - **TrafficDialPercentage** *(float) --* 
                  The percentage of traffic to send to an AWS Region. Additional traffic is distributed to other endpoint groups for this listener. 
                  Use this action to increase (dial up) or decrease (dial down) traffic to a specific Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing.
                  The default value is 100.
                - **HealthCheckPort** *(integer) --* 
                  The port that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group. 
                  The default port is the port for the listener that this endpoint group is associated with. If the listener port is a list, Global Accelerator uses the first specified port in the list of ports.
                - **HealthCheckProtocol** *(string) --* 
                  The protocol that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group. The default value is TCP.
                - **HealthCheckPath** *(string) --* 
                  If the protocol is HTTP/S, then this value provides the ping path that Global Accelerator uses for the destination on the endpoints for health checks. The default is slash (/).
                - **HealthCheckIntervalSeconds** *(integer) --* 
                  The time—10 seconds or 30 seconds—between health checks for each endpoint. The default value is 30.
                - **ThresholdCount** *(integer) --* 
                  The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.
        :type ListenerArn: string
        :param ListenerArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the listener.
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


class ListListeners(Paginator):
    def paginate(self, AcceleratorArn: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`GlobalAccelerator.Client.list_listeners`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/globalaccelerator-2018-08-08/ListListeners>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AcceleratorArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Listeners': [
                    {
                        'ListenerArn': 'string',
                        'PortRanges': [
                            {
                                'FromPort': 123,
                                'ToPort': 123
                            },
                        ],
                        'Protocol': 'TCP'|'UDP',
                        'ClientAffinity': 'NONE'|'SOURCE_IP'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Listeners** *(list) --* 
              The list of listeners for an accelerator.
              - *(dict) --* 
                A complex type for a listener.
                - **ListenerArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the listener.
                - **PortRanges** *(list) --* 
                  The list of port ranges for the connections from clients to the accelerator.
                  - *(dict) --* 
                    A complex type for a range of ports for a listener.
                    - **FromPort** *(integer) --* 
                      The first port in the range of ports, inclusive.
                    - **ToPort** *(integer) --* 
                      The last port in the range of ports, inclusive.
                - **Protocol** *(string) --* 
                  The protocol for the connections from clients to the accelerator.
                - **ClientAffinity** *(string) --* 
                  Client affinity lets you direct all requests from a user to the same endpoint, if you have stateful applications, regardless of the port and protocol of the client request. Clienty affinity gives you control over whether to always route each client to the same specific endpoint.
                  AWS Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal endpoint for a connection. If client affinity is ``NONE`` , Global Accelerator uses the "five-tuple" (5-tuple) properties—source IP address, source port, destination IP address, destination port, and protocol—to select the hash value, and then chooses the best endpoint. However, with this setting, if someone uses different ports to connect to Global Accelerator, their connections might not be always routed to the same endpoint because the hash value changes. 
                  If you want a given client to always be routed to the same endpoint, set client affinity to ``SOURCE_IP`` instead. When you use the ``SOURCE_IP`` setting, Global Accelerator uses the "two-tuple" (2-tuple) properties— source (client) IP address and destination IP address—to select the hash value.
                  The default value is ``NONE`` .
        :type AcceleratorArn: string
        :param AcceleratorArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the accelerator for which you want to list listener objects.
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
