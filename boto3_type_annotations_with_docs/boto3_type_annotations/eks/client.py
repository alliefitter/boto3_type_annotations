from typing import Optional
from typing import Union
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

    def create_cluster(self, name: str, roleArn: str, resourcesVpcConfig: Dict, version: str = None, clientRequestToken: str = None) -> Dict:
        """
        
        The Amazon EKS control plane consists of control plane instances that run the Kubernetes software, like ``etcd`` and the API server. The control plane runs in an account managed by AWS, and the Kubernetes API is exposed via the Amazon EKS API server endpoint.
        
        Amazon EKS worker nodes run in your AWS account and connect to your cluster\'s control plane via the Kubernetes API server endpoint and a certificate file that is created for your cluster.
        
        The cluster control plane is provisioned across multiple Availability Zones and fronted by an Elastic Load Balancing Network Load Balancer. Amazon EKS also provisions elastic network interfaces in your VPC subnets to provide connectivity from the control plane instances to the worker nodes (for example, to support ``kubectl exec`` , ``logs`` , and ``proxy`` data flows).
        
        After you create an Amazon EKS cluster, you must configure your Kubernetes tooling to communicate with the API server and launch worker nodes into your cluster. For more information, see `Managing Cluster Authentication <http://docs.aws.amazon.com/eks/latest/userguide/managing-auth.html>`__ and `Launching Amazon EKS Worker Nodes <http://docs.aws.amazon.com/eks/latest/userguide/launch-workers.html>`__ in the *Amazon EKS User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/CreateCluster>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_cluster(
              name=\'string\',
              version=\'string\',
              roleArn=\'string\',
              resourcesVpcConfig={
                  \'subnetIds\': [
                      \'string\',
                  ],
                  \'securityGroupIds\': [
                      \'string\',
                  ]
              },
              clientRequestToken=\'string\'
          )
        :type name: string
        :param name: **[REQUIRED]** 
        
          The unique name to give to your cluster.
        
        :type version: string
        :param version: 
        
          The desired Kubernetes version for your cluster. If you do not specify a value here, the latest version available in Amazon EKS is used.
        
        :type roleArn: string
        :param roleArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the IAM role that provides permissions for Amazon EKS to make calls to other AWS API operations on your behalf. For more information, see `Amazon EKS Service IAM Role <http://docs.aws.amazon.com/eks/latest/userguide/service_IAM_role.html>`__ in the * *Amazon EKS User Guide* * .
        
        :type resourcesVpcConfig: dict
        :param resourcesVpcConfig: **[REQUIRED]** 
        
          The VPC subnets and security groups used by the cluster control plane. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see `Cluster VPC Considerations <http://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html>`__ and `Cluster Security Group Considerations <http://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html>`__ in the *Amazon EKS User Guide* . You must specify at least two subnets. You may specify up to 5 security groups, but we recommend that you use a dedicated security group for your cluster control plane.
        
          - **subnetIds** *(list) --* **[REQUIRED]** 
        
            Specify subnets for your Amazon EKS worker nodes. Amazon EKS creates cross-account elastic network interfaces in these subnets to allow communication between your worker nodes and the Kubernetes control plane.
        
            - *(string) --* 
        
          - **securityGroupIds** *(list) --* 
        
            Specify one or more security groups for the cross-account elastic network interfaces that Amazon EKS creates to use to allow communication between your worker nodes and the Kubernetes control plane.
        
            - *(string) --* 
        
        :type clientRequestToken: string
        :param clientRequestToken: 
        
          Unique, case-sensitive identifier you provide to ensure the idempotency of the request.
        
          This field is autopopulated if not provided.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'cluster\': {
                    \'name\': \'string\',
                    \'arn\': \'string\',
                    \'createdAt\': datetime(2015, 1, 1),
                    \'version\': \'string\',
                    \'endpoint\': \'string\',
                    \'roleArn\': \'string\',
                    \'resourcesVpcConfig\': {
                        \'subnetIds\': [
                            \'string\',
                        ],
                        \'securityGroupIds\': [
                            \'string\',
                        ],
                        \'vpcId\': \'string\'
                    },
                    \'status\': \'CREATING\'|\'ACTIVE\'|\'DELETING\'|\'FAILED\',
                    \'certificateAuthority\': {
                        \'data\': \'string\'
                    },
                    \'clientRequestToken\': \'string\',
                    \'platformVersion\': \'string\'
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
        
                The Unix epoch time stamp in seconds for when the cluster was created.
        
              - **version** *(string) --* 
        
                The Kubernetes server version for the cluster.
        
              - **endpoint** *(string) --* 
        
                The endpoint for your Kubernetes API server.
        
              - **roleArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.
        
              - **resourcesVpcConfig** *(dict) --* 
        
                The VPC subnets and security groups used by the cluster control plane. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see `Cluster VPC Considerations <http://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html>`__ and `Cluster Security Group Considerations <http://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html>`__ in the *Amazon EKS User Guide* .
        
                - **subnetIds** *(list) --* 
        
                  The subnets associated with your cluster.
        
                  - *(string) --* 
              
                - **securityGroupIds** *(list) --* 
        
                  The security groups associated with the cross-account elastic network interfaces that are used to allow communication between your worker nodes and the Kubernetes control plane.
        
                  - *(string) --* 
              
                - **vpcId** *(string) --* 
        
                  The VPC associated with your cluster.
        
              - **status** *(string) --* 
        
                The current status of the cluster.
        
              - **certificateAuthority** *(dict) --* 
        
                The ``certificate-authority-data`` for your cluster.
        
                - **data** *(string) --* 
        
                  The base64 encoded certificate data required to communicate with your cluster. Add this to the ``certificate-authority-data`` section of the ``kubeconfig`` file for your cluster.
        
              - **clientRequestToken** *(string) --* 
        
                Unique, case-sensitive identifier you provide to ensure the idempotency of the request.
        
              - **platformVersion** *(string) --* 
        
                The platform version of your Amazon EKS cluster. For more information, see `Platform Versions <eks/latest/userguide/platform-versions.html>`__ in the * *Amazon EKS User Guide* * .
        
        """
        pass

    def delete_cluster(self, name: str) -> Dict:
        """
        
        .. note::
        
          If you have active services in your cluster that are associated with a load balancer, you must delete those services before deleting the cluster so that the load balancers are deleted properly. Otherwise, you can have orphaned resources in your VPC that prevent you from being able to delete the VPC. For more information, see `Deleting a Cluster <http://docs.aws.amazon.com/eks/latest/userguide/delete-cluster.html>`__ in the *Amazon EKS User Guide* .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/DeleteCluster>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_cluster(
              name=\'string\'
          )
        :type name: string
        :param name: **[REQUIRED]** 
        
          The name of the cluster to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'cluster\': {
                    \'name\': \'string\',
                    \'arn\': \'string\',
                    \'createdAt\': datetime(2015, 1, 1),
                    \'version\': \'string\',
                    \'endpoint\': \'string\',
                    \'roleArn\': \'string\',
                    \'resourcesVpcConfig\': {
                        \'subnetIds\': [
                            \'string\',
                        ],
                        \'securityGroupIds\': [
                            \'string\',
                        ],
                        \'vpcId\': \'string\'
                    },
                    \'status\': \'CREATING\'|\'ACTIVE\'|\'DELETING\'|\'FAILED\',
                    \'certificateAuthority\': {
                        \'data\': \'string\'
                    },
                    \'clientRequestToken\': \'string\',
                    \'platformVersion\': \'string\'
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
        
                The Unix epoch time stamp in seconds for when the cluster was created.
        
              - **version** *(string) --* 
        
                The Kubernetes server version for the cluster.
        
              - **endpoint** *(string) --* 
        
                The endpoint for your Kubernetes API server.
        
              - **roleArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.
        
              - **resourcesVpcConfig** *(dict) --* 
        
                The VPC subnets and security groups used by the cluster control plane. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see `Cluster VPC Considerations <http://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html>`__ and `Cluster Security Group Considerations <http://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html>`__ in the *Amazon EKS User Guide* .
        
                - **subnetIds** *(list) --* 
        
                  The subnets associated with your cluster.
        
                  - *(string) --* 
              
                - **securityGroupIds** *(list) --* 
        
                  The security groups associated with the cross-account elastic network interfaces that are used to allow communication between your worker nodes and the Kubernetes control plane.
        
                  - *(string) --* 
              
                - **vpcId** *(string) --* 
        
                  The VPC associated with your cluster.
        
              - **status** *(string) --* 
        
                The current status of the cluster.
        
              - **certificateAuthority** *(dict) --* 
        
                The ``certificate-authority-data`` for your cluster.
        
                - **data** *(string) --* 
        
                  The base64 encoded certificate data required to communicate with your cluster. Add this to the ``certificate-authority-data`` section of the ``kubeconfig`` file for your cluster.
        
              - **clientRequestToken** *(string) --* 
        
                Unique, case-sensitive identifier you provide to ensure the idempotency of the request.
        
              - **platformVersion** *(string) --* 
        
                The platform version of your Amazon EKS cluster. For more information, see `Platform Versions <eks/latest/userguide/platform-versions.html>`__ in the * *Amazon EKS User Guide* * .
        
        """
        pass

    def describe_cluster(self, name: str) -> Dict:
        """
        
        The API server endpoint and certificate authority data returned by this operation are required for ``kubelet`` and ``kubectl`` to communicate with your Kubernetes API server. For more information, see `Create a kubeconfig for Amazon EKS <http://docs.aws.amazon.com/eks/latest/userguide/create-kubeconfig.html>`__ .
        
        .. note::
        
          The API server endpoint and certificate authority data are not available until the cluster reaches the ``ACTIVE`` state.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/DescribeCluster>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_cluster(
              name=\'string\'
          )
        :type name: string
        :param name: **[REQUIRED]** 
        
          The name of the cluster to describe.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'cluster\': {
                    \'name\': \'string\',
                    \'arn\': \'string\',
                    \'createdAt\': datetime(2015, 1, 1),
                    \'version\': \'string\',
                    \'endpoint\': \'string\',
                    \'roleArn\': \'string\',
                    \'resourcesVpcConfig\': {
                        \'subnetIds\': [
                            \'string\',
                        ],
                        \'securityGroupIds\': [
                            \'string\',
                        ],
                        \'vpcId\': \'string\'
                    },
                    \'status\': \'CREATING\'|\'ACTIVE\'|\'DELETING\'|\'FAILED\',
                    \'certificateAuthority\': {
                        \'data\': \'string\'
                    },
                    \'clientRequestToken\': \'string\',
                    \'platformVersion\': \'string\'
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
        
                The Unix epoch time stamp in seconds for when the cluster was created.
        
              - **version** *(string) --* 
        
                The Kubernetes server version for the cluster.
        
              - **endpoint** *(string) --* 
        
                The endpoint for your Kubernetes API server.
        
              - **roleArn** *(string) --* 
        
                The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.
        
              - **resourcesVpcConfig** *(dict) --* 
        
                The VPC subnets and security groups used by the cluster control plane. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see `Cluster VPC Considerations <http://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html>`__ and `Cluster Security Group Considerations <http://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html>`__ in the *Amazon EKS User Guide* .
        
                - **subnetIds** *(list) --* 
        
                  The subnets associated with your cluster.
        
                  - *(string) --* 
              
                - **securityGroupIds** *(list) --* 
        
                  The security groups associated with the cross-account elastic network interfaces that are used to allow communication between your worker nodes and the Kubernetes control plane.
        
                  - *(string) --* 
              
                - **vpcId** *(string) --* 
        
                  The VPC associated with your cluster.
        
              - **status** *(string) --* 
        
                The current status of the cluster.
        
              - **certificateAuthority** *(dict) --* 
        
                The ``certificate-authority-data`` for your cluster.
        
                - **data** *(string) --* 
        
                  The base64 encoded certificate data required to communicate with your cluster. Add this to the ``certificate-authority-data`` section of the ``kubeconfig`` file for your cluster.
        
              - **clientRequestToken** *(string) --* 
        
                Unique, case-sensitive identifier you provide to ensure the idempotency of the request.
        
              - **platformVersion** *(string) --* 
        
                The platform version of your Amazon EKS cluster. For more information, see `Platform Versions <eks/latest/userguide/platform-versions.html>`__ in the * *Amazon EKS User Guide* * .
        
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

    def list_clusters(self, maxResults: int = None, nextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/ListClusters>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_clusters(
              maxResults=123,
              nextToken=\'string\'
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'clusters\': [
                    \'string\',
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **clusters** *(list) --* 
        
              A list of all of the clusters for your account in the specified Region.
        
              - *(string) --* 
          
            - **nextToken** *(string) --* 
        
              The ``nextToken`` value to include in a future ``ListClusters`` request. When the results of a ``ListClusters`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.
        
        """
        pass
