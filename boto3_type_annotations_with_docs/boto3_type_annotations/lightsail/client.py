from datetime import datetime
from typing import Optional
from typing import Union
from typing import List
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from botocore.client import BaseClient


class Client(BaseClient):
    def allocate_static_ip(self, staticIpName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/AllocateStaticIp>`_
        
        **Request Syntax** 
        ::
        
          response = client.allocate_static_ip(
              staticIpName=\'string\'
          )
        :type staticIpName: string
        :param staticIpName: **[REQUIRED]** 
        
          The name of the static IP address.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An array of key-value pairs containing information about the static IP address you allocated.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def attach_disk(self, diskName: str, instanceName: str, diskPath: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/AttachDisk>`_
        
        **Request Syntax** 
        ::
        
          response = client.attach_disk(
              diskName=\'string\',
              instanceName=\'string\',
              diskPath=\'string\'
          )
        :type diskName: string
        :param diskName: **[REQUIRED]** 
        
          The unique Lightsail disk name (e.g., ``my-disk`` ).
        
        :type instanceName: string
        :param instanceName: **[REQUIRED]** 
        
          The name of the Lightsail instance where you want to utilize the storage disk.
        
        :type diskPath: string
        :param diskPath: **[REQUIRED]** 
        
          The disk path to expose to the instance (e.g., ``/dev/xvdf`` ).
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An object describing the API operations.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def attach_instances_to_load_balancer(self, loadBalancerName: str, instanceNames: List) -> Dict:
        """
        
        After some time, the instances are attached to the load balancer and the health check status is available.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/AttachInstancesToLoadBalancer>`_
        
        **Request Syntax** 
        ::
        
          response = client.attach_instances_to_load_balancer(
              loadBalancerName=\'string\',
              instanceNames=[
                  \'string\',
              ]
          )
        :type loadBalancerName: string
        :param loadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
        :type instanceNames: list
        :param instanceNames: **[REQUIRED]** 
        
          An array of strings representing the instance name(s) you want to attach to your load balancer.
        
          An instance must be ``running`` before you can attach it to your load balancer.
        
          There are no additional limits on the number of instances you can attach to your load balancer, aside from the limit of Lightsail instances you can create in your account (20).
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An object representing the API operations.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def attach_load_balancer_tls_certificate(self, loadBalancerName: str, certificateName: str) -> Dict:
        """
        
        Once you create and validate your certificate, you can attach it to your load balancer. You can also use this API to rotate the certificates on your account. Use the ``AttachLoadBalancerTlsCertificate`` operation with the non-attached certificate, and it will replace the existing one and become the attached certificate.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/AttachLoadBalancerTlsCertificate>`_
        
        **Request Syntax** 
        ::
        
          response = client.attach_load_balancer_tls_certificate(
              loadBalancerName=\'string\',
              certificateName=\'string\'
          )
        :type loadBalancerName: string
        :param loadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer to which you want to associate the SSL/TLS certificate.
        
        :type certificateName: string
        :param certificateName: **[REQUIRED]** 
        
          The name of your SSL/TLS certificate.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An object representing the API operations.
        
              These SSL/TLS certificates are only usable by Lightsail load balancers. You can\'t get the certificate and use it for another purpose.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def attach_static_ip(self, staticIpName: str, instanceName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/AttachStaticIp>`_
        
        **Request Syntax** 
        ::
        
          response = client.attach_static_ip(
              staticIpName=\'string\',
              instanceName=\'string\'
          )
        :type staticIpName: string
        :param staticIpName: **[REQUIRED]** 
        
          The name of the static IP.
        
        :type instanceName: string
        :param instanceName: **[REQUIRED]** 
        
          The instance name to which you want to attach the static IP address.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An array of key-value pairs containing information about your API operations.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
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

    def close_instance_public_ports(self, portInfo: Dict, instanceName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CloseInstancePublicPorts>`_
        
        **Request Syntax** 
        ::
        
          response = client.close_instance_public_ports(
              portInfo={
                  \'fromPort\': 123,
                  \'toPort\': 123,
                  \'protocol\': \'tcp\'|\'all\'|\'udp\'
              },
              instanceName=\'string\'
          )
        :type portInfo: dict
        :param portInfo: **[REQUIRED]** 
        
          Information about the public port you are trying to close.
        
          - **fromPort** *(integer) --* 
        
            The first port in the range.
        
          - **toPort** *(integer) --* 
        
            The last port in the range.
        
          - **protocol** *(string) --* 
        
            The protocol. 
        
        :type instanceName: string
        :param instanceName: **[REQUIRED]** 
        
          The name of the instance on which you\'re attempting to close the public ports.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operation\': {
                    \'id\': \'string\',
                    \'resourceName\': \'string\',
                    \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                    \'createdAt\': datetime(2015, 1, 1),
                    \'location\': {
                        \'availabilityZone\': \'string\',
                        \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                    },
                    \'isTerminal\': True|False,
                    \'operationDetails\': \'string\',
                    \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                    \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                    \'statusChangedAt\': datetime(2015, 1, 1),
                    \'errorCode\': \'string\',
                    \'errorDetails\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operation** *(dict) --* 
        
              An array of key-value pairs that contains information about the operation.
        
              - **id** *(string) --* 
        
                The ID of the operation.
        
              - **resourceName** *(string) --* 
        
                The resource name.
        
              - **resourceType** *(string) --* 
        
                The resource type. 
        
              - **createdAt** *(datetime) --* 
        
                The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
              - **location** *(dict) --* 
        
                The region and Availability Zone.
        
                - **availabilityZone** *(string) --* 
        
                  The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                - **regionName** *(string) --* 
        
                  The AWS Region name.
        
              - **isTerminal** *(boolean) --* 
        
                A Boolean value indicating whether the operation is terminal.
        
              - **operationDetails** *(string) --* 
        
                Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
              - **operationType** *(string) --* 
        
                The type of operation. 
        
              - **status** *(string) --* 
        
                The status of the operation. 
        
              - **statusChangedAt** *(datetime) --* 
        
                The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
              - **errorCode** *(string) --* 
        
                The error code.
        
              - **errorDetails** *(string) --* 
        
                The error details.
        
        """
        pass

    def create_disk(self, diskName: str, availabilityZone: str, sizeInGb: int) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateDisk>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_disk(
              diskName=\'string\',
              availabilityZone=\'string\',
              sizeInGb=123
          )
        :type diskName: string
        :param diskName: **[REQUIRED]** 
        
          The unique Lightsail disk name (e.g., ``my-disk`` ).
        
        :type availabilityZone: string
        :param availabilityZone: **[REQUIRED]** 
        
          The Availability Zone where you want to create the disk (e.g., ``us-east-2a`` ). Choose the same Availability Zone as the Lightsail instance where you want to create the disk.
        
          Use the GetRegions operation to list the Availability Zones where Lightsail is currently available.
        
        :type sizeInGb: integer
        :param sizeInGb: **[REQUIRED]** 
        
          The size of the disk in GB (e.g., ``32`` ).
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An object describing the API operations.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def create_disk_from_snapshot(self, diskName: str, diskSnapshotName: str, availabilityZone: str, sizeInGb: int) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateDiskFromSnapshot>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_disk_from_snapshot(
              diskName=\'string\',
              diskSnapshotName=\'string\',
              availabilityZone=\'string\',
              sizeInGb=123
          )
        :type diskName: string
        :param diskName: **[REQUIRED]** 
        
          The unique Lightsail disk name (e.g., ``my-disk`` ).
        
        :type diskSnapshotName: string
        :param diskSnapshotName: **[REQUIRED]** 
        
          The name of the disk snapshot (e.g., ``my-snapshot`` ) from which to create the new storage disk.
        
        :type availabilityZone: string
        :param availabilityZone: **[REQUIRED]** 
        
          The Availability Zone where you want to create the disk (e.g., ``us-east-2a`` ). Choose the same Availability Zone as the Lightsail instance where you want to create the disk.
        
          Use the GetRegions operation to list the Availability Zones where Lightsail is currently available.
        
        :type sizeInGb: integer
        :param sizeInGb: **[REQUIRED]** 
        
          The size of the disk in GB (e.g., ``32`` ).
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An object describing the API operations.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def create_disk_snapshot(self, diskName: str, diskSnapshotName: str) -> Dict:
        """
        
        You can take a snapshot of an attached disk that is in use; however, snapshots only capture data that has been written to your disk at the time the snapshot command is issued. This may exclude any data that has been cached by any applications or the operating system. If you can pause any file systems on the disk long enough to take a snapshot, your snapshot should be complete. Nevertheless, if you cannot pause all file writes to the disk, you should unmount the disk from within the Lightsail instance, issue the create disk snapshot command, and then remount the disk to ensure a consistent and complete snapshot. You may remount and use your disk while the snapshot status is pending.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateDiskSnapshot>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_disk_snapshot(
              diskName=\'string\',
              diskSnapshotName=\'string\'
          )
        :type diskName: string
        :param diskName: **[REQUIRED]** 
        
          The unique name of the source disk (e.g., ``my-source-disk`` ).
        
        :type diskSnapshotName: string
        :param diskSnapshotName: **[REQUIRED]** 
        
          The name of the destination disk snapshot (e.g., ``my-disk-snapshot`` ) based on the source disk.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An object describing the API operations.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def create_domain(self, domainName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateDomain>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_domain(
              domainName=\'string\'
          )
        :type domainName: string
        :param domainName: **[REQUIRED]** 
        
          The domain name to manage (e.g., ``example.com`` ).
        
          .. note::
        
            You cannot register a new domain name using Lightsail. You must register a domain name using Amazon Route 53 or another domain name registrar. If you have already registered your domain, you can enter its name in this parameter to manage the DNS records for that domain.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operation\': {
                    \'id\': \'string\',
                    \'resourceName\': \'string\',
                    \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                    \'createdAt\': datetime(2015, 1, 1),
                    \'location\': {
                        \'availabilityZone\': \'string\',
                        \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                    },
                    \'isTerminal\': True|False,
                    \'operationDetails\': \'string\',
                    \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                    \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                    \'statusChangedAt\': datetime(2015, 1, 1),
                    \'errorCode\': \'string\',
                    \'errorDetails\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operation** *(dict) --* 
        
              An array of key-value pairs containing information about the domain resource you created.
        
              - **id** *(string) --* 
        
                The ID of the operation.
        
              - **resourceName** *(string) --* 
        
                The resource name.
        
              - **resourceType** *(string) --* 
        
                The resource type. 
        
              - **createdAt** *(datetime) --* 
        
                The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
              - **location** *(dict) --* 
        
                The region and Availability Zone.
        
                - **availabilityZone** *(string) --* 
        
                  The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                - **regionName** *(string) --* 
        
                  The AWS Region name.
        
              - **isTerminal** *(boolean) --* 
        
                A Boolean value indicating whether the operation is terminal.
        
              - **operationDetails** *(string) --* 
        
                Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
              - **operationType** *(string) --* 
        
                The type of operation. 
        
              - **status** *(string) --* 
        
                The status of the operation. 
        
              - **statusChangedAt** *(datetime) --* 
        
                The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
              - **errorCode** *(string) --* 
        
                The error code.
        
              - **errorDetails** *(string) --* 
        
                The error details.
        
        """
        pass

    def create_domain_entry(self, domainName: str, domainEntry: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateDomainEntry>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_domain_entry(
              domainName=\'string\',
              domainEntry={
                  \'id\': \'string\',
                  \'name\': \'string\',
                  \'target\': \'string\',
                  \'isAlias\': True|False,
                  \'type\': \'string\',
                  \'options\': {
                      \'string\': \'string\'
                  }
              }
          )
        :type domainName: string
        :param domainName: **[REQUIRED]** 
        
          The domain name (e.g., ``example.com`` ) for which you want to create the domain entry.
        
        :type domainEntry: dict
        :param domainEntry: **[REQUIRED]** 
        
          An array of key-value pairs containing information about the domain entry request.
        
          - **id** *(string) --* 
        
            The ID of the domain recordset entry.
        
          - **name** *(string) --* 
        
            The name of the domain.
        
          - **target** *(string) --* 
        
            The target AWS name server (e.g., ``ns-111.awsdns-22.com.`` ).
        
            For Lightsail load balancers, the value looks like ``ab1234c56789c6b86aba6fb203d443bc-123456789.us-east-2.elb.amazonaws.com`` . Be sure to also set ``isAlias`` to ``true`` when setting up an A record for a load balancer.
        
          - **isAlias** *(boolean) --* 
        
            When ``true`` , specifies whether the domain entry is an alias used by the Lightsail load balancer. You can include an alias (A type) record in your request, which points to a load balancer DNS name and routes traffic to your load balancer
        
          - **type** *(string) --* 
        
            The type of domain entry (e.g., ``SOA`` or ``NS`` ).
        
          - **options** *(dict) --* 
        
            (Deprecated) The options for the domain entry.
        
            .. note::
        
              In releases prior to November 29, 2017, this parameter was not included in the API response. It is now deprecated.
        
            - *(string) --* 
        
              - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operation\': {
                    \'id\': \'string\',
                    \'resourceName\': \'string\',
                    \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                    \'createdAt\': datetime(2015, 1, 1),
                    \'location\': {
                        \'availabilityZone\': \'string\',
                        \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                    },
                    \'isTerminal\': True|False,
                    \'operationDetails\': \'string\',
                    \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                    \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                    \'statusChangedAt\': datetime(2015, 1, 1),
                    \'errorCode\': \'string\',
                    \'errorDetails\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operation** *(dict) --* 
        
              An array of key-value pairs containing information about the operation.
        
              - **id** *(string) --* 
        
                The ID of the operation.
        
              - **resourceName** *(string) --* 
        
                The resource name.
        
              - **resourceType** *(string) --* 
        
                The resource type. 
        
              - **createdAt** *(datetime) --* 
        
                The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
              - **location** *(dict) --* 
        
                The region and Availability Zone.
        
                - **availabilityZone** *(string) --* 
        
                  The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                - **regionName** *(string) --* 
        
                  The AWS Region name.
        
              - **isTerminal** *(boolean) --* 
        
                A Boolean value indicating whether the operation is terminal.
        
              - **operationDetails** *(string) --* 
        
                Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
              - **operationType** *(string) --* 
        
                The type of operation. 
        
              - **status** *(string) --* 
        
                The status of the operation. 
        
              - **statusChangedAt** *(datetime) --* 
        
                The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
              - **errorCode** *(string) --* 
        
                The error code.
        
              - **errorDetails** *(string) --* 
        
                The error details.
        
        """
        pass

    def create_instance_snapshot(self, instanceSnapshotName: str, instanceName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateInstanceSnapshot>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_instance_snapshot(
              instanceSnapshotName=\'string\',
              instanceName=\'string\'
          )
        :type instanceSnapshotName: string
        :param instanceSnapshotName: **[REQUIRED]** 
        
          The name for your new snapshot.
        
        :type instanceName: string
        :param instanceName: **[REQUIRED]** 
        
          The Lightsail instance on which to base your snapshot.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An array of key-value pairs containing information about the results of your create instances snapshot request.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def create_instances(self, instanceNames: List, availabilityZone: str, blueprintId: str, bundleId: str, customImageName: str = None, userData: str = None, keyPairName: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateInstances>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_instances(
              instanceNames=[
                  \'string\',
              ],
              availabilityZone=\'string\',
              customImageName=\'string\',
              blueprintId=\'string\',
              bundleId=\'string\',
              userData=\'string\',
              keyPairName=\'string\'
          )
        :type instanceNames: list
        :param instanceNames: **[REQUIRED]** 
        
          The names to use for your new Lightsail instances. Separate multiple values using quotation marks and commas, for example: ``[\"MyFirstInstance\",\"MySecondInstance\"]``  
        
          - *(string) --* 
        
        :type availabilityZone: string
        :param availabilityZone: **[REQUIRED]** 
        
          The Availability Zone in which to create your instance. Use the following format: ``us-east-2a`` (case sensitive). You can get a list of Availability Zones by using the `get regions <http://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetRegions.html>`__ operation. Be sure to add the ``include Availability Zones`` parameter to your request.
        
        :type customImageName: string
        :param customImageName: 
        
          (Deprecated) The name for your custom image.
        
          .. note::
        
            In releases prior to June 12, 2017, this parameter was ignored by the API. It is now deprecated.
        
        :type blueprintId: string
        :param blueprintId: **[REQUIRED]** 
        
          The ID for a virtual private server image (e.g., ``app_wordpress_4_4`` or ``app_lamp_7_0`` ). Use the get blueprints operation to return a list of available images (or *blueprints* ).
        
        :type bundleId: string
        :param bundleId: **[REQUIRED]** 
        
          The bundle of specification information for your virtual private server (or *instance* ), including the pricing plan (e.g., ``micro_1_0`` ).
        
        :type userData: string
        :param userData: 
        
          A launch script you can create that configures a server with additional user data. For example, you might want to run ``apt-get -y update`` .
        
          .. note::
        
            Depending on the machine image you choose, the command to get software on your instance varies. Amazon Linux and CentOS use ``yum`` , Debian and Ubuntu use ``apt-get`` , and FreeBSD uses ``pkg`` . For a complete list, see the `Dev Guide <https://lightsail.aws.amazon.com/ls/docs/getting-started/article/compare-options-choose-lightsail-instance-image>`__ .
        
        :type keyPairName: string
        :param keyPairName: 
        
          The name of your key pair.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An array of key-value pairs containing information about the results of your create instances request.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def create_instances_from_snapshot(self, instanceNames: List, availabilityZone: str, instanceSnapshotName: str, bundleId: str, attachedDiskMapping: Dict = None, userData: str = None, keyPairName: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateInstancesFromSnapshot>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_instances_from_snapshot(
              instanceNames=[
                  \'string\',
              ],
              attachedDiskMapping={
                  \'string\': [
                      {
                          \'originalDiskPath\': \'string\',
                          \'newDiskName\': \'string\'
                      },
                  ]
              },
              availabilityZone=\'string\',
              instanceSnapshotName=\'string\',
              bundleId=\'string\',
              userData=\'string\',
              keyPairName=\'string\'
          )
        :type instanceNames: list
        :param instanceNames: **[REQUIRED]** 
        
          The names for your new instances.
        
          - *(string) --* 
        
        :type attachedDiskMapping: dict
        :param attachedDiskMapping: 
        
          An object containing information about one or more disk mappings.
        
          - *(string) --* 
        
            - *(list) --* 
        
              - *(dict) --* 
        
                Describes a block storage disk mapping.
        
                - **originalDiskPath** *(string) --* 
        
                  The original disk path exposed to the instance (for example, ``/dev/sdh`` ).
        
                - **newDiskName** *(string) --* 
        
                  The new disk name (e.g., ``my-new-disk`` ).
        
        :type availabilityZone: string
        :param availabilityZone: **[REQUIRED]** 
        
          The Availability Zone where you want to create your instances. Use the following formatting: ``us-east-2a`` (case sensitive). You can get a list of Availability Zones by using the `get regions <http://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetRegions.html>`__ operation. Be sure to add the ``include Availability Zones`` parameter to your request.
        
        :type instanceSnapshotName: string
        :param instanceSnapshotName: **[REQUIRED]** 
        
          The name of the instance snapshot on which you are basing your new instances. Use the get instance snapshots operation to return information about your existing snapshots.
        
        :type bundleId: string
        :param bundleId: **[REQUIRED]** 
        
          The bundle of specification information for your virtual private server (or *instance* ), including the pricing plan (e.g., ``micro_1_0`` ).
        
        :type userData: string
        :param userData: 
        
          You can create a launch script that configures a server with additional user data. For example, ``apt-get -y update`` .
        
          .. note::
        
            Depending on the machine image you choose, the command to get software on your instance varies. Amazon Linux and CentOS use ``yum`` , Debian and Ubuntu use ``apt-get`` , and FreeBSD uses ``pkg`` . For a complete list, see the `Dev Guide <https://lightsail.aws.amazon.com/ls/docs/getting-started/article/compare-options-choose-lightsail-instance-image>`__ .
        
        :type keyPairName: string
        :param keyPairName: 
        
          The name for your key pair.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An array of key-value pairs containing information about the results of your create instances from snapshot request.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def create_key_pair(self, keyPairName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateKeyPair>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_key_pair(
              keyPairName=\'string\'
          )
        :type keyPairName: string
        :param keyPairName: **[REQUIRED]** 
        
          The name for your new key pair.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'keyPair\': {
                    \'name\': \'string\',
                    \'arn\': \'string\',
                    \'supportCode\': \'string\',
                    \'createdAt\': datetime(2015, 1, 1),
                    \'location\': {
                        \'availabilityZone\': \'string\',
                        \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                    },
                    \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                    \'fingerprint\': \'string\'
                },
                \'publicKeyBase64\': \'string\',
                \'privateKeyBase64\': \'string\',
                \'operation\': {
                    \'id\': \'string\',
                    \'resourceName\': \'string\',
                    \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                    \'createdAt\': datetime(2015, 1, 1),
                    \'location\': {
                        \'availabilityZone\': \'string\',
                        \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                    },
                    \'isTerminal\': True|False,
                    \'operationDetails\': \'string\',
                    \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                    \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                    \'statusChangedAt\': datetime(2015, 1, 1),
                    \'errorCode\': \'string\',
                    \'errorDetails\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **keyPair** *(dict) --* 
        
              An array of key-value pairs containing information about the new key pair you just created.
        
              - **name** *(string) --* 
        
                The friendly name of the SSH key pair.
        
              - **arn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the key pair (e.g., ``arn:aws:lightsail:us-east-2:123456789101:KeyPair/05859e3d-331d-48ba-9034-12345EXAMPLE`` ).
        
              - **supportCode** *(string) --* 
        
                The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
        
              - **createdAt** *(datetime) --* 
        
                The timestamp when the key pair was created (e.g., ``1479816991.349`` ).
        
              - **location** *(dict) --* 
        
                The region name and Availability Zone where the key pair was created.
        
                - **availabilityZone** *(string) --* 
        
                  The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                - **regionName** *(string) --* 
        
                  The AWS Region name.
        
              - **resourceType** *(string) --* 
        
                The resource type (usually ``KeyPair`` ).
        
              - **fingerprint** *(string) --* 
        
                The RSA fingerprint of the key pair.
        
            - **publicKeyBase64** *(string) --* 
        
              A base64-encoded public key of the ``ssh-rsa`` type.
        
            - **privateKeyBase64** *(string) --* 
        
              A base64-encoded RSA private key.
        
            - **operation** *(dict) --* 
        
              An array of key-value pairs containing information about the results of your create key pair request.
        
              - **id** *(string) --* 
        
                The ID of the operation.
        
              - **resourceName** *(string) --* 
        
                The resource name.
        
              - **resourceType** *(string) --* 
        
                The resource type. 
        
              - **createdAt** *(datetime) --* 
        
                The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
              - **location** *(dict) --* 
        
                The region and Availability Zone.
        
                - **availabilityZone** *(string) --* 
        
                  The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                - **regionName** *(string) --* 
        
                  The AWS Region name.
        
              - **isTerminal** *(boolean) --* 
        
                A Boolean value indicating whether the operation is terminal.
        
              - **operationDetails** *(string) --* 
        
                Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
              - **operationType** *(string) --* 
        
                The type of operation. 
        
              - **status** *(string) --* 
        
                The status of the operation. 
        
              - **statusChangedAt** *(datetime) --* 
        
                The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
              - **errorCode** *(string) --* 
        
                The error code.
        
              - **errorDetails** *(string) --* 
        
                The error details.
        
        """
        pass

    def create_load_balancer(self, loadBalancerName: str, instancePort: int, healthCheckPath: str = None, certificateName: str = None, certificateDomainName: str = None, certificateAlternativeNames: List = None) -> Dict:
        """
        
        When you create a load balancer, you can specify a unique name and port settings. To change additional load balancer settings, use the ``UpdateLoadBalancerAttribute`` operation.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateLoadBalancer>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_load_balancer(
              loadBalancerName=\'string\',
              instancePort=123,
              healthCheckPath=\'string\',
              certificateName=\'string\',
              certificateDomainName=\'string\',
              certificateAlternativeNames=[
                  \'string\',
              ]
          )
        :type loadBalancerName: string
        :param loadBalancerName: **[REQUIRED]** 
        
          The name of your load balancer.
        
        :type instancePort: integer
        :param instancePort: **[REQUIRED]** 
        
          The instance port where you\'re creating your load balancer.
        
        :type healthCheckPath: string
        :param healthCheckPath: 
        
          The path you provided to perform the load balancer health check. If you didn\'t specify a health check path, Lightsail uses the root path of your website (e.g., ``\"/\"`` ).
        
          You may want to specify a custom health check path other than the root of your application if your home page loads slowly or has a lot of media or scripting on it.
        
        :type certificateName: string
        :param certificateName: 
        
          The name of the SSL/TLS certificate.
        
          If you specify ``certificateName`` , then ``certificateDomainName`` is required (and vice-versa).
        
        :type certificateDomainName: string
        :param certificateDomainName: 
        
          The domain name with which your certificate is associated (e.g., ``example.com`` ).
        
          If you specify ``certificateDomainName`` , then ``certificateName`` is required (and vice-versa).
        
        :type certificateAlternativeNames: list
        :param certificateAlternativeNames: 
        
          The optional alternative domains and subdomains to use with your SSL/TLS certificate (e.g., ``www.example.com`` , ``example.com`` , ``m.example.com`` , ``blog.example.com`` ).
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An object containing information about the API operations.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def create_load_balancer_tls_certificate(self, loadBalancerName: str, certificateName: str, certificateDomainName: str, certificateAlternativeNames: List = None) -> Dict:
        """
        
        TLS is just an updated, more secure version of Secure Socket Layer (SSL).
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateLoadBalancerTlsCertificate>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_load_balancer_tls_certificate(
              loadBalancerName=\'string\',
              certificateName=\'string\',
              certificateDomainName=\'string\',
              certificateAlternativeNames=[
                  \'string\',
              ]
          )
        :type loadBalancerName: string
        :param loadBalancerName: **[REQUIRED]** 
        
          The load balancer name where you want to create the SSL/TLS certificate.
        
        :type certificateName: string
        :param certificateName: **[REQUIRED]** 
        
          The SSL/TLS certificate name.
        
          You can have up to 10 certificates in your account at one time. Each Lightsail load balancer can have up to 2 certificates associated with it at one time. There is also an overall limit to the number of certificates that can be issue in a 365-day period. For more information, see `Limits <http://docs.aws.amazon.com/acm/latest/userguide/acm-limits.html>`__ .
        
        :type certificateDomainName: string
        :param certificateDomainName: **[REQUIRED]** 
        
          The domain name (e.g., ``example.com`` ) for your SSL/TLS certificate.
        
        :type certificateAlternativeNames: list
        :param certificateAlternativeNames: 
        
          An array of strings listing alternative domains and subdomains for your SSL/TLS certificate. Lightsail will de-dupe the names for you. You can have a maximum of 9 alternative names (in addition to the 1 primary domain). We do not support wildcards (e.g., ``*.example.com`` ).
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An object containing information about the API operations.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def create_relational_database(self, relationalDatabaseName: str, relationalDatabaseBlueprintId: str, relationalDatabaseBundleId: str, masterDatabaseName: str, masterUsername: str, availabilityZone: str = None, masterUserPassword: str = None, preferredBackupWindow: str = None, preferredMaintenanceWindow: str = None, publiclyAccessible: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateRelationalDatabase>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_relational_database(
              relationalDatabaseName=\'string\',
              availabilityZone=\'string\',
              relationalDatabaseBlueprintId=\'string\',
              relationalDatabaseBundleId=\'string\',
              masterDatabaseName=\'string\',
              masterUsername=\'string\',
              masterUserPassword=\'string\',
              preferredBackupWindow=\'string\',
              preferredMaintenanceWindow=\'string\',
              publiclyAccessible=True|False
          )
        :type relationalDatabaseName: string
        :param relationalDatabaseName: **[REQUIRED]** 
        
          The name to use for your new database.
        
          Constraints:
        
          * Must contain from 2 to 255 alphanumeric characters, or hyphens. 
           
          * The first and last character must be a letter or number. 
           
        :type availabilityZone: string
        :param availabilityZone: 
        
          The Availability Zone in which to create your new database. Use the ``us-east-2a`` case-sensitive format.
        
          You can get a list of Availability Zones by using the ``get regions`` operation. Be sure to add the ``include relational database Availability Zones`` parameter to your request.
        
        :type relationalDatabaseBlueprintId: string
        :param relationalDatabaseBlueprintId: **[REQUIRED]** 
        
          The blueprint ID for your new database. A blueprint describes the major engine version of a database.
        
          You can get a list of database blueprints IDs by using the ``get relational database blueprints`` operation.
        
        :type relationalDatabaseBundleId: string
        :param relationalDatabaseBundleId: **[REQUIRED]** 
        
          The bundle ID for your new database. A bundle describes the performance specifications for your database.
        
          You can get a list of database bundle IDs by using the ``get relational database bundles`` operation.
        
        :type masterDatabaseName: string
        :param masterDatabaseName: **[REQUIRED]** 
        
          The name of the master database created when the Lightsail database resource is created.
        
          Constraints:
        
          * Must contain from 1 to 64 alphanumeric characters. 
           
          * Cannot be a word reserved by the specified database engine 
           
        :type masterUsername: string
        :param masterUsername: **[REQUIRED]** 
        
          The master user name for your new database.
        
          Constraints:
        
          * Master user name is required. 
           
          * Must contain from 1 to 16 alphanumeric characters. 
           
          * The first character must be a letter. 
           
          * Cannot be a reserved word for the database engine you choose. For more information about reserved words in MySQL 5.6 or 5.7, see the Keywords and Reserved Words articles for `MySQL 5.6 <https://dev.mysql.com/doc/refman/5.6/en/keywords.html>`__ or `MySQL 5.7 <https://dev.mysql.com/doc/refman/5.7/en/keywords.html>`__ respectively. 
           
        :type masterUserPassword: string
        :param masterUserPassword: 
        
          The password for the master user of your new database. The password can include any printable ASCII character except \"/\", \"\"\", or \"@\".
        
          Constraints: Must contain 8 to 41 characters.
        
        :type preferredBackupWindow: string
        :param preferredBackupWindow: 
        
          The daily time range during which automated backups are created for your new database if automated backups are enabled.
        
          The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region. For more information about the preferred backup window time blocks for each region, see the `Working With Backups <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.BackupWindow>`__ guide in the Amazon Relational Database Service (Amazon RDS) documentation.
        
          Constraints:
        
          * Must be in the ``hh24:mi-hh24:mi`` format. Example: ``16:00-16:30``   
           
          * Specified in Universal Coordinated Time (UTC). 
           
          * Must not conflict with the preferred maintenance window. 
           
          * Must be at least 30 minutes. 
           
        :type preferredMaintenanceWindow: string
        :param preferredMaintenanceWindow: 
        
          The weekly time range during which system maintenance can occur on your new database.
        
          The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.
        
          Constraints:
        
          * Must be in the ``ddd:hh24:mi-ddd:hh24:mi`` format. 
           
          * Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun. 
           
          * Must be at least 30 minutes. 
           
          * Specified in Universal Coordinated Time (UTC). 
           
          * Example: ``Tue:17:00-Tue:17:30``   
           
        :type publiclyAccessible: boolean
        :param publiclyAccessible: 
        
          Specifies the accessibility options for your new database. A value of ``true`` specifies a database that is available to resources outside of your Lightsail account. A value of ``false`` specifies a database that is available only to your Lightsail resources in the same region as your database.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An object describing the result of your create relational database request.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def create_relational_database_from_snapshot(self, relationalDatabaseName: str, availabilityZone: str = None, publiclyAccessible: bool = None, relationalDatabaseSnapshotName: str = None, relationalDatabaseBundleId: str = None, sourceRelationalDatabaseName: str = None, restoreTime: datetime = None, useLatestRestorableTime: bool = None) -> Dict:
        """
        
        You can create a new database from a snapshot in if something goes wrong with your original database, or to change it to a different plan, such as a high availability or standard plan.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateRelationalDatabaseFromSnapshot>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_relational_database_from_snapshot(
              relationalDatabaseName=\'string\',
              availabilityZone=\'string\',
              publiclyAccessible=True|False,
              relationalDatabaseSnapshotName=\'string\',
              relationalDatabaseBundleId=\'string\',
              sourceRelationalDatabaseName=\'string\',
              restoreTime=datetime(2015, 1, 1),
              useLatestRestorableTime=True|False
          )
        :type relationalDatabaseName: string
        :param relationalDatabaseName: **[REQUIRED]** 
        
          The name to use for your new database.
        
          Constraints:
        
          * Must contain from 2 to 255 alphanumeric characters, or hyphens. 
           
          * The first and last character must be a letter or number. 
           
        :type availabilityZone: string
        :param availabilityZone: 
        
          The Availability Zone in which to create your new database. Use the ``us-east-2a`` case-sensitive format.
        
          You can get a list of Availability Zones by using the ``get regions`` operation. Be sure to add the ``include relational database Availability Zones`` parameter to your request.
        
        :type publiclyAccessible: boolean
        :param publiclyAccessible: 
        
          Specifies the accessibility options for your new database. A value of ``true`` specifies a database that is available to resources outside of your Lightsail account. A value of ``false`` specifies a database that is available only to your Lightsail resources in the same region as your database.
        
        :type relationalDatabaseSnapshotName: string
        :param relationalDatabaseSnapshotName: 
        
          The name of the database snapshot from which to create your new database.
        
        :type relationalDatabaseBundleId: string
        :param relationalDatabaseBundleId: 
        
          The bundle ID for your new database. A bundle describes the performance specifications for your database.
        
          You can get a list of database bundle IDs by using the ``get relational database bundles`` operation.
        
          When creating a new database from a snapshot, you cannot choose a bundle that is smaller than the bundle of the source database.
        
        :type sourceRelationalDatabaseName: string
        :param sourceRelationalDatabaseName: 
        
          The name of the source database.
        
        :type restoreTime: datetime
        :param restoreTime: 
        
          The date and time to restore your database from.
        
          Constraints:
        
          * Must be before the latest restorable time for the database. 
           
          * Cannot be specified if the ``use latest restorable time`` parameter is ``true`` . 
           
          * Specified in Universal Coordinated Time (UTC). 
           
          * Specified in the Unix time format. For example, if you wish to use a restore time of October 1, 2018, at 8 PM UTC, then you input ``1538424000`` as the restore time. 
           
        :type useLatestRestorableTime: boolean
        :param useLatestRestorableTime: 
        
          Specifies whether your database is restored from the latest backup time. A value of ``true`` restores from the latest backup time. 
        
          Default: ``false``  
        
          Constraints: Cannot be specified if the ``restore time`` parameter is provided.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An object describing the result of your create relational database from snapshot request.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def create_relational_database_snapshot(self, relationalDatabaseName: str, relationalDatabaseSnapshotName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateRelationalDatabaseSnapshot>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_relational_database_snapshot(
              relationalDatabaseName=\'string\',
              relationalDatabaseSnapshotName=\'string\'
          )
        :type relationalDatabaseName: string
        :param relationalDatabaseName: **[REQUIRED]** 
        
          The name of the database on which to base your new snapshot.
        
        :type relationalDatabaseSnapshotName: string
        :param relationalDatabaseSnapshotName: **[REQUIRED]** 
        
          The name for your new database snapshot.
        
          Constraints:
        
          * Must contain from 2 to 255 alphanumeric characters, or hyphens. 
           
          * The first and last character must be a letter or number. 
           
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An object describing the result of your create relational database snapshot request.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def delete_disk(self, diskName: str) -> Dict:
        """
        
        .. note::
        
          The disk may remain in the ``deleting`` state for several minutes.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DeleteDisk>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_disk(
              diskName=\'string\'
          )
        :type diskName: string
        :param diskName: **[REQUIRED]** 
        
          The unique name of the disk you want to delete (e.g., ``my-disk`` ).
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An object describing the API operations.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def delete_disk_snapshot(self, diskSnapshotName: str) -> Dict:
        """
        
        When you make periodic snapshots of a disk, the snapshots are incremental, and only the blocks on the device that have changed since your last snapshot are saved in the new snapshot. When you delete a snapshot, only the data not needed for any other snapshot is removed. So regardless of which prior snapshots have been deleted, all active snapshots will have access to all the information needed to restore the disk.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DeleteDiskSnapshot>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_disk_snapshot(
              diskSnapshotName=\'string\'
          )
        :type diskSnapshotName: string
        :param diskSnapshotName: **[REQUIRED]** 
        
          The name of the disk snapshot you want to delete (e.g., ``my-disk-snapshot`` ).
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An object describing the API operations.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def delete_domain(self, domainName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DeleteDomain>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_domain(
              domainName=\'string\'
          )
        :type domainName: string
        :param domainName: **[REQUIRED]** 
        
          The specific domain name to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operation\': {
                    \'id\': \'string\',
                    \'resourceName\': \'string\',
                    \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                    \'createdAt\': datetime(2015, 1, 1),
                    \'location\': {
                        \'availabilityZone\': \'string\',
                        \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                    },
                    \'isTerminal\': True|False,
                    \'operationDetails\': \'string\',
                    \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                    \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                    \'statusChangedAt\': datetime(2015, 1, 1),
                    \'errorCode\': \'string\',
                    \'errorDetails\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operation** *(dict) --* 
        
              An array of key-value pairs containing information about the results of your delete domain request.
        
              - **id** *(string) --* 
        
                The ID of the operation.
        
              - **resourceName** *(string) --* 
        
                The resource name.
        
              - **resourceType** *(string) --* 
        
                The resource type. 
        
              - **createdAt** *(datetime) --* 
        
                The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
              - **location** *(dict) --* 
        
                The region and Availability Zone.
        
                - **availabilityZone** *(string) --* 
        
                  The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                - **regionName** *(string) --* 
        
                  The AWS Region name.
        
              - **isTerminal** *(boolean) --* 
        
                A Boolean value indicating whether the operation is terminal.
        
              - **operationDetails** *(string) --* 
        
                Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
              - **operationType** *(string) --* 
        
                The type of operation. 
        
              - **status** *(string) --* 
        
                The status of the operation. 
        
              - **statusChangedAt** *(datetime) --* 
        
                The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
              - **errorCode** *(string) --* 
        
                The error code.
        
              - **errorDetails** *(string) --* 
        
                The error details.
        
        """
        pass

    def delete_domain_entry(self, domainName: str, domainEntry: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DeleteDomainEntry>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_domain_entry(
              domainName=\'string\',
              domainEntry={
                  \'id\': \'string\',
                  \'name\': \'string\',
                  \'target\': \'string\',
                  \'isAlias\': True|False,
                  \'type\': \'string\',
                  \'options\': {
                      \'string\': \'string\'
                  }
              }
          )
        :type domainName: string
        :param domainName: **[REQUIRED]** 
        
          The name of the domain entry to delete.
        
        :type domainEntry: dict
        :param domainEntry: **[REQUIRED]** 
        
          An array of key-value pairs containing information about your domain entries.
        
          - **id** *(string) --* 
        
            The ID of the domain recordset entry.
        
          - **name** *(string) --* 
        
            The name of the domain.
        
          - **target** *(string) --* 
        
            The target AWS name server (e.g., ``ns-111.awsdns-22.com.`` ).
        
            For Lightsail load balancers, the value looks like ``ab1234c56789c6b86aba6fb203d443bc-123456789.us-east-2.elb.amazonaws.com`` . Be sure to also set ``isAlias`` to ``true`` when setting up an A record for a load balancer.
        
          - **isAlias** *(boolean) --* 
        
            When ``true`` , specifies whether the domain entry is an alias used by the Lightsail load balancer. You can include an alias (A type) record in your request, which points to a load balancer DNS name and routes traffic to your load balancer
        
          - **type** *(string) --* 
        
            The type of domain entry (e.g., ``SOA`` or ``NS`` ).
        
          - **options** *(dict) --* 
        
            (Deprecated) The options for the domain entry.
        
            .. note::
        
              In releases prior to November 29, 2017, this parameter was not included in the API response. It is now deprecated.
        
            - *(string) --* 
        
              - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operation\': {
                    \'id\': \'string\',
                    \'resourceName\': \'string\',
                    \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                    \'createdAt\': datetime(2015, 1, 1),
                    \'location\': {
                        \'availabilityZone\': \'string\',
                        \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                    },
                    \'isTerminal\': True|False,
                    \'operationDetails\': \'string\',
                    \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                    \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                    \'statusChangedAt\': datetime(2015, 1, 1),
                    \'errorCode\': \'string\',
                    \'errorDetails\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operation** *(dict) --* 
        
              An array of key-value pairs containing information about the results of your delete domain entry request.
        
              - **id** *(string) --* 
        
                The ID of the operation.
        
              - **resourceName** *(string) --* 
        
                The resource name.
        
              - **resourceType** *(string) --* 
        
                The resource type. 
        
              - **createdAt** *(datetime) --* 
        
                The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
              - **location** *(dict) --* 
        
                The region and Availability Zone.
        
                - **availabilityZone** *(string) --* 
        
                  The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                - **regionName** *(string) --* 
        
                  The AWS Region name.
        
              - **isTerminal** *(boolean) --* 
        
                A Boolean value indicating whether the operation is terminal.
        
              - **operationDetails** *(string) --* 
        
                Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
              - **operationType** *(string) --* 
        
                The type of operation. 
        
              - **status** *(string) --* 
        
                The status of the operation. 
        
              - **statusChangedAt** *(datetime) --* 
        
                The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
              - **errorCode** *(string) --* 
        
                The error code.
        
              - **errorDetails** *(string) --* 
        
                The error details.
        
        """
        pass

    def delete_instance(self, instanceName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DeleteInstance>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_instance(
              instanceName=\'string\'
          )
        :type instanceName: string
        :param instanceName: **[REQUIRED]** 
        
          The name of the instance to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An array of key-value pairs containing information about the results of your delete instance request.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def delete_instance_snapshot(self, instanceSnapshotName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DeleteInstanceSnapshot>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_instance_snapshot(
              instanceSnapshotName=\'string\'
          )
        :type instanceSnapshotName: string
        :param instanceSnapshotName: **[REQUIRED]** 
        
          The name of the snapshot to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An array of key-value pairs containing information about the results of your delete instance snapshot request.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def delete_key_pair(self, keyPairName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DeleteKeyPair>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_key_pair(
              keyPairName=\'string\'
          )
        :type keyPairName: string
        :param keyPairName: **[REQUIRED]** 
        
          The name of the key pair to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operation\': {
                    \'id\': \'string\',
                    \'resourceName\': \'string\',
                    \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                    \'createdAt\': datetime(2015, 1, 1),
                    \'location\': {
                        \'availabilityZone\': \'string\',
                        \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                    },
                    \'isTerminal\': True|False,
                    \'operationDetails\': \'string\',
                    \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                    \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                    \'statusChangedAt\': datetime(2015, 1, 1),
                    \'errorCode\': \'string\',
                    \'errorDetails\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operation** *(dict) --* 
        
              An array of key-value pairs containing information about the results of your delete key pair request.
        
              - **id** *(string) --* 
        
                The ID of the operation.
        
              - **resourceName** *(string) --* 
        
                The resource name.
        
              - **resourceType** *(string) --* 
        
                The resource type. 
        
              - **createdAt** *(datetime) --* 
        
                The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
              - **location** *(dict) --* 
        
                The region and Availability Zone.
        
                - **availabilityZone** *(string) --* 
        
                  The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                - **regionName** *(string) --* 
        
                  The AWS Region name.
        
              - **isTerminal** *(boolean) --* 
        
                A Boolean value indicating whether the operation is terminal.
        
              - **operationDetails** *(string) --* 
        
                Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
              - **operationType** *(string) --* 
        
                The type of operation. 
        
              - **status** *(string) --* 
        
                The status of the operation. 
        
              - **statusChangedAt** *(datetime) --* 
        
                The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
              - **errorCode** *(string) --* 
        
                The error code.
        
              - **errorDetails** *(string) --* 
        
                The error details.
        
        """
        pass

    def delete_load_balancer(self, loadBalancerName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DeleteLoadBalancer>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_load_balancer(
              loadBalancerName=\'string\'
          )
        :type loadBalancerName: string
        :param loadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer you want to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An object describing the API operations.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def delete_load_balancer_tls_certificate(self, loadBalancerName: str, certificateName: str, force: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DeleteLoadBalancerTlsCertificate>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_load_balancer_tls_certificate(
              loadBalancerName=\'string\',
              certificateName=\'string\',
              force=True|False
          )
        :type loadBalancerName: string
        :param loadBalancerName: **[REQUIRED]** 
        
          The load balancer name.
        
        :type certificateName: string
        :param certificateName: **[REQUIRED]** 
        
          The SSL/TLS certificate name.
        
        :type force: boolean
        :param force: 
        
          When ``true`` , forces the deletion of an SSL/TLS certificate.
        
          There can be two certificates associated with a Lightsail load balancer: the primary and the backup. The ``force`` parameter is required when the primary SSL/TLS certificate is in use by an instance attached to the load balancer.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An object describing the API operations.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def delete_relational_database(self, relationalDatabaseName: str, skipFinalSnapshot: bool = None, finalRelationalDatabaseSnapshotName: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DeleteRelationalDatabase>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_relational_database(
              relationalDatabaseName=\'string\',
              skipFinalSnapshot=True|False,
              finalRelationalDatabaseSnapshotName=\'string\'
          )
        :type relationalDatabaseName: string
        :param relationalDatabaseName: **[REQUIRED]** 
        
          The name of the database that you are deleting.
        
        :type skipFinalSnapshot: boolean
        :param skipFinalSnapshot: 
        
          Determines whether a final database snapshot is created before your database is deleted. If ``true`` is specified, no database snapshot is created. If ``false`` is specified, a database snapshot is created before your database is deleted.
        
          You must specify the ``final relational database snapshot name`` parameter if the ``skip final snapshot`` parameter is ``false`` .
        
          Default: ``false``  
        
        :type finalRelationalDatabaseSnapshotName: string
        :param finalRelationalDatabaseSnapshotName: 
        
          The name of the database snapshot created if ``skip final snapshot`` is ``false`` , which is the default value for that parameter.
        
          .. note::
        
            Specifying this parameter and also specifying the ``skip final snapshot`` parameter to ``true`` results in an error.
        
          Constraints:
        
          * Must contain from 2 to 255 alphanumeric characters, or hyphens. 
           
          * The first and last character must be a letter or number. 
           
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An object describing the result of your delete relational database request.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def delete_relational_database_snapshot(self, relationalDatabaseSnapshotName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DeleteRelationalDatabaseSnapshot>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_relational_database_snapshot(
              relationalDatabaseSnapshotName=\'string\'
          )
        :type relationalDatabaseSnapshotName: string
        :param relationalDatabaseSnapshotName: **[REQUIRED]** 
        
          The name of the database snapshot that you are deleting.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An object describing the result of your delete relational database snapshot request.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def detach_disk(self, diskName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DetachDisk>`_
        
        **Request Syntax** 
        ::
        
          response = client.detach_disk(
              diskName=\'string\'
          )
        :type diskName: string
        :param diskName: **[REQUIRED]** 
        
          The unique name of the disk you want to detach from your instance (e.g., ``my-disk`` ).
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An object describing the API operations.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def detach_instances_from_load_balancer(self, loadBalancerName: str, instanceNames: List) -> Dict:
        """
        
        This operation waits until the instances are no longer needed before they are detached from the load balancer.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DetachInstancesFromLoadBalancer>`_
        
        **Request Syntax** 
        ::
        
          response = client.detach_instances_from_load_balancer(
              loadBalancerName=\'string\',
              instanceNames=[
                  \'string\',
              ]
          )
        :type loadBalancerName: string
        :param loadBalancerName: **[REQUIRED]** 
        
          The name of the Lightsail load balancer.
        
        :type instanceNames: list
        :param instanceNames: **[REQUIRED]** 
        
          An array of strings containing the names of the instances you want to detach from the load balancer.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An object describing the API operations.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def detach_static_ip(self, staticIpName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DetachStaticIp>`_
        
        **Request Syntax** 
        ::
        
          response = client.detach_static_ip(
              staticIpName=\'string\'
          )
        :type staticIpName: string
        :param staticIpName: **[REQUIRED]** 
        
          The name of the static IP to detach from the instance.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An array of key-value pairs containing information about the results of your detach static IP request.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def download_default_key_pair(self) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DownloadDefaultKeyPair>`_
        
        **Request Syntax** 
        ::
        
          response = client.download_default_key_pair()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'publicKeyBase64\': \'string\',
                \'privateKeyBase64\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **publicKeyBase64** *(string) --* 
        
              A base64-encoded public key of the ``ssh-rsa`` type.
        
            - **privateKeyBase64** *(string) --* 
        
              A base64-encoded RSA private key.
        
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

    def get_active_names(self, pageToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetActiveNames>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_active_names(
              pageToken=\'string\'
          )
        :type pageToken: string
        :param pageToken: 
        
          A token used for paginating results from your get active names request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'activeNames\': [
                    \'string\',
                ],
                \'nextPageToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **activeNames** *(list) --* 
        
              The list of active names returned by the get active names request.
        
              - *(string) --* 
          
            - **nextPageToken** *(string) --* 
        
              A token used for advancing to the next page of results from your get active names request.
        
        """
        pass

    def get_blueprints(self, includeInactive: bool = None, pageToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetBlueprints>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_blueprints(
              includeInactive=True|False,
              pageToken=\'string\'
          )
        :type includeInactive: boolean
        :param includeInactive: 
        
          A Boolean value indicating whether to include inactive results in your request.
        
        :type pageToken: string
        :param pageToken: 
        
          A token used for advancing to the next page of results from your get blueprints request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'blueprints\': [
                    {
                        \'blueprintId\': \'string\',
                        \'name\': \'string\',
                        \'group\': \'string\',
                        \'type\': \'os\'|\'app\',
                        \'description\': \'string\',
                        \'isActive\': True|False,
                        \'minPower\': 123,
                        \'version\': \'string\',
                        \'versionCode\': \'string\',
                        \'productUrl\': \'string\',
                        \'licenseUrl\': \'string\',
                        \'platform\': \'LINUX_UNIX\'|\'WINDOWS\'
                    },
                ],
                \'nextPageToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **blueprints** *(list) --* 
        
              An array of key-value pairs that contains information about the available blueprints.
        
              - *(dict) --* 
        
                Describes a blueprint (a virtual private server image).
        
                - **blueprintId** *(string) --* 
        
                  The ID for the virtual private server image (e.g., ``app_wordpress_4_4`` or ``app_lamp_7_0`` ).
        
                - **name** *(string) --* 
        
                  The friendly name of the blueprint (e.g., ``Amazon Linux`` ).
        
                - **group** *(string) --* 
        
                  The group name of the blueprint (e.g., ``amazon-linux`` ).
        
                - **type** *(string) --* 
        
                  The type of the blueprint (e.g., ``os`` or ``app`` ).
        
                - **description** *(string) --* 
        
                  The description of the blueprint.
        
                - **isActive** *(boolean) --* 
        
                  A Boolean value indicating whether the blueprint is active. Inactive blueprints are listed to support customers with existing instances but are not necessarily available for launch of new instances. Blueprints are marked inactive when they become outdated due to operating system updates or new application releases.
        
                - **minPower** *(integer) --* 
        
                  The minimum bundle power required to run this blueprint. For example, you need a bundle with a power value of 500 or more to create an instance that uses a blueprint with a minimum power value of 500. ``0`` indicates that the blueprint runs on all instance sizes. 
        
                - **version** *(string) --* 
        
                  The version number of the operating system, application, or stack (e.g., ``2016.03.0`` ).
        
                - **versionCode** *(string) --* 
        
                  The version code.
        
                - **productUrl** *(string) --* 
        
                  The product URL to learn more about the image or blueprint.
        
                - **licenseUrl** *(string) --* 
        
                  The end-user license agreement URL for the image or blueprint.
        
                - **platform** *(string) --* 
        
                  The operating system platform (either Linux/Unix-based or Windows Server-based) of the blueprint.
        
            - **nextPageToken** *(string) --* 
        
              A token used for advancing to the next page of results from your get blueprints request.
        
        """
        pass

    def get_bundles(self, includeInactive: bool = None, pageToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetBundles>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_bundles(
              includeInactive=True|False,
              pageToken=\'string\'
          )
        :type includeInactive: boolean
        :param includeInactive: 
        
          A Boolean value that indicates whether to include inactive bundle results in your request.
        
        :type pageToken: string
        :param pageToken: 
        
          A token used for advancing to the next page of results from your get bundles request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'bundles\': [
                    {
                        \'price\': ...,
                        \'cpuCount\': 123,
                        \'diskSizeInGb\': 123,
                        \'bundleId\': \'string\',
                        \'instanceType\': \'string\',
                        \'isActive\': True|False,
                        \'name\': \'string\',
                        \'power\': 123,
                        \'ramSizeInGb\': ...,
                        \'transferPerMonthInGb\': 123,
                        \'supportedPlatforms\': [
                            \'LINUX_UNIX\'|\'WINDOWS\',
                        ]
                    },
                ],
                \'nextPageToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **bundles** *(list) --* 
        
              An array of key-value pairs that contains information about the available bundles.
        
              - *(dict) --* 
        
                Describes a bundle, which is a set of specs describing your virtual private server (or *instance* ).
        
                - **price** *(float) --* 
        
                  The price in US dollars (e.g., ``5.0`` ).
        
                - **cpuCount** *(integer) --* 
        
                  The number of vCPUs included in the bundle (e.g., ``2`` ).
        
                - **diskSizeInGb** *(integer) --* 
        
                  The size of the SSD (e.g., ``30`` ).
        
                - **bundleId** *(string) --* 
        
                  The bundle ID (e.g., ``micro_1_0`` ).
        
                - **instanceType** *(string) --* 
        
                  The Amazon EC2 instance type (e.g., ``t2.micro`` ).
        
                - **isActive** *(boolean) --* 
        
                  A Boolean value indicating whether the bundle is active.
        
                - **name** *(string) --* 
        
                  A friendly name for the bundle (e.g., ``Micro`` ).
        
                - **power** *(integer) --* 
        
                  A numeric value that represents the power of the bundle (e.g., ``500`` ). You can use the bundle\'s power value in conjunction with a blueprint\'s minimum power value to determine whether the blueprint will run on the bundle. For example, you need a bundle with a power value of 500 or more to create an instance that uses a blueprint with a minimum power value of 500.
        
                - **ramSizeInGb** *(float) --* 
        
                  The amount of RAM in GB (e.g., ``2.0`` ).
        
                - **transferPerMonthInGb** *(integer) --* 
        
                  The data transfer rate per month in GB (e.g., ``2000`` ).
        
                - **supportedPlatforms** *(list) --* 
        
                  The operating system platform (Linux/Unix-based or Windows Server-based) that the bundle supports. You can only launch a ``WINDOWS`` bundle on a blueprint that supports the ``WINDOWS`` platform. ``LINUX_UNIX`` blueprints require a ``LINUX_UNIX`` bundle.
        
                  - *(string) --* 
              
            - **nextPageToken** *(string) --* 
        
              A token used for advancing to the next page of results from your get active names request.
        
        """
        pass

    def get_disk(self, diskName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetDisk>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_disk(
              diskName=\'string\'
          )
        :type diskName: string
        :param diskName: **[REQUIRED]** 
        
          The name of the disk (e.g., ``my-disk`` ).
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'disk\': {
                    \'name\': \'string\',
                    \'arn\': \'string\',
                    \'supportCode\': \'string\',
                    \'createdAt\': datetime(2015, 1, 1),
                    \'location\': {
                        \'availabilityZone\': \'string\',
                        \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                    },
                    \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                    \'sizeInGb\': 123,
                    \'isSystemDisk\': True|False,
                    \'iops\': 123,
                    \'path\': \'string\',
                    \'state\': \'pending\'|\'error\'|\'available\'|\'in-use\'|\'unknown\',
                    \'attachedTo\': \'string\',
                    \'isAttached\': True|False,
                    \'attachmentState\': \'string\',
                    \'gbInUse\': 123
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **disk** *(dict) --* 
        
              An object containing information about the disk.
        
              - **name** *(string) --* 
        
                The unique name of the disk.
        
              - **arn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the disk.
        
              - **supportCode** *(string) --* 
        
                The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
        
              - **createdAt** *(datetime) --* 
        
                The date when the disk was created.
        
              - **location** *(dict) --* 
        
                The AWS Region and Availability Zone where the disk is located.
        
                - **availabilityZone** *(string) --* 
        
                  The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                - **regionName** *(string) --* 
        
                  The AWS Region name.
        
              - **resourceType** *(string) --* 
        
                The Lightsail resource type (e.g., ``Disk`` ).
        
              - **sizeInGb** *(integer) --* 
        
                The size of the disk in GB.
        
              - **isSystemDisk** *(boolean) --* 
        
                A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).
        
              - **iops** *(integer) --* 
        
                The input/output operations per second (IOPS) of the disk.
        
              - **path** *(string) --* 
        
                The disk path.
        
              - **state** *(string) --* 
        
                Describes the status of the disk.
        
              - **attachedTo** *(string) --* 
        
                The resources to which the disk is attached.
        
              - **isAttached** *(boolean) --* 
        
                A Boolean value indicating whether the disk is attached.
        
              - **attachmentState** *(string) --* 
        
                (Deprecated) The attachment state of the disk.
        
                .. note::
        
                  In releases prior to November 14, 2017, this parameter returned ``attached`` for system disks in the API response. It is now deprecated, but still included in the response. Use ``isAttached`` instead.
        
              - **gbInUse** *(integer) --* 
        
                (Deprecated) The number of GB in use by the disk.
        
                .. note::
        
                  In releases prior to November 14, 2017, this parameter was not included in the API response. It is now deprecated.
        
        """
        pass

    def get_disk_snapshot(self, diskSnapshotName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetDiskSnapshot>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_disk_snapshot(
              diskSnapshotName=\'string\'
          )
        :type diskSnapshotName: string
        :param diskSnapshotName: **[REQUIRED]** 
        
          The name of the disk snapshot (e.g., ``my-disk-snapshot`` ).
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'diskSnapshot\': {
                    \'name\': \'string\',
                    \'arn\': \'string\',
                    \'supportCode\': \'string\',
                    \'createdAt\': datetime(2015, 1, 1),
                    \'location\': {
                        \'availabilityZone\': \'string\',
                        \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                    },
                    \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                    \'sizeInGb\': 123,
                    \'state\': \'pending\'|\'completed\'|\'error\'|\'unknown\',
                    \'progress\': \'string\',
                    \'fromDiskName\': \'string\',
                    \'fromDiskArn\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **diskSnapshot** *(dict) --* 
        
              An object containing information about the disk snapshot.
        
              - **name** *(string) --* 
        
                The name of the disk snapshot (e.g., ``my-disk-snapshot`` ).
        
              - **arn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the disk snapshot.
        
              - **supportCode** *(string) --* 
        
                The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
        
              - **createdAt** *(datetime) --* 
        
                The date when the disk snapshot was created.
        
              - **location** *(dict) --* 
        
                The AWS Region and Availability Zone where the disk snapshot was created.
        
                - **availabilityZone** *(string) --* 
        
                  The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                - **regionName** *(string) --* 
        
                  The AWS Region name.
        
              - **resourceType** *(string) --* 
        
                The Lightsail resource type (e.g., ``DiskSnapshot`` ).
        
              - **sizeInGb** *(integer) --* 
        
                The size of the disk in GB.
        
              - **state** *(string) --* 
        
                The status of the disk snapshot operation.
        
              - **progress** *(string) --* 
        
                The progress of the disk snapshot operation.
        
              - **fromDiskName** *(string) --* 
        
                The unique name of the source disk from which you are creating the disk snapshot.
        
              - **fromDiskArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the source disk from which you are creating the disk snapshot.
        
        """
        pass

    def get_disk_snapshots(self, pageToken: str = None) -> Dict:
        """
        
        If you are describing a long list of disk snapshots, you can paginate the output to make the list more manageable. You can use the pageToken and nextPageToken values to retrieve the next items in the list.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetDiskSnapshots>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_disk_snapshots(
              pageToken=\'string\'
          )
        :type pageToken: string
        :param pageToken: 
        
          A token used for advancing to the next page of results from your GetDiskSnapshots request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'diskSnapshots\': [
                    {
                        \'name\': \'string\',
                        \'arn\': \'string\',
                        \'supportCode\': \'string\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'sizeInGb\': 123,
                        \'state\': \'pending\'|\'completed\'|\'error\'|\'unknown\',
                        \'progress\': \'string\',
                        \'fromDiskName\': \'string\',
                        \'fromDiskArn\': \'string\'
                    },
                ],
                \'nextPageToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **diskSnapshots** *(list) --* 
        
              An array of objects containing information about all block storage disk snapshots.
        
              - *(dict) --* 
        
                Describes a block storage disk snapshot.
        
                - **name** *(string) --* 
        
                  The name of the disk snapshot (e.g., ``my-disk-snapshot`` ).
        
                - **arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the disk snapshot.
        
                - **supportCode** *(string) --* 
        
                  The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
        
                - **createdAt** *(datetime) --* 
        
                  The date when the disk snapshot was created.
        
                - **location** *(dict) --* 
        
                  The AWS Region and Availability Zone where the disk snapshot was created.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **resourceType** *(string) --* 
        
                  The Lightsail resource type (e.g., ``DiskSnapshot`` ).
        
                - **sizeInGb** *(integer) --* 
        
                  The size of the disk in GB.
        
                - **state** *(string) --* 
        
                  The status of the disk snapshot operation.
        
                - **progress** *(string) --* 
        
                  The progress of the disk snapshot operation.
        
                - **fromDiskName** *(string) --* 
        
                  The unique name of the source disk from which you are creating the disk snapshot.
        
                - **fromDiskArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the source disk from which you are creating the disk snapshot.
        
            - **nextPageToken** *(string) --* 
        
              A token used for advancing to the next page of results from your GetDiskSnapshots request.
        
        """
        pass

    def get_disks(self, pageToken: str = None) -> Dict:
        """
        
        If you are describing a long list of disks, you can paginate the output to make the list more manageable. You can use the pageToken and nextPageToken values to retrieve the next items in the list.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetDisks>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_disks(
              pageToken=\'string\'
          )
        :type pageToken: string
        :param pageToken: 
        
          A token used for advancing to the next page of results from your GetDisks request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'disks\': [
                    {
                        \'name\': \'string\',
                        \'arn\': \'string\',
                        \'supportCode\': \'string\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'sizeInGb\': 123,
                        \'isSystemDisk\': True|False,
                        \'iops\': 123,
                        \'path\': \'string\',
                        \'state\': \'pending\'|\'error\'|\'available\'|\'in-use\'|\'unknown\',
                        \'attachedTo\': \'string\',
                        \'isAttached\': True|False,
                        \'attachmentState\': \'string\',
                        \'gbInUse\': 123
                    },
                ],
                \'nextPageToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **disks** *(list) --* 
        
              An array of objects containing information about all block storage disks.
        
              - *(dict) --* 
        
                Describes a system disk or an block storage disk.
        
                - **name** *(string) --* 
        
                  The unique name of the disk.
        
                - **arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the disk.
        
                - **supportCode** *(string) --* 
        
                  The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
        
                - **createdAt** *(datetime) --* 
        
                  The date when the disk was created.
        
                - **location** *(dict) --* 
        
                  The AWS Region and Availability Zone where the disk is located.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **resourceType** *(string) --* 
        
                  The Lightsail resource type (e.g., ``Disk`` ).
        
                - **sizeInGb** *(integer) --* 
        
                  The size of the disk in GB.
        
                - **isSystemDisk** *(boolean) --* 
        
                  A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).
        
                - **iops** *(integer) --* 
        
                  The input/output operations per second (IOPS) of the disk.
        
                - **path** *(string) --* 
        
                  The disk path.
        
                - **state** *(string) --* 
        
                  Describes the status of the disk.
        
                - **attachedTo** *(string) --* 
        
                  The resources to which the disk is attached.
        
                - **isAttached** *(boolean) --* 
        
                  A Boolean value indicating whether the disk is attached.
        
                - **attachmentState** *(string) --* 
        
                  (Deprecated) The attachment state of the disk.
        
                  .. note::
        
                    In releases prior to November 14, 2017, this parameter returned ``attached`` for system disks in the API response. It is now deprecated, but still included in the response. Use ``isAttached`` instead.
        
                - **gbInUse** *(integer) --* 
        
                  (Deprecated) The number of GB in use by the disk.
        
                  .. note::
        
                    In releases prior to November 14, 2017, this parameter was not included in the API response. It is now deprecated.
        
            - **nextPageToken** *(string) --* 
        
              A token used for advancing to the next page of results from your GetDisks request.
        
        """
        pass

    def get_domain(self, domainName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetDomain>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_domain(
              domainName=\'string\'
          )
        :type domainName: string
        :param domainName: **[REQUIRED]** 
        
          The domain name for which your want to return information about.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'domain\': {
                    \'name\': \'string\',
                    \'arn\': \'string\',
                    \'supportCode\': \'string\',
                    \'createdAt\': datetime(2015, 1, 1),
                    \'location\': {
                        \'availabilityZone\': \'string\',
                        \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                    },
                    \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                    \'domainEntries\': [
                        {
                            \'id\': \'string\',
                            \'name\': \'string\',
                            \'target\': \'string\',
                            \'isAlias\': True|False,
                            \'type\': \'string\',
                            \'options\': {
                                \'string\': \'string\'
                            }
                        },
                    ]
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **domain** *(dict) --* 
        
              An array of key-value pairs containing information about your get domain request.
        
              - **name** *(string) --* 
        
                The name of the domain.
        
              - **arn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the domain recordset (e.g., ``arn:aws:lightsail:global:123456789101:Domain/824cede0-abc7-4f84-8dbc-12345EXAMPLE`` ).
        
              - **supportCode** *(string) --* 
        
                The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
        
              - **createdAt** *(datetime) --* 
        
                The date when the domain recordset was created.
        
              - **location** *(dict) --* 
        
                The AWS Region and Availability Zones where the domain recordset was created.
        
                - **availabilityZone** *(string) --* 
        
                  The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                - **regionName** *(string) --* 
        
                  The AWS Region name.
        
              - **resourceType** *(string) --* 
        
                The resource type. 
        
              - **domainEntries** *(list) --* 
        
                An array of key-value pairs containing information about the domain entries.
        
                - *(dict) --* 
        
                  Describes a domain recordset entry.
        
                  - **id** *(string) --* 
        
                    The ID of the domain recordset entry.
        
                  - **name** *(string) --* 
        
                    The name of the domain.
        
                  - **target** *(string) --* 
        
                    The target AWS name server (e.g., ``ns-111.awsdns-22.com.`` ).
        
                    For Lightsail load balancers, the value looks like ``ab1234c56789c6b86aba6fb203d443bc-123456789.us-east-2.elb.amazonaws.com`` . Be sure to also set ``isAlias`` to ``true`` when setting up an A record for a load balancer.
        
                  - **isAlias** *(boolean) --* 
        
                    When ``true`` , specifies whether the domain entry is an alias used by the Lightsail load balancer. You can include an alias (A type) record in your request, which points to a load balancer DNS name and routes traffic to your load balancer
        
                  - **type** *(string) --* 
        
                    The type of domain entry (e.g., ``SOA`` or ``NS`` ).
        
                  - **options** *(dict) --* 
        
                    (Deprecated) The options for the domain entry.
        
                    .. note::
        
                      In releases prior to November 29, 2017, this parameter was not included in the API response. It is now deprecated.
        
                    - *(string) --* 
                      
                      - *(string) --* 
                
        """
        pass

    def get_domains(self, pageToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetDomains>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_domains(
              pageToken=\'string\'
          )
        :type pageToken: string
        :param pageToken: 
        
          A token used for advancing to the next page of results from your get domains request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'domains\': [
                    {
                        \'name\': \'string\',
                        \'arn\': \'string\',
                        \'supportCode\': \'string\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'domainEntries\': [
                            {
                                \'id\': \'string\',
                                \'name\': \'string\',
                                \'target\': \'string\',
                                \'isAlias\': True|False,
                                \'type\': \'string\',
                                \'options\': {
                                    \'string\': \'string\'
                                }
                            },
                        ]
                    },
                ],
                \'nextPageToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **domains** *(list) --* 
        
              An array of key-value pairs containing information about each of the domain entries in the user\'s account.
        
              - *(dict) --* 
        
                Describes a domain where you are storing recordsets in Lightsail.
        
                - **name** *(string) --* 
        
                  The name of the domain.
        
                - **arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the domain recordset (e.g., ``arn:aws:lightsail:global:123456789101:Domain/824cede0-abc7-4f84-8dbc-12345EXAMPLE`` ).
        
                - **supportCode** *(string) --* 
        
                  The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
        
                - **createdAt** *(datetime) --* 
        
                  The date when the domain recordset was created.
        
                - **location** *(dict) --* 
        
                  The AWS Region and Availability Zones where the domain recordset was created.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **domainEntries** *(list) --* 
        
                  An array of key-value pairs containing information about the domain entries.
        
                  - *(dict) --* 
        
                    Describes a domain recordset entry.
        
                    - **id** *(string) --* 
        
                      The ID of the domain recordset entry.
        
                    - **name** *(string) --* 
        
                      The name of the domain.
        
                    - **target** *(string) --* 
        
                      The target AWS name server (e.g., ``ns-111.awsdns-22.com.`` ).
        
                      For Lightsail load balancers, the value looks like ``ab1234c56789c6b86aba6fb203d443bc-123456789.us-east-2.elb.amazonaws.com`` . Be sure to also set ``isAlias`` to ``true`` when setting up an A record for a load balancer.
        
                    - **isAlias** *(boolean) --* 
        
                      When ``true`` , specifies whether the domain entry is an alias used by the Lightsail load balancer. You can include an alias (A type) record in your request, which points to a load balancer DNS name and routes traffic to your load balancer
        
                    - **type** *(string) --* 
        
                      The type of domain entry (e.g., ``SOA`` or ``NS`` ).
        
                    - **options** *(dict) --* 
        
                      (Deprecated) The options for the domain entry.
        
                      .. note::
        
                        In releases prior to November 29, 2017, this parameter was not included in the API response. It is now deprecated.
        
                      - *(string) --* 
                        
                        - *(string) --* 
                  
            - **nextPageToken** *(string) --* 
        
              A token used for advancing to the next page of results from your get active names request.
        
        """
        pass

    def get_instance(self, instanceName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetInstance>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_instance(
              instanceName=\'string\'
          )
        :type instanceName: string
        :param instanceName: **[REQUIRED]** 
        
          The name of the instance.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'instance\': {
                    \'name\': \'string\',
                    \'arn\': \'string\',
                    \'supportCode\': \'string\',
                    \'createdAt\': datetime(2015, 1, 1),
                    \'location\': {
                        \'availabilityZone\': \'string\',
                        \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                    },
                    \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                    \'blueprintId\': \'string\',
                    \'blueprintName\': \'string\',
                    \'bundleId\': \'string\',
                    \'isStaticIp\': True|False,
                    \'privateIpAddress\': \'string\',
                    \'publicIpAddress\': \'string\',
                    \'ipv6Address\': \'string\',
                    \'hardware\': {
                        \'cpuCount\': 123,
                        \'disks\': [
                            {
                                \'name\': \'string\',
                                \'arn\': \'string\',
                                \'supportCode\': \'string\',
                                \'createdAt\': datetime(2015, 1, 1),
                                \'location\': {
                                    \'availabilityZone\': \'string\',
                                    \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                                },
                                \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                                \'sizeInGb\': 123,
                                \'isSystemDisk\': True|False,
                                \'iops\': 123,
                                \'path\': \'string\',
                                \'state\': \'pending\'|\'error\'|\'available\'|\'in-use\'|\'unknown\',
                                \'attachedTo\': \'string\',
                                \'isAttached\': True|False,
                                \'attachmentState\': \'string\',
                                \'gbInUse\': 123
                            },
                        ],
                        \'ramSizeInGb\': ...
                    },
                    \'networking\': {
                        \'monthlyTransfer\': {
                            \'gbPerMonthAllocated\': 123
                        },
                        \'ports\': [
                            {
                                \'fromPort\': 123,
                                \'toPort\': 123,
                                \'protocol\': \'tcp\'|\'all\'|\'udp\',
                                \'accessFrom\': \'string\',
                                \'accessType\': \'Public\'|\'Private\',
                                \'commonName\': \'string\',
                                \'accessDirection\': \'inbound\'|\'outbound\'
                            },
                        ]
                    },
                    \'state\': {
                        \'code\': 123,
                        \'name\': \'string\'
                    },
                    \'username\': \'string\',
                    \'sshKeyName\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **instance** *(dict) --* 
        
              An array of key-value pairs containing information about the specified instance.
        
              - **name** *(string) --* 
        
                The name the user gave the instance (e.g., ``Amazon_Linux-1GB-Ohio-1`` ).
        
              - **arn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the instance (e.g., ``arn:aws:lightsail:us-east-2:123456789101:Instance/244ad76f-8aad-4741-809f-12345EXAMPLE`` ).
        
              - **supportCode** *(string) --* 
        
                The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
        
              - **createdAt** *(datetime) --* 
        
                The timestamp when the instance was created (e.g., ``1479734909.17`` ).
        
              - **location** *(dict) --* 
        
                The region name and Availability Zone where the instance is located.
        
                - **availabilityZone** *(string) --* 
        
                  The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                - **regionName** *(string) --* 
        
                  The AWS Region name.
        
              - **resourceType** *(string) --* 
        
                The type of resource (usually ``Instance`` ).
        
              - **blueprintId** *(string) --* 
        
                The blueprint ID (e.g., ``os_amlinux_2016_03`` ).
        
              - **blueprintName** *(string) --* 
        
                The friendly name of the blueprint (e.g., ``Amazon Linux`` ).
        
              - **bundleId** *(string) --* 
        
                The bundle for the instance (e.g., ``micro_1_0`` ).
        
              - **isStaticIp** *(boolean) --* 
        
                A Boolean value indicating whether this instance has a static IP assigned to it.
        
              - **privateIpAddress** *(string) --* 
        
                The private IP address of the instance.
        
              - **publicIpAddress** *(string) --* 
        
                The public IP address of the instance.
        
              - **ipv6Address** *(string) --* 
        
                The IPv6 address of the instance.
        
              - **hardware** *(dict) --* 
        
                The size of the vCPU and the amount of RAM for the instance.
        
                - **cpuCount** *(integer) --* 
        
                  The number of vCPUs the instance has.
        
                - **disks** *(list) --* 
        
                  The disks attached to the instance.
        
                  - *(dict) --* 
        
                    Describes a system disk or an block storage disk.
        
                    - **name** *(string) --* 
        
                      The unique name of the disk.
        
                    - **arn** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the disk.
        
                    - **supportCode** *(string) --* 
        
                      The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
        
                    - **createdAt** *(datetime) --* 
        
                      The date when the disk was created.
        
                    - **location** *(dict) --* 
        
                      The AWS Region and Availability Zone where the disk is located.
        
                      - **availabilityZone** *(string) --* 
        
                        The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                      - **regionName** *(string) --* 
        
                        The AWS Region name.
        
                    - **resourceType** *(string) --* 
        
                      The Lightsail resource type (e.g., ``Disk`` ).
        
                    - **sizeInGb** *(integer) --* 
        
                      The size of the disk in GB.
        
                    - **isSystemDisk** *(boolean) --* 
        
                      A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).
        
                    - **iops** *(integer) --* 
        
                      The input/output operations per second (IOPS) of the disk.
        
                    - **path** *(string) --* 
        
                      The disk path.
        
                    - **state** *(string) --* 
        
                      Describes the status of the disk.
        
                    - **attachedTo** *(string) --* 
        
                      The resources to which the disk is attached.
        
                    - **isAttached** *(boolean) --* 
        
                      A Boolean value indicating whether the disk is attached.
        
                    - **attachmentState** *(string) --* 
        
                      (Deprecated) The attachment state of the disk.
        
                      .. note::
        
                        In releases prior to November 14, 2017, this parameter returned ``attached`` for system disks in the API response. It is now deprecated, but still included in the response. Use ``isAttached`` instead.
        
                    - **gbInUse** *(integer) --* 
        
                      (Deprecated) The number of GB in use by the disk.
        
                      .. note::
        
                        In releases prior to November 14, 2017, this parameter was not included in the API response. It is now deprecated.
        
                - **ramSizeInGb** *(float) --* 
        
                  The amount of RAM in GB on the instance (e.g., ``1.0`` ).
        
              - **networking** *(dict) --* 
        
                Information about the public ports and monthly data transfer rates for the instance.
        
                - **monthlyTransfer** *(dict) --* 
        
                  The amount of data in GB allocated for monthly data transfers.
        
                  - **gbPerMonthAllocated** *(integer) --* 
        
                    The amount allocated per month (in GB).
        
                - **ports** *(list) --* 
        
                  An array of key-value pairs containing information about the ports on the instance.
        
                  - *(dict) --* 
        
                    Describes information about the instance ports.
        
                    - **fromPort** *(integer) --* 
        
                      The first port in the range.
        
                    - **toPort** *(integer) --* 
        
                      The last port in the range.
        
                    - **protocol** *(string) --* 
        
                      The protocol being used. Can be one of the following.
        
                      * ``tcp`` - Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of streamed data between applications running on hosts communicating by an IP network. If you have an application that doesn\'t require reliable data stream service, use UDP instead. 
                       
                      * ``all`` - All transport layer protocol types. For more general information, see `Transport layer <https://en.wikipedia.org/wiki/Transport_layer>`__ on Wikipedia. 
                       
                      * ``udp`` - With User Datagram Protocol (UDP), computer applications can send messages (or datagrams) to other hosts on an Internet Protocol (IP) network. Prior communications are not required to set up transmission channels or data paths. Applications that don\'t require reliable data stream service can use UDP, which provides a connectionless datagram service that emphasizes reduced latency over reliability. If you do require reliable data stream service, use TCP instead. 
                       
                    - **accessFrom** *(string) --* 
        
                      The location from which access is allowed (e.g., ``Anywhere (0.0.0.0/0)`` ).
        
                    - **accessType** *(string) --* 
        
                      The type of access (``Public`` or ``Private`` ).
        
                    - **commonName** *(string) --* 
        
                      The common name.
        
                    - **accessDirection** *(string) --* 
        
                      The access direction (``inbound`` or ``outbound`` ).
        
              - **state** *(dict) --* 
        
                The status code and the state (e.g., ``running`` ) for the instance.
        
                - **code** *(integer) --* 
        
                  The status code for the instance.
        
                - **name** *(string) --* 
        
                  The state of the instance (e.g., ``running`` or ``pending`` ).
        
              - **username** *(string) --* 
        
                The user name for connecting to the instance (e.g., ``ec2-user`` ).
        
              - **sshKeyName** *(string) --* 
        
                The name of the SSH key being used to connect to the instance (e.g., ``LightsailDefaultKeyPair`` ).
        
        """
        pass

    def get_instance_access_details(self, instanceName: str, protocol: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetInstanceAccessDetails>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_instance_access_details(
              instanceName=\'string\',
              protocol=\'ssh\'|\'rdp\'
          )
        :type instanceName: string
        :param instanceName: **[REQUIRED]** 
        
          The name of the instance to access.
        
        :type protocol: string
        :param protocol: 
        
          The protocol to use to connect to your instance. Defaults to ``ssh`` .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'accessDetails\': {
                    \'certKey\': \'string\',
                    \'expiresAt\': datetime(2015, 1, 1),
                    \'ipAddress\': \'string\',
                    \'password\': \'string\',
                    \'passwordData\': {
                        \'ciphertext\': \'string\',
                        \'keyPairName\': \'string\'
                    },
                    \'privateKey\': \'string\',
                    \'protocol\': \'ssh\'|\'rdp\',
                    \'instanceName\': \'string\',
                    \'username\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **accessDetails** *(dict) --* 
        
              An array of key-value pairs containing information about a get instance access request.
        
              - **certKey** *(string) --* 
        
                For SSH access, the public key to use when accessing your instance For OpenSSH clients (e.g., command line SSH), you should save this value to ``tempkey-cert.pub`` .
        
              - **expiresAt** *(datetime) --* 
        
                For SSH access, the date on which the temporary keys expire.
        
              - **ipAddress** *(string) --* 
        
                The public IP address of the Amazon Lightsail instance.
        
              - **password** *(string) --* 
        
                For RDP access, the password for your Amazon Lightsail instance. Password will be an empty string if the password for your new instance is not ready yet. When you create an instance, it can take up to 15 minutes for the instance to be ready.
        
                .. note::
        
                  If you create an instance using any key pair other than the default (``LightsailDefaultKeyPair`` ), ``password`` will always be an empty string.
        
                  If you change the Administrator password on the instance, Lightsail will continue to return the original password value. When accessing the instance using RDP, you need to manually enter the Administrator password after changing it from the default.
        
              - **passwordData** *(dict) --* 
        
                For a Windows Server-based instance, an object with the data you can use to retrieve your password. This is only needed if ``password`` is empty and the instance is not new (and therefore the password is not ready yet). When you create an instance, it can take up to 15 minutes for the instance to be ready.
        
                - **ciphertext** *(string) --* 
        
                  The encrypted password. Ciphertext will be an empty string if access to your new instance is not ready yet. When you create an instance, it can take up to 15 minutes for the instance to be ready.
        
                  .. note::
        
                    If you use the default key pair (``LightsailDefaultKeyPair`` ), the decrypted password will be available in the password field.
        
                    If you are using a custom key pair, you need to use your own means of decryption.
        
                    If you change the Administrator password on the instance, Lightsail will continue to return the original ciphertext value. When accessing the instance using RDP, you need to manually enter the Administrator password after changing it from the default.
        
                - **keyPairName** *(string) --* 
        
                  The name of the key pair that you used when creating your instance. If no key pair name was specified when creating the instance, Lightsail uses the default key pair (``LightsailDefaultKeyPair`` ).
        
                  If you are using a custom key pair, you need to use your own means of decrypting your password using the ``ciphertext`` . Lightsail creates the ciphertext by encrypting your password with the public key part of this key pair.
        
              - **privateKey** *(string) --* 
        
                For SSH access, the temporary private key. For OpenSSH clients (e.g., command line SSH), you should save this value to ``tempkey`` ).
        
              - **protocol** *(string) --* 
        
                The protocol for these Amazon Lightsail instance access details.
        
              - **instanceName** *(string) --* 
        
                The name of this Amazon Lightsail instance.
        
              - **username** *(string) --* 
        
                The user name to use when logging in to the Amazon Lightsail instance.
        
        """
        pass

    def get_instance_metric_data(self, instanceName: str, metricName: str, period: int, startTime: datetime, endTime: datetime, unit: str, statistics: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetInstanceMetricData>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_instance_metric_data(
              instanceName=\'string\',
              metricName=\'CPUUtilization\'|\'NetworkIn\'|\'NetworkOut\'|\'StatusCheckFailed\'|\'StatusCheckFailed_Instance\'|\'StatusCheckFailed_System\',
              period=123,
              startTime=datetime(2015, 1, 1),
              endTime=datetime(2015, 1, 1),
              unit=\'Seconds\'|\'Microseconds\'|\'Milliseconds\'|\'Bytes\'|\'Kilobytes\'|\'Megabytes\'|\'Gigabytes\'|\'Terabytes\'|\'Bits\'|\'Kilobits\'|\'Megabits\'|\'Gigabits\'|\'Terabits\'|\'Percent\'|\'Count\'|\'Bytes/Second\'|\'Kilobytes/Second\'|\'Megabytes/Second\'|\'Gigabytes/Second\'|\'Terabytes/Second\'|\'Bits/Second\'|\'Kilobits/Second\'|\'Megabits/Second\'|\'Gigabits/Second\'|\'Terabits/Second\'|\'Count/Second\'|\'None\',
              statistics=[
                  \'Minimum\'|\'Maximum\'|\'Sum\'|\'Average\'|\'SampleCount\',
              ]
          )
        :type instanceName: string
        :param instanceName: **[REQUIRED]** 
        
          The name of the instance for which you want to get metrics data.
        
        :type metricName: string
        :param metricName: **[REQUIRED]** 
        
          The metric name to get data about. 
        
        :type period: integer
        :param period: **[REQUIRED]** 
        
          The granularity, in seconds, of the returned data points.
        
        :type startTime: datetime
        :param startTime: **[REQUIRED]** 
        
          The start time of the time period.
        
        :type endTime: datetime
        :param endTime: **[REQUIRED]** 
        
          The end time of the time period.
        
        :type unit: string
        :param unit: **[REQUIRED]** 
        
          The unit. The list of valid values is below.
        
        :type statistics: list
        :param statistics: **[REQUIRED]** 
        
          The instance statistics. 
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'metricName\': \'CPUUtilization\'|\'NetworkIn\'|\'NetworkOut\'|\'StatusCheckFailed\'|\'StatusCheckFailed_Instance\'|\'StatusCheckFailed_System\',
                \'metricData\': [
                    {
                        \'average\': 123.0,
                        \'maximum\': 123.0,
                        \'minimum\': 123.0,
                        \'sampleCount\': 123.0,
                        \'sum\': 123.0,
                        \'timestamp\': datetime(2015, 1, 1),
                        \'unit\': \'Seconds\'|\'Microseconds\'|\'Milliseconds\'|\'Bytes\'|\'Kilobytes\'|\'Megabytes\'|\'Gigabytes\'|\'Terabytes\'|\'Bits\'|\'Kilobits\'|\'Megabits\'|\'Gigabits\'|\'Terabits\'|\'Percent\'|\'Count\'|\'Bytes/Second\'|\'Kilobytes/Second\'|\'Megabytes/Second\'|\'Gigabytes/Second\'|\'Terabytes/Second\'|\'Bits/Second\'|\'Kilobits/Second\'|\'Megabits/Second\'|\'Gigabits/Second\'|\'Terabits/Second\'|\'Count/Second\'|\'None\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **metricName** *(string) --* 
        
              The metric name to return data for.
        
            - **metricData** *(list) --* 
        
              An array of key-value pairs containing information about the results of your get instance metric data request.
        
              - *(dict) --* 
        
                Describes the metric data point.
        
                - **average** *(float) --* 
        
                  The average.
        
                - **maximum** *(float) --* 
        
                  The maximum.
        
                - **minimum** *(float) --* 
        
                  The minimum.
        
                - **sampleCount** *(float) --* 
        
                  The sample count.
        
                - **sum** *(float) --* 
        
                  The sum.
        
                - **timestamp** *(datetime) --* 
        
                  The timestamp (e.g., ``1479816991.349`` ).
        
                - **unit** *(string) --* 
        
                  The unit. 
        
        """
        pass

    def get_instance_port_states(self, instanceName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetInstancePortStates>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_instance_port_states(
              instanceName=\'string\'
          )
        :type instanceName: string
        :param instanceName: **[REQUIRED]** 
        
          The name of the instance.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'portStates\': [
                    {
                        \'fromPort\': 123,
                        \'toPort\': 123,
                        \'protocol\': \'tcp\'|\'all\'|\'udp\',
                        \'state\': \'open\'|\'closed\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **portStates** *(list) --* 
        
              Information about the port states resulting from your request.
        
              - *(dict) --* 
        
                Describes the port state.
        
                - **fromPort** *(integer) --* 
        
                  The first port in the range.
        
                - **toPort** *(integer) --* 
        
                  The last port in the range.
        
                - **protocol** *(string) --* 
        
                  The protocol being used. Can be one of the following.
        
                  * ``tcp`` - Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of streamed data between applications running on hosts communicating by an IP network. If you have an application that doesn\'t require reliable data stream service, use UDP instead. 
                   
                  * ``all`` - All transport layer protocol types. For more general information, see `Transport layer <https://en.wikipedia.org/wiki/Transport_layer>`__ on Wikipedia. 
                   
                  * ``udp`` - With User Datagram Protocol (UDP), computer applications can send messages (or datagrams) to other hosts on an Internet Protocol (IP) network. Prior communications are not required to set up transmission channels or data paths. Applications that don\'t require reliable data stream service can use UDP, which provides a connectionless datagram service that emphasizes reduced latency over reliability. If you do require reliable data stream service, use TCP instead. 
                   
                - **state** *(string) --* 
        
                  Specifies whether the instance port is ``open`` or ``closed`` .
        
        """
        pass

    def get_instance_snapshot(self, instanceSnapshotName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetInstanceSnapshot>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_instance_snapshot(
              instanceSnapshotName=\'string\'
          )
        :type instanceSnapshotName: string
        :param instanceSnapshotName: **[REQUIRED]** 
        
          The name of the snapshot for which you are requesting information.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'instanceSnapshot\': {
                    \'name\': \'string\',
                    \'arn\': \'string\',
                    \'supportCode\': \'string\',
                    \'createdAt\': datetime(2015, 1, 1),
                    \'location\': {
                        \'availabilityZone\': \'string\',
                        \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                    },
                    \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                    \'state\': \'pending\'|\'error\'|\'available\',
                    \'progress\': \'string\',
                    \'fromAttachedDisks\': [
                        {
                            \'name\': \'string\',
                            \'arn\': \'string\',
                            \'supportCode\': \'string\',
                            \'createdAt\': datetime(2015, 1, 1),
                            \'location\': {
                                \'availabilityZone\': \'string\',
                                \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                            },
                            \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                            \'sizeInGb\': 123,
                            \'isSystemDisk\': True|False,
                            \'iops\': 123,
                            \'path\': \'string\',
                            \'state\': \'pending\'|\'error\'|\'available\'|\'in-use\'|\'unknown\',
                            \'attachedTo\': \'string\',
                            \'isAttached\': True|False,
                            \'attachmentState\': \'string\',
                            \'gbInUse\': 123
                        },
                    ],
                    \'fromInstanceName\': \'string\',
                    \'fromInstanceArn\': \'string\',
                    \'fromBlueprintId\': \'string\',
                    \'fromBundleId\': \'string\',
                    \'sizeInGb\': 123
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **instanceSnapshot** *(dict) --* 
        
              An array of key-value pairs containing information about the results of your get instance snapshot request.
        
              - **name** *(string) --* 
        
                The name of the snapshot.
        
              - **arn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the snapshot (e.g., ``arn:aws:lightsail:us-east-2:123456789101:InstanceSnapshot/d23b5706-3322-4d83-81e5-12345EXAMPLE`` ).
        
              - **supportCode** *(string) --* 
        
                The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
        
              - **createdAt** *(datetime) --* 
        
                The timestamp when the snapshot was created (e.g., ``1479907467.024`` ).
        
              - **location** *(dict) --* 
        
                The region name and Availability Zone where you created the snapshot.
        
                - **availabilityZone** *(string) --* 
        
                  The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                - **regionName** *(string) --* 
        
                  The AWS Region name.
        
              - **resourceType** *(string) --* 
        
                The type of resource (usually ``InstanceSnapshot`` ).
        
              - **state** *(string) --* 
        
                The state the snapshot is in.
        
              - **progress** *(string) --* 
        
                The progress of the snapshot.
        
              - **fromAttachedDisks** *(list) --* 
        
                An array of disk objects containing information about all block storage disks.
        
                - *(dict) --* 
        
                  Describes a system disk or an block storage disk.
        
                  - **name** *(string) --* 
        
                    The unique name of the disk.
        
                  - **arn** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the disk.
        
                  - **supportCode** *(string) --* 
        
                    The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
        
                  - **createdAt** *(datetime) --* 
        
                    The date when the disk was created.
        
                  - **location** *(dict) --* 
        
                    The AWS Region and Availability Zone where the disk is located.
        
                    - **availabilityZone** *(string) --* 
        
                      The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                    - **regionName** *(string) --* 
        
                      The AWS Region name.
        
                  - **resourceType** *(string) --* 
        
                    The Lightsail resource type (e.g., ``Disk`` ).
        
                  - **sizeInGb** *(integer) --* 
        
                    The size of the disk in GB.
        
                  - **isSystemDisk** *(boolean) --* 
        
                    A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).
        
                  - **iops** *(integer) --* 
        
                    The input/output operations per second (IOPS) of the disk.
        
                  - **path** *(string) --* 
        
                    The disk path.
        
                  - **state** *(string) --* 
        
                    Describes the status of the disk.
        
                  - **attachedTo** *(string) --* 
        
                    The resources to which the disk is attached.
        
                  - **isAttached** *(boolean) --* 
        
                    A Boolean value indicating whether the disk is attached.
        
                  - **attachmentState** *(string) --* 
        
                    (Deprecated) The attachment state of the disk.
        
                    .. note::
        
                      In releases prior to November 14, 2017, this parameter returned ``attached`` for system disks in the API response. It is now deprecated, but still included in the response. Use ``isAttached`` instead.
        
                  - **gbInUse** *(integer) --* 
        
                    (Deprecated) The number of GB in use by the disk.
        
                    .. note::
        
                      In releases prior to November 14, 2017, this parameter was not included in the API response. It is now deprecated.
        
              - **fromInstanceName** *(string) --* 
        
                The instance from which the snapshot was created.
        
              - **fromInstanceArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the instance from which the snapshot was created (e.g., ``arn:aws:lightsail:us-east-2:123456789101:Instance/64b8404c-ccb1-430b-8daf-12345EXAMPLE`` ).
        
              - **fromBlueprintId** *(string) --* 
        
                The blueprint ID from which you created the snapshot (e.g., ``os_debian_8_3`` ). A blueprint is a virtual private server (or *instance* ) image used to create instances quickly.
        
              - **fromBundleId** *(string) --* 
        
                The bundle ID from which you created the snapshot (e.g., ``micro_1_0`` ).
        
              - **sizeInGb** *(integer) --* 
        
                The size in GB of the SSD.
        
        """
        pass

    def get_instance_snapshots(self, pageToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetInstanceSnapshots>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_instance_snapshots(
              pageToken=\'string\'
          )
        :type pageToken: string
        :param pageToken: 
        
          A token used for advancing to the next page of results from your get instance snapshots request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'instanceSnapshots\': [
                    {
                        \'name\': \'string\',
                        \'arn\': \'string\',
                        \'supportCode\': \'string\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'state\': \'pending\'|\'error\'|\'available\',
                        \'progress\': \'string\',
                        \'fromAttachedDisks\': [
                            {
                                \'name\': \'string\',
                                \'arn\': \'string\',
                                \'supportCode\': \'string\',
                                \'createdAt\': datetime(2015, 1, 1),
                                \'location\': {
                                    \'availabilityZone\': \'string\',
                                    \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                                },
                                \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                                \'sizeInGb\': 123,
                                \'isSystemDisk\': True|False,
                                \'iops\': 123,
                                \'path\': \'string\',
                                \'state\': \'pending\'|\'error\'|\'available\'|\'in-use\'|\'unknown\',
                                \'attachedTo\': \'string\',
                                \'isAttached\': True|False,
                                \'attachmentState\': \'string\',
                                \'gbInUse\': 123
                            },
                        ],
                        \'fromInstanceName\': \'string\',
                        \'fromInstanceArn\': \'string\',
                        \'fromBlueprintId\': \'string\',
                        \'fromBundleId\': \'string\',
                        \'sizeInGb\': 123
                    },
                ],
                \'nextPageToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **instanceSnapshots** *(list) --* 
        
              An array of key-value pairs containing information about the results of your get instance snapshots request.
        
              - *(dict) --* 
        
                Describes the snapshot of the virtual private server, or *instance* .
        
                - **name** *(string) --* 
        
                  The name of the snapshot.
        
                - **arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the snapshot (e.g., ``arn:aws:lightsail:us-east-2:123456789101:InstanceSnapshot/d23b5706-3322-4d83-81e5-12345EXAMPLE`` ).
        
                - **supportCode** *(string) --* 
        
                  The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the snapshot was created (e.g., ``1479907467.024`` ).
        
                - **location** *(dict) --* 
        
                  The region name and Availability Zone where you created the snapshot.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **resourceType** *(string) --* 
        
                  The type of resource (usually ``InstanceSnapshot`` ).
        
                - **state** *(string) --* 
        
                  The state the snapshot is in.
        
                - **progress** *(string) --* 
        
                  The progress of the snapshot.
        
                - **fromAttachedDisks** *(list) --* 
        
                  An array of disk objects containing information about all block storage disks.
        
                  - *(dict) --* 
        
                    Describes a system disk or an block storage disk.
        
                    - **name** *(string) --* 
        
                      The unique name of the disk.
        
                    - **arn** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the disk.
        
                    - **supportCode** *(string) --* 
        
                      The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
        
                    - **createdAt** *(datetime) --* 
        
                      The date when the disk was created.
        
                    - **location** *(dict) --* 
        
                      The AWS Region and Availability Zone where the disk is located.
        
                      - **availabilityZone** *(string) --* 
        
                        The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                      - **regionName** *(string) --* 
        
                        The AWS Region name.
        
                    - **resourceType** *(string) --* 
        
                      The Lightsail resource type (e.g., ``Disk`` ).
        
                    - **sizeInGb** *(integer) --* 
        
                      The size of the disk in GB.
        
                    - **isSystemDisk** *(boolean) --* 
        
                      A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).
        
                    - **iops** *(integer) --* 
        
                      The input/output operations per second (IOPS) of the disk.
        
                    - **path** *(string) --* 
        
                      The disk path.
        
                    - **state** *(string) --* 
        
                      Describes the status of the disk.
        
                    - **attachedTo** *(string) --* 
        
                      The resources to which the disk is attached.
        
                    - **isAttached** *(boolean) --* 
        
                      A Boolean value indicating whether the disk is attached.
        
                    - **attachmentState** *(string) --* 
        
                      (Deprecated) The attachment state of the disk.
        
                      .. note::
        
                        In releases prior to November 14, 2017, this parameter returned ``attached`` for system disks in the API response. It is now deprecated, but still included in the response. Use ``isAttached`` instead.
        
                    - **gbInUse** *(integer) --* 
        
                      (Deprecated) The number of GB in use by the disk.
        
                      .. note::
        
                        In releases prior to November 14, 2017, this parameter was not included in the API response. It is now deprecated.
        
                - **fromInstanceName** *(string) --* 
        
                  The instance from which the snapshot was created.
        
                - **fromInstanceArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the instance from which the snapshot was created (e.g., ``arn:aws:lightsail:us-east-2:123456789101:Instance/64b8404c-ccb1-430b-8daf-12345EXAMPLE`` ).
        
                - **fromBlueprintId** *(string) --* 
        
                  The blueprint ID from which you created the snapshot (e.g., ``os_debian_8_3`` ). A blueprint is a virtual private server (or *instance* ) image used to create instances quickly.
        
                - **fromBundleId** *(string) --* 
        
                  The bundle ID from which you created the snapshot (e.g., ``micro_1_0`` ).
        
                - **sizeInGb** *(integer) --* 
        
                  The size in GB of the SSD.
        
            - **nextPageToken** *(string) --* 
        
              A token used for advancing to the next page of results from your get instance snapshots request.
        
        """
        pass

    def get_instance_state(self, instanceName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetInstanceState>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_instance_state(
              instanceName=\'string\'
          )
        :type instanceName: string
        :param instanceName: **[REQUIRED]** 
        
          The name of the instance to get state information about.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'state\': {
                    \'code\': 123,
                    \'name\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **state** *(dict) --* 
        
              The state of the instance.
        
              - **code** *(integer) --* 
        
                The status code for the instance.
        
              - **name** *(string) --* 
        
                The state of the instance (e.g., ``running`` or ``pending`` ).
        
        """
        pass

    def get_instances(self, pageToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetInstances>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_instances(
              pageToken=\'string\'
          )
        :type pageToken: string
        :param pageToken: 
        
          A token used for advancing to the next page of results from your get instances request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'instances\': [
                    {
                        \'name\': \'string\',
                        \'arn\': \'string\',
                        \'supportCode\': \'string\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'blueprintId\': \'string\',
                        \'blueprintName\': \'string\',
                        \'bundleId\': \'string\',
                        \'isStaticIp\': True|False,
                        \'privateIpAddress\': \'string\',
                        \'publicIpAddress\': \'string\',
                        \'ipv6Address\': \'string\',
                        \'hardware\': {
                            \'cpuCount\': 123,
                            \'disks\': [
                                {
                                    \'name\': \'string\',
                                    \'arn\': \'string\',
                                    \'supportCode\': \'string\',
                                    \'createdAt\': datetime(2015, 1, 1),
                                    \'location\': {
                                        \'availabilityZone\': \'string\',
                                        \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                                    },
                                    \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                                    \'sizeInGb\': 123,
                                    \'isSystemDisk\': True|False,
                                    \'iops\': 123,
                                    \'path\': \'string\',
                                    \'state\': \'pending\'|\'error\'|\'available\'|\'in-use\'|\'unknown\',
                                    \'attachedTo\': \'string\',
                                    \'isAttached\': True|False,
                                    \'attachmentState\': \'string\',
                                    \'gbInUse\': 123
                                },
                            ],
                            \'ramSizeInGb\': ...
                        },
                        \'networking\': {
                            \'monthlyTransfer\': {
                                \'gbPerMonthAllocated\': 123
                            },
                            \'ports\': [
                                {
                                    \'fromPort\': 123,
                                    \'toPort\': 123,
                                    \'protocol\': \'tcp\'|\'all\'|\'udp\',
                                    \'accessFrom\': \'string\',
                                    \'accessType\': \'Public\'|\'Private\',
                                    \'commonName\': \'string\',
                                    \'accessDirection\': \'inbound\'|\'outbound\'
                                },
                            ]
                        },
                        \'state\': {
                            \'code\': 123,
                            \'name\': \'string\'
                        },
                        \'username\': \'string\',
                        \'sshKeyName\': \'string\'
                    },
                ],
                \'nextPageToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **instances** *(list) --* 
        
              An array of key-value pairs containing information about your instances.
        
              - *(dict) --* 
        
                Describes an instance (a virtual private server).
        
                - **name** *(string) --* 
        
                  The name the user gave the instance (e.g., ``Amazon_Linux-1GB-Ohio-1`` ).
        
                - **arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the instance (e.g., ``arn:aws:lightsail:us-east-2:123456789101:Instance/244ad76f-8aad-4741-809f-12345EXAMPLE`` ).
        
                - **supportCode** *(string) --* 
        
                  The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the instance was created (e.g., ``1479734909.17`` ).
        
                - **location** *(dict) --* 
        
                  The region name and Availability Zone where the instance is located.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **resourceType** *(string) --* 
        
                  The type of resource (usually ``Instance`` ).
        
                - **blueprintId** *(string) --* 
        
                  The blueprint ID (e.g., ``os_amlinux_2016_03`` ).
        
                - **blueprintName** *(string) --* 
        
                  The friendly name of the blueprint (e.g., ``Amazon Linux`` ).
        
                - **bundleId** *(string) --* 
        
                  The bundle for the instance (e.g., ``micro_1_0`` ).
        
                - **isStaticIp** *(boolean) --* 
        
                  A Boolean value indicating whether this instance has a static IP assigned to it.
        
                - **privateIpAddress** *(string) --* 
        
                  The private IP address of the instance.
        
                - **publicIpAddress** *(string) --* 
        
                  The public IP address of the instance.
        
                - **ipv6Address** *(string) --* 
        
                  The IPv6 address of the instance.
        
                - **hardware** *(dict) --* 
        
                  The size of the vCPU and the amount of RAM for the instance.
        
                  - **cpuCount** *(integer) --* 
        
                    The number of vCPUs the instance has.
        
                  - **disks** *(list) --* 
        
                    The disks attached to the instance.
        
                    - *(dict) --* 
        
                      Describes a system disk or an block storage disk.
        
                      - **name** *(string) --* 
        
                        The unique name of the disk.
        
                      - **arn** *(string) --* 
        
                        The Amazon Resource Name (ARN) of the disk.
        
                      - **supportCode** *(string) --* 
        
                        The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
        
                      - **createdAt** *(datetime) --* 
        
                        The date when the disk was created.
        
                      - **location** *(dict) --* 
        
                        The AWS Region and Availability Zone where the disk is located.
        
                        - **availabilityZone** *(string) --* 
        
                          The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                        - **regionName** *(string) --* 
        
                          The AWS Region name.
        
                      - **resourceType** *(string) --* 
        
                        The Lightsail resource type (e.g., ``Disk`` ).
        
                      - **sizeInGb** *(integer) --* 
        
                        The size of the disk in GB.
        
                      - **isSystemDisk** *(boolean) --* 
        
                        A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).
        
                      - **iops** *(integer) --* 
        
                        The input/output operations per second (IOPS) of the disk.
        
                      - **path** *(string) --* 
        
                        The disk path.
        
                      - **state** *(string) --* 
        
                        Describes the status of the disk.
        
                      - **attachedTo** *(string) --* 
        
                        The resources to which the disk is attached.
        
                      - **isAttached** *(boolean) --* 
        
                        A Boolean value indicating whether the disk is attached.
        
                      - **attachmentState** *(string) --* 
        
                        (Deprecated) The attachment state of the disk.
        
                        .. note::
        
                          In releases prior to November 14, 2017, this parameter returned ``attached`` for system disks in the API response. It is now deprecated, but still included in the response. Use ``isAttached`` instead.
        
                      - **gbInUse** *(integer) --* 
        
                        (Deprecated) The number of GB in use by the disk.
        
                        .. note::
        
                          In releases prior to November 14, 2017, this parameter was not included in the API response. It is now deprecated.
        
                  - **ramSizeInGb** *(float) --* 
        
                    The amount of RAM in GB on the instance (e.g., ``1.0`` ).
        
                - **networking** *(dict) --* 
        
                  Information about the public ports and monthly data transfer rates for the instance.
        
                  - **monthlyTransfer** *(dict) --* 
        
                    The amount of data in GB allocated for monthly data transfers.
        
                    - **gbPerMonthAllocated** *(integer) --* 
        
                      The amount allocated per month (in GB).
        
                  - **ports** *(list) --* 
        
                    An array of key-value pairs containing information about the ports on the instance.
        
                    - *(dict) --* 
        
                      Describes information about the instance ports.
        
                      - **fromPort** *(integer) --* 
        
                        The first port in the range.
        
                      - **toPort** *(integer) --* 
        
                        The last port in the range.
        
                      - **protocol** *(string) --* 
        
                        The protocol being used. Can be one of the following.
        
                        * ``tcp`` - Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of streamed data between applications running on hosts communicating by an IP network. If you have an application that doesn\'t require reliable data stream service, use UDP instead. 
                         
                        * ``all`` - All transport layer protocol types. For more general information, see `Transport layer <https://en.wikipedia.org/wiki/Transport_layer>`__ on Wikipedia. 
                         
                        * ``udp`` - With User Datagram Protocol (UDP), computer applications can send messages (or datagrams) to other hosts on an Internet Protocol (IP) network. Prior communications are not required to set up transmission channels or data paths. Applications that don\'t require reliable data stream service can use UDP, which provides a connectionless datagram service that emphasizes reduced latency over reliability. If you do require reliable data stream service, use TCP instead. 
                         
                      - **accessFrom** *(string) --* 
        
                        The location from which access is allowed (e.g., ``Anywhere (0.0.0.0/0)`` ).
        
                      - **accessType** *(string) --* 
        
                        The type of access (``Public`` or ``Private`` ).
        
                      - **commonName** *(string) --* 
        
                        The common name.
        
                      - **accessDirection** *(string) --* 
        
                        The access direction (``inbound`` or ``outbound`` ).
        
                - **state** *(dict) --* 
        
                  The status code and the state (e.g., ``running`` ) for the instance.
        
                  - **code** *(integer) --* 
        
                    The status code for the instance.
        
                  - **name** *(string) --* 
        
                    The state of the instance (e.g., ``running`` or ``pending`` ).
        
                - **username** *(string) --* 
        
                  The user name for connecting to the instance (e.g., ``ec2-user`` ).
        
                - **sshKeyName** *(string) --* 
        
                  The name of the SSH key being used to connect to the instance (e.g., ``LightsailDefaultKeyPair`` ).
        
            - **nextPageToken** *(string) --* 
        
              A token used for advancing to the next page of results from your get instances request.
        
        """
        pass

    def get_key_pair(self, keyPairName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetKeyPair>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_key_pair(
              keyPairName=\'string\'
          )
        :type keyPairName: string
        :param keyPairName: **[REQUIRED]** 
        
          The name of the key pair for which you are requesting information.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'keyPair\': {
                    \'name\': \'string\',
                    \'arn\': \'string\',
                    \'supportCode\': \'string\',
                    \'createdAt\': datetime(2015, 1, 1),
                    \'location\': {
                        \'availabilityZone\': \'string\',
                        \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                    },
                    \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                    \'fingerprint\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **keyPair** *(dict) --* 
        
              An array of key-value pairs containing information about the key pair.
        
              - **name** *(string) --* 
        
                The friendly name of the SSH key pair.
        
              - **arn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the key pair (e.g., ``arn:aws:lightsail:us-east-2:123456789101:KeyPair/05859e3d-331d-48ba-9034-12345EXAMPLE`` ).
        
              - **supportCode** *(string) --* 
        
                The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
        
              - **createdAt** *(datetime) --* 
        
                The timestamp when the key pair was created (e.g., ``1479816991.349`` ).
        
              - **location** *(dict) --* 
        
                The region name and Availability Zone where the key pair was created.
        
                - **availabilityZone** *(string) --* 
        
                  The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                - **regionName** *(string) --* 
        
                  The AWS Region name.
        
              - **resourceType** *(string) --* 
        
                The resource type (usually ``KeyPair`` ).
        
              - **fingerprint** *(string) --* 
        
                The RSA fingerprint of the key pair.
        
        """
        pass

    def get_key_pairs(self, pageToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetKeyPairs>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_key_pairs(
              pageToken=\'string\'
          )
        :type pageToken: string
        :param pageToken: 
        
          A token used for advancing to the next page of results from your get key pairs request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'keyPairs\': [
                    {
                        \'name\': \'string\',
                        \'arn\': \'string\',
                        \'supportCode\': \'string\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'fingerprint\': \'string\'
                    },
                ],
                \'nextPageToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **keyPairs** *(list) --* 
        
              An array of key-value pairs containing information about the key pairs.
        
              - *(dict) --* 
        
                Describes the SSH key pair.
        
                - **name** *(string) --* 
        
                  The friendly name of the SSH key pair.
        
                - **arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the key pair (e.g., ``arn:aws:lightsail:us-east-2:123456789101:KeyPair/05859e3d-331d-48ba-9034-12345EXAMPLE`` ).
        
                - **supportCode** *(string) --* 
        
                  The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the key pair was created (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region name and Availability Zone where the key pair was created.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **resourceType** *(string) --* 
        
                  The resource type (usually ``KeyPair`` ).
        
                - **fingerprint** *(string) --* 
        
                  The RSA fingerprint of the key pair.
        
            - **nextPageToken** *(string) --* 
        
              A token used for advancing to the next page of results from your get key pairs request.
        
        """
        pass

    def get_load_balancer(self, loadBalancerName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetLoadBalancer>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_load_balancer(
              loadBalancerName=\'string\'
          )
        :type loadBalancerName: string
        :param loadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'loadBalancer\': {
                    \'name\': \'string\',
                    \'arn\': \'string\',
                    \'supportCode\': \'string\',
                    \'createdAt\': datetime(2015, 1, 1),
                    \'location\': {
                        \'availabilityZone\': \'string\',
                        \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                    },
                    \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                    \'dnsName\': \'string\',
                    \'state\': \'active\'|\'provisioning\'|\'active_impaired\'|\'failed\'|\'unknown\',
                    \'protocol\': \'HTTP_HTTPS\'|\'HTTP\',
                    \'publicPorts\': [
                        123,
                    ],
                    \'healthCheckPath\': \'string\',
                    \'instancePort\': 123,
                    \'instanceHealthSummary\': [
                        {
                            \'instanceName\': \'string\',
                            \'instanceHealth\': \'initial\'|\'healthy\'|\'unhealthy\'|\'unused\'|\'draining\'|\'unavailable\',
                            \'instanceHealthReason\': \'Lb.RegistrationInProgress\'|\'Lb.InitialHealthChecking\'|\'Lb.InternalError\'|\'Instance.ResponseCodeMismatch\'|\'Instance.Timeout\'|\'Instance.FailedHealthChecks\'|\'Instance.NotRegistered\'|\'Instance.NotInUse\'|\'Instance.DeregistrationInProgress\'|\'Instance.InvalidState\'|\'Instance.IpUnusable\'
                        },
                    ],
                    \'tlsCertificateSummaries\': [
                        {
                            \'name\': \'string\',
                            \'isAttached\': True|False
                        },
                    ],
                    \'configurationOptions\': {
                        \'string\': \'string\'
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **loadBalancer** *(dict) --* 
        
              An object containing information about your load balancer.
        
              - **name** *(string) --* 
        
                The name of the load balancer (e.g., ``my-load-balancer`` ).
        
              - **arn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the load balancer.
        
              - **supportCode** *(string) --* 
        
                The support code. Include this code in your email to support when you have questions about your Lightsail load balancer. This code enables our support team to look up your Lightsail information more easily.
        
              - **createdAt** *(datetime) --* 
        
                The date when your load balancer was created.
        
              - **location** *(dict) --* 
        
                The AWS Region where your load balancer was created (e.g., ``us-east-2a`` ). Lightsail automatically creates your load balancer across Availability Zones.
        
                - **availabilityZone** *(string) --* 
        
                  The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                - **regionName** *(string) --* 
        
                  The AWS Region name.
        
              - **resourceType** *(string) --* 
        
                The resource type (e.g., ``LoadBalancer`` .
        
              - **dnsName** *(string) --* 
        
                The DNS name of your Lightsail load balancer.
        
              - **state** *(string) --* 
        
                The status of your load balancer. Valid values are below.
        
              - **protocol** *(string) --* 
        
                The protocol you have enabled for your load balancer. Valid values are below.
        
                You can\'t just have ``HTTP_HTTPS`` , but you can have just ``HTTP`` .
        
              - **publicPorts** *(list) --* 
        
                An array of public port settings for your load balancer. For HTTP, use port 80. For HTTPS, use port 443.
        
                - *(integer) --* 
            
              - **healthCheckPath** *(string) --* 
        
                The path you specified to perform your health checks. If no path is specified, the load balancer tries to make a request to the default (root) page.
        
              - **instancePort** *(integer) --* 
        
                The port where the load balancer will direct traffic to your Lightsail instances. For HTTP traffic, it\'s port 80. For HTTPS traffic, it\'s port 443.
        
              - **instanceHealthSummary** *(list) --* 
        
                An array of InstanceHealthSummary objects describing the health of the load balancer.
        
                - *(dict) --* 
        
                  Describes information about the health of the instance.
        
                  - **instanceName** *(string) --* 
        
                    The name of the Lightsail instance for which you are requesting health check data.
        
                  - **instanceHealth** *(string) --* 
        
                    Describes the overall instance health. Valid values are below.
        
                  - **instanceHealthReason** *(string) --* 
        
                    More information about the instance health. If the ``instanceHealth`` is ``healthy`` , then an ``instanceHealthReason`` value is not provided.
        
                    If ** ``instanceHealth`` ** is ``initial`` , the ** ``instanceHealthReason`` ** value can be one of the following:
        
                    * **``Lb.RegistrationInProgress`` ** - The target instance is in the process of being registered with the load balancer. 
                     
                    * **``Lb.InitialHealthChecking`` ** - The Lightsail load balancer is still sending the target instance the minimum number of health checks required to determine its health status. 
                     
                    If ** ``instanceHealth`` ** is ``unhealthy`` , the ** ``instanceHealthReason`` ** value can be one of the following:
        
                    * **``Instance.ResponseCodeMismatch`` ** - The health checks did not return an expected HTTP code. 
                     
                    * **``Instance.Timeout`` ** - The health check requests timed out. 
                     
                    * **``Instance.FailedHealthChecks`` ** - The health checks failed because the connection to the target instance timed out, the target instance response was malformed, or the target instance failed the health check for an unknown reason. 
                     
                    * **``Lb.InternalError`` ** - The health checks failed due to an internal error. 
                     
                    If ** ``instanceHealth`` ** is ``unused`` , the ** ``instanceHealthReason`` ** value can be one of the following:
        
                    * **``Instance.NotRegistered`` ** - The target instance is not registered with the target group. 
                     
                    * **``Instance.NotInUse`` ** - The target group is not used by any load balancer, or the target instance is in an Availability Zone that is not enabled for its load balancer. 
                     
                    * **``Instance.IpUnusable`` ** - The target IP address is reserved for use by a Lightsail load balancer. 
                     
                    * **``Instance.InvalidState`` ** - The target is in the stopped or terminated state. 
                     
                    If ** ``instanceHealth`` ** is ``draining`` , the ** ``instanceHealthReason`` ** value can be one of the following:
        
                    * **``Instance.DeregistrationInProgress`` ** - The target instance is in the process of being deregistered and the deregistration delay period has not expired. 
                     
              - **tlsCertificateSummaries** *(list) --* 
        
                An array of LoadBalancerTlsCertificateSummary objects that provide additional information about the SSL/TLS certificates. For example, if ``true`` , the certificate is attached to the load balancer.
        
                - *(dict) --* 
        
                  Provides a summary of SSL/TLS certificate metadata.
        
                  - **name** *(string) --* 
        
                    The name of the SSL/TLS certificate.
        
                  - **isAttached** *(boolean) --* 
        
                    When ``true`` , the SSL/TLS certificate is attached to the Lightsail load balancer.
        
              - **configurationOptions** *(dict) --* 
        
                A string to string map of the configuration options for your load balancer. Valid values are listed below.
        
                - *(string) --* 
                  
                  - *(string) --* 
            
        """
        pass

    def get_load_balancer_metric_data(self, loadBalancerName: str, metricName: str, period: int, startTime: datetime, endTime: datetime, unit: str, statistics: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetLoadBalancerMetricData>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_load_balancer_metric_data(
              loadBalancerName=\'string\',
              metricName=\'ClientTLSNegotiationErrorCount\'|\'HealthyHostCount\'|\'UnhealthyHostCount\'|\'HTTPCode_LB_4XX_Count\'|\'HTTPCode_LB_5XX_Count\'|\'HTTPCode_Instance_2XX_Count\'|\'HTTPCode_Instance_3XX_Count\'|\'HTTPCode_Instance_4XX_Count\'|\'HTTPCode_Instance_5XX_Count\'|\'InstanceResponseTime\'|\'RejectedConnectionCount\'|\'RequestCount\',
              period=123,
              startTime=datetime(2015, 1, 1),
              endTime=datetime(2015, 1, 1),
              unit=\'Seconds\'|\'Microseconds\'|\'Milliseconds\'|\'Bytes\'|\'Kilobytes\'|\'Megabytes\'|\'Gigabytes\'|\'Terabytes\'|\'Bits\'|\'Kilobits\'|\'Megabits\'|\'Gigabits\'|\'Terabits\'|\'Percent\'|\'Count\'|\'Bytes/Second\'|\'Kilobytes/Second\'|\'Megabytes/Second\'|\'Gigabytes/Second\'|\'Terabytes/Second\'|\'Bits/Second\'|\'Kilobits/Second\'|\'Megabits/Second\'|\'Gigabits/Second\'|\'Terabits/Second\'|\'Count/Second\'|\'None\',
              statistics=[
                  \'Minimum\'|\'Maximum\'|\'Sum\'|\'Average\'|\'SampleCount\',
              ]
          )
        :type loadBalancerName: string
        :param loadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer.
        
        :type metricName: string
        :param metricName: **[REQUIRED]** 
        
          The metric about which you want to return information. Valid values are listed below, along with the most useful ``statistics`` to include in your request.
        
          * **``ClientTLSNegotiationErrorCount`` ** - The number of TLS connections initiated by the client that did not establish a session with the load balancer. Possible causes include a mismatch of ciphers or protocols.  ``Statistics`` : The most useful statistic is ``Sum`` . 
           
          * **``HealthyHostCount`` ** - The number of target instances that are considered healthy.  ``Statistics`` : The most useful statistic are ``Average`` , ``Minimum`` , and ``Maximum`` . 
           
          * **``UnhealthyHostCount`` ** - The number of target instances that are considered unhealthy.  ``Statistics`` : The most useful statistic are ``Average`` , ``Minimum`` , and ``Maximum`` . 
           
          * **``HTTPCode_LB_4XX_Count`` ** - The number of HTTP 4XX client error codes that originate from the load balancer. Client errors are generated when requests are malformed or incomplete. These requests have not been received by the target instance. This count does not include any response codes generated by the target instances.  ``Statistics`` : The most useful statistic is ``Sum`` . Note that ``Minimum`` , ``Maximum`` , and ``Average`` all return ``1`` . 
           
          * **``HTTPCode_LB_5XX_Count`` ** - The number of HTTP 5XX server error codes that originate from the load balancer. This count does not include any response codes generated by the target instances.  ``Statistics`` : The most useful statistic is ``Sum`` . Note that ``Minimum`` , ``Maximum`` , and ``Average`` all return ``1`` . Note that ``Minimum`` , ``Maximum`` , and ``Average`` all return ``1`` . 
           
          * **``HTTPCode_Instance_2XX_Count`` ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.  ``Statistics`` : The most useful statistic is ``Sum`` . Note that ``Minimum`` , ``Maximum`` , and ``Average`` all return ``1`` . 
           
          * **``HTTPCode_Instance_3XX_Count`` ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.   ``Statistics`` : The most useful statistic is ``Sum`` . Note that ``Minimum`` , ``Maximum`` , and ``Average`` all return ``1`` . 
           
          * **``HTTPCode_Instance_4XX_Count`` ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.  ``Statistics`` : The most useful statistic is ``Sum`` . Note that ``Minimum`` , ``Maximum`` , and ``Average`` all return ``1`` . 
           
          * **``HTTPCode_Instance_5XX_Count`` ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.  ``Statistics`` : The most useful statistic is ``Sum`` . Note that ``Minimum`` , ``Maximum`` , and ``Average`` all return ``1`` . 
           
          * **``InstanceResponseTime`` ** - The time elapsed, in seconds, after the request leaves the load balancer until a response from the target instance is received.  ``Statistics`` : The most useful statistic is ``Average`` . 
           
          * **``RejectedConnectionCount`` ** - The number of connections that were rejected because the load balancer had reached its maximum number of connections.  ``Statistics`` : The most useful statistic is ``Sum`` . 
           
          * **``RequestCount`` ** - The number of requests processed over IPv4. This count includes only the requests with a response generated by a target instance of the load balancer.  ``Statistics`` : The most useful statistic is ``Sum`` . Note that ``Minimum`` , ``Maximum`` , and ``Average`` all return ``1`` . 
           
        :type period: integer
        :param period: **[REQUIRED]** 
        
          The granularity, in seconds, of the returned data points.
        
        :type startTime: datetime
        :param startTime: **[REQUIRED]** 
        
          The start time of the period.
        
        :type endTime: datetime
        :param endTime: **[REQUIRED]** 
        
          The end time of the period.
        
        :type unit: string
        :param unit: **[REQUIRED]** 
        
          The unit for the time period request. Valid values are listed below.
        
        :type statistics: list
        :param statistics: **[REQUIRED]** 
        
          An array of statistics that you want to request metrics for. Valid values are listed below.
        
          * **``SampleCount`` ** - The count (number) of data points used for the statistical calculation. 
           
          * **``Average`` ** - The value of Sum / SampleCount during the specified period. By comparing this statistic with the Minimum and Maximum, you can determine the full scope of a metric and how close the average use is to the Minimum and Maximum. This comparison helps you to know when to increase or decrease your resources as needed. 
           
          * **``Sum`` ** - All values submitted for the matching metric added together. This statistic can be useful for determining the total volume of a metric. 
           
          * **``Minimum`` ** - The lowest value observed during the specified period. You can use this value to determine low volumes of activity for your application. 
           
          * **``Maximum`` ** - The highest value observed during the specified period. You can use this value to determine high volumes of activity for your application. 
           
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'metricName\': \'ClientTLSNegotiationErrorCount\'|\'HealthyHostCount\'|\'UnhealthyHostCount\'|\'HTTPCode_LB_4XX_Count\'|\'HTTPCode_LB_5XX_Count\'|\'HTTPCode_Instance_2XX_Count\'|\'HTTPCode_Instance_3XX_Count\'|\'HTTPCode_Instance_4XX_Count\'|\'HTTPCode_Instance_5XX_Count\'|\'InstanceResponseTime\'|\'RejectedConnectionCount\'|\'RequestCount\',
                \'metricData\': [
                    {
                        \'average\': 123.0,
                        \'maximum\': 123.0,
                        \'minimum\': 123.0,
                        \'sampleCount\': 123.0,
                        \'sum\': 123.0,
                        \'timestamp\': datetime(2015, 1, 1),
                        \'unit\': \'Seconds\'|\'Microseconds\'|\'Milliseconds\'|\'Bytes\'|\'Kilobytes\'|\'Megabytes\'|\'Gigabytes\'|\'Terabytes\'|\'Bits\'|\'Kilobits\'|\'Megabits\'|\'Gigabits\'|\'Terabits\'|\'Percent\'|\'Count\'|\'Bytes/Second\'|\'Kilobytes/Second\'|\'Megabytes/Second\'|\'Gigabytes/Second\'|\'Terabytes/Second\'|\'Bits/Second\'|\'Kilobits/Second\'|\'Megabits/Second\'|\'Gigabits/Second\'|\'Terabits/Second\'|\'Count/Second\'|\'None\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **metricName** *(string) --* 
        
              The metric about which you are receiving information. Valid values are listed below, along with the most useful ``statistics`` to include in your request.
        
              * **``ClientTLSNegotiationErrorCount`` ** - The number of TLS connections initiated by the client that did not establish a session with the load balancer. Possible causes include a mismatch of ciphers or protocols.  ``Statistics`` : The most useful statistic is ``Sum`` . 
               
              * **``HealthyHostCount`` ** - The number of target instances that are considered healthy.  ``Statistics`` : The most useful statistic are ``Average`` , ``Minimum`` , and ``Maximum`` . 
               
              * **``UnhealthyHostCount`` ** - The number of target instances that are considered unhealthy.  ``Statistics`` : The most useful statistic are ``Average`` , ``Minimum`` , and ``Maximum`` . 
               
              * **``HTTPCode_LB_4XX_Count`` ** - The number of HTTP 4XX client error codes that originate from the load balancer. Client errors are generated when requests are malformed or incomplete. These requests have not been received by the target instance. This count does not include any response codes generated by the target instances.  ``Statistics`` : The most useful statistic is ``Sum`` . Note that ``Minimum`` , ``Maximum`` , and ``Average`` all return ``1`` . 
               
              * **``HTTPCode_LB_5XX_Count`` ** - The number of HTTP 5XX server error codes that originate from the load balancer. This count does not include any response codes generated by the target instances.  ``Statistics`` : The most useful statistic is ``Sum`` . Note that ``Minimum`` , ``Maximum`` , and ``Average`` all return ``1`` . Note that ``Minimum`` , ``Maximum`` , and ``Average`` all return ``1`` . 
               
              * **``HTTPCode_Instance_2XX_Count`` ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.  ``Statistics`` : The most useful statistic is ``Sum`` . Note that ``Minimum`` , ``Maximum`` , and ``Average`` all return ``1`` . 
               
              * **``HTTPCode_Instance_3XX_Count`` ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.   ``Statistics`` : The most useful statistic is ``Sum`` . Note that ``Minimum`` , ``Maximum`` , and ``Average`` all return ``1`` . 
               
              * **``HTTPCode_Instance_4XX_Count`` ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.  ``Statistics`` : The most useful statistic is ``Sum`` . Note that ``Minimum`` , ``Maximum`` , and ``Average`` all return ``1`` . 
               
              * **``HTTPCode_Instance_5XX_Count`` ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.  ``Statistics`` : The most useful statistic is ``Sum`` . Note that ``Minimum`` , ``Maximum`` , and ``Average`` all return ``1`` . 
               
              * **``InstanceResponseTime`` ** - The time elapsed, in seconds, after the request leaves the load balancer until a response from the target instance is received.  ``Statistics`` : The most useful statistic is ``Average`` . 
               
              * **``RejectedConnectionCount`` ** - The number of connections that were rejected because the load balancer had reached its maximum number of connections.  ``Statistics`` : The most useful statistic is ``Sum`` . 
               
              * **``RequestCount`` ** - The number of requests processed over IPv4. This count includes only the requests with a response generated by a target instance of the load balancer.  ``Statistics`` : The most useful statistic is ``Sum`` . Note that ``Minimum`` , ``Maximum`` , and ``Average`` all return ``1`` . 
               
            - **metricData** *(list) --* 
        
              An array of metric datapoint objects.
        
              - *(dict) --* 
        
                Describes the metric data point.
        
                - **average** *(float) --* 
        
                  The average.
        
                - **maximum** *(float) --* 
        
                  The maximum.
        
                - **minimum** *(float) --* 
        
                  The minimum.
        
                - **sampleCount** *(float) --* 
        
                  The sample count.
        
                - **sum** *(float) --* 
        
                  The sum.
        
                - **timestamp** *(datetime) --* 
        
                  The timestamp (e.g., ``1479816991.349`` ).
        
                - **unit** *(string) --* 
        
                  The unit. 
        
        """
        pass

    def get_load_balancer_tls_certificates(self, loadBalancerName: str) -> Dict:
        """
        
        TLS is just an updated, more secure version of Secure Socket Layer (SSL).
        
        You can have a maximum of 2 certificates associated with a Lightsail load balancer. One is active and the other is inactive.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetLoadBalancerTlsCertificates>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_load_balancer_tls_certificates(
              loadBalancerName=\'string\'
          )
        :type loadBalancerName: string
        :param loadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer you associated with your SSL/TLS certificate.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'tlsCertificates\': [
                    {
                        \'name\': \'string\',
                        \'arn\': \'string\',
                        \'supportCode\': \'string\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'loadBalancerName\': \'string\',
                        \'isAttached\': True|False,
                        \'status\': \'PENDING_VALIDATION\'|\'ISSUED\'|\'INACTIVE\'|\'EXPIRED\'|\'VALIDATION_TIMED_OUT\'|\'REVOKED\'|\'FAILED\'|\'UNKNOWN\',
                        \'domainName\': \'string\',
                        \'domainValidationRecords\': [
                            {
                                \'name\': \'string\',
                                \'type\': \'string\',
                                \'value\': \'string\',
                                \'validationStatus\': \'PENDING_VALIDATION\'|\'FAILED\'|\'SUCCESS\',
                                \'domainName\': \'string\'
                            },
                        ],
                        \'failureReason\': \'NO_AVAILABLE_CONTACTS\'|\'ADDITIONAL_VERIFICATION_REQUIRED\'|\'DOMAIN_NOT_ALLOWED\'|\'INVALID_PUBLIC_DOMAIN\'|\'OTHER\',
                        \'issuedAt\': datetime(2015, 1, 1),
                        \'issuer\': \'string\',
                        \'keyAlgorithm\': \'string\',
                        \'notAfter\': datetime(2015, 1, 1),
                        \'notBefore\': datetime(2015, 1, 1),
                        \'renewalSummary\': {
                            \'renewalStatus\': \'PENDING_AUTO_RENEWAL\'|\'PENDING_VALIDATION\'|\'SUCCESS\'|\'FAILED\',
                            \'domainValidationOptions\': [
                                {
                                    \'domainName\': \'string\',
                                    \'validationStatus\': \'PENDING_VALIDATION\'|\'FAILED\'|\'SUCCESS\'
                                },
                            ]
                        },
                        \'revocationReason\': \'UNSPECIFIED\'|\'KEY_COMPROMISE\'|\'CA_COMPROMISE\'|\'AFFILIATION_CHANGED\'|\'SUPERCEDED\'|\'CESSATION_OF_OPERATION\'|\'CERTIFICATE_HOLD\'|\'REMOVE_FROM_CRL\'|\'PRIVILEGE_WITHDRAWN\'|\'A_A_COMPROMISE\',
                        \'revokedAt\': datetime(2015, 1, 1),
                        \'serial\': \'string\',
                        \'signatureAlgorithm\': \'string\',
                        \'subject\': \'string\',
                        \'subjectAlternativeNames\': [
                            \'string\',
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **tlsCertificates** *(list) --* 
        
              An array of LoadBalancerTlsCertificate objects describing your SSL/TLS certificates.
        
              - *(dict) --* 
        
                Describes a load balancer SSL/TLS certificate.
        
                TLS is just an updated, more secure version of Secure Socket Layer (SSL).
        
                - **name** *(string) --* 
        
                  The name of the SSL/TLS certificate (e.g., ``my-certificate`` ).
        
                - **arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the SSL/TLS certificate.
        
                - **supportCode** *(string) --* 
        
                  The support code. Include this code in your email to support when you have questions about your Lightsail load balancer or SSL/TLS certificate. This code enables our support team to look up your Lightsail information more easily.
        
                - **createdAt** *(datetime) --* 
        
                  The time when you created your SSL/TLS certificate.
        
                - **location** *(dict) --* 
        
                  The AWS Region and Availability Zone where you created your certificate.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **resourceType** *(string) --* 
        
                  The resource type (e.g., ``LoadBalancerTlsCertificate`` ).
        
                  * **``Instance`` ** - A Lightsail instance (a virtual private server) 
                   
                  * **``StaticIp`` ** - A static IP address 
                   
                  * **``KeyPair`` ** - The key pair used to connect to a Lightsail instance 
                   
                  * **``InstanceSnapshot`` ** - A Lightsail instance snapshot 
                   
                  * **``Domain`` ** - A DNS zone 
                   
                  * **``PeeredVpc`` ** - A peered VPC 
                   
                  * **``LoadBalancer`` ** - A Lightsail load balancer 
                   
                  * **``LoadBalancerTlsCertificate`` ** - An SSL/TLS certificate associated with a Lightsail load balancer 
                   
                  * **``Disk`` ** - A Lightsail block storage disk 
                   
                  * **``DiskSnapshot`` ** - A block storage disk snapshot 
                   
                - **loadBalancerName** *(string) --* 
        
                  The load balancer name where your SSL/TLS certificate is attached.
        
                - **isAttached** *(boolean) --* 
        
                  When ``true`` , the SSL/TLS certificate is attached to the Lightsail load balancer.
        
                - **status** *(string) --* 
        
                  The status of the SSL/TLS certificate. Valid values are below.
        
                - **domainName** *(string) --* 
        
                  The domain name for your SSL/TLS certificate.
        
                - **domainValidationRecords** *(list) --* 
        
                  An array of LoadBalancerTlsCertificateDomainValidationRecord objects describing the records.
        
                  - *(dict) --* 
        
                    Describes the validation record of each domain name in the SSL/TLS certificate.
        
                    - **name** *(string) --* 
        
                      A fully qualified domain name in the certificate. For example, ``example.com`` .
        
                    - **type** *(string) --* 
        
                      The type of validation record. For example, ``CNAME`` for domain validation.
        
                    - **value** *(string) --* 
        
                      The value for that type.
        
                    - **validationStatus** *(string) --* 
        
                      The validation status. Valid values are listed below.
        
                    - **domainName** *(string) --* 
        
                      The domain name against which your SSL/TLS certificate was validated.
        
                - **failureReason** *(string) --* 
        
                  The reason for the SSL/TLS certificate validation failure.
        
                - **issuedAt** *(datetime) --* 
        
                  The time when the SSL/TLS certificate was issued.
        
                - **issuer** *(string) --* 
        
                  The issuer of the certificate.
        
                - **keyAlgorithm** *(string) --* 
        
                  The algorithm that was used to generate the key pair (the public and private key).
        
                - **notAfter** *(datetime) --* 
        
                  The timestamp when the SSL/TLS certificate expires.
        
                - **notBefore** *(datetime) --* 
        
                  The timestamp when the SSL/TLS certificate is first valid.
        
                - **renewalSummary** *(dict) --* 
        
                  An object containing information about the status of Lightsail\'s managed renewal for the certificate.
        
                  - **renewalStatus** *(string) --* 
        
                    The status of Lightsail\'s managed renewal of the certificate. Valid values are listed below.
        
                  - **domainValidationOptions** *(list) --* 
        
                    Contains information about the validation of each domain name in the certificate, as it pertains to Lightsail\'s managed renewal. This is different from the initial validation that occurs as a result of the RequestCertificate request.
        
                    - *(dict) --* 
        
                      Contains information about the domain names on an SSL/TLS certificate that you will use to validate domain ownership.
        
                      - **domainName** *(string) --* 
        
                        The fully qualified domain name in the certificate request.
        
                      - **validationStatus** *(string) --* 
        
                        The status of the domain validation. Valid values are listed below.
        
                - **revocationReason** *(string) --* 
        
                  The reason the certificate was revoked. Valid values are below.
        
                - **revokedAt** *(datetime) --* 
        
                  The timestamp when the SSL/TLS certificate was revoked.
        
                - **serial** *(string) --* 
        
                  The serial number of the certificate.
        
                - **signatureAlgorithm** *(string) --* 
        
                  The algorithm that was used to sign the certificate.
        
                - **subject** *(string) --* 
        
                  The name of the entity that is associated with the public key contained in the certificate.
        
                - **subjectAlternativeNames** *(list) --* 
        
                  One or more domains or subdomains included in the certificate. This list contains the domain names that are bound to the public key that is contained in the certificate. The subject alternative names include the canonical domain name (CNAME) of the certificate and additional domain names that can be used to connect to the website, such as ``example.com`` , ``www.example.com`` , or ``m.example.com`` .
        
                  - *(string) --* 
              
        """
        pass

    def get_load_balancers(self, pageToken: str = None) -> Dict:
        """
        
        If you are describing a long list of load balancers, you can paginate the output to make the list more manageable. You can use the pageToken and nextPageToken values to retrieve the next items in the list.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetLoadBalancers>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_load_balancers(
              pageToken=\'string\'
          )
        :type pageToken: string
        :param pageToken: 
        
          A token used for paginating the results from your GetLoadBalancers request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'loadBalancers\': [
                    {
                        \'name\': \'string\',
                        \'arn\': \'string\',
                        \'supportCode\': \'string\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'dnsName\': \'string\',
                        \'state\': \'active\'|\'provisioning\'|\'active_impaired\'|\'failed\'|\'unknown\',
                        \'protocol\': \'HTTP_HTTPS\'|\'HTTP\',
                        \'publicPorts\': [
                            123,
                        ],
                        \'healthCheckPath\': \'string\',
                        \'instancePort\': 123,
                        \'instanceHealthSummary\': [
                            {
                                \'instanceName\': \'string\',
                                \'instanceHealth\': \'initial\'|\'healthy\'|\'unhealthy\'|\'unused\'|\'draining\'|\'unavailable\',
                                \'instanceHealthReason\': \'Lb.RegistrationInProgress\'|\'Lb.InitialHealthChecking\'|\'Lb.InternalError\'|\'Instance.ResponseCodeMismatch\'|\'Instance.Timeout\'|\'Instance.FailedHealthChecks\'|\'Instance.NotRegistered\'|\'Instance.NotInUse\'|\'Instance.DeregistrationInProgress\'|\'Instance.InvalidState\'|\'Instance.IpUnusable\'
                            },
                        ],
                        \'tlsCertificateSummaries\': [
                            {
                                \'name\': \'string\',
                                \'isAttached\': True|False
                            },
                        ],
                        \'configurationOptions\': {
                            \'string\': \'string\'
                        }
                    },
                ],
                \'nextPageToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **loadBalancers** *(list) --* 
        
              An array of LoadBalancer objects describing your load balancers.
        
              - *(dict) --* 
        
                Describes the Lightsail load balancer.
        
                - **name** *(string) --* 
        
                  The name of the load balancer (e.g., ``my-load-balancer`` ).
        
                - **arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the load balancer.
        
                - **supportCode** *(string) --* 
        
                  The support code. Include this code in your email to support when you have questions about your Lightsail load balancer. This code enables our support team to look up your Lightsail information more easily.
        
                - **createdAt** *(datetime) --* 
        
                  The date when your load balancer was created.
        
                - **location** *(dict) --* 
        
                  The AWS Region where your load balancer was created (e.g., ``us-east-2a`` ). Lightsail automatically creates your load balancer across Availability Zones.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **resourceType** *(string) --* 
        
                  The resource type (e.g., ``LoadBalancer`` .
        
                - **dnsName** *(string) --* 
        
                  The DNS name of your Lightsail load balancer.
        
                - **state** *(string) --* 
        
                  The status of your load balancer. Valid values are below.
        
                - **protocol** *(string) --* 
        
                  The protocol you have enabled for your load balancer. Valid values are below.
        
                  You can\'t just have ``HTTP_HTTPS`` , but you can have just ``HTTP`` .
        
                - **publicPorts** *(list) --* 
        
                  An array of public port settings for your load balancer. For HTTP, use port 80. For HTTPS, use port 443.
        
                  - *(integer) --* 
              
                - **healthCheckPath** *(string) --* 
        
                  The path you specified to perform your health checks. If no path is specified, the load balancer tries to make a request to the default (root) page.
        
                - **instancePort** *(integer) --* 
        
                  The port where the load balancer will direct traffic to your Lightsail instances. For HTTP traffic, it\'s port 80. For HTTPS traffic, it\'s port 443.
        
                - **instanceHealthSummary** *(list) --* 
        
                  An array of InstanceHealthSummary objects describing the health of the load balancer.
        
                  - *(dict) --* 
        
                    Describes information about the health of the instance.
        
                    - **instanceName** *(string) --* 
        
                      The name of the Lightsail instance for which you are requesting health check data.
        
                    - **instanceHealth** *(string) --* 
        
                      Describes the overall instance health. Valid values are below.
        
                    - **instanceHealthReason** *(string) --* 
        
                      More information about the instance health. If the ``instanceHealth`` is ``healthy`` , then an ``instanceHealthReason`` value is not provided.
        
                      If ** ``instanceHealth`` ** is ``initial`` , the ** ``instanceHealthReason`` ** value can be one of the following:
        
                      * **``Lb.RegistrationInProgress`` ** - The target instance is in the process of being registered with the load balancer. 
                       
                      * **``Lb.InitialHealthChecking`` ** - The Lightsail load balancer is still sending the target instance the minimum number of health checks required to determine its health status. 
                       
                      If ** ``instanceHealth`` ** is ``unhealthy`` , the ** ``instanceHealthReason`` ** value can be one of the following:
        
                      * **``Instance.ResponseCodeMismatch`` ** - The health checks did not return an expected HTTP code. 
                       
                      * **``Instance.Timeout`` ** - The health check requests timed out. 
                       
                      * **``Instance.FailedHealthChecks`` ** - The health checks failed because the connection to the target instance timed out, the target instance response was malformed, or the target instance failed the health check for an unknown reason. 
                       
                      * **``Lb.InternalError`` ** - The health checks failed due to an internal error. 
                       
                      If ** ``instanceHealth`` ** is ``unused`` , the ** ``instanceHealthReason`` ** value can be one of the following:
        
                      * **``Instance.NotRegistered`` ** - The target instance is not registered with the target group. 
                       
                      * **``Instance.NotInUse`` ** - The target group is not used by any load balancer, or the target instance is in an Availability Zone that is not enabled for its load balancer. 
                       
                      * **``Instance.IpUnusable`` ** - The target IP address is reserved for use by a Lightsail load balancer. 
                       
                      * **``Instance.InvalidState`` ** - The target is in the stopped or terminated state. 
                       
                      If ** ``instanceHealth`` ** is ``draining`` , the ** ``instanceHealthReason`` ** value can be one of the following:
        
                      * **``Instance.DeregistrationInProgress`` ** - The target instance is in the process of being deregistered and the deregistration delay period has not expired. 
                       
                - **tlsCertificateSummaries** *(list) --* 
        
                  An array of LoadBalancerTlsCertificateSummary objects that provide additional information about the SSL/TLS certificates. For example, if ``true`` , the certificate is attached to the load balancer.
        
                  - *(dict) --* 
        
                    Provides a summary of SSL/TLS certificate metadata.
        
                    - **name** *(string) --* 
        
                      The name of the SSL/TLS certificate.
        
                    - **isAttached** *(boolean) --* 
        
                      When ``true`` , the SSL/TLS certificate is attached to the Lightsail load balancer.
        
                - **configurationOptions** *(dict) --* 
        
                  A string to string map of the configuration options for your load balancer. Valid values are listed below.
        
                  - *(string) --* 
                    
                    - *(string) --* 
              
            - **nextPageToken** *(string) --* 
        
              A token used for advancing to the next page of results from your GetLoadBalancers request.
        
        """
        pass

    def get_operation(self, operationId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetOperation>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_operation(
              operationId=\'string\'
          )
        :type operationId: string
        :param operationId: **[REQUIRED]** 
        
          A GUID used to identify the operation.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operation\': {
                    \'id\': \'string\',
                    \'resourceName\': \'string\',
                    \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                    \'createdAt\': datetime(2015, 1, 1),
                    \'location\': {
                        \'availabilityZone\': \'string\',
                        \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                    },
                    \'isTerminal\': True|False,
                    \'operationDetails\': \'string\',
                    \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                    \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                    \'statusChangedAt\': datetime(2015, 1, 1),
                    \'errorCode\': \'string\',
                    \'errorDetails\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operation** *(dict) --* 
        
              An array of key-value pairs containing information about the results of your get operation request.
        
              - **id** *(string) --* 
        
                The ID of the operation.
        
              - **resourceName** *(string) --* 
        
                The resource name.
        
              - **resourceType** *(string) --* 
        
                The resource type. 
        
              - **createdAt** *(datetime) --* 
        
                The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
              - **location** *(dict) --* 
        
                The region and Availability Zone.
        
                - **availabilityZone** *(string) --* 
        
                  The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                - **regionName** *(string) --* 
        
                  The AWS Region name.
        
              - **isTerminal** *(boolean) --* 
        
                A Boolean value indicating whether the operation is terminal.
        
              - **operationDetails** *(string) --* 
        
                Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
              - **operationType** *(string) --* 
        
                The type of operation. 
        
              - **status** *(string) --* 
        
                The status of the operation. 
        
              - **statusChangedAt** *(datetime) --* 
        
                The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
              - **errorCode** *(string) --* 
        
                The error code.
        
              - **errorDetails** *(string) --* 
        
                The error details.
        
        """
        pass

    def get_operations(self, pageToken: str = None) -> Dict:
        """
        
        Results are returned from oldest to newest, up to a maximum of 200. Results can be paged by making each subsequent call to ``GetOperations`` use the maximum (last) ``statusChangedAt`` value from the previous request.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetOperations>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_operations(
              pageToken=\'string\'
          )
        :type pageToken: string
        :param pageToken: 
        
          A token used for advancing to the next page of results from your get operations request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ],
                \'nextPageToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An array of key-value pairs containing information about the results of your get operations request.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
            - **nextPageToken** *(string) --* 
        
              A token used for advancing to the next page of results from your get operations request.
        
        """
        pass

    def get_operations_for_resource(self, resourceName: str, pageToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetOperationsForResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_operations_for_resource(
              resourceName=\'string\',
              pageToken=\'string\'
          )
        :type resourceName: string
        :param resourceName: **[REQUIRED]** 
        
          The name of the resource for which you are requesting information.
        
        :type pageToken: string
        :param pageToken: 
        
          A token used for advancing to the next page of results from your get operations for resource request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ],
                \'nextPageCount\': \'string\',
                \'nextPageToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An array of key-value pairs containing information about the results of your get operations for resource request.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
            - **nextPageCount** *(string) --* 
        
              (Deprecated) Returns the number of pages of results that remain.
        
              .. note::
        
                In releases prior to June 12, 2017, this parameter returned ``null`` by the API. It is now deprecated, and the API returns the ``next page token`` parameter instead.
        
            - **nextPageToken** *(string) --* 
        
              An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        
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

    def get_regions(self, includeAvailabilityZones: bool = None, includeRelationalDatabaseAvailabilityZones: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetRegions>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_regions(
              includeAvailabilityZones=True|False,
              includeRelationalDatabaseAvailabilityZones=True|False
          )
        :type includeAvailabilityZones: boolean
        :param includeAvailabilityZones: 
        
          A Boolean value indicating whether to also include Availability Zones in your get regions request. Availability Zones are indicated with a letter: e.g., ``us-east-2a`` .
        
        :type includeRelationalDatabaseAvailabilityZones: boolean
        :param includeRelationalDatabaseAvailabilityZones: 
        
          >A Boolean value indicating whether to also include Availability Zones for databases in your get regions request. Availability Zones are indicated with a letter (e.g., ``us-east-2a`` ).
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'regions\': [
                    {
                        \'continentCode\': \'string\',
                        \'description\': \'string\',
                        \'displayName\': \'string\',
                        \'name\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\',
                        \'availabilityZones\': [
                            {
                                \'zoneName\': \'string\',
                                \'state\': \'string\'
                            },
                        ],
                        \'relationalDatabaseAvailabilityZones\': [
                            {
                                \'zoneName\': \'string\',
                                \'state\': \'string\'
                            },
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **regions** *(list) --* 
        
              An array of key-value pairs containing information about your get regions request.
        
              - *(dict) --* 
        
                Describes the AWS Region.
        
                - **continentCode** *(string) --* 
        
                  The continent code (e.g., ``NA`` , meaning North America).
        
                - **description** *(string) --* 
        
                  The description of the AWS Region (e.g., ``This region is recommended to serve users in the eastern United States and eastern Canada`` ).
        
                - **displayName** *(string) --* 
        
                  The display name (e.g., ``Ohio`` ).
        
                - **name** *(string) --* 
        
                  The region name (e.g., ``us-east-2`` ).
        
                - **availabilityZones** *(list) --* 
        
                  The Availability Zones. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - *(dict) --* 
        
                    Describes an Availability Zone.
        
                    - **zoneName** *(string) --* 
        
                      The name of the Availability Zone. The format is ``us-east-2a`` (case-sensitive).
        
                    - **state** *(string) --* 
        
                      The state of the Availability Zone.
        
                - **relationalDatabaseAvailabilityZones** *(list) --* 
        
                  The Availability Zones for databases. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - *(dict) --* 
        
                    Describes an Availability Zone.
        
                    - **zoneName** *(string) --* 
        
                      The name of the Availability Zone. The format is ``us-east-2a`` (case-sensitive).
        
                    - **state** *(string) --* 
        
                      The state of the Availability Zone.
        
        """
        pass

    def get_relational_database(self, relationalDatabaseName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetRelationalDatabase>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_relational_database(
              relationalDatabaseName=\'string\'
          )
        :type relationalDatabaseName: string
        :param relationalDatabaseName: **[REQUIRED]** 
        
          The name of the database that you are looking up.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'relationalDatabase\': {
                    \'name\': \'string\',
                    \'arn\': \'string\',
                    \'supportCode\': \'string\',
                    \'createdAt\': datetime(2015, 1, 1),
                    \'location\': {
                        \'availabilityZone\': \'string\',
                        \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                    },
                    \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                    \'relationalDatabaseBlueprintId\': \'string\',
                    \'relationalDatabaseBundleId\': \'string\',
                    \'masterDatabaseName\': \'string\',
                    \'hardware\': {
                        \'cpuCount\': 123,
                        \'diskSizeInGb\': 123,
                        \'ramSizeInGb\': ...
                    },
                    \'state\': \'string\',
                    \'secondaryAvailabilityZone\': \'string\',
                    \'backupRetentionEnabled\': True|False,
                    \'pendingModifiedValues\': {
                        \'masterUserPassword\': \'string\',
                        \'engineVersion\': \'string\',
                        \'backupRetentionEnabled\': True|False
                    },
                    \'engine\': \'string\',
                    \'engineVersion\': \'string\',
                    \'latestRestorableTime\': datetime(2015, 1, 1),
                    \'masterUsername\': \'string\',
                    \'parameterApplyStatus\': \'string\',
                    \'preferredBackupWindow\': \'string\',
                    \'preferredMaintenanceWindow\': \'string\',
                    \'publiclyAccessible\': True|False,
                    \'masterEndpoint\': {
                        \'port\': 123,
                        \'address\': \'string\'
                    },
                    \'pendingMaintenanceActions\': [
                        {
                            \'action\': \'string\',
                            \'description\': \'string\',
                            \'currentApplyDate\': datetime(2015, 1, 1)
                        },
                    ]
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **relationalDatabase** *(dict) --* 
        
              An object describing the specified database.
        
              - **name** *(string) --* 
        
                The unique name of the database resource in Lightsail.
        
              - **arn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the database.
        
              - **supportCode** *(string) --* 
        
                The support code for the database. Include this code in your email to support when you have questions about a database in Lightsail. This code enables our support team to look up your Lightsail information more easily.
        
              - **createdAt** *(datetime) --* 
        
                The timestamp when the database was created. Formatted in Unix time.
        
              - **location** *(dict) --* 
        
                The Region name and Availability Zone where the database is located.
        
                - **availabilityZone** *(string) --* 
        
                  The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                - **regionName** *(string) --* 
        
                  The AWS Region name.
        
              - **resourceType** *(string) --* 
        
                The Lightsail resource type for the database (for example, ``RelationalDatabase`` ).
        
              - **relationalDatabaseBlueprintId** *(string) --* 
        
                The blueprint ID for the database. A blueprint describes the major engine version of a database.
        
              - **relationalDatabaseBundleId** *(string) --* 
        
                The bundle ID for the database. A bundle describes the performance specifications for your database.
        
              - **masterDatabaseName** *(string) --* 
        
                The name of the master database created when the Lightsail database resource is created.
        
              - **hardware** *(dict) --* 
        
                Describes the hardware of the database.
        
                - **cpuCount** *(integer) --* 
        
                  The number of vCPUs for the database.
        
                - **diskSizeInGb** *(integer) --* 
        
                  The size of the disk for the database.
        
                - **ramSizeInGb** *(float) --* 
        
                  The amount of RAM in GB for the database.
        
              - **state** *(string) --* 
        
                Describes the current state of the database.
        
              - **secondaryAvailabilityZone** *(string) --* 
        
                Describes the secondary Availability Zone of a high availability database.
        
                The secondary database is used for failover support of a high availability database.
        
              - **backupRetentionEnabled** *(boolean) --* 
        
                A Boolean value indicating whether automated backup retention is enabled for the database.
        
              - **pendingModifiedValues** *(dict) --* 
        
                Describes pending database value modifications.
        
                - **masterUserPassword** *(string) --* 
        
                  The password for the master user of the database.
        
                - **engineVersion** *(string) --* 
        
                  The database engine version.
        
                - **backupRetentionEnabled** *(boolean) --* 
        
                  A Boolean value indicating whether automated backup retention is enabled.
        
              - **engine** *(string) --* 
        
                The database software (for example, ``MySQL`` ).
        
              - **engineVersion** *(string) --* 
        
                The database engine version (for example, ``5.7.23`` ).
        
              - **latestRestorableTime** *(datetime) --* 
        
                The latest point in time to which the database can be restored. Formatted in Unix time.
        
              - **masterUsername** *(string) --* 
        
                The master user name of the database.
        
              - **parameterApplyStatus** *(string) --* 
        
                The status of parameter updates for the database.
        
              - **preferredBackupWindow** *(string) --* 
        
                The daily time range during which automated backups are created for the database (for example, ``16:00-16:30`` ).
        
              - **preferredMaintenanceWindow** *(string) --* 
        
                The weekly time range during which system maintenance can occur on the database.
        
                In the format ``ddd:hh24:mi-ddd:hh24:mi`` . For example, ``Tue:17:00-Tue:17:30`` .
        
              - **publiclyAccessible** *(boolean) --* 
        
                A Boolean value indicating whether the database is publicly accessible.
        
              - **masterEndpoint** *(dict) --* 
        
                The master endpoint for the database.
        
                - **port** *(integer) --* 
        
                  Specifies the port that the database is listening on.
        
                - **address** *(string) --* 
        
                  Specifies the DNS address of the database.
        
              - **pendingMaintenanceActions** *(list) --* 
        
                Describes the pending maintenance actions for the database.
        
                - *(dict) --* 
        
                  Describes a pending database maintenance action.
        
                  - **action** *(string) --* 
        
                    The type of pending database maintenance action.
        
                  - **description** *(string) --* 
        
                    Additional detail about the pending database maintenance action.
        
                  - **currentApplyDate** *(datetime) --* 
        
                    The effective date of the pending database maintenance action.
        
        """
        pass

    def get_relational_database_blueprints(self, pageToken: str = None) -> Dict:
        """
        
        You can use a blueprint ID to create a new database that runs a specific database engine.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetRelationalDatabaseBlueprints>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_relational_database_blueprints(
              pageToken=\'string\'
          )
        :type pageToken: string
        :param pageToken: 
        
          A token used for advancing to a specific page of results for your get relational database blueprints request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'blueprints\': [
                    {
                        \'blueprintId\': \'string\',
                        \'engine\': \'mysql\',
                        \'engineVersion\': \'string\',
                        \'engineDescription\': \'string\',
                        \'engineVersionDescription\': \'string\',
                        \'isEngineDefault\': True|False
                    },
                ],
                \'nextPageToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **blueprints** *(list) --* 
        
              An object describing the result of your get relational database blueprints request.
        
              - *(dict) --* 
        
                Describes a database image, or blueprint. A blueprint describes the major engine version of a database.
        
                - **blueprintId** *(string) --* 
        
                  The ID for the database blueprint.
        
                - **engine** *(string) --* 
        
                  The database software of the database blueprint (for example, ``MySQL`` ).
        
                - **engineVersion** *(string) --* 
        
                  The database engine version for the database blueprint (for example, ``5.7.23`` ).
        
                - **engineDescription** *(string) --* 
        
                  The description of the database engine for the database blueprint.
        
                - **engineVersionDescription** *(string) --* 
        
                  The description of the database engine version for the database blueprint.
        
                - **isEngineDefault** *(boolean) --* 
        
                  A Boolean value indicating whether the engine version is the default for the database blueprint.
        
            - **nextPageToken** *(string) --* 
        
              A token used for advancing to the next page of results of your get relational database blueprints request.
        
        """
        pass

    def get_relational_database_bundles(self, pageToken: str = None) -> Dict:
        """
        
        You can use a bundle ID to create a new database with explicit performance specifications.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetRelationalDatabaseBundles>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_relational_database_bundles(
              pageToken=\'string\'
          )
        :type pageToken: string
        :param pageToken: 
        
          A token used for advancing to a specific page of results for your get relational database bundles request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'bundles\': [
                    {
                        \'bundleId\': \'string\',
                        \'name\': \'string\',
                        \'price\': ...,
                        \'ramSizeInGb\': ...,
                        \'diskSizeInGb\': 123,
                        \'transferPerMonthInGb\': 123,
                        \'cpuCount\': 123,
                        \'isEncrypted\': True|False,
                        \'isActive\': True|False
                    },
                ],
                \'nextPageToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **bundles** *(list) --* 
        
              An object describing the result of your get relational database bundles request.
        
              - *(dict) --* 
        
                Describes a database bundle. A bundle describes the performance specifications of the database.
        
                - **bundleId** *(string) --* 
        
                  The ID for the database bundle.
        
                - **name** *(string) --* 
        
                  The name for the database bundle.
        
                - **price** *(float) --* 
        
                  The cost of the database bundle in US currency.
        
                - **ramSizeInGb** *(float) --* 
        
                  The amount of RAM in GB (for example, ``2.0`` ) for the database bundle.
        
                - **diskSizeInGb** *(integer) --* 
        
                  The size of the disk for the database bundle.
        
                - **transferPerMonthInGb** *(integer) --* 
        
                  The data transfer rate per month in GB for the database bundle.
        
                - **cpuCount** *(integer) --* 
        
                  The number of virtual CPUs (vCPUs) for the database bundle.
        
                - **isEncrypted** *(boolean) --* 
        
                  A Boolean value indicating whether the database bundle is encrypted.
        
                - **isActive** *(boolean) --* 
        
                  A Boolean value indicating whether the database bundle is active.
        
            - **nextPageToken** *(string) --* 
        
              A token used for advancing to the next page of results of your get relational database bundles request.
        
        """
        pass

    def get_relational_database_events(self, relationalDatabaseName: str, durationInMinutes: int = None, pageToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetRelationalDatabaseEvents>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_relational_database_events(
              relationalDatabaseName=\'string\',
              durationInMinutes=123,
              pageToken=\'string\'
          )
        :type relationalDatabaseName: string
        :param relationalDatabaseName: **[REQUIRED]** 
        
          The name of the database from which to get events.
        
        :type durationInMinutes: integer
        :param durationInMinutes: 
        
          The number of minutes in the past from which to retrieve events. For example, to get all events from the past 2 hours, enter 120.
        
          Default: ``60``  
        
          The minimum is 1 and the maximum is 14 days (20160 minutes).
        
        :type pageToken: string
        :param pageToken: 
        
          A token used for advancing to a specific page of results from for get relational database events request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'relationalDatabaseEvents\': [
                    {
                        \'resource\': \'string\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'message\': \'string\',
                        \'eventCategories\': [
                            \'string\',
                        ]
                    },
                ],
                \'nextPageToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **relationalDatabaseEvents** *(list) --* 
        
              An object describing the result of your get relational database events request.
        
              - *(dict) --* 
        
                Describes an event for a database.
        
                - **resource** *(string) --* 
        
                  The database that the database event relates to.
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the database event was created.
        
                - **message** *(string) --* 
        
                  The message of the database event.
        
                - **eventCategories** *(list) --* 
        
                  The category that the database event belongs to.
        
                  - *(string) --* 
              
            - **nextPageToken** *(string) --* 
        
              A token used for advancing to the next page of results from your get relational database events request.
        
        """
        pass

    def get_relational_database_log_events(self, relationalDatabaseName: str, logStreamName: str, startTime: datetime = None, endTime: datetime = None, startFromHead: bool = None, pageToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetRelationalDatabaseLogEvents>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_relational_database_log_events(
              relationalDatabaseName=\'string\',
              logStreamName=\'string\',
              startTime=datetime(2015, 1, 1),
              endTime=datetime(2015, 1, 1),
              startFromHead=True|False,
              pageToken=\'string\'
          )
        :type relationalDatabaseName: string
        :param relationalDatabaseName: **[REQUIRED]** 
        
          The name of your database for which to get log events.
        
        :type logStreamName: string
        :param logStreamName: **[REQUIRED]** 
        
          The name of the log stream.
        
          Use the ``get relational database log streams`` operation to get a list of available log streams.
        
        :type startTime: datetime
        :param startTime: 
        
          The start of the time interval from which to get log events.
        
          Constraints:
        
          * Specified in Universal Coordinated Time (UTC). 
           
          * Specified in the Unix time format. For example, if you wish to use a start time of October 1, 2018, at 8 PM UTC, then you input ``1538424000`` as the start time. 
           
        :type endTime: datetime
        :param endTime: 
        
          The end of the time interval from which to get log events.
        
          Constraints:
        
          * Specified in Universal Coordinated Time (UTC). 
           
          * Specified in the Unix time format. For example, if you wish to use an end time of October 1, 2018, at 8 PM UTC, then you input ``1538424000`` as the end time. 
           
        :type startFromHead: boolean
        :param startFromHead: 
        
          Parameter to specify if the log should start from head or tail. If ``true`` is specified, the log event starts from the head of the log. If ``false`` is specified, the log event starts from the tail of the log.
        
          Default: ``false``  
        
        :type pageToken: string
        :param pageToken: 
        
          A token used for advancing to a specific page of results for your get relational database log events request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'resourceLogEvents\': [
                    {
                        \'createdAt\': datetime(2015, 1, 1),
                        \'message\': \'string\'
                    },
                ],
                \'nextBackwardToken\': \'string\',
                \'nextForwardToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **resourceLogEvents** *(list) --* 
        
              An object describing the result of your get relational database log events request.
        
              - *(dict) --* 
        
                Describes a database log event.
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the database log event was created.
        
                - **message** *(string) --* 
        
                  The message of the database log event.
        
            - **nextBackwardToken** *(string) --* 
        
              A token used for advancing to the previous page of results from your get relational database log events request.
        
            - **nextForwardToken** *(string) --* 
        
              A token used for advancing to the next page of results from your get relational database log events request.
        
        """
        pass

    def get_relational_database_log_streams(self, relationalDatabaseName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetRelationalDatabaseLogStreams>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_relational_database_log_streams(
              relationalDatabaseName=\'string\'
          )
        :type relationalDatabaseName: string
        :param relationalDatabaseName: **[REQUIRED]** 
        
          The name of your database for which to get log streams.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'logStreams\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **logStreams** *(list) --* 
        
              An object describing the result of your get relational database log streams request.
        
              - *(string) --* 
          
        """
        pass

    def get_relational_database_master_user_password(self, relationalDatabaseName: str, passwordVersion: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetRelationalDatabaseMasterUserPassword>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_relational_database_master_user_password(
              relationalDatabaseName=\'string\',
              passwordVersion=\'CURRENT\'|\'PREVIOUS\'|\'PENDING\'
          )
        :type relationalDatabaseName: string
        :param relationalDatabaseName: **[REQUIRED]** 
        
          The name of your database for which to get the master user password.
        
        :type passwordVersion: string
        :param passwordVersion: 
        
          The password version to return.
        
          Specifying ``CURRENT`` or ``PREVIOUS`` returns the current or previous passwords respectively. Specifying ``PENDING`` returns the newest version of the password that will rotate to ``CURRENT`` . After the ``PENDING`` password rotates to ``CURRENT`` , the ``PENDING`` password is no longer available.
        
          Default: ``CURRENT``  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'masterUserPassword\': \'string\',
                \'createdAt\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **masterUserPassword** *(string) --* 
        
              The master user password for the ``password version`` specified.
        
            - **createdAt** *(datetime) --* 
        
              The timestamp when the specified version of the master user password was created.
        
        """
        pass

    def get_relational_database_metric_data(self, relationalDatabaseName: str, metricName: str, period: int, startTime: datetime, endTime: datetime, unit: str, statistics: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetRelationalDatabaseMetricData>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_relational_database_metric_data(
              relationalDatabaseName=\'string\',
              metricName=\'CPUUtilization\'|\'DatabaseConnections\'|\'DiskQueueDepth\'|\'FreeStorageSpace\'|\'NetworkReceiveThroughput\'|\'NetworkTransmitThroughput\',
              period=123,
              startTime=datetime(2015, 1, 1),
              endTime=datetime(2015, 1, 1),
              unit=\'Seconds\'|\'Microseconds\'|\'Milliseconds\'|\'Bytes\'|\'Kilobytes\'|\'Megabytes\'|\'Gigabytes\'|\'Terabytes\'|\'Bits\'|\'Kilobits\'|\'Megabits\'|\'Gigabits\'|\'Terabits\'|\'Percent\'|\'Count\'|\'Bytes/Second\'|\'Kilobytes/Second\'|\'Megabytes/Second\'|\'Gigabytes/Second\'|\'Terabytes/Second\'|\'Bits/Second\'|\'Kilobits/Second\'|\'Megabits/Second\'|\'Gigabits/Second\'|\'Terabits/Second\'|\'Count/Second\'|\'None\',
              statistics=[
                  \'Minimum\'|\'Maximum\'|\'Sum\'|\'Average\'|\'SampleCount\',
              ]
          )
        :type relationalDatabaseName: string
        :param relationalDatabaseName: **[REQUIRED]** 
        
          The name of your database from which to get metric data.
        
        :type metricName: string
        :param metricName: **[REQUIRED]** 
        
          The name of the metric data to return.
        
        :type period: integer
        :param period: **[REQUIRED]** 
        
          The granularity, in seconds, of the returned data points.
        
        :type startTime: datetime
        :param startTime: **[REQUIRED]** 
        
          The start of the time interval from which to get metric data.
        
          Constraints:
        
          * Specified in Universal Coordinated Time (UTC). 
           
          * Specified in the Unix time format. For example, if you wish to use a start time of October 1, 2018, at 8 PM UTC, then you input ``1538424000`` as the start time. 
           
        :type endTime: datetime
        :param endTime: **[REQUIRED]** 
        
          The end of the time interval from which to get metric data.
        
          Constraints:
        
          * Specified in Universal Coordinated Time (UTC). 
           
          * Specified in the Unix time format. For example, if you wish to use an end time of October 1, 2018, at 8 PM UTC, then you input ``1538424000`` as the end time. 
           
        :type unit: string
        :param unit: **[REQUIRED]** 
        
          The unit for the metric data request.
        
        :type statistics: list
        :param statistics: **[REQUIRED]** 
        
          The array of statistics for your metric data request.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'metricName\': \'CPUUtilization\'|\'DatabaseConnections\'|\'DiskQueueDepth\'|\'FreeStorageSpace\'|\'NetworkReceiveThroughput\'|\'NetworkTransmitThroughput\',
                \'metricData\': [
                    {
                        \'average\': 123.0,
                        \'maximum\': 123.0,
                        \'minimum\': 123.0,
                        \'sampleCount\': 123.0,
                        \'sum\': 123.0,
                        \'timestamp\': datetime(2015, 1, 1),
                        \'unit\': \'Seconds\'|\'Microseconds\'|\'Milliseconds\'|\'Bytes\'|\'Kilobytes\'|\'Megabytes\'|\'Gigabytes\'|\'Terabytes\'|\'Bits\'|\'Kilobits\'|\'Megabits\'|\'Gigabits\'|\'Terabits\'|\'Percent\'|\'Count\'|\'Bytes/Second\'|\'Kilobytes/Second\'|\'Megabytes/Second\'|\'Gigabytes/Second\'|\'Terabytes/Second\'|\'Bits/Second\'|\'Kilobits/Second\'|\'Megabits/Second\'|\'Gigabits/Second\'|\'Terabits/Second\'|\'Count/Second\'|\'None\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **metricName** *(string) --* 
        
              The name of the metric.
        
            - **metricData** *(list) --* 
        
              An object describing the result of your get relational database metric data request.
        
              - *(dict) --* 
        
                Describes the metric data point.
        
                - **average** *(float) --* 
        
                  The average.
        
                - **maximum** *(float) --* 
        
                  The maximum.
        
                - **minimum** *(float) --* 
        
                  The minimum.
        
                - **sampleCount** *(float) --* 
        
                  The sample count.
        
                - **sum** *(float) --* 
        
                  The sum.
        
                - **timestamp** *(datetime) --* 
        
                  The timestamp (e.g., ``1479816991.349`` ).
        
                - **unit** *(string) --* 
        
                  The unit. 
        
        """
        pass

    def get_relational_database_parameters(self, relationalDatabaseName: str, pageToken: str = None) -> Dict:
        """
        
        In addition to the parameter names and values, this operation returns other information about each parameter. This information includes whether changes require a reboot, whether the parameter is modifiable, the allowed values, and the data types.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetRelationalDatabaseParameters>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_relational_database_parameters(
              relationalDatabaseName=\'string\',
              pageToken=\'string\'
          )
        :type relationalDatabaseName: string
        :param relationalDatabaseName: **[REQUIRED]** 
        
          The name of your database for which to get parameters.
        
        :type pageToken: string
        :param pageToken: 
        
          A token used for advancing to a specific page of results for your get relational database parameters request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'parameters\': [
                    {
                        \'allowedValues\': \'string\',
                        \'applyMethod\': \'string\',
                        \'applyType\': \'string\',
                        \'dataType\': \'string\',
                        \'description\': \'string\',
                        \'isModifiable\': True|False,
                        \'parameterName\': \'string\',
                        \'parameterValue\': \'string\'
                    },
                ],
                \'nextPageToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **parameters** *(list) --* 
        
              An object describing the result of your get relational database parameters request.
        
              - *(dict) --* 
        
                Describes the parameters of a database.
        
                - **allowedValues** *(string) --* 
        
                  Specifies the valid range of values for the parameter.
        
                - **applyMethod** *(string) --* 
        
                  Indicates when parameter updates are applied.
        
                  Can be ``immediate`` or ``pending-reboot`` .
        
                - **applyType** *(string) --* 
        
                  Specifies the engine-specific parameter type.
        
                - **dataType** *(string) --* 
        
                  Specifies the valid data type for the parameter.
        
                - **description** *(string) --* 
        
                  Provides a description of the parameter.
        
                - **isModifiable** *(boolean) --* 
        
                  A Boolean value indicating whether the parameter can be modified.
        
                - **parameterName** *(string) --* 
        
                  Specifies the name of the parameter.
        
                - **parameterValue** *(string) --* 
        
                  Specifies the value of the parameter.
        
            - **nextPageToken** *(string) --* 
        
              A token used for advancing to the next page of results from your get static IPs request.
        
        """
        pass

    def get_relational_database_snapshot(self, relationalDatabaseSnapshotName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetRelationalDatabaseSnapshot>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_relational_database_snapshot(
              relationalDatabaseSnapshotName=\'string\'
          )
        :type relationalDatabaseSnapshotName: string
        :param relationalDatabaseSnapshotName: **[REQUIRED]** 
        
          The name of the database snapshot for which to get information.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'relationalDatabaseSnapshot\': {
                    \'name\': \'string\',
                    \'arn\': \'string\',
                    \'supportCode\': \'string\',
                    \'createdAt\': datetime(2015, 1, 1),
                    \'location\': {
                        \'availabilityZone\': \'string\',
                        \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                    },
                    \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                    \'engine\': \'string\',
                    \'engineVersion\': \'string\',
                    \'sizeInGb\': 123,
                    \'state\': \'string\',
                    \'fromRelationalDatabaseName\': \'string\',
                    \'fromRelationalDatabaseArn\': \'string\',
                    \'fromRelationalDatabaseBundleId\': \'string\',
                    \'fromRelationalDatabaseBlueprintId\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **relationalDatabaseSnapshot** *(dict) --* 
        
              An object describing the specified database snapshot.
        
              - **name** *(string) --* 
        
                The name of the database snapshot.
        
              - **arn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the database snapshot.
        
              - **supportCode** *(string) --* 
        
                The support code for the database snapshot. Include this code in your email to support when you have questions about a database snapshot in Lightsail. This code enables our support team to look up your Lightsail information more easily.
        
              - **createdAt** *(datetime) --* 
        
                The timestamp when the database snapshot was created.
        
              - **location** *(dict) --* 
        
                The Region name and Availability Zone where the database snapshot is located.
        
                - **availabilityZone** *(string) --* 
        
                  The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                - **regionName** *(string) --* 
        
                  The AWS Region name.
        
              - **resourceType** *(string) --* 
        
                The Lightsail resource type.
        
              - **engine** *(string) --* 
        
                The software of the database snapshot (for example, ``MySQL`` )
        
              - **engineVersion** *(string) --* 
        
                The database engine version for the database snapshot (for example, ``5.7.23`` ).
        
              - **sizeInGb** *(integer) --* 
        
                The size of the disk in GB (for example, ``32`` ) for the database snapshot.
        
              - **state** *(string) --* 
        
                The state of the database snapshot.
        
              - **fromRelationalDatabaseName** *(string) --* 
        
                The name of the source database from which the database snapshot was created.
        
              - **fromRelationalDatabaseArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the database from which the database snapshot was created.
        
              - **fromRelationalDatabaseBundleId** *(string) --* 
        
                The bundle ID of the database from which the database snapshot was created.
        
              - **fromRelationalDatabaseBlueprintId** *(string) --* 
        
                The blueprint ID of the database from which the database snapshot was created. A blueprint describes the major engine version of a database.
        
        """
        pass

    def get_relational_database_snapshots(self, pageToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetRelationalDatabaseSnapshots>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_relational_database_snapshots(
              pageToken=\'string\'
          )
        :type pageToken: string
        :param pageToken: 
        
          A token used for advancing to a specific page of results for your get relational database snapshots request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'relationalDatabaseSnapshots\': [
                    {
                        \'name\': \'string\',
                        \'arn\': \'string\',
                        \'supportCode\': \'string\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'engine\': \'string\',
                        \'engineVersion\': \'string\',
                        \'sizeInGb\': 123,
                        \'state\': \'string\',
                        \'fromRelationalDatabaseName\': \'string\',
                        \'fromRelationalDatabaseArn\': \'string\',
                        \'fromRelationalDatabaseBundleId\': \'string\',
                        \'fromRelationalDatabaseBlueprintId\': \'string\'
                    },
                ],
                \'nextPageToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **relationalDatabaseSnapshots** *(list) --* 
        
              An object describing the result of your get relational database snapshots request.
        
              - *(dict) --* 
        
                Describes a database snapshot.
        
                - **name** *(string) --* 
        
                  The name of the database snapshot.
        
                - **arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the database snapshot.
        
                - **supportCode** *(string) --* 
        
                  The support code for the database snapshot. Include this code in your email to support when you have questions about a database snapshot in Lightsail. This code enables our support team to look up your Lightsail information more easily.
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the database snapshot was created.
        
                - **location** *(dict) --* 
        
                  The Region name and Availability Zone where the database snapshot is located.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **resourceType** *(string) --* 
        
                  The Lightsail resource type.
        
                - **engine** *(string) --* 
        
                  The software of the database snapshot (for example, ``MySQL`` )
        
                - **engineVersion** *(string) --* 
        
                  The database engine version for the database snapshot (for example, ``5.7.23`` ).
        
                - **sizeInGb** *(integer) --* 
        
                  The size of the disk in GB (for example, ``32`` ) for the database snapshot.
        
                - **state** *(string) --* 
        
                  The state of the database snapshot.
        
                - **fromRelationalDatabaseName** *(string) --* 
        
                  The name of the source database from which the database snapshot was created.
        
                - **fromRelationalDatabaseArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the database from which the database snapshot was created.
        
                - **fromRelationalDatabaseBundleId** *(string) --* 
        
                  The bundle ID of the database from which the database snapshot was created.
        
                - **fromRelationalDatabaseBlueprintId** *(string) --* 
        
                  The blueprint ID of the database from which the database snapshot was created. A blueprint describes the major engine version of a database.
        
            - **nextPageToken** *(string) --* 
        
              A token used for advancing to the next page of results from your get relational database snapshots request.
        
        """
        pass

    def get_relational_databases(self, pageToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetRelationalDatabases>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_relational_databases(
              pageToken=\'string\'
          )
        :type pageToken: string
        :param pageToken: 
        
          A token used for advancing to a specific page of results for your get relational database request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'relationalDatabases\': [
                    {
                        \'name\': \'string\',
                        \'arn\': \'string\',
                        \'supportCode\': \'string\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'relationalDatabaseBlueprintId\': \'string\',
                        \'relationalDatabaseBundleId\': \'string\',
                        \'masterDatabaseName\': \'string\',
                        \'hardware\': {
                            \'cpuCount\': 123,
                            \'diskSizeInGb\': 123,
                            \'ramSizeInGb\': ...
                        },
                        \'state\': \'string\',
                        \'secondaryAvailabilityZone\': \'string\',
                        \'backupRetentionEnabled\': True|False,
                        \'pendingModifiedValues\': {
                            \'masterUserPassword\': \'string\',
                            \'engineVersion\': \'string\',
                            \'backupRetentionEnabled\': True|False
                        },
                        \'engine\': \'string\',
                        \'engineVersion\': \'string\',
                        \'latestRestorableTime\': datetime(2015, 1, 1),
                        \'masterUsername\': \'string\',
                        \'parameterApplyStatus\': \'string\',
                        \'preferredBackupWindow\': \'string\',
                        \'preferredMaintenanceWindow\': \'string\',
                        \'publiclyAccessible\': True|False,
                        \'masterEndpoint\': {
                            \'port\': 123,
                            \'address\': \'string\'
                        },
                        \'pendingMaintenanceActions\': [
                            {
                                \'action\': \'string\',
                                \'description\': \'string\',
                                \'currentApplyDate\': datetime(2015, 1, 1)
                            },
                        ]
                    },
                ],
                \'nextPageToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **relationalDatabases** *(list) --* 
        
              An object describing the result of your get relational databases request.
        
              - *(dict) --* 
        
                Describes a database.
        
                - **name** *(string) --* 
        
                  The unique name of the database resource in Lightsail.
        
                - **arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the database.
        
                - **supportCode** *(string) --* 
        
                  The support code for the database. Include this code in your email to support when you have questions about a database in Lightsail. This code enables our support team to look up your Lightsail information more easily.
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the database was created. Formatted in Unix time.
        
                - **location** *(dict) --* 
        
                  The Region name and Availability Zone where the database is located.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **resourceType** *(string) --* 
        
                  The Lightsail resource type for the database (for example, ``RelationalDatabase`` ).
        
                - **relationalDatabaseBlueprintId** *(string) --* 
        
                  The blueprint ID for the database. A blueprint describes the major engine version of a database.
        
                - **relationalDatabaseBundleId** *(string) --* 
        
                  The bundle ID for the database. A bundle describes the performance specifications for your database.
        
                - **masterDatabaseName** *(string) --* 
        
                  The name of the master database created when the Lightsail database resource is created.
        
                - **hardware** *(dict) --* 
        
                  Describes the hardware of the database.
        
                  - **cpuCount** *(integer) --* 
        
                    The number of vCPUs for the database.
        
                  - **diskSizeInGb** *(integer) --* 
        
                    The size of the disk for the database.
        
                  - **ramSizeInGb** *(float) --* 
        
                    The amount of RAM in GB for the database.
        
                - **state** *(string) --* 
        
                  Describes the current state of the database.
        
                - **secondaryAvailabilityZone** *(string) --* 
        
                  Describes the secondary Availability Zone of a high availability database.
        
                  The secondary database is used for failover support of a high availability database.
        
                - **backupRetentionEnabled** *(boolean) --* 
        
                  A Boolean value indicating whether automated backup retention is enabled for the database.
        
                - **pendingModifiedValues** *(dict) --* 
        
                  Describes pending database value modifications.
        
                  - **masterUserPassword** *(string) --* 
        
                    The password for the master user of the database.
        
                  - **engineVersion** *(string) --* 
        
                    The database engine version.
        
                  - **backupRetentionEnabled** *(boolean) --* 
        
                    A Boolean value indicating whether automated backup retention is enabled.
        
                - **engine** *(string) --* 
        
                  The database software (for example, ``MySQL`` ).
        
                - **engineVersion** *(string) --* 
        
                  The database engine version (for example, ``5.7.23`` ).
        
                - **latestRestorableTime** *(datetime) --* 
        
                  The latest point in time to which the database can be restored. Formatted in Unix time.
        
                - **masterUsername** *(string) --* 
        
                  The master user name of the database.
        
                - **parameterApplyStatus** *(string) --* 
        
                  The status of parameter updates for the database.
        
                - **preferredBackupWindow** *(string) --* 
        
                  The daily time range during which automated backups are created for the database (for example, ``16:00-16:30`` ).
        
                - **preferredMaintenanceWindow** *(string) --* 
        
                  The weekly time range during which system maintenance can occur on the database.
        
                  In the format ``ddd:hh24:mi-ddd:hh24:mi`` . For example, ``Tue:17:00-Tue:17:30`` .
        
                - **publiclyAccessible** *(boolean) --* 
        
                  A Boolean value indicating whether the database is publicly accessible.
        
                - **masterEndpoint** *(dict) --* 
        
                  The master endpoint for the database.
        
                  - **port** *(integer) --* 
        
                    Specifies the port that the database is listening on.
        
                  - **address** *(string) --* 
        
                    Specifies the DNS address of the database.
        
                - **pendingMaintenanceActions** *(list) --* 
        
                  Describes the pending maintenance actions for the database.
        
                  - *(dict) --* 
        
                    Describes a pending database maintenance action.
        
                    - **action** *(string) --* 
        
                      The type of pending database maintenance action.
        
                    - **description** *(string) --* 
        
                      Additional detail about the pending database maintenance action.
        
                    - **currentApplyDate** *(datetime) --* 
        
                      The effective date of the pending database maintenance action.
        
            - **nextPageToken** *(string) --* 
        
              A token used for advancing to the next page of results from your get relational databases request.
        
        """
        pass

    def get_static_ip(self, staticIpName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetStaticIp>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_static_ip(
              staticIpName=\'string\'
          )
        :type staticIpName: string
        :param staticIpName: **[REQUIRED]** 
        
          The name of the static IP in Lightsail.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'staticIp\': {
                    \'name\': \'string\',
                    \'arn\': \'string\',
                    \'supportCode\': \'string\',
                    \'createdAt\': datetime(2015, 1, 1),
                    \'location\': {
                        \'availabilityZone\': \'string\',
                        \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                    },
                    \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                    \'ipAddress\': \'string\',
                    \'attachedTo\': \'string\',
                    \'isAttached\': True|False
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **staticIp** *(dict) --* 
        
              An array of key-value pairs containing information about the requested static IP.
        
              - **name** *(string) --* 
        
                The name of the static IP (e.g., ``StaticIP-Ohio-EXAMPLE`` ).
        
              - **arn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the static IP (e.g., ``arn:aws:lightsail:us-east-2:123456789101:StaticIp/9cbb4a9e-f8e3-4dfe-b57e-12345EXAMPLE`` ).
        
              - **supportCode** *(string) --* 
        
                The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
        
              - **createdAt** *(datetime) --* 
        
                The timestamp when the static IP was created (e.g., ``1479735304.222`` ).
        
              - **location** *(dict) --* 
        
                The region and Availability Zone where the static IP was created.
        
                - **availabilityZone** *(string) --* 
        
                  The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                - **regionName** *(string) --* 
        
                  The AWS Region name.
        
              - **resourceType** *(string) --* 
        
                The resource type (usually ``StaticIp`` ).
        
              - **ipAddress** *(string) --* 
        
                The static IP address.
        
              - **attachedTo** *(string) --* 
        
                The instance where the static IP is attached (e.g., ``Amazon_Linux-1GB-Ohio-1`` ).
        
              - **isAttached** *(boolean) --* 
        
                A Boolean value indicating whether the static IP is attached.
        
        """
        pass

    def get_static_ips(self, pageToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetStaticIps>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_static_ips(
              pageToken=\'string\'
          )
        :type pageToken: string
        :param pageToken: 
        
          A token used for advancing to the next page of results from your get static IPs request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'staticIps\': [
                    {
                        \'name\': \'string\',
                        \'arn\': \'string\',
                        \'supportCode\': \'string\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'ipAddress\': \'string\',
                        \'attachedTo\': \'string\',
                        \'isAttached\': True|False
                    },
                ],
                \'nextPageToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **staticIps** *(list) --* 
        
              An array of key-value pairs containing information about your get static IPs request.
        
              - *(dict) --* 
        
                Describes the static IP.
        
                - **name** *(string) --* 
        
                  The name of the static IP (e.g., ``StaticIP-Ohio-EXAMPLE`` ).
        
                - **arn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the static IP (e.g., ``arn:aws:lightsail:us-east-2:123456789101:StaticIp/9cbb4a9e-f8e3-4dfe-b57e-12345EXAMPLE`` ).
        
                - **supportCode** *(string) --* 
        
                  The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the static IP was created (e.g., ``1479735304.222`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone where the static IP was created.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **resourceType** *(string) --* 
        
                  The resource type (usually ``StaticIp`` ).
        
                - **ipAddress** *(string) --* 
        
                  The static IP address.
        
                - **attachedTo** *(string) --* 
        
                  The instance where the static IP is attached (e.g., ``Amazon_Linux-1GB-Ohio-1`` ).
        
                - **isAttached** *(boolean) --* 
        
                  A Boolean value indicating whether the static IP is attached.
        
            - **nextPageToken** *(string) --* 
        
              A token used for advancing to the next page of results from your get static IPs request.
        
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

    def import_key_pair(self, keyPairName: str, publicKeyBase64: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/ImportKeyPair>`_
        
        **Request Syntax** 
        ::
        
          response = client.import_key_pair(
              keyPairName=\'string\',
              publicKeyBase64=\'string\'
          )
        :type keyPairName: string
        :param keyPairName: **[REQUIRED]** 
        
          The name of the key pair for which you want to import the public key.
        
        :type publicKeyBase64: string
        :param publicKeyBase64: **[REQUIRED]** 
        
          A base64-encoded public key of the ``ssh-rsa`` type.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operation\': {
                    \'id\': \'string\',
                    \'resourceName\': \'string\',
                    \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                    \'createdAt\': datetime(2015, 1, 1),
                    \'location\': {
                        \'availabilityZone\': \'string\',
                        \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                    },
                    \'isTerminal\': True|False,
                    \'operationDetails\': \'string\',
                    \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                    \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                    \'statusChangedAt\': datetime(2015, 1, 1),
                    \'errorCode\': \'string\',
                    \'errorDetails\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operation** *(dict) --* 
        
              An array of key-value pairs containing information about the request operation.
        
              - **id** *(string) --* 
        
                The ID of the operation.
        
              - **resourceName** *(string) --* 
        
                The resource name.
        
              - **resourceType** *(string) --* 
        
                The resource type. 
        
              - **createdAt** *(datetime) --* 
        
                The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
              - **location** *(dict) --* 
        
                The region and Availability Zone.
        
                - **availabilityZone** *(string) --* 
        
                  The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                - **regionName** *(string) --* 
        
                  The AWS Region name.
        
              - **isTerminal** *(boolean) --* 
        
                A Boolean value indicating whether the operation is terminal.
        
              - **operationDetails** *(string) --* 
        
                Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
              - **operationType** *(string) --* 
        
                The type of operation. 
        
              - **status** *(string) --* 
        
                The status of the operation. 
        
              - **statusChangedAt** *(datetime) --* 
        
                The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
              - **errorCode** *(string) --* 
        
                The error code.
        
              - **errorDetails** *(string) --* 
        
                The error details.
        
        """
        pass

    def is_vpc_peered(self) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/IsVpcPeered>`_
        
        **Request Syntax** 
        ::
        
          response = client.is_vpc_peered()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'isPeered\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **isPeered** *(boolean) --* 
        
              Returns ``true`` if the Lightsail VPC is peered; otherwise, ``false`` .
        
        """
        pass

    def open_instance_public_ports(self, portInfo: Dict, instanceName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/OpenInstancePublicPorts>`_
        
        **Request Syntax** 
        ::
        
          response = client.open_instance_public_ports(
              portInfo={
                  \'fromPort\': 123,
                  \'toPort\': 123,
                  \'protocol\': \'tcp\'|\'all\'|\'udp\'
              },
              instanceName=\'string\'
          )
        :type portInfo: dict
        :param portInfo: **[REQUIRED]** 
        
          An array of key-value pairs containing information about the port mappings.
        
          - **fromPort** *(integer) --* 
        
            The first port in the range.
        
          - **toPort** *(integer) --* 
        
            The last port in the range.
        
          - **protocol** *(string) --* 
        
            The protocol. 
        
        :type instanceName: string
        :param instanceName: **[REQUIRED]** 
        
          The name of the instance for which you want to open the public ports.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operation\': {
                    \'id\': \'string\',
                    \'resourceName\': \'string\',
                    \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                    \'createdAt\': datetime(2015, 1, 1),
                    \'location\': {
                        \'availabilityZone\': \'string\',
                        \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                    },
                    \'isTerminal\': True|False,
                    \'operationDetails\': \'string\',
                    \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                    \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                    \'statusChangedAt\': datetime(2015, 1, 1),
                    \'errorCode\': \'string\',
                    \'errorDetails\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operation** *(dict) --* 
        
              An array of key-value pairs containing information about the request operation.
        
              - **id** *(string) --* 
        
                The ID of the operation.
        
              - **resourceName** *(string) --* 
        
                The resource name.
        
              - **resourceType** *(string) --* 
        
                The resource type. 
        
              - **createdAt** *(datetime) --* 
        
                The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
              - **location** *(dict) --* 
        
                The region and Availability Zone.
        
                - **availabilityZone** *(string) --* 
        
                  The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                - **regionName** *(string) --* 
        
                  The AWS Region name.
        
              - **isTerminal** *(boolean) --* 
        
                A Boolean value indicating whether the operation is terminal.
        
              - **operationDetails** *(string) --* 
        
                Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
              - **operationType** *(string) --* 
        
                The type of operation. 
        
              - **status** *(string) --* 
        
                The status of the operation. 
        
              - **statusChangedAt** *(datetime) --* 
        
                The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
              - **errorCode** *(string) --* 
        
                The error code.
        
              - **errorDetails** *(string) --* 
        
                The error details.
        
        """
        pass

    def peer_vpc(self) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/PeerVpc>`_
        
        **Request Syntax** 
        ::
        
          response = client.peer_vpc()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operation\': {
                    \'id\': \'string\',
                    \'resourceName\': \'string\',
                    \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                    \'createdAt\': datetime(2015, 1, 1),
                    \'location\': {
                        \'availabilityZone\': \'string\',
                        \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                    },
                    \'isTerminal\': True|False,
                    \'operationDetails\': \'string\',
                    \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                    \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                    \'statusChangedAt\': datetime(2015, 1, 1),
                    \'errorCode\': \'string\',
                    \'errorDetails\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operation** *(dict) --* 
        
              An array of key-value pairs containing information about the request operation.
        
              - **id** *(string) --* 
        
                The ID of the operation.
        
              - **resourceName** *(string) --* 
        
                The resource name.
        
              - **resourceType** *(string) --* 
        
                The resource type. 
        
              - **createdAt** *(datetime) --* 
        
                The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
              - **location** *(dict) --* 
        
                The region and Availability Zone.
        
                - **availabilityZone** *(string) --* 
        
                  The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                - **regionName** *(string) --* 
        
                  The AWS Region name.
        
              - **isTerminal** *(boolean) --* 
        
                A Boolean value indicating whether the operation is terminal.
        
              - **operationDetails** *(string) --* 
        
                Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
              - **operationType** *(string) --* 
        
                The type of operation. 
        
              - **status** *(string) --* 
        
                The status of the operation. 
        
              - **statusChangedAt** *(datetime) --* 
        
                The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
              - **errorCode** *(string) --* 
        
                The error code.
        
              - **errorDetails** *(string) --* 
        
                The error details.
        
        """
        pass

    def put_instance_public_ports(self, portInfos: List, instanceName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/PutInstancePublicPorts>`_
        
        **Request Syntax** 
        ::
        
          response = client.put_instance_public_ports(
              portInfos=[
                  {
                      \'fromPort\': 123,
                      \'toPort\': 123,
                      \'protocol\': \'tcp\'|\'all\'|\'udp\'
                  },
              ],
              instanceName=\'string\'
          )
        :type portInfos: list
        :param portInfos: **[REQUIRED]** 
        
          Specifies information about the public port(s).
        
          - *(dict) --* 
        
            Describes information about the ports on your virtual private server (or *instance* ).
        
            - **fromPort** *(integer) --* 
        
              The first port in the range.
        
            - **toPort** *(integer) --* 
        
              The last port in the range.
        
            - **protocol** *(string) --* 
        
              The protocol. 
        
        :type instanceName: string
        :param instanceName: **[REQUIRED]** 
        
          The Lightsail instance name of the public port(s) you are setting.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operation\': {
                    \'id\': \'string\',
                    \'resourceName\': \'string\',
                    \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                    \'createdAt\': datetime(2015, 1, 1),
                    \'location\': {
                        \'availabilityZone\': \'string\',
                        \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                    },
                    \'isTerminal\': True|False,
                    \'operationDetails\': \'string\',
                    \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                    \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                    \'statusChangedAt\': datetime(2015, 1, 1),
                    \'errorCode\': \'string\',
                    \'errorDetails\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operation** *(dict) --* 
        
              Describes metadata about the operation you just executed.
        
              - **id** *(string) --* 
        
                The ID of the operation.
        
              - **resourceName** *(string) --* 
        
                The resource name.
        
              - **resourceType** *(string) --* 
        
                The resource type. 
        
              - **createdAt** *(datetime) --* 
        
                The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
              - **location** *(dict) --* 
        
                The region and Availability Zone.
        
                - **availabilityZone** *(string) --* 
        
                  The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                - **regionName** *(string) --* 
        
                  The AWS Region name.
        
              - **isTerminal** *(boolean) --* 
        
                A Boolean value indicating whether the operation is terminal.
        
              - **operationDetails** *(string) --* 
        
                Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
              - **operationType** *(string) --* 
        
                The type of operation. 
        
              - **status** *(string) --* 
        
                The status of the operation. 
        
              - **statusChangedAt** *(datetime) --* 
        
                The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
              - **errorCode** *(string) --* 
        
                The error code.
        
              - **errorDetails** *(string) --* 
        
                The error details.
        
        """
        pass

    def reboot_instance(self, instanceName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/RebootInstance>`_
        
        **Request Syntax** 
        ::
        
          response = client.reboot_instance(
              instanceName=\'string\'
          )
        :type instanceName: string
        :param instanceName: **[REQUIRED]** 
        
          The name of the instance to reboot.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An array of key-value pairs containing information about the request operations.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def reboot_relational_database(self, relationalDatabaseName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/RebootRelationalDatabase>`_
        
        **Request Syntax** 
        ::
        
          response = client.reboot_relational_database(
              relationalDatabaseName=\'string\'
          )
        :type relationalDatabaseName: string
        :param relationalDatabaseName: **[REQUIRED]** 
        
          The name of your database to reboot.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An object describing the result of your reboot relational database request.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def release_static_ip(self, staticIpName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/ReleaseStaticIp>`_
        
        **Request Syntax** 
        ::
        
          response = client.release_static_ip(
              staticIpName=\'string\'
          )
        :type staticIpName: string
        :param staticIpName: **[REQUIRED]** 
        
          The name of the static IP to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An array of key-value pairs containing information about the request operation.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def start_instance(self, instanceName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/StartInstance>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_instance(
              instanceName=\'string\'
          )
        :type instanceName: string
        :param instanceName: **[REQUIRED]** 
        
          The name of the instance (a virtual private server) to start.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An array of key-value pairs containing information about the request operation.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def start_relational_database(self, relationalDatabaseName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/StartRelationalDatabase>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_relational_database(
              relationalDatabaseName=\'string\'
          )
        :type relationalDatabaseName: string
        :param relationalDatabaseName: **[REQUIRED]** 
        
          The name of your database to start.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An object describing the result of your start relational database request.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def stop_instance(self, instanceName: str, force: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/StopInstance>`_
        
        **Request Syntax** 
        ::
        
          response = client.stop_instance(
              instanceName=\'string\',
              force=True|False
          )
        :type instanceName: string
        :param instanceName: **[REQUIRED]** 
        
          The name of the instance (a virtual private server) to stop.
        
        :type force: boolean
        :param force: 
        
          When set to ``True`` , forces a Lightsail instance that is stuck in a ``stopping`` state to stop.
        
          .. warning::
        
            Only use the ``force`` parameter if your instance is stuck in the ``stopping`` state. In any other state, your instance should stop normally without adding this parameter to your API request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An array of key-value pairs containing information about the request operation.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def stop_relational_database(self, relationalDatabaseName: str, relationalDatabaseSnapshotName: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/StopRelationalDatabase>`_
        
        **Request Syntax** 
        ::
        
          response = client.stop_relational_database(
              relationalDatabaseName=\'string\',
              relationalDatabaseSnapshotName=\'string\'
          )
        :type relationalDatabaseName: string
        :param relationalDatabaseName: **[REQUIRED]** 
        
          The name of your database to stop.
        
        :type relationalDatabaseSnapshotName: string
        :param relationalDatabaseSnapshotName: 
        
          The name of your new database snapshot to be created before stopping your database.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An object describing the result of your stop relational database request.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def unpeer_vpc(self) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/UnpeerVpc>`_
        
        **Request Syntax** 
        ::
        
          response = client.unpeer_vpc()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operation\': {
                    \'id\': \'string\',
                    \'resourceName\': \'string\',
                    \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                    \'createdAt\': datetime(2015, 1, 1),
                    \'location\': {
                        \'availabilityZone\': \'string\',
                        \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                    },
                    \'isTerminal\': True|False,
                    \'operationDetails\': \'string\',
                    \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                    \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                    \'statusChangedAt\': datetime(2015, 1, 1),
                    \'errorCode\': \'string\',
                    \'errorDetails\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operation** *(dict) --* 
        
              An array of key-value pairs containing information about the request operation.
        
              - **id** *(string) --* 
        
                The ID of the operation.
        
              - **resourceName** *(string) --* 
        
                The resource name.
        
              - **resourceType** *(string) --* 
        
                The resource type. 
        
              - **createdAt** *(datetime) --* 
        
                The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
              - **location** *(dict) --* 
        
                The region and Availability Zone.
        
                - **availabilityZone** *(string) --* 
        
                  The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                - **regionName** *(string) --* 
        
                  The AWS Region name.
        
              - **isTerminal** *(boolean) --* 
        
                A Boolean value indicating whether the operation is terminal.
        
              - **operationDetails** *(string) --* 
        
                Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
              - **operationType** *(string) --* 
        
                The type of operation. 
        
              - **status** *(string) --* 
        
                The status of the operation. 
        
              - **statusChangedAt** *(datetime) --* 
        
                The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
              - **errorCode** *(string) --* 
        
                The error code.
        
              - **errorDetails** *(string) --* 
        
                The error details.
        
        """
        pass

    def update_domain_entry(self, domainName: str, domainEntry: Dict) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/UpdateDomainEntry>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_domain_entry(
              domainName=\'string\',
              domainEntry={
                  \'id\': \'string\',
                  \'name\': \'string\',
                  \'target\': \'string\',
                  \'isAlias\': True|False,
                  \'type\': \'string\',
                  \'options\': {
                      \'string\': \'string\'
                  }
              }
          )
        :type domainName: string
        :param domainName: **[REQUIRED]** 
        
          The name of the domain recordset to update.
        
        :type domainEntry: dict
        :param domainEntry: **[REQUIRED]** 
        
          An array of key-value pairs containing information about the domain entry.
        
          - **id** *(string) --* 
        
            The ID of the domain recordset entry.
        
          - **name** *(string) --* 
        
            The name of the domain.
        
          - **target** *(string) --* 
        
            The target AWS name server (e.g., ``ns-111.awsdns-22.com.`` ).
        
            For Lightsail load balancers, the value looks like ``ab1234c56789c6b86aba6fb203d443bc-123456789.us-east-2.elb.amazonaws.com`` . Be sure to also set ``isAlias`` to ``true`` when setting up an A record for a load balancer.
        
          - **isAlias** *(boolean) --* 
        
            When ``true`` , specifies whether the domain entry is an alias used by the Lightsail load balancer. You can include an alias (A type) record in your request, which points to a load balancer DNS name and routes traffic to your load balancer
        
          - **type** *(string) --* 
        
            The type of domain entry (e.g., ``SOA`` or ``NS`` ).
        
          - **options** *(dict) --* 
        
            (Deprecated) The options for the domain entry.
        
            .. note::
        
              In releases prior to November 29, 2017, this parameter was not included in the API response. It is now deprecated.
        
            - *(string) --* 
        
              - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An array of key-value pairs containing information about the request operation.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def update_load_balancer_attribute(self, loadBalancerName: str, attributeName: str, attributeValue: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/UpdateLoadBalancerAttribute>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_load_balancer_attribute(
              loadBalancerName=\'string\',
              attributeName=\'HealthCheckPath\'|\'SessionStickinessEnabled\'|\'SessionStickiness_LB_CookieDurationSeconds\',
              attributeValue=\'string\'
          )
        :type loadBalancerName: string
        :param loadBalancerName: **[REQUIRED]** 
        
          The name of the load balancer that you want to modify (e.g., ``my-load-balancer`` .
        
        :type attributeName: string
        :param attributeName: **[REQUIRED]** 
        
          The name of the attribute you want to update. Valid values are below.
        
        :type attributeValue: string
        :param attributeValue: **[REQUIRED]** 
        
          The value that you want to specify for the attribute name.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An object describing the API operations.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def update_relational_database(self, relationalDatabaseName: str, masterUserPassword: str = None, rotateMasterUserPassword: bool = None, preferredBackupWindow: str = None, preferredMaintenanceWindow: str = None, enableBackupRetention: bool = None, disableBackupRetention: bool = None, publiclyAccessible: bool = None, applyImmediately: bool = None) -> Dict:
        """
        
        Updates are applied immediately, or in cases where the updates could result in an outage, are applied during the database\'s predefined maintenance window.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/UpdateRelationalDatabase>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_relational_database(
              relationalDatabaseName=\'string\',
              masterUserPassword=\'string\',
              rotateMasterUserPassword=True|False,
              preferredBackupWindow=\'string\',
              preferredMaintenanceWindow=\'string\',
              enableBackupRetention=True|False,
              disableBackupRetention=True|False,
              publiclyAccessible=True|False,
              applyImmediately=True|False
          )
        :type relationalDatabaseName: string
        :param relationalDatabaseName: **[REQUIRED]** 
        
          The name of your database to update.
        
        :type masterUserPassword: string
        :param masterUserPassword: 
        
          The password for the master user of your database. The password can include any printable ASCII character except \"/\", \"\"\", or \"@\".
        
          Constraints: Must contain 8 to 41 characters.
        
        :type rotateMasterUserPassword: boolean
        :param rotateMasterUserPassword: 
        
          When ``true`` , the master user password is changed to a new strong password generated by Lightsail.
        
          Use the ``get relational database master user password`` operation to get the new password.
        
        :type preferredBackupWindow: string
        :param preferredBackupWindow: 
        
          The daily time range during which automated backups are created for your database if automated backups are enabled.
        
          Constraints:
        
          * Must be in the ``hh24:mi-hh24:mi`` format. Example: ``16:00-16:30``   
           
          * Specified in Universal Coordinated Time (UTC). 
           
          * Must not conflict with the preferred maintenance window. 
           
          * Must be at least 30 minutes. 
           
        :type preferredMaintenanceWindow: string
        :param preferredMaintenanceWindow: 
        
          The weekly time range during which system maintenance can occur on your database.
        
          The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.
        
          Constraints:
        
          * Must be in the ``ddd:hh24:mi-ddd:hh24:mi`` format. 
           
          * Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun. 
           
          * Must be at least 30 minutes. 
           
          * Specified in Universal Coordinated Time (UTC). 
           
          * Example: ``Tue:17:00-Tue:17:30``   
           
        :type enableBackupRetention: boolean
        :param enableBackupRetention: 
        
          When ``true`` , enables automated backup retention for your database.
        
          Updates are applied during the next maintenance window because this can result in an outage.
        
        :type disableBackupRetention: boolean
        :param disableBackupRetention: 
        
          When ``true`` , disables automated backup retention for your database.
        
          Disabling backup retention deletes all automated database backups. Before disabling this, you may want to create a snapshot of your database using the ``create relational database snapshot`` operation.
        
          Updates are applied during the next maintenance window because this can result in an outage.
        
        :type publiclyAccessible: boolean
        :param publiclyAccessible: 
        
          Specifies the accessibility options for your database. A value of ``true`` specifies a database that is available to resources outside of your Lightsail account. A value of ``false`` specifies a database that is available only to your Lightsail resources in the same region as your database.
        
        :type applyImmediately: boolean
        :param applyImmediately: 
        
          When ``true`` , applies changes immediately. When ``false`` , applies changes during the preferred maintenance window. Some changes may cause an outage.
        
          Default: ``false``  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An object describing the result of your update relational database request.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass

    def update_relational_database_parameters(self, relationalDatabaseName: str, parameters: List) -> Dict:
        """
        
        Parameter updates don\'t cause outages; therefore, their application is not subject to the preferred maintenance window. However, there are two ways in which paramater updates are applied: ``dynamic`` or ``pending-reboot`` . Parameters marked with a ``dynamic`` apply type are applied immediately. Parameters marked with a ``pending-reboot`` apply type are applied only after the database is rebooted using the ``reboot relational database`` operation.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/UpdateRelationalDatabaseParameters>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_relational_database_parameters(
              relationalDatabaseName=\'string\',
              parameters=[
                  {
                      \'allowedValues\': \'string\',
                      \'applyMethod\': \'string\',
                      \'applyType\': \'string\',
                      \'dataType\': \'string\',
                      \'description\': \'string\',
                      \'isModifiable\': True|False,
                      \'parameterName\': \'string\',
                      \'parameterValue\': \'string\'
                  },
              ]
          )
        :type relationalDatabaseName: string
        :param relationalDatabaseName: **[REQUIRED]** 
        
          The name of your database for which to update parameters.
        
        :type parameters: list
        :param parameters: **[REQUIRED]** 
        
          The database parameters to update.
        
          - *(dict) --* 
        
            Describes the parameters of a database.
        
            - **allowedValues** *(string) --* 
        
              Specifies the valid range of values for the parameter.
        
            - **applyMethod** *(string) --* 
        
              Indicates when parameter updates are applied.
        
              Can be ``immediate`` or ``pending-reboot`` .
        
            - **applyType** *(string) --* 
        
              Specifies the engine-specific parameter type.
        
            - **dataType** *(string) --* 
        
              Specifies the valid data type for the parameter.
        
            - **description** *(string) --* 
        
              Provides a description of the parameter.
        
            - **isModifiable** *(boolean) --* 
        
              A Boolean value indicating whether the parameter can be modified.
        
            - **parameterName** *(string) --* 
        
              Specifies the name of the parameter.
        
            - **parameterValue** *(string) --* 
        
              Specifies the value of the parameter.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'operations\': [
                    {
                        \'id\': \'string\',
                        \'resourceName\': \'string\',
                        \'resourceType\': \'Instance\'|\'StaticIp\'|\'KeyPair\'|\'InstanceSnapshot\'|\'Domain\'|\'PeeredVpc\'|\'LoadBalancer\'|\'LoadBalancerTlsCertificate\'|\'Disk\'|\'DiskSnapshot\'|\'RelationalDatabase\'|\'RelationalDatabaseSnapshot\',
                        \'createdAt\': datetime(2015, 1, 1),
                        \'location\': {
                            \'availabilityZone\': \'string\',
                            \'regionName\': \'us-east-1\'|\'us-east-2\'|\'us-west-1\'|\'us-west-2\'|\'eu-west-1\'|\'eu-west-2\'|\'eu-west-3\'|\'eu-central-1\'|\'ca-central-1\'|\'ap-south-1\'|\'ap-southeast-1\'|\'ap-southeast-2\'|\'ap-northeast-1\'|\'ap-northeast-2\'
                        },
                        \'isTerminal\': True|False,
                        \'operationDetails\': \'string\',
                        \'operationType\': \'DeleteInstance\'|\'CreateInstance\'|\'StopInstance\'|\'StartInstance\'|\'RebootInstance\'|\'OpenInstancePublicPorts\'|\'PutInstancePublicPorts\'|\'CloseInstancePublicPorts\'|\'AllocateStaticIp\'|\'ReleaseStaticIp\'|\'AttachStaticIp\'|\'DetachStaticIp\'|\'UpdateDomainEntry\'|\'DeleteDomainEntry\'|\'CreateDomain\'|\'DeleteDomain\'|\'CreateInstanceSnapshot\'|\'DeleteInstanceSnapshot\'|\'CreateInstancesFromSnapshot\'|\'CreateLoadBalancer\'|\'DeleteLoadBalancer\'|\'AttachInstancesToLoadBalancer\'|\'DetachInstancesFromLoadBalancer\'|\'UpdateLoadBalancerAttribute\'|\'CreateLoadBalancerTlsCertificate\'|\'DeleteLoadBalancerTlsCertificate\'|\'AttachLoadBalancerTlsCertificate\'|\'CreateDisk\'|\'DeleteDisk\'|\'AttachDisk\'|\'DetachDisk\'|\'CreateDiskSnapshot\'|\'DeleteDiskSnapshot\'|\'CreateDiskFromSnapshot\',
                        \'status\': \'NotStarted\'|\'Started\'|\'Failed\'|\'Completed\'|\'Succeeded\',
                        \'statusChangedAt\': datetime(2015, 1, 1),
                        \'errorCode\': \'string\',
                        \'errorDetails\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **operations** *(list) --* 
        
              An object describing the result of your update relational database parameters request.
        
              - *(dict) --* 
        
                Describes the API operation.
        
                - **id** *(string) --* 
        
                  The ID of the operation.
        
                - **resourceName** *(string) --* 
        
                  The resource name.
        
                - **resourceType** *(string) --* 
        
                  The resource type. 
        
                - **createdAt** *(datetime) --* 
        
                  The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).
        
                - **location** *(dict) --* 
        
                  The region and Availability Zone.
        
                  - **availabilityZone** *(string) --* 
        
                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).
        
                  - **regionName** *(string) --* 
        
                    The AWS Region name.
        
                - **isTerminal** *(boolean) --* 
        
                  A Boolean value indicating whether the operation is terminal.
        
                - **operationDetails** *(string) --* 
        
                  Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).
        
                - **operationType** *(string) --* 
        
                  The type of operation. 
        
                - **status** *(string) --* 
        
                  The status of the operation. 
        
                - **statusChangedAt** *(datetime) --* 
        
                  The timestamp when the status was changed (e.g., ``1479816991.349`` ).
        
                - **errorCode** *(string) --* 
        
                  The error code.
        
                - **errorDetails** *(string) --* 
        
                  The error details.
        
        """
        pass
