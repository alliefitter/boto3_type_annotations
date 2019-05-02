from typing import Optional
from botocore.client import BaseClient
from botocore.waiter import Waiter
from typing import Union
from typing import Dict
from botocore.paginate import Paginator


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

    def create_cluster(self, name: str, roleArn: str, resourcesVpcConfig: Dict, version: str = None, logging: Dict = None, clientRequestToken: str = None) -> Dict:
        """
        Creates an Amazon EKS control plane. 
        The Amazon EKS control plane consists of control plane instances that run the Kubernetes software, like ``etcd`` and the API server. The control plane runs in an account managed by AWS, and the Kubernetes API is exposed via the Amazon EKS API server endpoint. Each Amazon EKS cluster control plane is single-tenant and unique, and runs on its own set of Amazon EC2 instances.
        The cluster control plane is provisioned across multiple Availability Zones and fronted by an Elastic Load Balancing Network Load Balancer. Amazon EKS also provisions elastic network interfaces in your VPC subnets to provide connectivity from the control plane instances to the worker nodes (for example, to support ``kubectl exec`` , ``logs`` , and ``proxy`` data flows).
        Amazon EKS worker nodes run in your AWS account and connect to your cluster's control plane via the Kubernetes API server endpoint and a certificate file that is created for your cluster.
        You can use the ``endpointPublicAccess`` and ``endpointPrivateAccess`` parameters to enable or disable public and private access to your cluster's Kubernetes API server endpoint. By default, public access is enabled and private access is disabled. For more information, see `Amazon EKS Cluster Endpoint Access Control <https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html>`__ in the * *Amazon EKS User Guide* * . 
        You can use the ``logging`` parameter to enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch Logs. By default, cluster control plane logs are not exported to CloudWatch Logs. For more information, see `Amazon EKS Cluster Control Plane Logs <https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html>`__ in the * *Amazon EKS User Guide* * .
        .. note::
          CloudWatch Logs ingestion, archive storage, and data scanning rates apply to exported control plane logs. For more information, see `Amazon CloudWatch Pricing <http://aws.amazon.com/cloudwatch/pricing/>`__ .
        Cluster creation typically takes between 10 and 15 minutes. After you create an Amazon EKS cluster, you must configure your Kubernetes tooling to communicate with the API server and launch worker nodes into your cluster. For more information, see `Managing Cluster Authentication <https://docs.aws.amazon.com/eks/latest/userguide/managing-auth.html>`__ and `Launching Amazon EKS Worker Nodes <https://docs.aws.amazon.com/eks/latest/userguide/launch-workers.html>`__ in the *Amazon EKS User Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/CreateCluster>`_
        
        **Request Syntax**
        ::
          response = client.create_cluster(
              name='string',
              version='string',
              roleArn='string',
              resourcesVpcConfig={
                  'subnetIds': [
                      'string',
                  ],
                  'securityGroupIds': [
                      'string',
                  ],
                  'endpointPublicAccess': True|False,
                  'endpointPrivateAccess': True|False
              },
              logging={
                  'clusterLogging': [
                      {
                          'types': [
                              'api'|'audit'|'authenticator'|'controllerManager'|'scheduler',
                          ],
                          'enabled': True|False
                      },
                  ]
              },
              clientRequestToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'cluster': {
                    'name': 'string',
                    'arn': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'version': 'string',
                    'endpoint': 'string',
                    'roleArn': 'string',
                    'resourcesVpcConfig': {
                        'subnetIds': [
                            'string',
                        ],
                        'securityGroupIds': [
                            'string',
                        ],
                        'vpcId': 'string',
                        'endpointPublicAccess': True|False,
                        'endpointPrivateAccess': True|False
                    },
                    'logging': {
                        'clusterLogging': [
                            {
                                'types': [
                                    'api'|'audit'|'authenticator'|'controllerManager'|'scheduler',
                                ],
                                'enabled': True|False
                            },
                        ]
                    },
                    'status': 'CREATING'|'ACTIVE'|'DELETING'|'FAILED',
                    'certificateAuthority': {
                        'data': 'string'
                    },
                    'clientRequestToken': 'string',
                    'platformVersion': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **cluster** *(dict) --* 
              The full description of your new cluster.
              - **name** *(string) --* 
                The name of the cluster.
              - **arn** *(string) --* 
                The Amazon Resource Name (ARN) of the cluster.
              - **createdAt** *(datetime) --* 
                The Unix epoch timestamp in seconds for when the cluster was created.
              - **version** *(string) --* 
                The Kubernetes server version for the cluster.
              - **endpoint** *(string) --* 
                The endpoint for your Kubernetes API server.
              - **roleArn** *(string) --* 
                The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.
              - **resourcesVpcConfig** *(dict) --* 
                The VPC configuration used by the cluster control plane. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see `Cluster VPC Considerations <https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html>`__ and `Cluster Security Group Considerations <https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html>`__ in the *Amazon EKS User Guide* .
                - **subnetIds** *(list) --* 
                  The subnets associated with your cluster.
                  - *(string) --* 
                - **securityGroupIds** *(list) --* 
                  The security groups associated with the cross-account elastic network interfaces that are used to allow communication between your worker nodes and the Kubernetes control plane.
                  - *(string) --* 
                - **vpcId** *(string) --* 
                  The VPC associated with your cluster.
                - **endpointPublicAccess** *(boolean) --* 
                  This parameter indicates whether the Amazon EKS public API server endpoint is enabled. If the Amazon EKS public API server endpoint is disabled, your cluster's Kubernetes API server can only receive requests that originate from within the cluster VPC. 
                - **endpointPrivateAccess** *(boolean) --* 
                  This parameter indicates whether the Amazon EKS private API server endpoint is enabled. If the Amazon EKS private API server endpoint is enabled, Kubernetes API requests that originate from within your cluster's VPC will use the private VPC endpoint instead of traversing the internet.
              - **logging** *(dict) --* 
                The logging configuration for your cluster.
                - **clusterLogging** *(list) --* 
                  The cluster control plane logging configuration for your cluster.
                  - *(dict) --* 
                    An object representing the enabled or disabled Kubernetes control plane logs for your cluster.
                    - **types** *(list) --* 
                      The available cluster control plane log types.
                      - *(string) --* 
                    - **enabled** *(boolean) --* 
                      If a log type is enabled, then that log type exports its control plane logs to CloudWatch Logs. If a log type is not enabled, then that log type does not export its control plane logs. Each individual log type can be enabled or disabled independently.
              - **status** *(string) --* 
                The current status of the cluster.
              - **certificateAuthority** *(dict) --* 
                The ``certificate-authority-data`` for your cluster.
                - **data** *(string) --* 
                  The base64 encoded certificate data required to communicate with your cluster. Add this to the ``certificate-authority-data`` section of the ``kubeconfig`` file for your cluster.
              - **clientRequestToken** *(string) --* 
                Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
              - **platformVersion** *(string) --* 
                The platform version of your Amazon EKS cluster. For more information, see `Platform Versions <https://docs.aws.amazon.com/eks/latest/userguide/platform-versions.html>`__ in the * *Amazon EKS User Guide* * .
        :type name: string
        :param name: **[REQUIRED]**
          The unique name to give to your cluster.
        :type version: string
        :param version:
          The desired Kubernetes version for your cluster. If you do not specify a value here, the latest version available in Amazon EKS is used.
        :type roleArn: string
        :param roleArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the IAM role that provides permissions for Amazon EKS to make calls to other AWS API operations on your behalf. For more information, see `Amazon EKS Service IAM Role <https://docs.aws.amazon.com/eks/latest/userguide/service_IAM_role.html>`__ in the * *Amazon EKS User Guide* * .
        :type resourcesVpcConfig: dict
        :param resourcesVpcConfig: **[REQUIRED]**
          The VPC configuration used by the cluster control plane. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see `Cluster VPC Considerations <https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html>`__ and `Cluster Security Group Considerations <https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html>`__ in the *Amazon EKS User Guide* . You must specify at least two subnets. You may specify up to five security groups, but we recommend that you use a dedicated security group for your cluster control plane.
          - **subnetIds** *(list) --*
            Specify subnets for your Amazon EKS worker nodes. Amazon EKS creates cross-account elastic network interfaces in these subnets to allow communication between your worker nodes and the Kubernetes control plane.
            - *(string) --*
          - **securityGroupIds** *(list) --*
            Specify one or more security groups for the cross-account elastic network interfaces that Amazon EKS creates to use to allow communication between your worker nodes and the Kubernetes control plane. If you do not specify a security group, the default security group for your VPC is used.
            - *(string) --*
          - **endpointPublicAccess** *(boolean) --*
            Set this value to ``false`` to disable public access for your cluster\'s Kubernetes API server endpoint. If you disable public access, your cluster\'s Kubernetes API server can only receive requests from within the cluster VPC. The default value for this parameter is ``true`` , which enables public access for your Kubernetes API server. For more information, see `Amazon EKS Cluster Endpoint Access Control <https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html>`__ in the * *Amazon EKS User Guide* * .
          - **endpointPrivateAccess** *(boolean) --*
            Set this value to ``true`` to enable private access for your cluster\'s Kubernetes API server endpoint. If you enable private access, Kubernetes API requests from within your cluster\'s VPC will use the private VPC endpoint. The default value for this parameter is ``false`` , which disables private access for your Kubernetes API server. For more information, see `Amazon EKS Cluster Endpoint Access Control <https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html>`__ in the * *Amazon EKS User Guide* * .
        :type logging: dict
        :param logging:
          Enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch Logs. By default, cluster control plane logs are not exported to CloudWatch Logs. For more information, see `Amazon EKS Cluster Control Plane Logs <https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html>`__ in the * *Amazon EKS User Guide* * .
          .. note::
            CloudWatch Logs ingestion, archive storage, and data scanning rates apply to exported control plane logs. For more information, see `Amazon CloudWatch Pricing <http://aws.amazon.com/cloudwatch/pricing/>`__ .
          - **clusterLogging** *(list) --*
            The cluster control plane logging configuration for your cluster.
            - *(dict) --*
              An object representing the enabled or disabled Kubernetes control plane logs for your cluster.
              - **types** *(list) --*
                The available cluster control plane log types.
                - *(string) --*
              - **enabled** *(boolean) --*
                If a log type is enabled, then that log type exports its control plane logs to CloudWatch Logs. If a log type is not enabled, then that log type does not export its control plane logs. Each individual log type can be enabled or disabled independently.
        :type clientRequestToken: string
        :param clientRequestToken:
          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
          This field is autopopulated if not provided.
        :rtype: dict
        :returns:
        """
        pass

    def delete_cluster(self, name: str) -> Dict:
        """
        Deletes the Amazon EKS cluster control plane. 
        .. note::
          If you have active services in your cluster that are associated with a load balancer, you must delete those services before deleting the cluster so that the load balancers are deleted properly. Otherwise, you can have orphaned resources in your VPC that prevent you from being able to delete the VPC. For more information, see `Deleting a Cluster <https://docs.aws.amazon.com/eks/latest/userguide/delete-cluster.html>`__ in the *Amazon EKS User Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/DeleteCluster>`_
        
        **Request Syntax**
        ::
          response = client.delete_cluster(
              name='string'
          )
        
        **Response Syntax**
        ::
            {
                'cluster': {
                    'name': 'string',
                    'arn': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'version': 'string',
                    'endpoint': 'string',
                    'roleArn': 'string',
                    'resourcesVpcConfig': {
                        'subnetIds': [
                            'string',
                        ],
                        'securityGroupIds': [
                            'string',
                        ],
                        'vpcId': 'string',
                        'endpointPublicAccess': True|False,
                        'endpointPrivateAccess': True|False
                    },
                    'logging': {
                        'clusterLogging': [
                            {
                                'types': [
                                    'api'|'audit'|'authenticator'|'controllerManager'|'scheduler',
                                ],
                                'enabled': True|False
                            },
                        ]
                    },
                    'status': 'CREATING'|'ACTIVE'|'DELETING'|'FAILED',
                    'certificateAuthority': {
                        'data': 'string'
                    },
                    'clientRequestToken': 'string',
                    'platformVersion': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **cluster** *(dict) --* 
              The full description of the cluster to delete.
              - **name** *(string) --* 
                The name of the cluster.
              - **arn** *(string) --* 
                The Amazon Resource Name (ARN) of the cluster.
              - **createdAt** *(datetime) --* 
                The Unix epoch timestamp in seconds for when the cluster was created.
              - **version** *(string) --* 
                The Kubernetes server version for the cluster.
              - **endpoint** *(string) --* 
                The endpoint for your Kubernetes API server.
              - **roleArn** *(string) --* 
                The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.
              - **resourcesVpcConfig** *(dict) --* 
                The VPC configuration used by the cluster control plane. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see `Cluster VPC Considerations <https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html>`__ and `Cluster Security Group Considerations <https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html>`__ in the *Amazon EKS User Guide* .
                - **subnetIds** *(list) --* 
                  The subnets associated with your cluster.
                  - *(string) --* 
                - **securityGroupIds** *(list) --* 
                  The security groups associated with the cross-account elastic network interfaces that are used to allow communication between your worker nodes and the Kubernetes control plane.
                  - *(string) --* 
                - **vpcId** *(string) --* 
                  The VPC associated with your cluster.
                - **endpointPublicAccess** *(boolean) --* 
                  This parameter indicates whether the Amazon EKS public API server endpoint is enabled. If the Amazon EKS public API server endpoint is disabled, your cluster's Kubernetes API server can only receive requests that originate from within the cluster VPC. 
                - **endpointPrivateAccess** *(boolean) --* 
                  This parameter indicates whether the Amazon EKS private API server endpoint is enabled. If the Amazon EKS private API server endpoint is enabled, Kubernetes API requests that originate from within your cluster's VPC will use the private VPC endpoint instead of traversing the internet.
              - **logging** *(dict) --* 
                The logging configuration for your cluster.
                - **clusterLogging** *(list) --* 
                  The cluster control plane logging configuration for your cluster.
                  - *(dict) --* 
                    An object representing the enabled or disabled Kubernetes control plane logs for your cluster.
                    - **types** *(list) --* 
                      The available cluster control plane log types.
                      - *(string) --* 
                    - **enabled** *(boolean) --* 
                      If a log type is enabled, then that log type exports its control plane logs to CloudWatch Logs. If a log type is not enabled, then that log type does not export its control plane logs. Each individual log type can be enabled or disabled independently.
              - **status** *(string) --* 
                The current status of the cluster.
              - **certificateAuthority** *(dict) --* 
                The ``certificate-authority-data`` for your cluster.
                - **data** *(string) --* 
                  The base64 encoded certificate data required to communicate with your cluster. Add this to the ``certificate-authority-data`` section of the ``kubeconfig`` file for your cluster.
              - **clientRequestToken** *(string) --* 
                Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
              - **platformVersion** *(string) --* 
                The platform version of your Amazon EKS cluster. For more information, see `Platform Versions <https://docs.aws.amazon.com/eks/latest/userguide/platform-versions.html>`__ in the * *Amazon EKS User Guide* * .
        :type name: string
        :param name: **[REQUIRED]**
          The name of the cluster to delete.
        :rtype: dict
        :returns:
        """
        pass

    def describe_cluster(self, name: str) -> Dict:
        """
        Returns descriptive information about an Amazon EKS cluster.
        The API server endpoint and certificate authority data returned by this operation are required for ``kubelet`` and ``kubectl`` to communicate with your Kubernetes API server. For more information, see `Create a kubeconfig for Amazon EKS <https://docs.aws.amazon.com/eks/latest/userguide/create-kubeconfig.html>`__ .
        .. note::
          The API server endpoint and certificate authority data are not available until the cluster reaches the ``ACTIVE`` state.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/DescribeCluster>`_
        
        **Request Syntax**
        ::
          response = client.describe_cluster(
              name='string'
          )
        
        **Response Syntax**
        ::
            {
                'cluster': {
                    'name': 'string',
                    'arn': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'version': 'string',
                    'endpoint': 'string',
                    'roleArn': 'string',
                    'resourcesVpcConfig': {
                        'subnetIds': [
                            'string',
                        ],
                        'securityGroupIds': [
                            'string',
                        ],
                        'vpcId': 'string',
                        'endpointPublicAccess': True|False,
                        'endpointPrivateAccess': True|False
                    },
                    'logging': {
                        'clusterLogging': [
                            {
                                'types': [
                                    'api'|'audit'|'authenticator'|'controllerManager'|'scheduler',
                                ],
                                'enabled': True|False
                            },
                        ]
                    },
                    'status': 'CREATING'|'ACTIVE'|'DELETING'|'FAILED',
                    'certificateAuthority': {
                        'data': 'string'
                    },
                    'clientRequestToken': 'string',
                    'platformVersion': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **cluster** *(dict) --* 
              The full description of your specified cluster.
              - **name** *(string) --* 
                The name of the cluster.
              - **arn** *(string) --* 
                The Amazon Resource Name (ARN) of the cluster.
              - **createdAt** *(datetime) --* 
                The Unix epoch timestamp in seconds for when the cluster was created.
              - **version** *(string) --* 
                The Kubernetes server version for the cluster.
              - **endpoint** *(string) --* 
                The endpoint for your Kubernetes API server.
              - **roleArn** *(string) --* 
                The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.
              - **resourcesVpcConfig** *(dict) --* 
                The VPC configuration used by the cluster control plane. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see `Cluster VPC Considerations <https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html>`__ and `Cluster Security Group Considerations <https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html>`__ in the *Amazon EKS User Guide* .
                - **subnetIds** *(list) --* 
                  The subnets associated with your cluster.
                  - *(string) --* 
                - **securityGroupIds** *(list) --* 
                  The security groups associated with the cross-account elastic network interfaces that are used to allow communication between your worker nodes and the Kubernetes control plane.
                  - *(string) --* 
                - **vpcId** *(string) --* 
                  The VPC associated with your cluster.
                - **endpointPublicAccess** *(boolean) --* 
                  This parameter indicates whether the Amazon EKS public API server endpoint is enabled. If the Amazon EKS public API server endpoint is disabled, your cluster's Kubernetes API server can only receive requests that originate from within the cluster VPC. 
                - **endpointPrivateAccess** *(boolean) --* 
                  This parameter indicates whether the Amazon EKS private API server endpoint is enabled. If the Amazon EKS private API server endpoint is enabled, Kubernetes API requests that originate from within your cluster's VPC will use the private VPC endpoint instead of traversing the internet.
              - **logging** *(dict) --* 
                The logging configuration for your cluster.
                - **clusterLogging** *(list) --* 
                  The cluster control plane logging configuration for your cluster.
                  - *(dict) --* 
                    An object representing the enabled or disabled Kubernetes control plane logs for your cluster.
                    - **types** *(list) --* 
                      The available cluster control plane log types.
                      - *(string) --* 
                    - **enabled** *(boolean) --* 
                      If a log type is enabled, then that log type exports its control plane logs to CloudWatch Logs. If a log type is not enabled, then that log type does not export its control plane logs. Each individual log type can be enabled or disabled independently.
              - **status** *(string) --* 
                The current status of the cluster.
              - **certificateAuthority** *(dict) --* 
                The ``certificate-authority-data`` for your cluster.
                - **data** *(string) --* 
                  The base64 encoded certificate data required to communicate with your cluster. Add this to the ``certificate-authority-data`` section of the ``kubeconfig`` file for your cluster.
              - **clientRequestToken** *(string) --* 
                Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
              - **platformVersion** *(string) --* 
                The platform version of your Amazon EKS cluster. For more information, see `Platform Versions <https://docs.aws.amazon.com/eks/latest/userguide/platform-versions.html>`__ in the * *Amazon EKS User Guide* * .
        :type name: string
        :param name: **[REQUIRED]**
          The name of the cluster to describe.
        :rtype: dict
        :returns:
        """
        pass

    def describe_update(self, name: str, updateId: str) -> Dict:
        """
        Returns descriptive information about an update against your Amazon EKS cluster.
        When the status of the update is ``Succeeded`` , the update is complete. If an update fails, the status is ``Failed`` , and an error detail explains the reason for the failure.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/DescribeUpdate>`_
        
        **Request Syntax**
        ::
          response = client.describe_update(
              name='string',
              updateId='string'
          )
        
        **Response Syntax**
        ::
            {
                'update': {
                    'id': 'string',
                    'status': 'InProgress'|'Failed'|'Cancelled'|'Successful',
                    'type': 'VersionUpdate'|'EndpointAccessUpdate'|'LoggingUpdate',
                    'params': [
                        {
                            'type': 'Version'|'PlatformVersion'|'EndpointPrivateAccess'|'EndpointPublicAccess'|'ClusterLogging',
                            'value': 'string'
                        },
                    ],
                    'createdAt': datetime(2015, 1, 1),
                    'errors': [
                        {
                            'errorCode': 'SubnetNotFound'|'SecurityGroupNotFound'|'EniLimitReached'|'IpNotAvailable'|'AccessDenied'|'OperationNotPermitted'|'VpcIdNotFound'|'Unknown',
                            'errorMessage': 'string',
                            'resourceIds': [
                                'string',
                            ]
                        },
                    ]
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **update** *(dict) --* 
              The full description of the specified update.
              - **id** *(string) --* 
                A UUID that is used to track the update.
              - **status** *(string) --* 
                The current status of the update.
              - **type** *(string) --* 
                The type of the update.
              - **params** *(list) --* 
                A key-value map that contains the parameters associated with the update.
                - *(dict) --* 
                  An object representing the details of an update request.
                  - **type** *(string) --* 
                    The keys associated with an update request.
                  - **value** *(string) --* 
                    The value of the keys submitted as part of an update request.
              - **createdAt** *(datetime) --* 
                The Unix epoch timestamp in seconds for when the update was created.
              - **errors** *(list) --* 
                Any errors associated with a ``Failed`` update.
                - *(dict) --* 
                  An object representing an error when an asynchronous operation fails.
                  - **errorCode** *(string) --* 
                    A brief description of the error. 
                    * **SubnetNotFound** : One of the subnets associated with the cluster could not be found. 
                    * **SecurityGroupNotFound** : One of the security groups associated with the cluster could not be found. 
                    * **EniLimitReached** : You have reached the elastic network interface limit for your account. 
                    * **IpNotAvailable** : A subnet associated with the cluster does not have any free IP addresses. 
                    * **AccessDenied** : You do not have permissions to perform the specified operation. 
                    * **OperationNotPermitted** : The service role associated with the cluster does not have the required access permissions for Amazon EKS. 
                    * **VpcIdNotFound** : The VPC associated with the cluster could not be found. 
                  - **errorMessage** *(string) --* 
                    A more complete description of the error.
                  - **resourceIds** *(list) --* 
                    An optional field that contains the resource IDs associated with the error.
                    - *(string) --* 
        :type name: string
        :param name: **[REQUIRED]**
          The name of the Amazon EKS cluster to update.
        :type updateId: string
        :param updateId: **[REQUIRED]**
          The ID of the update to describe.
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

    def list_clusters(self, maxResults: int = None, nextToken: str = None) -> Dict:
        """
        Lists the Amazon EKS clusters in your AWS account in the specified Region.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/ListClusters>`_
        
        **Request Syntax**
        ::
          response = client.list_clusters(
              maxResults=123,
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'clusters': [
                    'string',
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **clusters** *(list) --* 
              A list of all of the clusters for your account in the specified Region.
              - *(string) --* 
            - **nextToken** *(string) --* 
              The ``nextToken`` value to include in a future ``ListClusters`` request. When the results of a ``ListClusters`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.
        :type maxResults: integer
        :param maxResults:
          The maximum number of cluster results returned by ``ListClusters`` in paginated output. When this parameter is used, ``ListClusters`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListClusters`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListClusters`` returns up to 100 results and a ``nextToken`` value if applicable.
        :type nextToken: string
        :param nextToken:
          The ``nextToken`` value returned from a previous paginated ``ListClusters`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value.
          .. note::
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
        :rtype: dict
        :returns:
        """
        pass

    def list_updates(self, name: str, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Lists the updates associated with an Amazon EKS cluster in your AWS account, in the specified Region.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/ListUpdates>`_
        
        **Request Syntax**
        ::
          response = client.list_updates(
              name='string',
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'updateIds': [
                    'string',
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **updateIds** *(list) --* 
              A list of all the updates for the specified cluster and Region.
              - *(string) --* 
            - **nextToken** *(string) --* 
              The ``nextToken`` value to include in a future ``ListUpdates`` request. When the results of a ``ListUpdates`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.
        :type name: string
        :param name: **[REQUIRED]**
          The name of the Amazon EKS cluster for which to list updates.
        :type nextToken: string
        :param nextToken:
          The ``nextToken`` value returned from a previous paginated ``ListUpdates`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value.
        :type maxResults: integer
        :param maxResults:
          The maximum number of update results returned by ``ListUpdates`` in paginated output. When this parameter is used, ``ListUpdates`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListUpdates`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListUpdates`` returns up to 100 results and a ``nextToken`` value if applicable.
        :rtype: dict
        :returns:
        """
        pass

    def update_cluster_config(self, name: str, resourcesVpcConfig: Dict = None, logging: Dict = None, clientRequestToken: str = None) -> Dict:
        """
        Updates an Amazon EKS cluster configuration. Your cluster continues to function during the update. The response output includes an update ID that you can use to track the status of your cluster update with the  DescribeUpdate API operation.
        You can use this API operation to enable or disable public and private access to your cluster's Kubernetes API server endpoint. By default, public access is enabled and private access is disabled. For more information, see `Amazon EKS Cluster Endpoint Access Control <https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html>`__ in the * *Amazon EKS User Guide* * . 
        You can also use this API operation to enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch Logs. By default, cluster control plane logs are not exported to CloudWatch Logs. For more information, see `Amazon EKS Cluster Control Plane Logs <https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html>`__ in the * *Amazon EKS User Guide* * .
        .. note::
          CloudWatch Logs ingestion, archive storage, and data scanning rates apply to exported control plane logs. For more information, see `Amazon CloudWatch Pricing <http://aws.amazon.com/cloudwatch/pricing/>`__ .
        Cluster updates are asynchronous, and they should finish within a few minutes. During an update, the cluster status moves to ``UPDATING`` (this status transition is eventually consistent). When the update is complete (either ``Failed`` or ``Successful`` ), the cluster status moves to ``Active`` .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/UpdateClusterConfig>`_
        
        **Request Syntax**
        ::
          response = client.update_cluster_config(
              name='string',
              resourcesVpcConfig={
                  'subnetIds': [
                      'string',
                  ],
                  'securityGroupIds': [
                      'string',
                  ],
                  'endpointPublicAccess': True|False,
                  'endpointPrivateAccess': True|False
              },
              logging={
                  'clusterLogging': [
                      {
                          'types': [
                              'api'|'audit'|'authenticator'|'controllerManager'|'scheduler',
                          ],
                          'enabled': True|False
                      },
                  ]
              },
              clientRequestToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'update': {
                    'id': 'string',
                    'status': 'InProgress'|'Failed'|'Cancelled'|'Successful',
                    'type': 'VersionUpdate'|'EndpointAccessUpdate'|'LoggingUpdate',
                    'params': [
                        {
                            'type': 'Version'|'PlatformVersion'|'EndpointPrivateAccess'|'EndpointPublicAccess'|'ClusterLogging',
                            'value': 'string'
                        },
                    ],
                    'createdAt': datetime(2015, 1, 1),
                    'errors': [
                        {
                            'errorCode': 'SubnetNotFound'|'SecurityGroupNotFound'|'EniLimitReached'|'IpNotAvailable'|'AccessDenied'|'OperationNotPermitted'|'VpcIdNotFound'|'Unknown',
                            'errorMessage': 'string',
                            'resourceIds': [
                                'string',
                            ]
                        },
                    ]
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **update** *(dict) --* 
              An object representing an asynchronous update.
              - **id** *(string) --* 
                A UUID that is used to track the update.
              - **status** *(string) --* 
                The current status of the update.
              - **type** *(string) --* 
                The type of the update.
              - **params** *(list) --* 
                A key-value map that contains the parameters associated with the update.
                - *(dict) --* 
                  An object representing the details of an update request.
                  - **type** *(string) --* 
                    The keys associated with an update request.
                  - **value** *(string) --* 
                    The value of the keys submitted as part of an update request.
              - **createdAt** *(datetime) --* 
                The Unix epoch timestamp in seconds for when the update was created.
              - **errors** *(list) --* 
                Any errors associated with a ``Failed`` update.
                - *(dict) --* 
                  An object representing an error when an asynchronous operation fails.
                  - **errorCode** *(string) --* 
                    A brief description of the error. 
                    * **SubnetNotFound** : One of the subnets associated with the cluster could not be found. 
                    * **SecurityGroupNotFound** : One of the security groups associated with the cluster could not be found. 
                    * **EniLimitReached** : You have reached the elastic network interface limit for your account. 
                    * **IpNotAvailable** : A subnet associated with the cluster does not have any free IP addresses. 
                    * **AccessDenied** : You do not have permissions to perform the specified operation. 
                    * **OperationNotPermitted** : The service role associated with the cluster does not have the required access permissions for Amazon EKS. 
                    * **VpcIdNotFound** : The VPC associated with the cluster could not be found. 
                  - **errorMessage** *(string) --* 
                    A more complete description of the error.
                  - **resourceIds** *(list) --* 
                    An optional field that contains the resource IDs associated with the error.
                    - *(string) --* 
        :type name: string
        :param name: **[REQUIRED]**
          The name of the Amazon EKS cluster to update.
        :type resourcesVpcConfig: dict
        :param resourcesVpcConfig:
          An object representing the VPC configuration to use for an Amazon EKS cluster.
          - **subnetIds** *(list) --*
            Specify subnets for your Amazon EKS worker nodes. Amazon EKS creates cross-account elastic network interfaces in these subnets to allow communication between your worker nodes and the Kubernetes control plane.
            - *(string) --*
          - **securityGroupIds** *(list) --*
            Specify one or more security groups for the cross-account elastic network interfaces that Amazon EKS creates to use to allow communication between your worker nodes and the Kubernetes control plane. If you do not specify a security group, the default security group for your VPC is used.
            - *(string) --*
          - **endpointPublicAccess** *(boolean) --*
            Set this value to ``false`` to disable public access for your cluster\'s Kubernetes API server endpoint. If you disable public access, your cluster\'s Kubernetes API server can only receive requests from within the cluster VPC. The default value for this parameter is ``true`` , which enables public access for your Kubernetes API server. For more information, see `Amazon EKS Cluster Endpoint Access Control <https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html>`__ in the * *Amazon EKS User Guide* * .
          - **endpointPrivateAccess** *(boolean) --*
            Set this value to ``true`` to enable private access for your cluster\'s Kubernetes API server endpoint. If you enable private access, Kubernetes API requests from within your cluster\'s VPC will use the private VPC endpoint. The default value for this parameter is ``false`` , which disables private access for your Kubernetes API server. For more information, see `Amazon EKS Cluster Endpoint Access Control <https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html>`__ in the * *Amazon EKS User Guide* * .
        :type logging: dict
        :param logging:
          Enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch Logs. By default, cluster control plane logs are not exported to CloudWatch Logs. For more information, see `Amazon EKS Cluster Control Plane Logs <https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html>`__ in the * *Amazon EKS User Guide* * .
          .. note::
            CloudWatch Logs ingestion, archive storage, and data scanning rates apply to exported control plane logs. For more information, see `Amazon CloudWatch Pricing <http://aws.amazon.com/cloudwatch/pricing/>`__ .
          - **clusterLogging** *(list) --*
            The cluster control plane logging configuration for your cluster.
            - *(dict) --*
              An object representing the enabled or disabled Kubernetes control plane logs for your cluster.
              - **types** *(list) --*
                The available cluster control plane log types.
                - *(string) --*
              - **enabled** *(boolean) --*
                If a log type is enabled, then that log type exports its control plane logs to CloudWatch Logs. If a log type is not enabled, then that log type does not export its control plane logs. Each individual log type can be enabled or disabled independently.
        :type clientRequestToken: string
        :param clientRequestToken:
          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
          This field is autopopulated if not provided.
        :rtype: dict
        :returns:
        """
        pass

    def update_cluster_version(self, name: str, version: str, clientRequestToken: str = None) -> Dict:
        """
        Updates an Amazon EKS cluster to the specified Kubernetes version. Your cluster continues to function during the update. The response output includes an update ID that you can use to track the status of your cluster update with the  DescribeUpdate API operation.
        Cluster updates are asynchronous, and they should finish within a few minutes. During an update, the cluster status moves to ``UPDATING`` (this status transition is eventually consistent). When the update is complete (either ``Failed`` or ``Successful`` ), the cluster status moves to ``Active`` .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/UpdateClusterVersion>`_
        
        **Request Syntax**
        ::
          response = client.update_cluster_version(
              name='string',
              version='string',
              clientRequestToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'update': {
                    'id': 'string',
                    'status': 'InProgress'|'Failed'|'Cancelled'|'Successful',
                    'type': 'VersionUpdate'|'EndpointAccessUpdate'|'LoggingUpdate',
                    'params': [
                        {
                            'type': 'Version'|'PlatformVersion'|'EndpointPrivateAccess'|'EndpointPublicAccess'|'ClusterLogging',
                            'value': 'string'
                        },
                    ],
                    'createdAt': datetime(2015, 1, 1),
                    'errors': [
                        {
                            'errorCode': 'SubnetNotFound'|'SecurityGroupNotFound'|'EniLimitReached'|'IpNotAvailable'|'AccessDenied'|'OperationNotPermitted'|'VpcIdNotFound'|'Unknown',
                            'errorMessage': 'string',
                            'resourceIds': [
                                'string',
                            ]
                        },
                    ]
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **update** *(dict) --* 
              The full description of the specified update
              - **id** *(string) --* 
                A UUID that is used to track the update.
              - **status** *(string) --* 
                The current status of the update.
              - **type** *(string) --* 
                The type of the update.
              - **params** *(list) --* 
                A key-value map that contains the parameters associated with the update.
                - *(dict) --* 
                  An object representing the details of an update request.
                  - **type** *(string) --* 
                    The keys associated with an update request.
                  - **value** *(string) --* 
                    The value of the keys submitted as part of an update request.
              - **createdAt** *(datetime) --* 
                The Unix epoch timestamp in seconds for when the update was created.
              - **errors** *(list) --* 
                Any errors associated with a ``Failed`` update.
                - *(dict) --* 
                  An object representing an error when an asynchronous operation fails.
                  - **errorCode** *(string) --* 
                    A brief description of the error. 
                    * **SubnetNotFound** : One of the subnets associated with the cluster could not be found. 
                    * **SecurityGroupNotFound** : One of the security groups associated with the cluster could not be found. 
                    * **EniLimitReached** : You have reached the elastic network interface limit for your account. 
                    * **IpNotAvailable** : A subnet associated with the cluster does not have any free IP addresses. 
                    * **AccessDenied** : You do not have permissions to perform the specified operation. 
                    * **OperationNotPermitted** : The service role associated with the cluster does not have the required access permissions for Amazon EKS. 
                    * **VpcIdNotFound** : The VPC associated with the cluster could not be found. 
                  - **errorMessage** *(string) --* 
                    A more complete description of the error.
                  - **resourceIds** *(list) --* 
                    An optional field that contains the resource IDs associated with the error.
                    - *(string) --* 
        :type name: string
        :param name: **[REQUIRED]**
          The name of the Amazon EKS cluster to update.
        :type version: string
        :param version: **[REQUIRED]**
          The desired Kubernetes version following a successful update.
        :type clientRequestToken: string
        :param clientRequestToken:
          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
          This field is autopopulated if not provided.
        :rtype: dict
        :returns:
        """
        pass
