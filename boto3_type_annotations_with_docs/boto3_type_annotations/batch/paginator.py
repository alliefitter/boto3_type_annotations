from typing import Dict
from typing import List
from botocore.paginate import Paginator


class DescribeComputeEnvironments(Paginator):
    def paginate(self, computeEnvironments: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Batch.Client.describe_compute_environments`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/DescribeComputeEnvironments>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              computeEnvironments=[
                  'string',
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
                'computeEnvironments': [
                    {
                        'computeEnvironmentName': 'string',
                        'computeEnvironmentArn': 'string',
                        'ecsClusterArn': 'string',
                        'type': 'MANAGED'|'UNMANAGED',
                        'state': 'ENABLED'|'DISABLED',
                        'status': 'CREATING'|'UPDATING'|'DELETING'|'DELETED'|'VALID'|'INVALID',
                        'statusReason': 'string',
                        'computeResources': {
                            'type': 'EC2'|'SPOT',
                            'minvCpus': 123,
                            'maxvCpus': 123,
                            'desiredvCpus': 123,
                            'instanceTypes': [
                                'string',
                            ],
                            'imageId': 'string',
                            'subnets': [
                                'string',
                            ],
                            'securityGroupIds': [
                                'string',
                            ],
                            'ec2KeyPair': 'string',
                            'instanceRole': 'string',
                            'tags': {
                                'string': 'string'
                            },
                            'placementGroup': 'string',
                            'bidPercentage': 123,
                            'spotIamFleetRole': 'string',
                            'launchTemplate': {
                                'launchTemplateId': 'string',
                                'launchTemplateName': 'string',
                                'version': 'string'
                            }
                        },
                        'serviceRole': 'string'
                    },
                ],
                'NextToken': 'string'
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
                  If the state is ``ENABLED`` , then the AWS Batch scheduler can attempt to place jobs from an associated job queue on the compute resources within the environment. If the compute environment is managed, then it can scale its instances out or in automatically, based on the job queue demand.
                  If the state is ``DISABLED`` , then the AWS Batch scheduler does not attempt to place jobs within the environment. Jobs in a ``STARTING`` or ``RUNNING`` state continue to progress normally. Managed compute environments in the ``DISABLED`` state do not scale out. However, they scale in to ``minvCpus`` value after instances become idle.
                - **status** *(string) --* 
                  The current status of the compute environment (for example, ``CREATING`` or ``VALID`` ).
                - **statusReason** *(string) --* 
                  A short, human-readable string to provide additional details about the current status of the compute environment.
                - **computeResources** *(dict) --* 
                  The compute resources defined for the compute environment. 
                  - **type** *(string) --* 
                    The type of compute environment: EC2 or SPOT.
                  - **minvCpus** *(integer) --* 
                    The minimum number of EC2 vCPUs that an environment should maintain (even if the compute environment is ``DISABLED`` ). 
                  - **maxvCpus** *(integer) --* 
                    The maximum number of EC2 vCPUs that an environment can reach. 
                  - **desiredvCpus** *(integer) --* 
                    The desired number of EC2 vCPUS in the compute environment. 
                  - **instanceTypes** *(list) --* 
                    The instances types that may be launched. You can specify instance families to launch any instance type within those families (for example, ``c4`` or ``p3`` ), or you can specify specific sizes within a family (such as ``c4.8xlarge`` ). You can also choose ``optimal`` to pick instance types (from the C, M, and R instance families) on the fly that match the demand of your job queues.
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
                    The Amazon ECS instance profile applied to Amazon EC2 instances in a compute environment. You can specify the short name or full Amazon Resource Name (ARN) of an instance profile. For example, `` *ecsInstanceRole* `` or ``arn:aws:iam::*<aws_account_id>* :instance-profile/*ecsInstanceRole* `` . For more information, see `Amazon ECS Instance Role <https://docs.aws.amazon.com/batch/latest/userguide/instance_IAM_role.html>`__ in the *AWS Batch User Guide* .
                  - **tags** *(dict) --* 
                    Key-value pair tags to be applied to resources that are launched in the compute environment. For AWS Batch, these take the form of "String1": "String2", where String1 is the tag key and String2 is the tag value—for example, { "Name": "AWS Batch Instance - C4OnDemand" }.
                    - *(string) --* 
                      - *(string) --* 
                  - **placementGroup** *(string) --* 
                    The Amazon EC2 placement group to associate with your compute resources. If you intend to submit multi-node parallel jobs to your compute environment, you should consider creating a cluster placement group and associate it with your compute resources. This keeps your multi-node parallel job on a logical grouping of instances within a single Availability Zone with high network flow potential. For more information, see `Placement Groups <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html>`__ in the *Amazon EC2 User Guide for Linux Instances* .
                  - **bidPercentage** *(integer) --* 
                    The maximum percentage that a Spot Instance price can be when compared with the On-Demand price for that instance type before instances are launched. For example, if your maximum percentage is 20%, then the Spot price must be below 20% of the current On-Demand price for that EC2 instance. You always pay the lowest (market) price and never more than your maximum percentage. If you leave this field empty, the default value is 100% of the On-Demand price.
                  - **spotIamFleetRole** *(string) --* 
                    The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a ``SPOT`` compute environment. For more information, see `Amazon EC2 Spot Fleet Role <https://docs.aws.amazon.com/batch/latest/userguide/spot_fleet_IAM_role.html>`__ in the *AWS Batch User Guide* .
                  - **launchTemplate** *(dict) --* 
                    The launch template to use for your compute resources. Any other compute resource parameters that you specify in a  CreateComputeEnvironment API operation override the same parameters in the launch template. You must specify either the launch template ID or launch template name in the request, but not both. For more information, see `Launch Template Support <https://docs.aws.amazon.com/batch/latest/userguide/launch-templates.html>`__ in the *AWS Batch User Guide* .
                    - **launchTemplateId** *(string) --* 
                      The ID of the launch template.
                    - **launchTemplateName** *(string) --* 
                      The name of the launch template.
                    - **version** *(string) --* 
                      The version number of the launch template.
                      Default: The default version of the launch template.
                - **serviceRole** *(string) --* 
                  The service role associated with the compute environment that allows AWS Batch to make calls to AWS API operations on your behalf.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type computeEnvironments: list
        :param computeEnvironments:
          A list of up to 100 compute environment names or full Amazon Resource Name (ARN) entries.
          - *(string) --*
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


class DescribeJobDefinitions(Paginator):
    def paginate(self, jobDefinitions: List = None, jobDefinitionName: str = None, status: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Batch.Client.describe_job_definitions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/DescribeJobDefinitions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              jobDefinitions=[
                  'string',
              ],
              jobDefinitionName='string',
              status='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'jobDefinitions': [
                    {
                        'jobDefinitionName': 'string',
                        'jobDefinitionArn': 'string',
                        'revision': 123,
                        'status': 'string',
                        'type': 'string',
                        'parameters': {
                            'string': 'string'
                        },
                        'retryStrategy': {
                            'attempts': 123
                        },
                        'containerProperties': {
                            'image': 'string',
                            'vcpus': 123,
                            'memory': 123,
                            'command': [
                                'string',
                            ],
                            'jobRoleArn': 'string',
                            'volumes': [
                                {
                                    'host': {
                                        'sourcePath': 'string'
                                    },
                                    'name': 'string'
                                },
                            ],
                            'environment': [
                                {
                                    'name': 'string',
                                    'value': 'string'
                                },
                            ],
                            'mountPoints': [
                                {
                                    'containerPath': 'string',
                                    'readOnly': True|False,
                                    'sourceVolume': 'string'
                                },
                            ],
                            'readonlyRootFilesystem': True|False,
                            'privileged': True|False,
                            'ulimits': [
                                {
                                    'hardLimit': 123,
                                    'name': 'string',
                                    'softLimit': 123
                                },
                            ],
                            'user': 'string',
                            'instanceType': 'string',
                            'resourceRequirements': [
                                {
                                    'value': 'string',
                                    'type': 'GPU'
                                },
                            ]
                        },
                        'timeout': {
                            'attemptDurationSeconds': 123
                        },
                        'nodeProperties': {
                            'numNodes': 123,
                            'mainNode': 123,
                            'nodeRangeProperties': [
                                {
                                    'targetNodes': 'string',
                                    'container': {
                                        'image': 'string',
                                        'vcpus': 123,
                                        'memory': 123,
                                        'command': [
                                            'string',
                                        ],
                                        'jobRoleArn': 'string',
                                        'volumes': [
                                            {
                                                'host': {
                                                    'sourcePath': 'string'
                                                },
                                                'name': 'string'
                                            },
                                        ],
                                        'environment': [
                                            {
                                                'name': 'string',
                                                'value': 'string'
                                            },
                                        ],
                                        'mountPoints': [
                                            {
                                                'containerPath': 'string',
                                                'readOnly': True|False,
                                                'sourceVolume': 'string'
                                            },
                                        ],
                                        'readonlyRootFilesystem': True|False,
                                        'privileged': True|False,
                                        'ulimits': [
                                            {
                                                'hardLimit': 123,
                                                'name': 'string',
                                                'softLimit': 123
                                            },
                                        ],
                                        'user': 'string',
                                        'instanceType': 'string',
                                        'resourceRequirements': [
                                            {
                                                'value': 'string',
                                                'type': 'GPU'
                                            },
                                        ]
                                    }
                                },
                            ]
                        }
                    },
                ],
                'NextToken': 'string'
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
                  Default parameters or parameter substitution placeholders that are set in the job definition. Parameters are specified as a key-value pair mapping. Parameters in a ``SubmitJob`` request override any corresponding parameter defaults from the job definition. For more information about specifying parameters, see `Job Definition Parameters <https://docs.aws.amazon.com/batch/latest/userguide/job_definition_parameters.html>`__ in the *AWS Batch User Guide* .
                  - *(string) --* 
                    - *(string) --* 
                - **retryStrategy** *(dict) --* 
                  The retry strategy to use for failed jobs that are submitted with this job definition.
                  - **attempts** *(integer) --* 
                    The number of times to move a job to the ``RUNNABLE`` status. You may specify between 1 and 10 attempts. If the value of ``attempts`` is greater than one, the job is retried on failure the same number of attempts as the value.
                - **containerProperties** *(dict) --* 
                  An object with various properties specific to container-based jobs. 
                  - **image** *(string) --* 
                    The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with `` *repository-url* /*image* :*tag* `` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to ``Image`` in the `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``IMAGE`` parameter of `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    * Images in Amazon ECR repositories use the full registry and repository URI (for example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ). 
                    * Images in official repositories on Docker Hub use a single name (for example, ``ubuntu`` or ``mongo`` ). 
                    * Images in other repositories on Docker Hub are qualified with an organization name (for example, ``amazon/amazon-ecs-agent`` ). 
                    * Images in other online repositories are qualified further by a domain name (for example, ``quay.io/assemblyline/ubuntu`` ). 
                  - **vcpus** *(integer) --* 
                    The number of vCPUs reserved for the container. This parameter maps to ``CpuShares`` in the `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--cpu-shares`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . Each vCPU is equivalent to 1,024 CPU shares. You must specify at least one vCPU.
                  - **memory** *(integer) --* 
                    The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. This parameter maps to ``Memory`` in the `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--memory`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . You must specify at least 4 MiB of memory for a job.
                    .. note::
                      If you are trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular instance type, see `Memory Management <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__ in the *AWS Batch User Guide* .
                  - **command** *(list) --* 
                    The command that is passed to the container. This parameter maps to ``Cmd`` in the `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``COMMAND`` parameter to `docker run <https://docs.docker.com/engine/reference/run/>`__ . For more information, see `https\://docs.docker.com/engine/reference/builder/#cmd <https://docs.docker.com/engine/reference/builder/#cmd>`__ .
                    - *(string) --* 
                  - **jobRoleArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS permissions.
                  - **volumes** *(list) --* 
                    A list of data volumes used in a job.
                    - *(dict) --* 
                      A data volume used in a job's container properties.
                      - **host** *(dict) --* 
                        The contents of the ``host`` parameter determine whether your data volume persists on the host container instance and where it is stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data is not guaranteed to persist after the containers associated with it stop running.
                        - **sourcePath** *(string) --* 
                          The path on the host container instance that is presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If this parameter contains a file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the source path location does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.
                      - **name** *(string) --* 
                        The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the ``sourceVolume`` parameter of container definition ``mountPoints`` .
                  - **environment** *(list) --* 
                    The environment variables to pass to a container. This parameter maps to ``Env`` in the `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--env`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
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
                    The mount points for data volumes in your container. This parameter maps to ``Volumes`` in the `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--volume`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    - *(dict) --* 
                      Details on a Docker volume mount point that is used in a job's container properties. This parameter maps to ``Volumes`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__ section of the Docker Remote API and the ``--volume`` option to docker run.
                      - **containerPath** *(string) --* 
                        The path on the container at which to mount the host volume.
                      - **readOnly** *(boolean) --* 
                        If this value is ``true`` , the container has read-only access to the volume; otherwise, the container can write to the volume. The default value is ``false`` .
                      - **sourceVolume** *(string) --* 
                        The name of the volume to mount.
                  - **readonlyRootFilesystem** *(boolean) --* 
                    When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--read-only`` option to ``docker run`` .
                  - **privileged** *(boolean) --* 
                    When this parameter is true, the container is given elevated privileges on the host container instance (similar to the ``root`` user). This parameter maps to ``Privileged`` in the `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--privileged`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                  - **ulimits** *(list) --* 
                    A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits`` in the `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--ulimit`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    - *(dict) --* 
                      The ``ulimit`` settings to pass to the container.
                      - **hardLimit** *(integer) --* 
                        The hard limit for the ``ulimit`` type.
                      - **name** *(string) --* 
                        The ``type`` of the ``ulimit`` .
                      - **softLimit** *(integer) --* 
                        The soft limit for the ``ulimit`` type.
                  - **user** *(string) --* 
                    The user name to use inside the container. This parameter maps to ``User`` in the `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--user`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                  - **instanceType** *(string) --* 
                    The instance type to use for a multi-node parallel job. Currently all node groups in a multi-node parallel job must use the same instance type. This parameter is not valid for single-node container jobs.
                  - **resourceRequirements** *(list) --* 
                    The type and amount of a resource to assign to a container. Currently, the only supported resource is ``GPU`` .
                    - *(dict) --* 
                      The type and amount of a resource to assign to a container. Currently, the only supported resource type is ``GPU`` .
                      - **value** *(string) --* 
                        The number of physical GPUs to reserve for the container. The number of GPUs reserved for all containers in a job should not exceed the number of available GPUs on the compute resource that the job is launched on.
                      - **type** *(string) --* 
                        The type of resource to assign to a container. Currently, the only supported resource type is ``GPU`` .
                - **timeout** *(dict) --* 
                  The timeout configuration for jobs that are submitted with this job definition. You can specify a timeout duration after which AWS Batch terminates your jobs if they have not finished.
                  - **attemptDurationSeconds** *(integer) --* 
                    The time duration in seconds (measured from the job attempt's ``startedAt`` timestamp) after which AWS Batch terminates your jobs if they have not finished.
                - **nodeProperties** *(dict) --* 
                  An object with various properties specific to multi-node parallel jobs.
                  - **numNodes** *(integer) --* 
                    The number of nodes associated with a multi-node parallel job.
                  - **mainNode** *(integer) --* 
                    Specifies the node index for the main node of a multi-node parallel job. This node index value must be fewer than the number of nodes.
                  - **nodeRangeProperties** *(list) --* 
                    A list of node ranges and their properties associated with a multi-node parallel job.
                    - *(dict) --* 
                      An object representing the properties of the node range for a multi-node parallel job.
                      - **targetNodes** *(string) --* 
                        The range of nodes, using node index values. A range of ``0:3`` indicates nodes with index values of ``0`` through ``3`` . If the starting range value is omitted (``:n`` ), then ``0`` is used to start the range. If the ending range value is omitted (``n:`` ), then the highest possible node index is used to end the range. Your accumulative node ranges must account for all nodes (0:n). You may nest node ranges, for example 0:10 and 4:5, in which case the 4:5 range properties override the 0:10 properties. 
                      - **container** *(dict) --* 
                        The container details for the node range.
                        - **image** *(string) --* 
                          The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with `` *repository-url* /*image* :*tag* `` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to ``Image`` in the `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``IMAGE`` parameter of `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                          * Images in Amazon ECR repositories use the full registry and repository URI (for example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>`` ). 
                          * Images in official repositories on Docker Hub use a single name (for example, ``ubuntu`` or ``mongo`` ). 
                          * Images in other repositories on Docker Hub are qualified with an organization name (for example, ``amazon/amazon-ecs-agent`` ). 
                          * Images in other online repositories are qualified further by a domain name (for example, ``quay.io/assemblyline/ubuntu`` ). 
                        - **vcpus** *(integer) --* 
                          The number of vCPUs reserved for the container. This parameter maps to ``CpuShares`` in the `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--cpu-shares`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . Each vCPU is equivalent to 1,024 CPU shares. You must specify at least one vCPU.
                        - **memory** *(integer) --* 
                          The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. This parameter maps to ``Memory`` in the `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--memory`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . You must specify at least 4 MiB of memory for a job.
                          .. note::
                            If you are trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular instance type, see `Memory Management <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`__ in the *AWS Batch User Guide* .
                        - **command** *(list) --* 
                          The command that is passed to the container. This parameter maps to ``Cmd`` in the `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``COMMAND`` parameter to `docker run <https://docs.docker.com/engine/reference/run/>`__ . For more information, see `https\://docs.docker.com/engine/reference/builder/#cmd <https://docs.docker.com/engine/reference/builder/#cmd>`__ .
                          - *(string) --* 
                        - **jobRoleArn** *(string) --* 
                          The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS permissions.
                        - **volumes** *(list) --* 
                          A list of data volumes used in a job.
                          - *(dict) --* 
                            A data volume used in a job's container properties.
                            - **host** *(dict) --* 
                              The contents of the ``host`` parameter determine whether your data volume persists on the host container instance and where it is stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data is not guaranteed to persist after the containers associated with it stop running.
                              - **sourcePath** *(string) --* 
                                The path on the host container instance that is presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If this parameter contains a file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the source path location does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.
                            - **name** *(string) --* 
                              The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the ``sourceVolume`` parameter of container definition ``mountPoints`` .
                        - **environment** *(list) --* 
                          The environment variables to pass to a container. This parameter maps to ``Env`` in the `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--env`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
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
                          The mount points for data volumes in your container. This parameter maps to ``Volumes`` in the `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--volume`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                          - *(dict) --* 
                            Details on a Docker volume mount point that is used in a job's container properties. This parameter maps to ``Volumes`` in the `Create a container <https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container>`__ section of the Docker Remote API and the ``--volume`` option to docker run.
                            - **containerPath** *(string) --* 
                              The path on the container at which to mount the host volume.
                            - **readOnly** *(boolean) --* 
                              If this value is ``true`` , the container has read-only access to the volume; otherwise, the container can write to the volume. The default value is ``false`` .
                            - **sourceVolume** *(string) --* 
                              The name of the volume to mount.
                        - **readonlyRootFilesystem** *(boolean) --* 
                          When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--read-only`` option to ``docker run`` .
                        - **privileged** *(boolean) --* 
                          When this parameter is true, the container is given elevated privileges on the host container instance (similar to the ``root`` user). This parameter maps to ``Privileged`` in the `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--privileged`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                        - **ulimits** *(list) --* 
                          A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits`` in the `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--ulimit`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                          - *(dict) --* 
                            The ``ulimit`` settings to pass to the container.
                            - **hardLimit** *(integer) --* 
                              The hard limit for the ``ulimit`` type.
                            - **name** *(string) --* 
                              The ``type`` of the ``ulimit`` .
                            - **softLimit** *(integer) --* 
                              The soft limit for the ``ulimit`` type.
                        - **user** *(string) --* 
                          The user name to use inside the container. This parameter maps to ``User`` in the `Create a container <https://docs.docker.com/engine/api/v1.23/#create-a-container>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.23/>`__ and the ``--user`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                        - **instanceType** *(string) --* 
                          The instance type to use for a multi-node parallel job. Currently all node groups in a multi-node parallel job must use the same instance type. This parameter is not valid for single-node container jobs.
                        - **resourceRequirements** *(list) --* 
                          The type and amount of a resource to assign to a container. Currently, the only supported resource is ``GPU`` .
                          - *(dict) --* 
                            The type and amount of a resource to assign to a container. Currently, the only supported resource type is ``GPU`` .
                            - **value** *(string) --* 
                              The number of physical GPUs to reserve for the container. The number of GPUs reserved for all containers in a job should not exceed the number of available GPUs on the compute resource that the job is launched on.
                            - **type** *(string) --* 
                              The type of resource to assign to a container. Currently, the only supported resource type is ``GPU`` .
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type jobDefinitions: list
        :param jobDefinitions:
          A list of up to 100 job definition names or full Amazon Resource Name (ARN) entries.
          - *(string) --*
        :type jobDefinitionName: string
        :param jobDefinitionName:
          The name of the job definition to describe.
        :type status: string
        :param status:
          The status with which to filter job definitions.
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


class DescribeJobQueues(Paginator):
    def paginate(self, jobQueues: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Batch.Client.describe_job_queues`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/DescribeJobQueues>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              jobQueues=[
                  'string',
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
                'jobQueues': [
                    {
                        'jobQueueName': 'string',
                        'jobQueueArn': 'string',
                        'state': 'ENABLED'|'DISABLED',
                        'status': 'CREATING'|'UPDATING'|'DELETING'|'DELETED'|'VALID'|'INVALID',
                        'statusReason': 'string',
                        'priority': 123,
                        'computeEnvironmentOrder': [
                            {
                                'order': 123,
                                'computeEnvironment': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type jobQueues: list
        :param jobQueues:
          A list of up to 100 queue names or full queue Amazon Resource Name (ARN) entries.
          - *(string) --*
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


class ListJobs(Paginator):
    def paginate(self, jobQueue: str = None, arrayJobId: str = None, multiNodeJobId: str = None, jobStatus: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Batch.Client.list_jobs`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/ListJobs>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              jobQueue='string',
              arrayJobId='string',
              multiNodeJobId='string',
              jobStatus='SUBMITTED'|'PENDING'|'RUNNABLE'|'STARTING'|'RUNNING'|'SUCCEEDED'|'FAILED',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'jobSummaryList': [
                    {
                        'jobId': 'string',
                        'jobName': 'string',
                        'createdAt': 123,
                        'status': 'SUBMITTED'|'PENDING'|'RUNNABLE'|'STARTING'|'RUNNING'|'SUCCEEDED'|'FAILED',
                        'statusReason': 'string',
                        'startedAt': 123,
                        'stoppedAt': 123,
                        'container': {
                            'exitCode': 123,
                            'reason': 'string'
                        },
                        'arrayProperties': {
                            'size': 123,
                            'index': 123
                        },
                        'nodeProperties': {
                            'isMainNode': True|False,
                            'numNodes': 123,
                            'nodeIndex': 123
                        }
                    },
                ],
                'NextToken': 'string'
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
                  The Unix timestamp for when the job was created. For non-array jobs and parent array jobs, this is when the job entered the ``SUBMITTED`` state (at the time  SubmitJob was called). For array child jobs, this is when the child job was spawned by its parent and entered the ``PENDING`` state.
                - **status** *(string) --* 
                  The current status for the job.
                - **statusReason** *(string) --* 
                  A short, human-readable string to provide additional details about the current status of the job.
                - **startedAt** *(integer) --* 
                  The Unix timestamp for when the job was started (when the job transitioned from the ``STARTING`` state to the ``RUNNING`` state).
                - **stoppedAt** *(integer) --* 
                  The Unix timestamp for when the job was stopped (when the job transitioned from the ``RUNNING`` state to a terminal state, such as ``SUCCEEDED`` or ``FAILED`` ).
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
                - **nodeProperties** *(dict) --* 
                  The node properties for a single node in a job summary list.
                  - **isMainNode** *(boolean) --* 
                    Specifies whether the current node is the main node for a multi-node parallel job.
                  - **numNodes** *(integer) --* 
                    The number of nodes associated with a multi-node parallel job.
                  - **nodeIndex** *(integer) --* 
                    The node index for the node. Node index numbering begins at zero. This index is also available on the node with the ``AWS_BATCH_JOB_NODE_INDEX`` environment variable.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type jobQueue: string
        :param jobQueue:
          The name or full Amazon Resource Name (ARN) of the job queue with which to list jobs.
        :type arrayJobId: string
        :param arrayJobId:
          The job ID for an array job. Specifying an array job ID with this parameter lists all child jobs from within the specified array.
        :type multiNodeJobId: string
        :param multiNodeJobId:
          The job ID for a multi-node parallel job. Specifying a multi-node parallel job ID with this parameter lists all nodes that are associated with the specified job.
        :type jobStatus: string
        :param jobStatus:
          The job status with which to filter jobs in the specified queue. If you do not specify a status, only ``RUNNING`` jobs are returned.
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
