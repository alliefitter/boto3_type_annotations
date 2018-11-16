from typing import Optional
from typing import Union
from typing import List
from botocore.waiter import Waiter
from botocore.paginate import Paginator
from typing import Dict
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

    def cancel_job(self, jobId: str, reason: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/CancelJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.cancel_job(
              jobId=\'string\',
              reason=\'string\'
          )
        :type jobId: string
        :param jobId: **[REQUIRED]** 
        
          The AWS Batch job ID of the job to cancel.
        
        :type reason: string
        :param reason: **[REQUIRED]** 
        
          A message to attach to the job that explains the reason for canceling it. This message is returned by future  DescribeJobs operations on the job. This message is also recorded in the AWS Batch activity logs. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def create_compute_environment(self, computeEnvironmentName: str, type: str, serviceRole: str, state: str = None, computeResources: Dict = None) -> Dict:
        """
        
        In a managed compute environment, AWS Batch manages the capacity and instance types of the compute resources within the environment, based on the compute resource specification that you define or `launch template <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html>`__ that you specify when you create the compute environment. You can choose to use Amazon EC2 On-Demand Instances or Spot Instances in your managed compute environment. You can optionally set a maximum price so that Spot Instances only launch when the Spot Instance price is below a specified percentage of the On-Demand price.
        
        In an unmanaged compute environment, you can manage your own compute resources. This provides more compute resource configuration options, such as using a custom AMI, but you must ensure that your AMI meets the Amazon ECS container instance AMI specification. For more information, see `Container Instance AMIs <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/container_instance_AMIs.html>`__ in the *Amazon Elastic Container Service Developer Guide* . After you have created your unmanaged compute environment, you can use the  DescribeComputeEnvironments operation to find the Amazon ECS cluster that is associated with it and then manually launch your container instances into that Amazon ECS cluster. For more information, see `Launching an Amazon ECS Container Instance <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_container_instance.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        
        .. note::
        
          AWS Batch does not upgrade the AMIs in a compute environment after it is created (for example, when a newer version of the Amazon ECS-optimized AMI is available). You are responsible for the management of the guest operating system (including updates and security patches) and any additional application software or utilities that you install on the compute resources. To use a new AMI for your AWS Batch jobs:
        
          * Create a new compute environment with the new AMI. 
           
          * Add the compute environment to an existing job queue. 
           
          * Remove the old compute environment from your job queue. 
           
          * Delete the old compute environment. 
           
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/CreateComputeEnvironment>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_compute_environment(
              computeEnvironmentName=\'string\',
              type=\'MANAGED\'|\'UNMANAGED\',
              state=\'ENABLED\'|\'DISABLED\',
              computeResources={
                  \'type\': \'EC2\'|\'SPOT\',
                  \'minvCpus\': 123,
                  \'maxvCpus\': 123,
                  \'desiredvCpus\': 123,
                  \'instanceTypes\': [
                      \'string\',
                  ],
                  \'imageId\': \'string\',
                  \'subnets\': [
                      \'string\',
                  ],
                  \'securityGroupIds\': [
                      \'string\',
                  ],
                  \'ec2KeyPair\': \'string\',
                  \'instanceRole\': \'string\',
                  \'tags\': {
                      \'string\': \'string\'
                  },
                  \'bidPercentage\': 123,
                  \'spotIamFleetRole\': \'string\',
                  \'launchTemplate\': {
                      \'launchTemplateId\': \'string\',
                      \'launchTemplateName\': \'string\',
                      \'version\': \'string\'
                  }
              },
              serviceRole=\'string\'
          )
        :type computeEnvironmentName: string
        :param computeEnvironmentName: **[REQUIRED]** 
        
          The name for your compute environment. Up to 128 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.
        
        :type type: string
        :param type: **[REQUIRED]** 
        
          The type of the compute environment. For more information, see `Compute Environments <http://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html>`__ in the *AWS Batch User Guide* .
        
        :type state: string
        :param state: 
        
          The state of the compute environment. If the state is ``ENABLED`` , then the compute environment accepts jobs from a queue and can scale out automatically based on queues.
        
        :type computeResources: dict
        :param computeResources: 
        
          Details of the compute resources managed by the compute environment. This parameter is required for managed compute environments.
        
          - **type** *(string) --* **[REQUIRED]** 
        
            The type of compute environment.
        
          - **minvCpus** *(integer) --* **[REQUIRED]** 
        
            The minimum number of EC2 vCPUs that an environment should maintain (even if the compute environment is ``DISABLED`` ). 
        
          - **maxvCpus** *(integer) --* **[REQUIRED]** 
        
            The maximum number of EC2 vCPUs that an environment can reach. 
        
          - **desiredvCpus** *(integer) --* 
        
            The desired number of EC2 vCPUS in the compute environment. 
        
          - **instanceTypes** *(list) --* **[REQUIRED]** 
        
            The instances types that may be launched. You can specify instance families to launch any instance type within those families (for example, ``c4`` or ``p3`` ), or you can specify specific sizes within a family (such as ``c4.8xlarge`` ). You can also choose ``optimal`` to pick instance types (from the latest C, M, and R instance families) on the fly that match the demand of your job queues.
        
            - *(string) --* 
        
          - **imageId** *(string) --* 
        
            The Amazon Machine Image (AMI) ID used for instances launched in the compute environment.
        
          - **subnets** *(list) --* **[REQUIRED]** 
        
            The VPC subnets into which the compute resources are launched. 
        
            - *(string) --* 
        
          - **securityGroupIds** *(list) --* 
        
            The EC2 security group that is associated with instances launched in the compute environment. 
        
            - *(string) --* 
        
          - **ec2KeyPair** *(string) --* 
        
            The EC2 key pair that is used for instances launched in the compute environment.
        
          - **instanceRole** *(string) --* **[REQUIRED]** 
        
            The Amazon ECS instance profile applied to Amazon EC2 instances in a compute environment. You can specify the short name or full Amazon Resource Name (ARN) of an instance profile. For example, ``ecsInstanceRole`` or ``arn:aws:iam::<aws_account_id>:instance-profile/ecsInstanceRole`` . For more information, see `Amazon ECS Instance Role <http://docs.aws.amazon.com/batch/latest/userguide/instance_IAM_role.html>`__ in the *AWS Batch User Guide* .
        
          - **tags** *(dict) --* 
        
            Key-value pair tags to be applied to resources that are launched in the compute environment. 
        
            - *(string) --* 
        
              - *(string) --* 
        
          - **bidPercentage** *(integer) --* 
        
            The maximum percentage that a Spot Instance price can be when compared with the On-Demand price for that instance type before instances are launched. For example, if your maximum percentage is 20%, then the Spot price must be below 20% of the current On-Demand price for that EC2 instance. You always pay the lowest (market) price and never more than your maximum percentage. If you leave this field empty, the default value is 100% of the On-Demand price.
        
          - **spotIamFleetRole** *(string) --* 
        
            The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a ``SPOT`` compute environment.
        
          - **launchTemplate** *(dict) --* 
        
            The launch template to use for your compute resources. Any other compute resource parameters that you specify in a  CreateComputeEnvironment API operation override the same parameters in the launch template. You must specify either the launch template ID or launch template name in the request, but not both. 
        
            - **launchTemplateId** *(string) --* 
        
              The ID of the launch template.
        
            - **launchTemplateName** *(string) --* 
        
              The name of the launch template.
        
            - **version** *(string) --* 
        
              The version number of the launch template.
        
              Default: The default version of the launch template.
        
        :type serviceRole: string
        :param serviceRole: **[REQUIRED]** 
        
          The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.
        
          If your specified role has a path other than ``/`` , then you must either specify the full role ARN (this is recommended) or prefix the role name with the path.
        
          .. note::
        
            Depending on how you created your AWS Batch service role, its ARN may contain the ``service-role`` path prefix. When you only specify the name of the service role, AWS Batch assumes that your ARN does not use the ``service-role`` path prefix. Because of this, we recommend that you specify the full ARN of your service role when you create compute environments.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'computeEnvironmentName\': \'string\',
                \'computeEnvironmentArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **computeEnvironmentName** *(string) --* 
        
              The name of the compute environment.
        
            - **computeEnvironmentArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the compute environment. 
        
        """
        pass

    def create_job_queue(self, jobQueueName: str, priority: int, computeEnvironmentOrder: List, state: str = None) -> Dict:
        """
        
        You also set a priority to the job queue that determines the order in which the AWS Batch scheduler places jobs onto its associated compute environments. For example, if a compute environment is associated with more than one job queue, the job queue with a higher priority is given preference for scheduling jobs to that compute environment.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/CreateJobQueue>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_job_queue(
              jobQueueName=\'string\',
              state=\'ENABLED\'|\'DISABLED\',
              priority=123,
              computeEnvironmentOrder=[
                  {
                      \'order\': 123,
                      \'computeEnvironment\': \'string\'
                  },
              ]
          )
        :type jobQueueName: string
        :param jobQueueName: **[REQUIRED]** 
        
          The name of the job queue.
        
        :type state: string
        :param state: 
        
          The state of the job queue. If the job queue state is ``ENABLED`` , it is able to accept jobs.
        
        :type priority: integer
        :param priority: **[REQUIRED]** 
        
          The priority of the job queue. Job queues with a higher priority (or a higher integer value for the ``priority`` parameter) are evaluated first when associated with same compute environment. Priority is determined in descending order, for example, a job queue with a priority value of ``10`` is given scheduling preference over a job queue with a priority value of ``1`` .
        
        :type computeEnvironmentOrder: list
        :param computeEnvironmentOrder: **[REQUIRED]** 
        
          The set of compute environments mapped to a job queue and their order relative to each other. The job scheduler uses this parameter to determine which compute environment should execute a given job. Compute environments must be in the ``VALID`` state before you can associate them with a job queue. You can associate up to three compute environments with a job queue.
        
          - *(dict) --* 
        
            The order in which compute environments are tried for job placement within a queue. Compute environments are tried in ascending order. For example, if two compute environments are associated with a job queue, the compute environment with a lower order integer value is tried for job placement first.
        
            - **order** *(integer) --* **[REQUIRED]** 
        
              The order of the compute environment.
        
            - **computeEnvironment** *(string) --* **[REQUIRED]** 
        
              The Amazon Resource Name (ARN) of the compute environment.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'jobQueueName\': \'string\',
                \'jobQueueArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **jobQueueName** *(string) --* 
        
              The name of the job queue.
        
            - **jobQueueArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the job queue.
        
        """
        pass

    def delete_compute_environment(self, computeEnvironment: str) -> Dict:
        """
        
        Before you can delete a compute environment, you must set its state to ``DISABLED`` with the  UpdateComputeEnvironment API operation and disassociate it from any job queues with the  UpdateJobQueue API operation.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/DeleteComputeEnvironment>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_compute_environment(
              computeEnvironment=\'string\'
          )
        :type computeEnvironment: string
        :param computeEnvironment: **[REQUIRED]** 
        
          The name or Amazon Resource Name (ARN) of the compute environment to delete. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def delete_job_queue(self, jobQueue: str) -> Dict:
        """
        
        It is not necessary to disassociate compute environments from a queue before submitting a ``DeleteJobQueue`` request. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/DeleteJobQueue>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_job_queue(
              jobQueue=\'string\'
          )
        :type jobQueue: string
        :param jobQueue: **[REQUIRED]** 
        
          The short name or full Amazon Resource Name (ARN) of the queue to delete. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def deregister_job_definition(self, jobDefinition: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/DeregisterJobDefinition>`_
        
        **Request Syntax** 
        ::
        
          response = client.deregister_job_definition(
              jobDefinition=\'string\'
          )
        :type jobDefinition: string
        :param jobDefinition: **[REQUIRED]** 
        
          The name and revision (``name:revision`` ) or full Amazon Resource Name (ARN) of the job definition to deregister. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def describe_compute_environments(self, computeEnvironments: List = None, maxResults: int = None, nextToken: str = None) -> Dict:
        """
        
        If you are using an unmanaged compute environment, you can use the ``DescribeComputeEnvironment`` operation to determine the ``ecsClusterArn`` that you should launch your Amazon ECS container instances into.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/DescribeComputeEnvironments>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_compute_environments(
              computeEnvironments=[
                  \'string\',
              ],
              maxResults=123,
              nextToken=\'string\'
          )
        :type computeEnvironments: list
        :param computeEnvironments: 
        
          A list of up to 100 compute environment names or full Amazon Resource Name (ARN) entries. 
        
          - *(string) --* 
        
        :type maxResults: integer
        :param maxResults: 
        
          The maximum number of cluster results returned by ``DescribeComputeEnvironments`` in paginated output. When this parameter is used, ``DescribeComputeEnvironments`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``DescribeComputeEnvironments`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``DescribeComputeEnvironments`` returns up to 100 results and a ``nextToken`` value if applicable.
        
        :type nextToken: string
        :param nextToken: 
        
          The ``nextToken`` value returned from a previous paginated ``DescribeComputeEnvironments`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value. This value is ``null`` when there are no more results to return.
        
          .. note::
        
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'computeEnvironments\': [
                    {
                        \'computeEnvironmentName\': \'string\',
                        \'computeEnvironmentArn\': \'string\',
                        \'ecsClusterArn\': \'string\',
                        \'type\': \'MANAGED\'|\'UNMANAGED\',
                        \'state\': \'ENABLED\'|\'DISABLED\',
                        \'status\': \'CREATING\'|\'UPDATING\'|\'DELETING\'|\'DELETED\'|\'VALID\'|\'INVALID\',
                        \'statusReason\': \'string\',
                        \'computeResources\': {
                            \'type\': \'EC2\'|\'SPOT\',
                            \'minvCpus\': 123,
                            \'maxvCpus\': 123,
                            \'desiredvCpus\': 123,
                            \'instanceTypes\': [
                                \'string\',
                            ],
                            \'imageId\': \'string\',
                            \'subnets\': [
                                \'string\',
                            ],
                            \'securityGroupIds\': [
                                \'string\',
                            ],
                            \'ec2KeyPair\': \'string\',
                            \'instanceRole\': \'string\',
                            \'tags\': {
                                \'string\': \'string\'
                            },
                            \'bidPercentage\': 123,
                            \'spotIamFleetRole\': \'string\',
                            \'launchTemplate\': {
                                \'launchTemplateId\': \'string\',
                                \'launchTemplateName\': \'string\',
                                \'version\': \'string\'
                            }
                        },
                        \'serviceRole\': \'string\'
                    },
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **computeEnvironments** *(list) --* 
        
              The list of compute environments.
        
              - *(dict) --* 
        
                An object representing an AWS Batch compute environment.
        
                - **computeEnvironmentName** *(string) --* 
        
                  The name of the compute environment. 
        
                - **computeEnvironmentArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the compute environment. 
        
                - **ecsClusterArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the underlying Amazon ECS cluster used by the compute environment. 
        
                - **type** *(string) --* 
        
                  The type of the compute environment.
        
                - **state** *(string) --* 
        
                  The state of the compute environment. The valid values are ``ENABLED`` or ``DISABLED`` . 
        
                  If the state is ``ENABLED`` , then the AWS Batch scheduler can attempt to place jobs from an associated job queue on the compute resources within the environment. If the compute environment is managed, then it can scale its instances out or in automatically, based on job queue demand.
        
                  If the state is ``DISABLED`` , then the AWS Batch scheduler does not attempt to place jobs within the environment. Jobs in a ``STARTING`` or ``RUNNING`` state continue to progress normally. Managed compute environments in the ``DISABLED`` state do not scale out; however, they scale in to ``minvCpus`` value once instances become idle.
        
                - **status** *(string) --* 
        
                  The current status of the compute environment (for example, ``CREATING`` or ``VALID`` ).
        
                - **statusReason** *(string) --* 
        
                  A short, human-readable string to provide additional details about the current status of the compute environment.
        
                - **computeResources** *(dict) --* 
        
                  The compute resources defined for the compute environment. 
        
                  - **type** *(string) --* 
        
                    The type of compute environment.
        
                  - **minvCpus** *(integer) --* 
        
                    The minimum number of EC2 vCPUs that an environment should maintain (even if the compute environment is ``DISABLED`` ). 
        
                  - **maxvCpus** *(integer) --* 
        
                    The maximum number of EC2 vCPUs that an environment can reach. 
        
                  - **desiredvCpus** *(integer) --* 
        
                    The desired number of EC2 vCPUS in the compute environment. 
        
                  - **instanceTypes** *(list) --* 
        
                    The instances types that may be launched. You can specify instance families to launch any instance type within those families (for example, ``c4`` or ``p3`` ), or you can specify specific sizes within a family (such as ``c4.8xlarge`` ). You can also choose ``optimal`` to pick instance types (from the latest C, M, and R instance families) on the fly that match the demand of your job queues.
        
                    - *(string) --* 
                
                  - **imageId** *(string) --* 
        
                    The Amazon Machine Image (AMI) ID used for instances launched in the compute environment.
        
                  - **subnets** *(list) --* 
        
                    The VPC subnets into which the compute resources are launched. 
        
                    - *(string) --* 
                
                  - **securityGroupIds** *(list) --* 
        
                    The EC2 security group that is associated with instances launched in the compute environment. 
        
                    - *(string) --* 
                
                  - **ec2KeyPair** *(string) --* 
        
                    The EC2 key pair that is used for instances launched in the compute environment.
        
                  - **instanceRole** *(string) --* 
        
                    The Amazon ECS instance profile applied to Amazon EC2 instances in a compute environment. You can specify the short name or full Amazon Resource Name (ARN) of an instance profile. For example, ``ecsInstanceRole`` or ``arn:aws:iam::<aws_account_id>:instance-profile/ecsInstanceRole`` . For more information, see `Amazon ECS Instance Role <http://docs.aws.amazon.com/batch/latest/userguide/instance_IAM_role.html>`__ in the *AWS Batch User Guide* .
        
                  - **tags** *(dict) --* 
        
                    Key-value pair tags to be applied to resources that are launched in the compute environment. 
        
                    - *(string) --* 
                      
                      - *(string) --* 
                
                  - **bidPercentage** *(integer) --* 
        
                    The maximum percentage that a Spot Instance price can be when compared with the On-Demand price for that instance type before instances are launched. For example, if your maximum percentage is 20%, then the Spot price must be below 20% of the current On-Demand price for that EC2 instance. You always pay the lowest (market) price and never more than your maximum percentage. If you leave this field empty, the default value is 100% of the On-Demand price.
        
                  - **spotIamFleetRole** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a ``SPOT`` compute environment.
        
                  - **launchTemplate** *(dict) --* 
        
                    The launch template to use for your compute resources. Any other compute resource parameters that you specify in a  CreateComputeEnvironment API operation override the same parameters in the launch template. You must specify either the launch template ID or launch template name in the request, but not both. 
        
                    - **launchTemplateId** *(string) --* 
        
                      The ID of the launch template.
        
                    - **launchTemplateName** *(string) --* 
        
                      The name of the launch template.
        
                    - **version** *(string) --* 
        
                      The version number of the launch template.
        
                      Default: The default version of the launch template.
        
                - **serviceRole** *(string) --* 
        
                  The service role associated with the compute environment that allows AWS Batch to make calls to AWS API operations on your behalf.
        
            - **nextToken** *(string) --* 
        
              The ``nextToken`` value to include in a future ``DescribeComputeEnvironments`` request. When the results of a ``DescribeJobDefinitions`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.
        
        """
        pass

    def describe_job_definitions(self, jobDefinitions: List = None, maxResults: int = None, jobDefinitionName: str = None, status: str = None, nextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/DescribeJobDefinitions>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_job_definitions(
              jobDefinitions=[
                  \'string\',
              ],
              maxResults=123,
              jobDefinitionName=\'string\',
              status=\'string\',
              nextToken=\'string\'
          )
        :type jobDefinitions: list
        :param jobDefinitions: 
        
          A space-separated list of up to 100 job definition names or full Amazon Resource Name (ARN) entries.
        
          - *(string) --* 
        
        :type maxResults: integer
        :param maxResults: 
        
          The maximum number of results returned by ``DescribeJobDefinitions`` in paginated output. When this parameter is used, ``DescribeJobDefinitions`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``DescribeJobDefinitions`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``DescribeJobDefinitions`` returns up to 100 results and a ``nextToken`` value if applicable.
        
        :type jobDefinitionName: string
        :param jobDefinitionName: 
        
          The name of the job definition to describe.
        
        :type status: string
        :param status: 
        
          The status with which to filter job definitions.
        
        :type nextToken: string
        :param nextToken: 
        
          The ``nextToken`` value returned from a previous paginated ``DescribeJobDefinitions`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value. This value is ``null`` when there are no more results to return.
        
          .. note::
        
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'jobDefinitions\': [
                    {
                        \'jobDefinitionName\': \'string\',
                        \'jobDefinitionArn\': \'string\',
                        \'revision\': 123,
                        \'status\': \'string\',
                        \'type\': \'string\',
                        \'parameters\': {
                            \'string\': \'string\'
                        },
                        \'retryStrategy\': {
                            \'attempts\': 123
                        },
                        \'containerProperties\': {
                            \'image\': \'string\',
                            \'vcpus\': 123,
                            \'memory\': 123,
                            \'command\': [
                                \'string\',
                            ],
                            \'jobRoleArn\': \'string\',
                            \'volumes\': [
                                {
                                    \'host\': {
                                        \'sourcePath\': \'string\'
                                    },
                                    \'name\': \'string\'
                                },
                            ],
                            \'environment\': [
                                {
                                    \'name\': \'string\',
                                    \'value\': \'string\'
                                },
                            ],
                            \'mountPoints\': [
                                {
                                    \'containerPath\': \'string\',
                                    \'readOnly\': True|False,
                                    \'sourceVolume\': \'string\'
                                },
                            ],
                            \'readonlyRootFilesystem\': True|False,
                            \'privileged\': True|False,
                            \'ulimits\': [
                                {
                                    \'hardLimit\': 123,
                                    \'name\': \'string\',
                                    \'softLimit\': 123
                                },
                            ],
                            \'user\': \'string\'
                        },
                        \'timeout\': {
                            \'attemptDurationSeconds\': 123
                        }
                    },
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **jobDefinitions** *(list) --* 
        
              The list of job definitions. 
        
              - *(dict) --* 
        
                An object representing an AWS Batch job definition.
        
                - **jobDefinitionName** *(string) --* 
        
                  The name of the job definition. 
        
                - **jobDefinitionArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) for the job definition. 
        
                - **revision** *(integer) --* 
        
                  The revision of the job definition.
        
                - **status** *(string) --* 
        
                  The status of the job definition.
        
                - **type** *(string) --* 
        
                  The type of job definition.
        
                - **parameters** *(dict) --* 
        
                  Default parameters or parameter substitution placeholders that are set in the job definition. Parameters are specified as a key-value pair mapping. Parameters in a ``SubmitJob`` request override any corresponding parameter defaults from the job definition.
        
                  - *(string) --* 
                    
                    - *(string) --* 
              
                - **retryStrategy** *(dict) --* 
        
                  The retry strategy to use for failed jobs that are submitted with this job definition.
        
                  - **attempts** *(integer) --* 
        
                    The number of times to move a job to the ``RUNNABLE`` status. You may specify between 1 and 10 attempts. If the value of ``attempts`` is greater than one, the job is retried if it fails until it has moved to ``RUNNABLE`` that many times.
        
                - **containerProperties** *(dict) --* 
        
                  An object with various properties specific to container-based jobs. 
        
                  - **image** *(string) --* 
        
                    The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with `` *repository-url* /*image* :*tag* `` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to ``Image`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``IMAGE`` parameter of `docker run <https://docs.docker.com/engine/reference/run/>`__ .
        
                    * Images in Amazon ECR repositories use the full registry and repository URI (for example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).  
                     
                    * Images in official repositories on Docker Hub use a single name (for example, ``ubuntu`` or ``mongo`` ). 
                     
                    * Images in other repositories on Docker Hub are qualified with an organization name (for example, ``amazon/amazon-ecs-agent`` ). 
                     
                    * Images in other online repositories are qualified further by a domain name (for example, ``quay.io/assemblyline/ubuntu`` ). 
                     
                  - **vcpus** *(integer) --* 
        
                    The number of vCPUs reserved for the container. This parameter maps to ``CpuShares`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--cpu-shares`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . Each vCPU is equivalent to 1,024 CPU shares. You must specify at least one vCPU.
        
                  - **memory** *(integer) --* 
        
                    The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. This parameter maps to ``Memory`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--memory`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . You must specify at least 4 MiB of memory for a job.
        
                    .. note::
        
                      If you are trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular instance type, see `Memory Management <http://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__ in the *AWS Batch User Guide* .
        
                  - **command** *(list) --* 
        
                    The command that is passed to the container. This parameter maps to ``Cmd`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``COMMAND`` parameter to `docker run <https://docs.docker.com/engine/reference/run/>`__ . For more information, see `https\://docs.docker.com/engine/reference/builder/#cmd <https://docs.docker.com/engine/reference/builder/#cmd>`__ .
        
                    - *(string) --* 
                
                  - **jobRoleArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS permissions.
        
                  - **volumes** *(list) --* 
        
                    A list of data volumes used in a job.
        
                    - *(dict) --* 
        
                      A data volume used in a job\'s container properties.
        
                      - **host** *(dict) --* 
        
                        The contents of the ``host`` parameter determine whether your data volume persists on the host container instance and where it is stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data is not guaranteed to persist after the containers associated with it stop running.
        
                        - **sourcePath** *(string) --* 
        
                          The path on the host container instance that is presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If the ``host`` parameter contains a ``sourcePath`` file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the ``sourcePath`` value does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.
        
                      - **name** *(string) --* 
        
                        The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the ``sourceVolume`` parameter of container definition ``mountPoints`` .
        
                  - **environment** *(list) --* 
        
                    The environment variables to pass to a container. This parameter maps to ``Env`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--env`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
        
                    .. warning::
        
                      We do not recommend using plaintext environment variables for sensitive information, such as credential data.
        
                    .. note::
        
                      Environment variables must not start with ``AWS_BATCH`` ; this naming convention is reserved for variables that are set by the AWS Batch service.
        
                    - *(dict) --* 
        
                      A key-value pair object.
        
                      - **name** *(string) --* 
        
                        The name of the key-value pair. For environment variables, this is the name of the environment variable.
        
                      - **value** *(string) --* 
        
                        The value of the key-value pair. For environment variables, this is the value of the environment variable.
        
                  - **mountPoints** *(list) --* 
        
                    The mount points for data volumes in your container. This parameter maps to ``Volumes`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--volume`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
        
                    - *(dict) --* 
        
                      Details on a Docker volume mount point that is used in a job\'s container properties.
        
                      - **containerPath** *(string) --* 
        
                        The path on the container at which to mount the host volume.
        
                      - **readOnly** *(boolean) --* 
        
                        If this value is ``true`` , the container has read-only access to the volume; otherwise, the container can write to the volume. The default value is ``false`` .
        
                      - **sourceVolume** *(string) --* 
        
                        The name of the volume to mount.
        
                  - **readonlyRootFilesystem** *(boolean) --* 
        
                    When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--read-only`` option to ``docker run`` .
        
                  - **privileged** *(boolean) --* 
        
                    When this parameter is true, the container is given elevated privileges on the host container instance (similar to the ``root`` user). This parameter maps to ``Privileged`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--privileged`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
        
                  - **ulimits** *(list) --* 
        
                    A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--ulimit`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
        
                    - *(dict) --* 
        
                      The ``ulimit`` settings to pass to the container.
        
                      - **hardLimit** *(integer) --* 
        
                        The hard limit for the ``ulimit`` type.
        
                      - **name** *(string) --* 
        
                        The ``type`` of the ``ulimit`` .
        
                      - **softLimit** *(integer) --* 
        
                        The soft limit for the ``ulimit`` type.
        
                  - **user** *(string) --* 
        
                    The user name to use inside the container. This parameter maps to ``User`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--user`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
        
                - **timeout** *(dict) --* 
        
                  The timeout configuration for jobs that are submitted with this job definition. You can specify a timeout duration after which AWS Batch terminates your jobs if they have not finished.
        
                  - **attemptDurationSeconds** *(integer) --* 
        
                    The time duration in seconds (measured from the job attempt\'s ``startedAt`` timestamp) after which AWS Batch terminates your jobs if they have not finished.
        
            - **nextToken** *(string) --* 
        
              The ``nextToken`` value to include in a future ``DescribeJobDefinitions`` request. When the results of a ``DescribeJobDefinitions`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.
        
        """
        pass

    def describe_job_queues(self, jobQueues: List = None, maxResults: int = None, nextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/DescribeJobQueues>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_job_queues(
              jobQueues=[
                  \'string\',
              ],
              maxResults=123,
              nextToken=\'string\'
          )
        :type jobQueues: list
        :param jobQueues: 
        
          A list of up to 100 queue names or full queue Amazon Resource Name (ARN) entries.
        
          - *(string) --* 
        
        :type maxResults: integer
        :param maxResults: 
        
          The maximum number of results returned by ``DescribeJobQueues`` in paginated output. When this parameter is used, ``DescribeJobQueues`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``DescribeJobQueues`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``DescribeJobQueues`` returns up to 100 results and a ``nextToken`` value if applicable.
        
        :type nextToken: string
        :param nextToken: 
        
          The ``nextToken`` value returned from a previous paginated ``DescribeJobQueues`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value. This value is ``null`` when there are no more results to return.
        
          .. note::
        
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'jobQueues\': [
                    {
                        \'jobQueueName\': \'string\',
                        \'jobQueueArn\': \'string\',
                        \'state\': \'ENABLED\'|\'DISABLED\',
                        \'status\': \'CREATING\'|\'UPDATING\'|\'DELETING\'|\'DELETED\'|\'VALID\'|\'INVALID\',
                        \'statusReason\': \'string\',
                        \'priority\': 123,
                        \'computeEnvironmentOrder\': [
                            {
                                \'order\': 123,
                                \'computeEnvironment\': \'string\'
                            },
                        ]
                    },
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **jobQueues** *(list) --* 
        
              The list of job queues. 
        
              - *(dict) --* 
        
                An object representing the details of an AWS Batch job queue.
        
                - **jobQueueName** *(string) --* 
        
                  The name of the job queue.
        
                - **jobQueueArn** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the job queue.
        
                - **state** *(string) --* 
        
                  Describes the ability of the queue to accept new jobs.
        
                - **status** *(string) --* 
        
                  The status of the job queue (for example, ``CREATING`` or ``VALID`` ).
        
                - **statusReason** *(string) --* 
        
                  A short, human-readable string to provide additional details about the current status of the job queue.
        
                - **priority** *(integer) --* 
        
                  The priority of the job queue. 
        
                - **computeEnvironmentOrder** *(list) --* 
        
                  The compute environments that are attached to the job queue and the order in which job placement is preferred. Compute environments are selected for job placement in ascending order.
        
                  - *(dict) --* 
        
                    The order in which compute environments are tried for job placement within a queue. Compute environments are tried in ascending order. For example, if two compute environments are associated with a job queue, the compute environment with a lower order integer value is tried for job placement first.
        
                    - **order** *(integer) --* 
        
                      The order of the compute environment.
        
                    - **computeEnvironment** *(string) --* 
        
                      The Amazon Resource Name (ARN) of the compute environment.
        
            - **nextToken** *(string) --* 
        
              The ``nextToken`` value to include in a future ``DescribeJobQueues`` request. When the results of a ``DescribeJobQueues`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.
        
        """
        pass

    def describe_jobs(self, jobs: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/DescribeJobs>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_jobs(
              jobs=[
                  \'string\',
              ]
          )
        :type jobs: list
        :param jobs: **[REQUIRED]** 
        
          A space-separated list of up to 100 job IDs.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'jobs\': [
                    {
                        \'jobName\': \'string\',
                        \'jobId\': \'string\',
                        \'jobQueue\': \'string\',
                        \'status\': \'SUBMITTED\'|\'PENDING\'|\'RUNNABLE\'|\'STARTING\'|\'RUNNING\'|\'SUCCEEDED\'|\'FAILED\',
                        \'attempts\': [
                            {
                                \'container\': {
                                    \'containerInstanceArn\': \'string\',
                                    \'taskArn\': \'string\',
                                    \'exitCode\': 123,
                                    \'reason\': \'string\',
                                    \'logStreamName\': \'string\'
                                },
                                \'startedAt\': 123,
                                \'stoppedAt\': 123,
                                \'statusReason\': \'string\'
                            },
                        ],
                        \'statusReason\': \'string\',
                        \'createdAt\': 123,
                        \'retryStrategy\': {
                            \'attempts\': 123
                        },
                        \'startedAt\': 123,
                        \'stoppedAt\': 123,
                        \'dependsOn\': [
                            {
                                \'jobId\': \'string\',
                                \'type\': \'N_TO_N\'|\'SEQUENTIAL\'
                            },
                        ],
                        \'jobDefinition\': \'string\',
                        \'parameters\': {
                            \'string\': \'string\'
                        },
                        \'container\': {
                            \'image\': \'string\',
                            \'vcpus\': 123,
                            \'memory\': 123,
                            \'command\': [
                                \'string\',
                            ],
                            \'jobRoleArn\': \'string\',
                            \'volumes\': [
                                {
                                    \'host\': {
                                        \'sourcePath\': \'string\'
                                    },
                                    \'name\': \'string\'
                                },
                            ],
                            \'environment\': [
                                {
                                    \'name\': \'string\',
                                    \'value\': \'string\'
                                },
                            ],
                            \'mountPoints\': [
                                {
                                    \'containerPath\': \'string\',
                                    \'readOnly\': True|False,
                                    \'sourceVolume\': \'string\'
                                },
                            ],
                            \'readonlyRootFilesystem\': True|False,
                            \'ulimits\': [
                                {
                                    \'hardLimit\': 123,
                                    \'name\': \'string\',
                                    \'softLimit\': 123
                                },
                            ],
                            \'privileged\': True|False,
                            \'user\': \'string\',
                            \'exitCode\': 123,
                            \'reason\': \'string\',
                            \'containerInstanceArn\': \'string\',
                            \'taskArn\': \'string\',
                            \'logStreamName\': \'string\'
                        },
                        \'arrayProperties\': {
                            \'statusSummary\': {
                                \'string\': 123
                            },
                            \'size\': 123,
                            \'index\': 123
                        },
                        \'timeout\': {
                            \'attemptDurationSeconds\': 123
                        }
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **jobs** *(list) --* 
        
              The list of jobs. 
        
              - *(dict) --* 
        
                An object representing an AWS Batch job.
        
                - **jobName** *(string) --* 
        
                  The name of the job.
        
                - **jobId** *(string) --* 
        
                  The ID for the job.
        
                - **jobQueue** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the job queue with which the job is associated.
        
                - **status** *(string) --* 
        
                  The current status for the job. 
        
                  .. note::
        
                    If your jobs do not progress to ``STARTING`` , see `Jobs Stuck in ``RUNNABLE`` Status <http://docs.aws.amazon.com/batch/latest/userguide/troubleshooting.html#job_stuck_in_runnable>`__ in the troubleshooting section of the *AWS Batch User Guide* .
        
                - **attempts** *(list) --* 
        
                  A list of job attempts associated with this job.
        
                  - *(dict) --* 
        
                    An object representing a job attempt.
        
                    - **container** *(dict) --* 
        
                      Details about the container in this job attempt.
        
                      - **containerInstanceArn** *(string) --* 
        
                        The Amazon Resource Name (ARN) of the Amazon ECS container instance that hosts the job attempt.
        
                      - **taskArn** *(string) --* 
        
                        The Amazon Resource Name (ARN) of the Amazon ECS task that is associated with the job attempt. Each container attempt receives a task ARN when they reach the ``STARTING`` status.
        
                      - **exitCode** *(integer) --* 
        
                        The exit code for the job attempt. A non-zero exit code is considered a failure.
        
                      - **reason** *(string) --* 
        
                        A short (255 max characters) human-readable string to provide additional details about a running or stopped container.
        
                      - **logStreamName** *(string) --* 
        
                        The name of the CloudWatch Logs log stream associated with the container. The log group for AWS Batch jobs is ``/aws/batch/job`` . Each container attempt receives a log stream name when they reach the ``RUNNING`` status.
        
                    - **startedAt** *(integer) --* 
        
                      The Unix time stamp (in seconds and milliseconds) for when the attempt was started (when the attempt transitioned from the ``STARTING`` state to the ``RUNNING`` state).
        
                    - **stoppedAt** *(integer) --* 
        
                      The Unix time stamp (in seconds and milliseconds) for when the attempt was stopped (when the attempt transitioned from the ``RUNNING`` state to a terminal state, such as ``SUCCEEDED`` or ``FAILED`` ).
        
                    - **statusReason** *(string) --* 
        
                      A short, human-readable string to provide additional details about the current status of the job attempt.
        
                - **statusReason** *(string) --* 
        
                  A short, human-readable string to provide additional details about the current status of the job. 
        
                - **createdAt** *(integer) --* 
        
                  The Unix time stamp (in seconds and milliseconds) for when the job was created. For non-array jobs and parent array jobs, this is when the job entered the ``SUBMITTED`` state (at the time  SubmitJob was called). For array child jobs, this is when the child job was spawned by its parent and entered the ``PENDING`` state.
        
                - **retryStrategy** *(dict) --* 
        
                  The retry strategy to use for this job if an attempt fails.
        
                  - **attempts** *(integer) --* 
        
                    The number of times to move a job to the ``RUNNABLE`` status. You may specify between 1 and 10 attempts. If the value of ``attempts`` is greater than one, the job is retried if it fails until it has moved to ``RUNNABLE`` that many times.
        
                - **startedAt** *(integer) --* 
        
                  The Unix time stamp (in seconds and milliseconds) for when the job was started (when the job transitioned from the ``STARTING`` state to the ``RUNNING`` state).
        
                - **stoppedAt** *(integer) --* 
        
                  The Unix time stamp (in seconds and milliseconds) for when the job was stopped (when the job transitioned from the ``RUNNING`` state to a terminal state, such as ``SUCCEEDED`` or ``FAILED`` ).
        
                - **dependsOn** *(list) --* 
        
                  A list of job names or IDs on which this job depends.
        
                  - *(dict) --* 
        
                    An object representing an AWS Batch job dependency.
        
                    - **jobId** *(string) --* 
        
                      The job ID of the AWS Batch job associated with this dependency.
        
                    - **type** *(string) --* 
        
                      The type of the job dependency.
        
                - **jobDefinition** *(string) --* 
        
                  The job definition that is used by this job.
        
                - **parameters** *(dict) --* 
        
                  Additional parameters passed to the job that replace parameter substitution placeholders or override any corresponding parameter defaults from the job definition. 
        
                  - *(string) --* 
                    
                    - *(string) --* 
              
                - **container** *(dict) --* 
        
                  An object representing the details of the container that is associated with the job.
        
                  - **image** *(string) --* 
        
                    The image used to start the container.
        
                  - **vcpus** *(integer) --* 
        
                    The number of VCPUs allocated for the job. 
        
                  - **memory** *(integer) --* 
        
                    The number of MiB of memory reserved for the job.
        
                  - **command** *(list) --* 
        
                    The command that is passed to the container. 
        
                    - *(string) --* 
                
                  - **jobRoleArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) associated with the job upon execution. 
        
                  - **volumes** *(list) --* 
        
                    A list of volumes associated with the job.
        
                    - *(dict) --* 
        
                      A data volume used in a job\'s container properties.
        
                      - **host** *(dict) --* 
        
                        The contents of the ``host`` parameter determine whether your data volume persists on the host container instance and where it is stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data is not guaranteed to persist after the containers associated with it stop running.
        
                        - **sourcePath** *(string) --* 
        
                          The path on the host container instance that is presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If the ``host`` parameter contains a ``sourcePath`` file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the ``sourcePath`` value does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.
        
                      - **name** *(string) --* 
        
                        The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the ``sourceVolume`` parameter of container definition ``mountPoints`` .
        
                  - **environment** *(list) --* 
        
                    The environment variables to pass to a container.
        
                    .. note::
        
                      Environment variables must not start with ``AWS_BATCH`` ; this naming convention is reserved for variables that are set by the AWS Batch service.
        
                    - *(dict) --* 
        
                      A key-value pair object.
        
                      - **name** *(string) --* 
        
                        The name of the key-value pair. For environment variables, this is the name of the environment variable.
        
                      - **value** *(string) --* 
        
                        The value of the key-value pair. For environment variables, this is the value of the environment variable.
        
                  - **mountPoints** *(list) --* 
        
                    The mount points for data volumes in your container.
        
                    - *(dict) --* 
        
                      Details on a Docker volume mount point that is used in a job\'s container properties.
        
                      - **containerPath** *(string) --* 
        
                        The path on the container at which to mount the host volume.
        
                      - **readOnly** *(boolean) --* 
        
                        If this value is ``true`` , the container has read-only access to the volume; otherwise, the container can write to the volume. The default value is ``false`` .
        
                      - **sourceVolume** *(string) --* 
        
                        The name of the volume to mount.
        
                  - **readonlyRootFilesystem** *(boolean) --* 
        
                    When this parameter is true, the container is given read-only access to its root file system.
        
                  - **ulimits** *(list) --* 
        
                    A list of ``ulimit`` values to set in the container.
        
                    - *(dict) --* 
        
                      The ``ulimit`` settings to pass to the container.
        
                      - **hardLimit** *(integer) --* 
        
                        The hard limit for the ``ulimit`` type.
        
                      - **name** *(string) --* 
        
                        The ``type`` of the ``ulimit`` .
        
                      - **softLimit** *(integer) --* 
        
                        The soft limit for the ``ulimit`` type.
        
                  - **privileged** *(boolean) --* 
        
                    When this parameter is true, the container is given elevated privileges on the host container instance (similar to the ``root`` user).
        
                  - **user** *(string) --* 
        
                    The user name to use inside the container.
        
                  - **exitCode** *(integer) --* 
        
                    The exit code to return upon completion.
        
                  - **reason** *(string) --* 
        
                    A short (255 max characters) human-readable string to provide additional details about a running or stopped container.
        
                  - **containerInstanceArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the container instance on which the container is running.
        
                  - **taskArn** *(string) --* 
        
                    The Amazon Resource Name (ARN) of the Amazon ECS task that is associated with the container job. Each container attempt receives a task ARN when they reach the ``STARTING`` status.
        
                  - **logStreamName** *(string) --* 
        
                    The name of the CloudWatch Logs log stream associated with the container. The log group for AWS Batch jobs is ``/aws/batch/job`` . Each container attempt receives a log stream name when they reach the ``RUNNING`` status.
        
                - **arrayProperties** *(dict) --* 
        
                  The array properties of the job, if it is an array job.
        
                  - **statusSummary** *(dict) --* 
        
                    A summary of the number of array job children in each available job status. This parameter is returned for parent array jobs.
        
                    - *(string) --* 
                      
                      - *(integer) --* 
                
                  - **size** *(integer) --* 
        
                    The size of the array job. This parameter is returned for parent array jobs.
        
                  - **index** *(integer) --* 
        
                    The job index within the array that is associated with this job. This parameter is returned for array job children.
        
                - **timeout** *(dict) --* 
        
                  The timeout configuration for the job. 
        
                  - **attemptDurationSeconds** *(integer) --* 
        
                    The time duration in seconds (measured from the job attempt\'s ``startedAt`` timestamp) after which AWS Batch terminates your jobs if they have not finished.
        
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

    def list_jobs(self, jobQueue: str = None, arrayJobId: str = None, jobStatus: str = None, maxResults: int = None, nextToken: str = None) -> Dict:
        """
        
        You can filter the results by job status with the ``jobStatus`` parameter. If you do not specify a status, only ``RUNNING`` jobs are returned.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/ListJobs>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_jobs(
              jobQueue=\'string\',
              arrayJobId=\'string\',
              jobStatus=\'SUBMITTED\'|\'PENDING\'|\'RUNNABLE\'|\'STARTING\'|\'RUNNING\'|\'SUCCEEDED\'|\'FAILED\',
              maxResults=123,
              nextToken=\'string\'
          )
        :type jobQueue: string
        :param jobQueue: 
        
          The name or full Amazon Resource Name (ARN) of the job queue with which to list jobs. You must specify either a job queue or an array job ID.
        
        :type arrayJobId: string
        :param arrayJobId: 
        
          The job ID for an array job. Specifying an array job ID with this parameter lists all child jobs from within the specified array. You must specify either a job queue or an array job ID.
        
        :type jobStatus: string
        :param jobStatus: 
        
          The job status with which to filter jobs in the specified queue. If you do not specify a status, only ``RUNNING`` jobs are returned.
        
        :type maxResults: integer
        :param maxResults: 
        
          The maximum number of results returned by ``ListJobs`` in paginated output. When this parameter is used, ``ListJobs`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListJobs`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListJobs`` returns up to 100 results and a ``nextToken`` value if applicable.
        
        :type nextToken: string
        :param nextToken: 
        
          The ``nextToken`` value returned from a previous paginated ``ListJobs`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value. This value is ``null`` when there are no more results to return.
        
          .. note::
        
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'jobSummaryList\': [
                    {
                        \'jobId\': \'string\',
                        \'jobName\': \'string\',
                        \'createdAt\': 123,
                        \'status\': \'SUBMITTED\'|\'PENDING\'|\'RUNNABLE\'|\'STARTING\'|\'RUNNING\'|\'SUCCEEDED\'|\'FAILED\',
                        \'statusReason\': \'string\',
                        \'startedAt\': 123,
                        \'stoppedAt\': 123,
                        \'container\': {
                            \'exitCode\': 123,
                            \'reason\': \'string\'
                        },
                        \'arrayProperties\': {
                            \'size\': 123,
                            \'index\': 123
                        }
                    },
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **jobSummaryList** *(list) --* 
        
              A list of job summaries that match the request.
        
              - *(dict) --* 
        
                An object representing summary details of a job.
        
                - **jobId** *(string) --* 
        
                  The ID of the job.
        
                - **jobName** *(string) --* 
        
                  The name of the job.
        
                - **createdAt** *(integer) --* 
        
                  The Unix time stamp for when the job was created. For non-array jobs and parent array jobs, this is when the job entered the ``SUBMITTED`` state (at the time  SubmitJob was called). For array child jobs, this is when the child job was spawned by its parent and entered the ``PENDING`` state.
        
                - **status** *(string) --* 
        
                  The current status for the job.
        
                - **statusReason** *(string) --* 
        
                  A short, human-readable string to provide additional details about the current status of the job.
        
                - **startedAt** *(integer) --* 
        
                  The Unix time stamp for when the job was started (when the job transitioned from the ``STARTING`` state to the ``RUNNING`` state).
        
                - **stoppedAt** *(integer) --* 
        
                  The Unix time stamp for when the job was stopped (when the job transitioned from the ``RUNNING`` state to a terminal state, such as ``SUCCEEDED`` or ``FAILED`` ).
        
                - **container** *(dict) --* 
        
                  An object representing the details of the container that is associated with the job.
        
                  - **exitCode** *(integer) --* 
        
                    The exit code to return upon completion.
        
                  - **reason** *(string) --* 
        
                    A short (255 max characters) human-readable string to provide additional details about a running or stopped container.
        
                - **arrayProperties** *(dict) --* 
        
                  The array properties of the job, if it is an array job.
        
                  - **size** *(integer) --* 
        
                    The size of the array job. This parameter is returned for parent array jobs.
        
                  - **index** *(integer) --* 
        
                    The job index within the array that is associated with this job. This parameter is returned for children of array jobs.
        
            - **nextToken** *(string) --* 
        
              The ``nextToken`` value to include in a future ``ListJobs`` request. When the results of a ``ListJobs`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.
        
        """
        pass

    def register_job_definition(self, jobDefinitionName: str, type: str, parameters: Dict = None, containerProperties: Dict = None, retryStrategy: Dict = None, timeout: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/RegisterJobDefinition>`_
        
        **Request Syntax** 
        ::
        
          response = client.register_job_definition(
              jobDefinitionName=\'string\',
              type=\'container\',
              parameters={
                  \'string\': \'string\'
              },
              containerProperties={
                  \'image\': \'string\',
                  \'vcpus\': 123,
                  \'memory\': 123,
                  \'command\': [
                      \'string\',
                  ],
                  \'jobRoleArn\': \'string\',
                  \'volumes\': [
                      {
                          \'host\': {
                              \'sourcePath\': \'string\'
                          },
                          \'name\': \'string\'
                      },
                  ],
                  \'environment\': [
                      {
                          \'name\': \'string\',
                          \'value\': \'string\'
                      },
                  ],
                  \'mountPoints\': [
                      {
                          \'containerPath\': \'string\',
                          \'readOnly\': True|False,
                          \'sourceVolume\': \'string\'
                      },
                  ],
                  \'readonlyRootFilesystem\': True|False,
                  \'privileged\': True|False,
                  \'ulimits\': [
                      {
                          \'hardLimit\': 123,
                          \'name\': \'string\',
                          \'softLimit\': 123
                      },
                  ],
                  \'user\': \'string\'
              },
              retryStrategy={
                  \'attempts\': 123
              },
              timeout={
                  \'attemptDurationSeconds\': 123
              }
          )
        :type jobDefinitionName: string
        :param jobDefinitionName: **[REQUIRED]** 
        
          The name of the job definition to register. Up to 128 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.
        
        :type type: string
        :param type: **[REQUIRED]** 
        
          The type of job definition.
        
        :type parameters: dict
        :param parameters: 
        
          Default parameter substitution placeholders to set in the job definition. Parameters are specified as a key-value pair mapping. Parameters in a ``SubmitJob`` request override any corresponding parameter defaults from the job definition.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type containerProperties: dict
        :param containerProperties: 
        
          An object with various properties specific for container-based jobs. This parameter is required if the ``type`` parameter is ``container`` .
        
          - **image** *(string) --* **[REQUIRED]** 
        
            The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with `` *repository-url* /*image* :*tag* `` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to ``Image`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``IMAGE`` parameter of `docker run <https://docs.docker.com/engine/reference/run/>`__ .
        
            * Images in Amazon ECR repositories use the full registry and repository URI (for example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ).  
             
            * Images in official repositories on Docker Hub use a single name (for example, ``ubuntu`` or ``mongo`` ). 
             
            * Images in other repositories on Docker Hub are qualified with an organization name (for example, ``amazon/amazon-ecs-agent`` ). 
             
            * Images in other online repositories are qualified further by a domain name (for example, ``quay.io/assemblyline/ubuntu`` ). 
             
          - **vcpus** *(integer) --* **[REQUIRED]** 
        
            The number of vCPUs reserved for the container. This parameter maps to ``CpuShares`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--cpu-shares`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . Each vCPU is equivalent to 1,024 CPU shares. You must specify at least one vCPU.
        
          - **memory** *(integer) --* **[REQUIRED]** 
        
            The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. This parameter maps to ``Memory`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--memory`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . You must specify at least 4 MiB of memory for a job.
        
            .. note::
        
              If you are trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular instance type, see `Memory Management <http://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__ in the *AWS Batch User Guide* .
        
          - **command** *(list) --* 
        
            The command that is passed to the container. This parameter maps to ``Cmd`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``COMMAND`` parameter to `docker run <https://docs.docker.com/engine/reference/run/>`__ . For more information, see `https\://docs.docker.com/engine/reference/builder/#cmd <https://docs.docker.com/engine/reference/builder/#cmd>`__ .
        
            - *(string) --* 
        
          - **jobRoleArn** *(string) --* 
        
            The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS permissions.
        
          - **volumes** *(list) --* 
        
            A list of data volumes used in a job.
        
            - *(dict) --* 
        
              A data volume used in a job\'s container properties.
        
              - **host** *(dict) --* 
        
                The contents of the ``host`` parameter determine whether your data volume persists on the host container instance and where it is stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data is not guaranteed to persist after the containers associated with it stop running.
        
                - **sourcePath** *(string) --* 
        
                  The path on the host container instance that is presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If the ``host`` parameter contains a ``sourcePath`` file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the ``sourcePath`` value does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.
        
              - **name** *(string) --* 
        
                The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the ``sourceVolume`` parameter of container definition ``mountPoints`` .
        
          - **environment** *(list) --* 
        
            The environment variables to pass to a container. This parameter maps to ``Env`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--env`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
        
            .. warning::
        
              We do not recommend using plaintext environment variables for sensitive information, such as credential data.
        
            .. note::
        
              Environment variables must not start with ``AWS_BATCH`` ; this naming convention is reserved for variables that are set by the AWS Batch service.
        
            - *(dict) --* 
        
              A key-value pair object.
        
              - **name** *(string) --* 
        
                The name of the key-value pair. For environment variables, this is the name of the environment variable.
        
              - **value** *(string) --* 
        
                The value of the key-value pair. For environment variables, this is the value of the environment variable.
        
          - **mountPoints** *(list) --* 
        
            The mount points for data volumes in your container. This parameter maps to ``Volumes`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--volume`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
        
            - *(dict) --* 
        
              Details on a Docker volume mount point that is used in a job\'s container properties.
        
              - **containerPath** *(string) --* 
        
                The path on the container at which to mount the host volume.
        
              - **readOnly** *(boolean) --* 
        
                If this value is ``true`` , the container has read-only access to the volume; otherwise, the container can write to the volume. The default value is ``false`` .
        
              - **sourceVolume** *(string) --* 
        
                The name of the volume to mount.
        
          - **readonlyRootFilesystem** *(boolean) --* 
        
            When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--read-only`` option to ``docker run`` .
        
          - **privileged** *(boolean) --* 
        
            When this parameter is true, the container is given elevated privileges on the host container instance (similar to the ``root`` user). This parameter maps to ``Privileged`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--privileged`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
        
          - **ulimits** *(list) --* 
        
            A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--ulimit`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
        
            - *(dict) --* 
        
              The ``ulimit`` settings to pass to the container.
        
              - **hardLimit** *(integer) --* **[REQUIRED]** 
        
                The hard limit for the ``ulimit`` type.
        
              - **name** *(string) --* **[REQUIRED]** 
        
                The ``type`` of the ``ulimit`` .
        
              - **softLimit** *(integer) --* **[REQUIRED]** 
        
                The soft limit for the ``ulimit`` type.
        
          - **user** *(string) --* 
        
            The user name to use inside the container. This parameter maps to ``User`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.23/>`__ and the ``--user`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
        
        :type retryStrategy: dict
        :param retryStrategy: 
        
          The retry strategy to use for failed jobs that are submitted with this job definition. Any retry strategy that is specified during a  SubmitJob operation overrides the retry strategy defined here. If a job is terminated due to a timeout, it is not retried. 
        
          - **attempts** *(integer) --* 
        
            The number of times to move a job to the ``RUNNABLE`` status. You may specify between 1 and 10 attempts. If the value of ``attempts`` is greater than one, the job is retried if it fails until it has moved to ``RUNNABLE`` that many times.
        
        :type timeout: dict
        :param timeout: 
        
          The timeout configuration for jobs that are submitted with this job definition, after which AWS Batch terminates your jobs if they have not finished. If a job is terminated due to a timeout, it is not retried. The minimum value for the timeout is 60 seconds. Any timeout configuration that is specified during a  SubmitJob operation overrides the timeout configuration defined here. For more information, see `Job Timeouts <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/job_timeouts.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        
          - **attemptDurationSeconds** *(integer) --* 
        
            The time duration in seconds (measured from the job attempt\'s ``startedAt`` timestamp) after which AWS Batch terminates your jobs if they have not finished.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'jobDefinitionName\': \'string\',
                \'jobDefinitionArn\': \'string\',
                \'revision\': 123
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **jobDefinitionName** *(string) --* 
        
              The name of the job definition.
        
            - **jobDefinitionArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the job definition. 
        
            - **revision** *(integer) --* 
        
              The revision of the job definition.
        
        """
        pass

    def submit_job(self, jobName: str, jobQueue: str, jobDefinition: str, arrayProperties: Dict = None, dependsOn: List = None, parameters: Dict = None, containerOverrides: Dict = None, retryStrategy: Dict = None, timeout: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/SubmitJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.submit_job(
              jobName=\'string\',
              jobQueue=\'string\',
              arrayProperties={
                  \'size\': 123
              },
              dependsOn=[
                  {
                      \'jobId\': \'string\',
                      \'type\': \'N_TO_N\'|\'SEQUENTIAL\'
                  },
              ],
              jobDefinition=\'string\',
              parameters={
                  \'string\': \'string\'
              },
              containerOverrides={
                  \'vcpus\': 123,
                  \'memory\': 123,
                  \'command\': [
                      \'string\',
                  ],
                  \'environment\': [
                      {
                          \'name\': \'string\',
                          \'value\': \'string\'
                      },
                  ]
              },
              retryStrategy={
                  \'attempts\': 123
              },
              timeout={
                  \'attemptDurationSeconds\': 123
              }
          )
        :type jobName: string
        :param jobName: **[REQUIRED]** 
        
          The name of the job. The first character must be alphanumeric, and up to 128 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. 
        
        :type jobQueue: string
        :param jobQueue: **[REQUIRED]** 
        
          The job queue into which the job is submitted. You can specify either the name or the Amazon Resource Name (ARN) of the queue. 
        
        :type arrayProperties: dict
        :param arrayProperties: 
        
          The array properties for the submitted job, such as the size of the array. The array size can be between 2 and 10,000. If you specify array properties for a job, it becomes an array job. For more information, see `Array Jobs <http://docs.aws.amazon.com/batch/latest/userguide/array_jobs.html>`__ in the *AWS Batch User Guide* .
        
          - **size** *(integer) --* 
        
            The size of the array job.
        
        :type dependsOn: list
        :param dependsOn: 
        
          A list of dependencies for the job. A job can depend upon a maximum of 20 jobs. You can specify a ``SEQUENTIAL`` type dependency without specifying a job ID for array jobs so that each child array job completes sequentially, starting at index 0. You can also specify an ``N_TO_N`` type dependency with a job ID for array jobs so that each index child of this job must wait for the corresponding index child of each dependency to complete before it can begin.
        
          - *(dict) --* 
        
            An object representing an AWS Batch job dependency.
        
            - **jobId** *(string) --* 
        
              The job ID of the AWS Batch job associated with this dependency.
        
            - **type** *(string) --* 
        
              The type of the job dependency.
        
        :type jobDefinition: string
        :param jobDefinition: **[REQUIRED]** 
        
          The job definition used by this job. This value can be either a ``name:revision`` or the Amazon Resource Name (ARN) for the job definition.
        
        :type parameters: dict
        :param parameters: 
        
          Additional parameters passed to the job that replace parameter substitution placeholders that are set in the job definition. Parameters are specified as a key and value pair mapping. Parameters in a ``SubmitJob`` request override any corresponding parameter defaults from the job definition.
        
          - *(string) --* 
        
            - *(string) --* 
        
        :type containerOverrides: dict
        :param containerOverrides: 
        
          A list of container overrides in JSON format that specify the name of a container in the specified job definition and the overrides it should receive. You can override the default command for a container (that is specified in the job definition or the Docker image) with a ``command`` override. You can also override existing environment variables (that are specified in the job definition or Docker image) on a container or add new environment variables to it with an ``environment`` override.
        
          - **vcpus** *(integer) --* 
        
            The number of vCPUs to reserve for the container. This value overrides the value set in the job definition.
        
          - **memory** *(integer) --* 
        
            The number of MiB of memory reserved for the job. This value overrides the value set in the job definition.
        
          - **command** *(list) --* 
        
            The command to send to the container that overrides the default command from the Docker image or the job definition.
        
            - *(string) --* 
        
          - **environment** *(list) --* 
        
            The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the job definition.
        
            .. note::
        
              Environment variables must not start with ``AWS_BATCH`` ; this naming convention is reserved for variables that are set by the AWS Batch service.
        
            - *(dict) --* 
        
              A key-value pair object.
        
              - **name** *(string) --* 
        
                The name of the key-value pair. For environment variables, this is the name of the environment variable.
        
              - **value** *(string) --* 
        
                The value of the key-value pair. For environment variables, this is the value of the environment variable.
        
        :type retryStrategy: dict
        :param retryStrategy: 
        
          The retry strategy to use for failed jobs from this  SubmitJob operation. When a retry strategy is specified here, it overrides the retry strategy defined in the job definition.
        
          - **attempts** *(integer) --* 
        
            The number of times to move a job to the ``RUNNABLE`` status. You may specify between 1 and 10 attempts. If the value of ``attempts`` is greater than one, the job is retried if it fails until it has moved to ``RUNNABLE`` that many times.
        
        :type timeout: dict
        :param timeout: 
        
          The timeout configuration for this  SubmitJob operation. You can specify a timeout duration after which AWS Batch terminates your jobs if they have not finished. If a job is terminated due to a timeout, it is not retried. The minimum value for the timeout is 60 seconds. This configuration overrides any timeout configuration specified in the job definition. For array jobs, child jobs have the same timeout configuration as the parent job. For more information, see `Job Timeouts <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/job_timeouts.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        
          - **attemptDurationSeconds** *(integer) --* 
        
            The time duration in seconds (measured from the job attempt\'s ``startedAt`` timestamp) after which AWS Batch terminates your jobs if they have not finished.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'jobName\': \'string\',
                \'jobId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **jobName** *(string) --* 
        
              The name of the job. 
        
            - **jobId** *(string) --* 
        
              The unique identifier for the job.
        
        """
        pass

    def terminate_job(self, jobId: str, reason: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/TerminateJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.terminate_job(
              jobId=\'string\',
              reason=\'string\'
          )
        :type jobId: string
        :param jobId: **[REQUIRED]** 
        
          The AWS Batch job ID of the job to terminate.
        
        :type reason: string
        :param reason: **[REQUIRED]** 
        
          A message to attach to the job that explains the reason for canceling it. This message is returned by future  DescribeJobs operations on the job. This message is also recorded in the AWS Batch activity logs. 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def update_compute_environment(self, computeEnvironment: str, state: str = None, computeResources: Dict = None, serviceRole: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/UpdateComputeEnvironment>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_compute_environment(
              computeEnvironment=\'string\',
              state=\'ENABLED\'|\'DISABLED\',
              computeResources={
                  \'minvCpus\': 123,
                  \'maxvCpus\': 123,
                  \'desiredvCpus\': 123
              },
              serviceRole=\'string\'
          )
        :type computeEnvironment: string
        :param computeEnvironment: **[REQUIRED]** 
        
          The name or full Amazon Resource Name (ARN) of the compute environment to update.
        
        :type state: string
        :param state: 
        
          The state of the compute environment. Compute environments in the ``ENABLED`` state can accept jobs from a queue and scale in or out automatically based on the workload demand of its associated queues.
        
        :type computeResources: dict
        :param computeResources: 
        
          Details of the compute resources managed by the compute environment. Required for a managed compute environment.
        
          - **minvCpus** *(integer) --* 
        
            The minimum number of EC2 vCPUs that an environment should maintain.
        
          - **maxvCpus** *(integer) --* 
        
            The maximum number of EC2 vCPUs that an environment can reach.
        
          - **desiredvCpus** *(integer) --* 
        
            The desired number of EC2 vCPUS in the compute environment.
        
        :type serviceRole: string
        :param serviceRole: 
        
          The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.
        
          If your specified role has a path other than ``/`` , then you must either specify the full role ARN (this is recommended) or prefix the role name with the path.
        
          .. note::
        
            Depending on how you created your AWS Batch service role, its ARN may contain the ``service-role`` path prefix. When you only specify the name of the service role, AWS Batch assumes that your ARN does not use the ``service-role`` path prefix. Because of this, we recommend that you specify the full ARN of your service role when you create compute environments.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'computeEnvironmentName\': \'string\',
                \'computeEnvironmentArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **computeEnvironmentName** *(string) --* 
        
              The name of compute environment.
        
            - **computeEnvironmentArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the compute environment. 
        
        """
        pass

    def update_job_queue(self, jobQueue: str, state: str = None, priority: int = None, computeEnvironmentOrder: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/UpdateJobQueue>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_job_queue(
              jobQueue=\'string\',
              state=\'ENABLED\'|\'DISABLED\',
              priority=123,
              computeEnvironmentOrder=[
                  {
                      \'order\': 123,
                      \'computeEnvironment\': \'string\'
                  },
              ]
          )
        :type jobQueue: string
        :param jobQueue: **[REQUIRED]** 
        
          The name or the Amazon Resource Name (ARN) of the job queue.
        
        :type state: string
        :param state: 
        
          Describes the queue\'s ability to accept new jobs.
        
        :type priority: integer
        :param priority: 
        
          The priority of the job queue. Job queues with a higher priority (or a higher integer value for the ``priority`` parameter) are evaluated first when associated with same compute environment. Priority is determined in descending order, for example, a job queue with a priority value of ``10`` is given scheduling preference over a job queue with a priority value of ``1`` .
        
        :type computeEnvironmentOrder: list
        :param computeEnvironmentOrder: 
        
          Details the set of compute environments mapped to a job queue and their order relative to each other. This is one of the parameters used by the job scheduler to determine which compute environment should execute a given job. 
        
          - *(dict) --* 
        
            The order in which compute environments are tried for job placement within a queue. Compute environments are tried in ascending order. For example, if two compute environments are associated with a job queue, the compute environment with a lower order integer value is tried for job placement first.
        
            - **order** *(integer) --* **[REQUIRED]** 
        
              The order of the compute environment.
        
            - **computeEnvironment** *(string) --* **[REQUIRED]** 
        
              The Amazon Resource Name (ARN) of the compute environment.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'jobQueueName\': \'string\',
                \'jobQueueArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **jobQueueName** *(string) --* 
        
              The name of the job queue.
        
            - **jobQueueArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the job queue.
        
        """
        pass
