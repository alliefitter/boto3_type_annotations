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

    def create_accelerator(self, Name: str, IdempotencyToken: str, IpAddressType: str = None, Enabled: bool = None) -> Dict:
        """
        Create an accelerator. An accelerator includes one or more listeners that process inbound connections and direct traffic to one or more endpoint groups, each of which includes endpoints, such as Network Load Balancers. To see an AWS CLI example of creating an accelerator, scroll down to **Example** .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/globalaccelerator-2018-08-08/CreateAccelerator>`_
        
        **Request Syntax**
        ::
          response = client.create_accelerator(
              Name='string',
              IpAddressType='IPV4',
              Enabled=True|False,
              IdempotencyToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'Accelerator': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Accelerator** *(dict) --* 
              The accelerator that is created by specifying a listener and the supported IP address types.
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
        :type Name: string
        :param Name: **[REQUIRED]**
          The name of an accelerator. The name can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens (-), and must not begin or end with a hyphen.
        :type IpAddressType: string
        :param IpAddressType:
          The value for the address type must be IPv4.
        :type Enabled: boolean
        :param Enabled:
          Indicates whether an accelerator is enabled. The value is true or false. The default value is true.
          If the value is set to true, an accelerator cannot be deleted. If set to false, the accelerator can be deleted.
        :type IdempotencyToken: string
        :param IdempotencyToken: **[REQUIRED]**
          A unique, case-sensitive identifier that you provide to ensure the idempotency—that is, the uniqueness—of an accelerator.
        :rtype: dict
        :returns:
        """
        pass

    def create_endpoint_group(self, ListenerArn: str, EndpointGroupRegion: str, IdempotencyToken: str, EndpointConfigurations: List = None, TrafficDialPercentage: float = None, HealthCheckPort: int = None, HealthCheckProtocol: str = None, HealthCheckPath: str = None, HealthCheckIntervalSeconds: int = None, ThresholdCount: int = None) -> Dict:
        """
        Create an endpoint group for the specified listener. An endpoint group is a collection of endpoints in one AWS Region. To see an AWS CLI example of creating an endpoint group, scroll down to **Example** .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/globalaccelerator-2018-08-08/CreateEndpointGroup>`_
        
        **Request Syntax**
        ::
          response = client.create_endpoint_group(
              ListenerArn='string',
              EndpointGroupRegion='string',
              EndpointConfigurations=[
                  {
                      'EndpointId': 'string',
                      'Weight': 123
                  },
              ],
              TrafficDialPercentage=...,
              HealthCheckPort=123,
              HealthCheckProtocol='TCP'|'HTTP'|'HTTPS',
              HealthCheckPath='string',
              HealthCheckIntervalSeconds=123,
              ThresholdCount=123,
              IdempotencyToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'EndpointGroup': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **EndpointGroup** *(dict) --* 
              The information about the endpoint group that was created.
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
        :type EndpointGroupRegion: string
        :param EndpointGroupRegion: **[REQUIRED]**
          The name of the AWS Region where the endpoint group is located. A listener can have only one endpoint group in a specific Region.
        :type EndpointConfigurations: list
        :param EndpointConfigurations:
          The list of endpoint objects.
          - *(dict) --*
            A complex type for endpoints.
            - **EndpointId** *(string) --*
              An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an Elastic IP address, this is the Elastic IP address allocation ID.
            - **Weight** *(integer) --*
              The weight associated with the endpoint. When you add weights to endpoints, you configure AWS Global Accelerator to route traffic based on proportions that you specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20). The result is that 4/20 of your traffic, on average, is routed to the first endpoint, 5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last endpoint. For more information, see `Endpoint Weights <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html>`__ in the *AWS Global Accelerator Developer Guide* .
        :type TrafficDialPercentage: float
        :param TrafficDialPercentage:
          The percentage of traffic to send to an AWS Region. Additional traffic is distributed to other endpoint groups for this listener.
          Use this action to increase (dial up) or decrease (dial down) traffic to a specific Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing.
          The default value is 100.
        :type HealthCheckPort: integer
        :param HealthCheckPort:
          The port that AWS Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default port is the listener port that this endpoint group is associated with. If listener port is a list of ports, Global Accelerator uses the first port in the list.
        :type HealthCheckProtocol: string
        :param HealthCheckProtocol:
          The protocol that AWS Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default value is TCP.
        :type HealthCheckPath: string
        :param HealthCheckPath:
          If the protocol is HTTP/S, then this specifies the path that is the destination for health check targets. The default value is slash (/).
        :type HealthCheckIntervalSeconds: integer
        :param HealthCheckIntervalSeconds:
          The time—10 seconds or 30 seconds—between each health check for an endpoint. The default value is 30.
        :type ThresholdCount: integer
        :param ThresholdCount:
          The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.
        :type IdempotencyToken: string
        :param IdempotencyToken: **[REQUIRED]**
          A unique, case-sensitive identifier that you provide to ensure the idempotency—that is, the uniqueness—of the request.
        :rtype: dict
        :returns:
        """
        pass

    def create_listener(self, AcceleratorArn: str, PortRanges: List, Protocol: str, IdempotencyToken: str, ClientAffinity: str = None) -> Dict:
        """
        Create a listener to process inbound connections from clients to an accelerator. Connections arrive to assigned static IP addresses on a port, port range, or list of port ranges that you specify. To see an AWS CLI example of creating a listener, scroll down to **Example** .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/globalaccelerator-2018-08-08/CreateListener>`_
        
        **Request Syntax**
        ::
          response = client.create_listener(
              AcceleratorArn='string',
              PortRanges=[
                  {
                      'FromPort': 123,
                      'ToPort': 123
                  },
              ],
              Protocol='TCP'|'UDP',
              ClientAffinity='NONE'|'SOURCE_IP',
              IdempotencyToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'Listener': {
                    'ListenerArn': 'string',
                    'PortRanges': [
                        {
                            'FromPort': 123,
                            'ToPort': 123
                        },
                    ],
                    'Protocol': 'TCP'|'UDP',
                    'ClientAffinity': 'NONE'|'SOURCE_IP'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Listener** *(dict) --* 
              The listener that you've created.
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
          The Amazon Resource Name (ARN) of your accelerator.
        :type PortRanges: list
        :param PortRanges: **[REQUIRED]**
          The list of port ranges to support for connections from clients to your accelerator.
          - *(dict) --*
            A complex type for a range of ports for a listener.
            - **FromPort** *(integer) --*
              The first port in the range of ports, inclusive.
            - **ToPort** *(integer) --*
              The last port in the range of ports, inclusive.
        :type Protocol: string
        :param Protocol: **[REQUIRED]**
          The protocol for connections from clients to your accelerator.
        :type ClientAffinity: string
        :param ClientAffinity:
          Client affinity lets you direct all requests from a user to the same endpoint, if you have stateful applications, regardless of the port and protocol of the client request. Clienty affinity gives you control over whether to always route each client to the same specific endpoint.
          AWS Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal endpoint for a connection. If client affinity is ``NONE`` , Global Accelerator uses the \"five-tuple\" (5-tuple) properties—source IP address, source port, destination IP address, destination port, and protocol—to select the hash value, and then chooses the best endpoint. However, with this setting, if someone uses different ports to connect to Global Accelerator, their connections might not be always routed to the same endpoint because the hash value changes.
          If you want a given client to always be routed to the same endpoint, set client affinity to ``SOURCE_IP`` instead. When you use the ``SOURCE_IP`` setting, Global Accelerator uses the \"two-tuple\" (2-tuple) properties— source (client) IP address and destination IP address—to select the hash value.
          The default value is ``NONE`` .
        :type IdempotencyToken: string
        :param IdempotencyToken: **[REQUIRED]**
          A unique, case-sensitive identifier that you provide to ensure the idempotency—that is, the uniqueness—of the request.
        :rtype: dict
        :returns:
        """
        pass

    def delete_accelerator(self, AcceleratorArn: str):
        """
        Delete an accelerator. Note: before you can delete an accelerator, you must disable it and remove all dependent resources (listeners and endpoint groups).
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/globalaccelerator-2018-08-08/DeleteAccelerator>`_
        
        **Request Syntax**
        ::
          response = client.delete_accelerator(
              AcceleratorArn='string'
          )
        :type AcceleratorArn: string
        :param AcceleratorArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of an accelerator.
        :returns: None
        """
        pass

    def delete_endpoint_group(self, EndpointGroupArn: str):
        """
        Delete an endpoint group from a listener.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/globalaccelerator-2018-08-08/DeleteEndpointGroup>`_
        
        **Request Syntax**
        ::
          response = client.delete_endpoint_group(
              EndpointGroupArn='string'
          )
        :type EndpointGroupArn: string
        :param EndpointGroupArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the endpoint group to delete.
        :returns: None
        """
        pass

    def delete_listener(self, ListenerArn: str):
        """
        Delete a listener from an accelerator.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/globalaccelerator-2018-08-08/DeleteListener>`_
        
        **Request Syntax**
        ::
          response = client.delete_listener(
              ListenerArn='string'
          )
        :type ListenerArn: string
        :param ListenerArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the listener.
        :returns: None
        """
        pass

    def describe_accelerator(self, AcceleratorArn: str) -> Dict:
        """
        Describe an accelerator. To see an AWS CLI example of describing an accelerator, scroll down to **Example** .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/globalaccelerator-2018-08-08/DescribeAccelerator>`_
        
        **Request Syntax**
        ::
          response = client.describe_accelerator(
              AcceleratorArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'Accelerator': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Accelerator** *(dict) --* 
              The description of the accelerator.
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
        :type AcceleratorArn: string
        :param AcceleratorArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the accelerator to describe.
        :rtype: dict
        :returns:
        """
        pass

    def describe_accelerator_attributes(self, AcceleratorArn: str = None) -> Dict:
        """
        Describe the attributes of an accelerator.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/globalaccelerator-2018-08-08/DescribeAcceleratorAttributes>`_
        
        **Request Syntax**
        ::
          response = client.describe_accelerator_attributes(
              AcceleratorArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'AcceleratorAttributes': {
                    'FlowLogsEnabled': True|False,
                    'FlowLogsS3Bucket': 'string',
                    'FlowLogsS3Prefix': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AcceleratorAttributes** *(dict) --* 
              The attributes of the accelerator.
              - **FlowLogsEnabled** *(boolean) --* 
                Indicates whether flow logs are enabled. The default value is false. If the value is true, ``FlowLogsS3Bucket`` and ``FlowLogsS3Prefix`` must be specified.
                For more information, see `Flow Logs <https://docs.aws.amazon.com/global-accelerator/latest/dg/monitoring-global-accelerator.flow-logs.html>`__ in the *AWS Global Accelerator Developer Guide* .
              - **FlowLogsS3Bucket** *(string) --* 
                The name of the Amazon S3 bucket for the flow logs. Attribute is required if ``FlowLogsEnabled`` is ``true`` . The bucket must exist and have a bucket policy that grants AWS Global Accelerator permission to write to the bucket.
              - **FlowLogsS3Prefix** *(string) --* 
                The prefix for the location in the Amazon S3 bucket for the flow logs. Attribute is required if ``FlowLogsEnabled`` is ``true`` . If you don’t specify a prefix, the flow logs are stored in the root of the bucket.
        :type AcceleratorArn: string
        :param AcceleratorArn:
          The Amazon Resource Name (ARN) of the accelerator with the attributes that you want to describe. Value is required.
        :rtype: dict
        :returns:
        """
        pass

    def describe_endpoint_group(self, EndpointGroupArn: str) -> Dict:
        """
        Describe an endpoint group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/globalaccelerator-2018-08-08/DescribeEndpointGroup>`_
        
        **Request Syntax**
        ::
          response = client.describe_endpoint_group(
              EndpointGroupArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'EndpointGroup': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **EndpointGroup** *(dict) --* 
              The description of an endpoint group.
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
        :type EndpointGroupArn: string
        :param EndpointGroupArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the endpoint group to describe.
        :rtype: dict
        :returns:
        """
        pass

    def describe_listener(self, ListenerArn: str) -> Dict:
        """
        Describe a listener.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/globalaccelerator-2018-08-08/DescribeListener>`_
        
        **Request Syntax**
        ::
          response = client.describe_listener(
              ListenerArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'Listener': {
                    'ListenerArn': 'string',
                    'PortRanges': [
                        {
                            'FromPort': 123,
                            'ToPort': 123
                        },
                    ],
                    'Protocol': 'TCP'|'UDP',
                    'ClientAffinity': 'NONE'|'SOURCE_IP'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Listener** *(dict) --* 
              The description of a listener.
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
        :type ListenerArn: string
        :param ListenerArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the listener to describe.
        :rtype: dict
        :returns:
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

    def list_accelerators(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        List the accelerators for an AWS account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/globalaccelerator-2018-08-08/ListAccelerators>`_
        
        **Request Syntax**
        ::
          response = client.list_accelerators(
              MaxResults=123,
              NextToken='string'
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              The token for the next set of results. You receive this token from a previous call.
        :type MaxResults: integer
        :param MaxResults:
          The number of Global Accelerator objects that you want to return with this call. The default value is 10.
        :type NextToken: string
        :param NextToken:
          The token for the next set of results. You receive this token from a previous call.
        :rtype: dict
        :returns:
        """
        pass

    def list_endpoint_groups(self, ListenerArn: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        List the endpoint groups that are associated with a listener.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/globalaccelerator-2018-08-08/ListEndpointGroups>`_
        
        **Request Syntax**
        ::
          response = client.list_endpoint_groups(
              ListenerArn='string',
              MaxResults=123,
              NextToken='string'
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              The token for the next set of results. You receive this token from a previous call.
        :type ListenerArn: string
        :param ListenerArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the listener.
        :type MaxResults: integer
        :param MaxResults:
          The number of endpoint group objects that you want to return with this call. The default value is 10.
        :type NextToken: string
        :param NextToken:
          The token for the next set of results. You receive this token from a previous call.
        :rtype: dict
        :returns:
        """
        pass

    def list_listeners(self, AcceleratorArn: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        List the listeners for an accelerator.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/globalaccelerator-2018-08-08/ListListeners>`_
        
        **Request Syntax**
        ::
          response = client.list_listeners(
              AcceleratorArn='string',
              MaxResults=123,
              NextToken='string'
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              The token for the next set of results. You receive this token from a previous call.
        :type AcceleratorArn: string
        :param AcceleratorArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the accelerator for which you want to list listener objects.
        :type MaxResults: integer
        :param MaxResults:
          The number of listener objects that you want to return with this call. The default value is 10.
        :type NextToken: string
        :param NextToken:
          The token for the next set of results. You receive this token from a previous call.
        :rtype: dict
        :returns:
        """
        pass

    def update_accelerator(self, AcceleratorArn: str, Name: str = None, IpAddressType: str = None, Enabled: bool = None) -> Dict:
        """
        Update an accelerator.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/globalaccelerator-2018-08-08/UpdateAccelerator>`_
        
        **Request Syntax**
        ::
          response = client.update_accelerator(
              AcceleratorArn='string',
              Name='string',
              IpAddressType='IPV4',
              Enabled=True|False
          )
        
        **Response Syntax**
        ::
            {
                'Accelerator': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Accelerator** *(dict) --* 
              Information about the updated accelerator.
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
        :type AcceleratorArn: string
        :param AcceleratorArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the accelerator to update.
        :type Name: string
        :param Name:
          The name of the accelerator. The name can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens (-), and must not begin or end with a hyphen.
        :type IpAddressType: string
        :param IpAddressType:
          The value for the address type must be IPv4.
        :type Enabled: boolean
        :param Enabled:
          Indicates whether an accelerator is enabled. The value is true or false. The default value is true.
          If the value is set to true, the accelerator cannot be deleted. If set to false, the accelerator can be deleted.
        :rtype: dict
        :returns:
        """
        pass

    def update_accelerator_attributes(self, AcceleratorArn: str = None, FlowLogsEnabled: bool = None, FlowLogsS3Bucket: str = None, FlowLogsS3Prefix: str = None) -> Dict:
        """
        Update the attributes for an accelerator. To see an AWS CLI example of updating an accelerator to enable flow logs, scroll down to **Example** .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/globalaccelerator-2018-08-08/UpdateAcceleratorAttributes>`_
        
        **Request Syntax**
        ::
          response = client.update_accelerator_attributes(
              AcceleratorArn='string',
              FlowLogsEnabled=True|False,
              FlowLogsS3Bucket='string',
              FlowLogsS3Prefix='string'
          )
        
        **Response Syntax**
        ::
            {
                'AcceleratorAttributes': {
                    'FlowLogsEnabled': True|False,
                    'FlowLogsS3Bucket': 'string',
                    'FlowLogsS3Prefix': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AcceleratorAttributes** *(dict) --* 
              Updated attributes for the accelerator.
              - **FlowLogsEnabled** *(boolean) --* 
                Indicates whether flow logs are enabled. The default value is false. If the value is true, ``FlowLogsS3Bucket`` and ``FlowLogsS3Prefix`` must be specified.
                For more information, see `Flow Logs <https://docs.aws.amazon.com/global-accelerator/latest/dg/monitoring-global-accelerator.flow-logs.html>`__ in the *AWS Global Accelerator Developer Guide* .
              - **FlowLogsS3Bucket** *(string) --* 
                The name of the Amazon S3 bucket for the flow logs. Attribute is required if ``FlowLogsEnabled`` is ``true`` . The bucket must exist and have a bucket policy that grants AWS Global Accelerator permission to write to the bucket.
              - **FlowLogsS3Prefix** *(string) --* 
                The prefix for the location in the Amazon S3 bucket for the flow logs. Attribute is required if ``FlowLogsEnabled`` is ``true`` . If you don’t specify a prefix, the flow logs are stored in the root of the bucket.
        :type AcceleratorArn: string
        :param AcceleratorArn:
          The Amazon Resource Name (ARN) of the accelerator that you want to update. Attribute is required.
        :type FlowLogsEnabled: boolean
        :param FlowLogsEnabled:
          Update whether flow logs are enabled. The default value is false. If the value is true, ``FlowLogsS3Bucket`` and ``FlowLogsS3Prefix`` must be specified.
          For more information, see `Flow Logs <https://docs.aws.amazon.com/global-accelerator/latest/dg/monitoring-global-accelerator.flow-logs.html>`__ in the *AWS Global Accelerator Developer Guide* .
        :type FlowLogsS3Bucket: string
        :param FlowLogsS3Bucket:
          The name of the Amazon S3 bucket for the flow logs. Attribute is required if ``FlowLogsEnabled`` is ``true`` . The bucket must exist and have a bucket policy that grants AWS Global Accelerator permission to write to the bucket.
        :type FlowLogsS3Prefix: string
        :param FlowLogsS3Prefix:
          Update the prefix for the location in the Amazon S3 bucket for the flow logs. Attribute is required if ``FlowLogsEnabled`` is ``true`` . If you don’t specify a prefix, the flow logs are stored in the root of the bucket.
        :rtype: dict
        :returns:
        """
        pass

    def update_endpoint_group(self, EndpointGroupArn: str, EndpointConfigurations: List = None, TrafficDialPercentage: float = None, HealthCheckPort: int = None, HealthCheckProtocol: str = None, HealthCheckPath: str = None, HealthCheckIntervalSeconds: int = None, ThresholdCount: int = None) -> Dict:
        """
        Update an endpoint group. To see an AWS CLI example of updating an endpoint group, scroll down to **Example** .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/globalaccelerator-2018-08-08/UpdateEndpointGroup>`_
        
        **Request Syntax**
        ::
          response = client.update_endpoint_group(
              EndpointGroupArn='string',
              EndpointConfigurations=[
                  {
                      'EndpointId': 'string',
                      'Weight': 123
                  },
              ],
              TrafficDialPercentage=...,
              HealthCheckPort=123,
              HealthCheckProtocol='TCP'|'HTTP'|'HTTPS',
              HealthCheckPath='string',
              HealthCheckIntervalSeconds=123,
              ThresholdCount=123
          )
        
        **Response Syntax**
        ::
            {
                'EndpointGroup': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **EndpointGroup** *(dict) --* 
              The information about the endpoint group that was updated.
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
        :type EndpointGroupArn: string
        :param EndpointGroupArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the endpoint group.
        :type EndpointConfigurations: list
        :param EndpointConfigurations:
          The list of endpoint objects.
          - *(dict) --*
            A complex type for endpoints.
            - **EndpointId** *(string) --*
              An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an Elastic IP address, this is the Elastic IP address allocation ID.
            - **Weight** *(integer) --*
              The weight associated with the endpoint. When you add weights to endpoints, you configure AWS Global Accelerator to route traffic based on proportions that you specify. For example, you might specify endpoint weights of 4, 5, 5, and 6 (sum=20). The result is that 4/20 of your traffic, on average, is routed to the first endpoint, 5/20 is routed both to the second and third endpoints, and 6/20 is routed to the last endpoint. For more information, see `Endpoint Weights <https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints-endpoint-weights.html>`__ in the *AWS Global Accelerator Developer Guide* .
        :type TrafficDialPercentage: float
        :param TrafficDialPercentage:
          The percentage of traffic to send to an AWS Region. Additional traffic is distributed to other endpoint groups for this listener.
          Use this action to increase (dial up) or decrease (dial down) traffic to a specific Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing.
          The default value is 100.
        :type HealthCheckPort: integer
        :param HealthCheckPort:
          The port that AWS Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default port is the listener port that this endpoint group is associated with. If the listener port is a list of ports, Global Accelerator uses the first port in the list.
        :type HealthCheckProtocol: string
        :param HealthCheckProtocol:
          The protocol that AWS Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default value is TCP.
        :type HealthCheckPath: string
        :param HealthCheckPath:
          If the protocol is HTTP/S, then this specifies the path that is the destination for health check targets. The default value is slash (/).
        :type HealthCheckIntervalSeconds: integer
        :param HealthCheckIntervalSeconds:
          The time—10 seconds or 30 seconds—between each health check for an endpoint. The default value is 30.
        :type ThresholdCount: integer
        :param ThresholdCount:
          The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.
        :rtype: dict
        :returns:
        """
        pass

    def update_listener(self, ListenerArn: str, PortRanges: List = None, Protocol: str = None, ClientAffinity: str = None) -> Dict:
        """
        Update a listener.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/globalaccelerator-2018-08-08/UpdateListener>`_
        
        **Request Syntax**
        ::
          response = client.update_listener(
              ListenerArn='string',
              PortRanges=[
                  {
                      'FromPort': 123,
                      'ToPort': 123
                  },
              ],
              Protocol='TCP'|'UDP',
              ClientAffinity='NONE'|'SOURCE_IP'
          )
        
        **Response Syntax**
        ::
            {
                'Listener': {
                    'ListenerArn': 'string',
                    'PortRanges': [
                        {
                            'FromPort': 123,
                            'ToPort': 123
                        },
                    ],
                    'Protocol': 'TCP'|'UDP',
                    'ClientAffinity': 'NONE'|'SOURCE_IP'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Listener** *(dict) --* 
              Information for the updated listener.
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
        :type ListenerArn: string
        :param ListenerArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the listener to update.
        :type PortRanges: list
        :param PortRanges:
          The updated list of port ranges for the connections from clients to the accelerator.
          - *(dict) --*
            A complex type for a range of ports for a listener.
            - **FromPort** *(integer) --*
              The first port in the range of ports, inclusive.
            - **ToPort** *(integer) --*
              The last port in the range of ports, inclusive.
        :type Protocol: string
        :param Protocol:
          The updated protocol for the connections from clients to the accelerator.
        :type ClientAffinity: string
        :param ClientAffinity:
          Client affinity lets you direct all requests from a user to the same endpoint, if you have stateful applications, regardless of the port and protocol of the client request. Clienty affinity gives you control over whether to always route each client to the same specific endpoint.
          AWS Global Accelerator uses a consistent-flow hashing algorithm to choose the optimal endpoint for a connection. If client affinity is ``NONE`` , Global Accelerator uses the \"five-tuple\" (5-tuple) properties—source IP address, source port, destination IP address, destination port, and protocol—to select the hash value, and then chooses the best endpoint. However, with this setting, if someone uses different ports to connect to Global Accelerator, their connections might not be always routed to the same endpoint because the hash value changes.
          If you want a given client to always be routed to the same endpoint, set client affinity to ``SOURCE_IP`` instead. When you use the ``SOURCE_IP`` setting, Global Accelerator uses the \"two-tuple\" (2-tuple) properties— source (client) IP address and destination IP address—to select the hash value.
          The default value is ``NONE`` .
        :rtype: dict
        :returns:
        """
        pass
