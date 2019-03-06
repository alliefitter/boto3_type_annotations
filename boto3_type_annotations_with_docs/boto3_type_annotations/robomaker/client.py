from typing import Union
from typing import List
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import Optional
from typing import Dict
from botocore.client import BaseClient


class Client(BaseClient):
    def batch_describe_simulation_job(self, jobs: List) -> Dict:
        """
        Describes one or more simulation jobs.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/BatchDescribeSimulationJob>`_
        
        **Request Syntax**
        ::
          response = client.batch_describe_simulation_job(
              jobs=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'jobs': [
                    {
                        'arn': 'string',
                        'name': 'string',
                        'status': 'Pending'|'Preparing'|'Running'|'Restarting'|'Completed'|'Failed'|'RunningFailed'|'Terminating'|'Terminated'|'Canceled',
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'failureBehavior': 'Fail'|'Continue',
                        'failureCode': 'InternalServiceError'|'RobotApplicationCrash'|'SimulationApplicationCrash'|'BadPermissionsRobotApplication'|'BadPermissionsSimulationApplication'|'BadPermissionsS3Output'|'BadPermissionsCloudwatchLogs'|'SubnetIpLimitExceeded'|'ENILimitExceeded'|'BadPermissionsUserCredentials'|'InvalidBundleRobotApplication'|'InvalidBundleSimulationApplication'|'RobotApplicationVersionMismatchedEtag'|'SimulationApplicationVersionMismatchedEtag'|'WrongRegionS3Output'|'WrongRegionRobotApplication'|'WrongRegionSimulationApplication',
                        'failureReason': 'string',
                        'clientRequestToken': 'string',
                        'outputLocation': {
                            's3Bucket': 'string',
                            's3Prefix': 'string'
                        },
                        'maxJobDurationInSeconds': 123,
                        'simulationTimeMillis': 123,
                        'iamRole': 'string',
                        'robotApplications': [
                            {
                                'application': 'string',
                                'applicationVersion': 'string',
                                'launchConfig': {
                                    'packageName': 'string',
                                    'launchFile': 'string',
                                    'environmentVariables': {
                                        'string': 'string'
                                    }
                                }
                            },
                        ],
                        'simulationApplications': [
                            {
                                'application': 'string',
                                'applicationVersion': 'string',
                                'launchConfig': {
                                    'packageName': 'string',
                                    'launchFile': 'string',
                                    'environmentVariables': {
                                        'string': 'string'
                                    }
                                }
                            },
                        ],
                        'tags': {
                            'string': 'string'
                        },
                        'vpcConfig': {
                            'subnets': [
                                'string',
                            ],
                            'securityGroups': [
                                'string',
                            ],
                            'vpcId': 'string',
                            'assignPublicIp': True|False
                        }
                    },
                ],
                'unprocessedJobs': [
                    'string',
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **jobs** *(list) --* 
              A list of simulation jobs.
              - *(dict) --* 
                Information about a simulation job.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the simulation job.
                - **name** *(string) --* 
                  The name of the simulation job.
                - **status** *(string) --* 
                  Status of the simulation job.
                - **lastUpdatedAt** *(datetime) --* 
                  The time, in milliseconds since the epoch, when the simulation job was last updated.
                - **failureBehavior** *(string) --* 
                  The failure behavior the simulation job.
                    Continue  
                  Restart the simulation job in the same host instance.
                    Fail  
                  Stop the simulation job and terminate the instance.
                - **failureCode** *(string) --* 
                  The failure code of the simulation job if it failed.
                - **failureReason** *(string) --* 
                  The reason why the simulation job failed.
                - **clientRequestToken** *(string) --* 
                  A unique identifier for this ``SimulationJob`` request.
                - **outputLocation** *(dict) --* 
                  Location for output files generated by the simulation job.
                  - **s3Bucket** *(string) --* 
                    The S3 bucket for output.
                  - **s3Prefix** *(string) --* 
                    The S3 folder in the ``s3Bucket`` where output files will be placed.
                - **maxJobDurationInSeconds** *(integer) --* 
                  The maximum simulation job duration in seconds. The value must be 8 days (691,200 seconds) or less.
                - **simulationTimeMillis** *(integer) --* 
                  The simulation job execution duration in milliseconds.
                - **iamRole** *(string) --* 
                  The IAM role that allows the simulation instance to call the AWS APIs that are specified in its associated policies on your behalf. This is how credentials are passed in to your simulation job. See how to `specify AWS security credentials for your application <https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/deployment-ecs-specify-credentials>`__ . 
                - **robotApplications** *(list) --* 
                  A list of robot applications.
                  - *(dict) --* 
                    Application configuration information for a robot.
                    - **application** *(string) --* 
                      The application information for the robot application.
                    - **applicationVersion** *(string) --* 
                      The version of the robot application.
                    - **launchConfig** *(dict) --* 
                      The launch configuration for the robot application.
                      - **packageName** *(string) --* 
                        The package name.
                      - **launchFile** *(string) --* 
                        The launch file name.
                      - **environmentVariables** *(dict) --* 
                        The environment variables for the application launch.
                        - *(string) --* 
                          - *(string) --* 
                - **simulationApplications** *(list) --* 
                  A list of simulation applications.
                  - *(dict) --* 
                    Information about a simulation application configuration.
                    - **application** *(string) --* 
                      The application information for the simulation application.
                    - **applicationVersion** *(string) --* 
                      The version of the simulation application.
                    - **launchConfig** *(dict) --* 
                      The launch configuration for the simulation application.
                      - **packageName** *(string) --* 
                        The package name.
                      - **launchFile** *(string) --* 
                        The launch file name.
                      - **environmentVariables** *(dict) --* 
                        The environment variables for the application launch.
                        - *(string) --* 
                          - *(string) --* 
                - **tags** *(dict) --* 
                  A map that contains tag keys and tag values that are attached to the simulation job.
                  - *(string) --* 
                    - *(string) --* 
                - **vpcConfig** *(dict) --* 
                  VPC configuration information.
                  - **subnets** *(list) --* 
                    A list of subnet IDs associated with the simulation job.
                    - *(string) --* 
                  - **securityGroups** *(list) --* 
                    A list of security group IDs associated with the simulation job.
                    - *(string) --* 
                  - **vpcId** *(string) --* 
                    The VPC ID associated with your simulation job.
                  - **assignPublicIp** *(boolean) --* 
                    A boolean indicating if a public IP was assigned.
            - **unprocessedJobs** *(list) --* 
              A list of unprocessed simulation job Amazon Resource Names (ARNs).
              - *(string) --* 
        :type jobs: list
        :param jobs: **[REQUIRED]**
          A list of Amazon Resource Names (ARNs) of simulation jobs to describe.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

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

    def cancel_simulation_job(self, job: str) -> Dict:
        """
        Cancels the specified simulation job.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/CancelSimulationJob>`_
        
        **Request Syntax**
        ::
          response = client.cancel_simulation_job(
              job='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type job: string
        :param job: **[REQUIRED]**
          The simulation job ARN to cancel.
        :rtype: dict
        :returns:
        """
        pass

    def create_deployment_job(self, clientRequestToken: str, fleet: str, deploymentApplicationConfigs: List, deploymentConfig: Dict = None, tags: Dict = None) -> Dict:
        """
        Deploys a specific version of a robot application to robots in a fleet.
        The robot application must have a numbered ``applicationVersion`` for consistency reasons. To create a new version, use ``CreateRobotApplicationVersion`` or see `Creating a Robot Application Version <https://docs.aws.amazon.com/robomaker/latest/dg/create-robot-application-version.html>`__ . 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/CreateDeploymentJob>`_
        
        **Request Syntax**
        ::
          response = client.create_deployment_job(
              deploymentConfig={
                  'concurrentDeploymentPercentage': 123,
                  'failureThresholdPercentage': 123
              },
              clientRequestToken='string',
              fleet='string',
              deploymentApplicationConfigs=[
                  {
                      'application': 'string',
                      'applicationVersion': 'string',
                      'launchConfig': {
                          'packageName': 'string',
                          'preLaunchFile': 'string',
                          'launchFile': 'string',
                          'postLaunchFile': 'string',
                          'environmentVariables': {
                              'string': 'string'
                          }
                      }
                  },
              ],
              tags={
                  'string': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'arn': 'string',
                'fleet': 'string',
                'status': 'Pending'|'Preparing'|'InProgress'|'Failed'|'Succeeded',
                'deploymentApplicationConfigs': [
                    {
                        'application': 'string',
                        'applicationVersion': 'string',
                        'launchConfig': {
                            'packageName': 'string',
                            'preLaunchFile': 'string',
                            'launchFile': 'string',
                            'postLaunchFile': 'string',
                            'environmentVariables': {
                                'string': 'string'
                            }
                        }
                    },
                ],
                'failureReason': 'string',
                'failureCode': 'ResourceNotFound'|'FailureThresholdBreached'|'RobotDeploymentNoResponse'|'GreengrassDeploymentFailed'|'MissingRobotArchitecture'|'MissingRobotApplicationArchitecture'|'MissingRobotDeploymentResource'|'GreengrassGroupVersionDoesNotExist'|'ExtractingBundleFailure'|'PreLaunchFileFailure'|'PostLaunchFileFailure'|'BadPermissionError'|'InternalServerError',
                'createdAt': datetime(2015, 1, 1),
                'deploymentConfig': {
                    'concurrentDeploymentPercentage': 123,
                    'failureThresholdPercentage': 123
                },
                'tags': {
                    'string': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **arn** *(string) --* 
              The Amazon Resource Name (ARN) of the deployment job.
            - **fleet** *(string) --* 
              The target fleet for the deployment job.
            - **status** *(string) --* 
              The status of the deployment job.
            - **deploymentApplicationConfigs** *(list) --* 
              The deployment application configuration.
              - *(dict) --* 
                Information about a deployment application configuration.
                - **application** *(string) --* 
                  The Amazon Resource Name (ARN) of the robot application.
                - **applicationVersion** *(string) --* 
                  The version of the application.
                - **launchConfig** *(dict) --* 
                  The launch configuration.
                  - **packageName** *(string) --* 
                    The package name.
                  - **preLaunchFile** *(string) --* 
                    The deployment pre-launch file. This file will be executed prior to the launch file.
                  - **launchFile** *(string) --* 
                    The launch file name.
                  - **postLaunchFile** *(string) --* 
                    The deployment post-launch file. This file will be executed after the launch file.
                  - **environmentVariables** *(dict) --* 
                    An array of key/value pairs specifying environment variables for the robot application
                    - *(string) --* 
                      - *(string) --* 
            - **failureReason** *(string) --* 
              The failure reason of the deployment job if it failed.
            - **failureCode** *(string) --* 
              The failure code of the simulation job if it failed:
                BadPermissionError  
              AWS Greengrass requires a service-level role permission to access other services. The role must include the ` ``AWSGreengrassResourceAccessRolePolicy`` managed policy <https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/service-role/AWSGreengrassResourceAccessRolePolicy$jsonEditor>`__ . 
                ExtractingBundleFailure  
              The robot application could not be extracted from the bundle.
                FailureThresholdBreached  
              The percentage of robots that could not be updated exceeded the percentage set for the deployment.
                GreengrassDeploymentFailed  
              The robot application could not be deployed to the robot.
                GreengrassGroupVersionDoesNotExist  
              The AWS Greengrass group or version associated with a robot is missing.
                InternalServerError  
              An internal error has occurred. Retry your request, but if the problem persists, contact us with details.
                MissingRobotApplicationArchitecture  
              The robot application does not have a source that matches the architecture of the robot.
                MissingRobotDeploymentResource  
              One or more of the resources specified for the robot application are missing. For example, does the robot application have the correct launch package and launch file?
                PostLaunchFileFailure  
              The post-launch script failed.
                PreLaunchFileFailure  
              The pre-launch script failed.
                ResourceNotFound  
              One or more deployment resources are missing. For example, do robot application source bundles still exist? 
                RobotDeploymentNoResponse  
              There is no response from the robot. It might not be powered on or connected to the internet.
            - **createdAt** *(datetime) --* 
              The time, in milliseconds since the epoch, when the fleet was created.
            - **deploymentConfig** *(dict) --* 
              The deployment configuration.
              - **concurrentDeploymentPercentage** *(integer) --* 
                The percentage of robots receiving the deployment at the same time.
              - **failureThresholdPercentage** *(integer) --* 
                The percentage of deployments that need to fail before stopping deployment.
            - **tags** *(dict) --* 
              The list of all tags added to the deployment job.
              - *(string) --* 
                - *(string) --* 
        :type deploymentConfig: dict
        :param deploymentConfig:
          The requested deployment configuration.
          - **concurrentDeploymentPercentage** *(integer) --*
            The percentage of robots receiving the deployment at the same time.
          - **failureThresholdPercentage** *(integer) --*
            The percentage of deployments that need to fail before stopping deployment.
        :type clientRequestToken: string
        :param clientRequestToken: **[REQUIRED]**
          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
          This field is autopopulated if not provided.
        :type fleet: string
        :param fleet: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the fleet to deploy.
        :type deploymentApplicationConfigs: list
        :param deploymentApplicationConfigs: **[REQUIRED]**
          The deployment application configuration.
          - *(dict) --*
            Information about a deployment application configuration.
            - **application** *(string) --* **[REQUIRED]**
              The Amazon Resource Name (ARN) of the robot application.
            - **applicationVersion** *(string) --* **[REQUIRED]**
              The version of the application.
            - **launchConfig** *(dict) --* **[REQUIRED]**
              The launch configuration.
              - **packageName** *(string) --* **[REQUIRED]**
                The package name.
              - **preLaunchFile** *(string) --*
                The deployment pre-launch file. This file will be executed prior to the launch file.
              - **launchFile** *(string) --* **[REQUIRED]**
                The launch file name.
              - **postLaunchFile** *(string) --*
                The deployment post-launch file. This file will be executed after the launch file.
              - **environmentVariables** *(dict) --*
                An array of key/value pairs specifying environment variables for the robot application
                - *(string) --*
                  - *(string) --*
        :type tags: dict
        :param tags:
          A map that contains tag keys and tag values that are attached to the deployment job.
          - *(string) --*
            - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def create_fleet(self, name: str, tags: Dict = None) -> Dict:
        """
        Creates a fleet, a logical group of robots running the same robot application.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/CreateFleet>`_
        
        **Request Syntax**
        ::
          response = client.create_fleet(
              name='string',
              tags={
                  'string': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'arn': 'string',
                'name': 'string',
                'createdAt': datetime(2015, 1, 1),
                'tags': {
                    'string': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **arn** *(string) --* 
              The Amazon Resource Name (ARN) of the fleet.
            - **name** *(string) --* 
              The name of the fleet.
            - **createdAt** *(datetime) --* 
              The time, in milliseconds since the epoch, when the fleet was created.
            - **tags** *(dict) --* 
              The list of all tags added to the fleet.
              - *(string) --* 
                - *(string) --* 
        :type name: string
        :param name: **[REQUIRED]**
          The name of the fleet.
        :type tags: dict
        :param tags:
          A map that contains tag keys and tag values that are attached to the fleet.
          - *(string) --*
            - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def create_robot(self, name: str, architecture: str, greengrassGroupId: str, tags: Dict = None) -> Dict:
        """
        Creates a robot.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/CreateRobot>`_
        
        **Request Syntax**
        ::
          response = client.create_robot(
              name='string',
              architecture='X86_64'|'ARM64'|'ARMHF',
              greengrassGroupId='string',
              tags={
                  'string': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'arn': 'string',
                'name': 'string',
                'createdAt': datetime(2015, 1, 1),
                'greengrassGroupId': 'string',
                'architecture': 'X86_64'|'ARM64'|'ARMHF',
                'tags': {
                    'string': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **arn** *(string) --* 
              The Amazon Resource Name (ARN) of the robot.
            - **name** *(string) --* 
              The name of the robot.
            - **createdAt** *(datetime) --* 
              The time, in milliseconds since the epoch, when the robot was created.
            - **greengrassGroupId** *(string) --* 
              The Amazon Resource Name (ARN) of the Greengrass group associated with the robot.
            - **architecture** *(string) --* 
              The target architecture of the robot.
            - **tags** *(dict) --* 
              The list of all tags added to the robot.
              - *(string) --* 
                - *(string) --* 
        :type name: string
        :param name: **[REQUIRED]**
          The name for the robot.
        :type architecture: string
        :param architecture: **[REQUIRED]**
          The target architecture of the robot.
        :type greengrassGroupId: string
        :param greengrassGroupId: **[REQUIRED]**
          The Greengrass group id.
        :type tags: dict
        :param tags:
          A map that contains tag keys and tag values that are attached to the robot.
          - *(string) --*
            - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def create_robot_application(self, name: str, sources: List, robotSoftwareSuite: Dict, tags: Dict = None) -> Dict:
        """
        Creates a robot application. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/CreateRobotApplication>`_
        
        **Request Syntax**
        ::
          response = client.create_robot_application(
              name='string',
              sources=[
                  {
                      's3Bucket': 'string',
                      's3Key': 'string',
                      'architecture': 'X86_64'|'ARM64'|'ARMHF'
                  },
              ],
              robotSoftwareSuite={
                  'name': 'ROS',
                  'version': 'Kinetic'
              },
              tags={
                  'string': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'arn': 'string',
                'name': 'string',
                'version': 'string',
                'sources': [
                    {
                        's3Bucket': 'string',
                        's3Key': 'string',
                        'etag': 'string',
                        'architecture': 'X86_64'|'ARM64'|'ARMHF'
                    },
                ],
                'robotSoftwareSuite': {
                    'name': 'ROS',
                    'version': 'Kinetic'
                },
                'lastUpdatedAt': datetime(2015, 1, 1),
                'revisionId': 'string',
                'tags': {
                    'string': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **arn** *(string) --* 
              The Amazon Resource Name (ARN) of the robot application.
            - **name** *(string) --* 
              The name of the robot application.
            - **version** *(string) --* 
              The version of the robot application.
            - **sources** *(list) --* 
              The sources of the robot application.
              - *(dict) --* 
                Information about a source.
                - **s3Bucket** *(string) --* 
                  The s3 bucket name.
                - **s3Key** *(string) --* 
                  The s3 object key.
                - **etag** *(string) --* 
                  A hash of the object specified by ``s3Bucket`` and ``s3Key`` .
                - **architecture** *(string) --* 
                  The taget processor architecture for the application.
            - **robotSoftwareSuite** *(dict) --* 
              The robot software suite used by the robot application.
              - **name** *(string) --* 
                The name of the robot software suite.
              - **version** *(string) --* 
                The version of the robot software suite.
            - **lastUpdatedAt** *(datetime) --* 
              The time, in milliseconds since the epoch, when the robot application was last updated.
            - **revisionId** *(string) --* 
              The revision id of the robot application.
            - **tags** *(dict) --* 
              The list of all tags added to the robot application.
              - *(string) --* 
                - *(string) --* 
        :type name: string
        :param name: **[REQUIRED]**
          The name of the robot application.
        :type sources: list
        :param sources: **[REQUIRED]**
          The sources of the robot application.
          - *(dict) --*
            Information about a source configuration.
            - **s3Bucket** *(string) --*
              The Amazon S3 bucket name.
            - **s3Key** *(string) --*
              The s3 object key.
            - **architecture** *(string) --*
              The target processor architecture for the application.
        :type robotSoftwareSuite: dict
        :param robotSoftwareSuite: **[REQUIRED]**
          The robot software suite used by the robot application.
          - **name** *(string) --*
            The name of the robot software suite.
          - **version** *(string) --*
            The version of the robot software suite.
        :type tags: dict
        :param tags:
          A map that contains tag keys and tag values that are attached to the robot application.
          - *(string) --*
            - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def create_robot_application_version(self, application: str, currentRevisionId: str = None) -> Dict:
        """
        Creates a version of a robot application.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/CreateRobotApplicationVersion>`_
        
        **Request Syntax**
        ::
          response = client.create_robot_application_version(
              application='string',
              currentRevisionId='string'
          )
        
        **Response Syntax**
        ::
            {
                'arn': 'string',
                'name': 'string',
                'version': 'string',
                'sources': [
                    {
                        's3Bucket': 'string',
                        's3Key': 'string',
                        'etag': 'string',
                        'architecture': 'X86_64'|'ARM64'|'ARMHF'
                    },
                ],
                'robotSoftwareSuite': {
                    'name': 'ROS',
                    'version': 'Kinetic'
                },
                'lastUpdatedAt': datetime(2015, 1, 1),
                'revisionId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **arn** *(string) --* 
              The Amazon Resource Name (ARN) of the robot application.
            - **name** *(string) --* 
              The name of the robot application.
            - **version** *(string) --* 
              The version of the robot application.
            - **sources** *(list) --* 
              The sources of the robot application.
              - *(dict) --* 
                Information about a source.
                - **s3Bucket** *(string) --* 
                  The s3 bucket name.
                - **s3Key** *(string) --* 
                  The s3 object key.
                - **etag** *(string) --* 
                  A hash of the object specified by ``s3Bucket`` and ``s3Key`` .
                - **architecture** *(string) --* 
                  The taget processor architecture for the application.
            - **robotSoftwareSuite** *(dict) --* 
              The robot software suite used by the robot application.
              - **name** *(string) --* 
                The name of the robot software suite.
              - **version** *(string) --* 
                The version of the robot software suite.
            - **lastUpdatedAt** *(datetime) --* 
              The time, in milliseconds since the epoch, when the robot application was last updated.
            - **revisionId** *(string) --* 
              The revision id of the robot application.
        :type application: string
        :param application: **[REQUIRED]**
          The application information for the robot application.
        :type currentRevisionId: string
        :param currentRevisionId:
          The current revision id for the robot application. If you provide a value and it matches the latest revision ID, a new version will be created.
        :rtype: dict
        :returns:
        """
        pass

    def create_simulation_application(self, name: str, sources: List, simulationSoftwareSuite: Dict, robotSoftwareSuite: Dict, renderingEngine: Dict, tags: Dict = None) -> Dict:
        """
        Creates a simulation application.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/CreateSimulationApplication>`_
        
        **Request Syntax**
        ::
          response = client.create_simulation_application(
              name='string',
              sources=[
                  {
                      's3Bucket': 'string',
                      's3Key': 'string',
                      'architecture': 'X86_64'|'ARM64'|'ARMHF'
                  },
              ],
              simulationSoftwareSuite={
                  'name': 'Gazebo',
                  'version': 'string'
              },
              robotSoftwareSuite={
                  'name': 'ROS',
                  'version': 'Kinetic'
              },
              renderingEngine={
                  'name': 'OGRE',
                  'version': 'string'
              },
              tags={
                  'string': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'arn': 'string',
                'name': 'string',
                'version': 'string',
                'sources': [
                    {
                        's3Bucket': 'string',
                        's3Key': 'string',
                        'etag': 'string',
                        'architecture': 'X86_64'|'ARM64'|'ARMHF'
                    },
                ],
                'simulationSoftwareSuite': {
                    'name': 'Gazebo',
                    'version': 'string'
                },
                'robotSoftwareSuite': {
                    'name': 'ROS',
                    'version': 'Kinetic'
                },
                'renderingEngine': {
                    'name': 'OGRE',
                    'version': 'string'
                },
                'lastUpdatedAt': datetime(2015, 1, 1),
                'revisionId': 'string',
                'tags': {
                    'string': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **arn** *(string) --* 
              The Amazon Resource Name (ARN) of the simulation application.
            - **name** *(string) --* 
              The name of the simulation application.
            - **version** *(string) --* 
              The version of the simulation application.
            - **sources** *(list) --* 
              The sources of the simulation application.
              - *(dict) --* 
                Information about a source.
                - **s3Bucket** *(string) --* 
                  The s3 bucket name.
                - **s3Key** *(string) --* 
                  The s3 object key.
                - **etag** *(string) --* 
                  A hash of the object specified by ``s3Bucket`` and ``s3Key`` .
                - **architecture** *(string) --* 
                  The taget processor architecture for the application.
            - **simulationSoftwareSuite** *(dict) --* 
              The simulation software suite used by the simulation application.
              - **name** *(string) --* 
                The name of the simulation software suite.
              - **version** *(string) --* 
                The version of the simulation software suite.
            - **robotSoftwareSuite** *(dict) --* 
              Information about the robot software suite.
              - **name** *(string) --* 
                The name of the robot software suite.
              - **version** *(string) --* 
                The version of the robot software suite.
            - **renderingEngine** *(dict) --* 
              The rendering engine for the simulation application.
              - **name** *(string) --* 
                The name of the rendering engine.
              - **version** *(string) --* 
                The version of the rendering engine.
            - **lastUpdatedAt** *(datetime) --* 
              The time, in milliseconds since the epoch, when the simulation application was last updated.
            - **revisionId** *(string) --* 
              The revision id of the simulation application.
            - **tags** *(dict) --* 
              The list of all tags added to the simulation application.
              - *(string) --* 
                - *(string) --* 
        :type name: string
        :param name: **[REQUIRED]**
          The name of the simulation application.
        :type sources: list
        :param sources: **[REQUIRED]**
          The sources of the simulation application.
          - *(dict) --*
            Information about a source configuration.
            - **s3Bucket** *(string) --*
              The Amazon S3 bucket name.
            - **s3Key** *(string) --*
              The s3 object key.
            - **architecture** *(string) --*
              The target processor architecture for the application.
        :type simulationSoftwareSuite: dict
        :param simulationSoftwareSuite: **[REQUIRED]**
          The simulation software suite used by the simulation application.
          - **name** *(string) --*
            The name of the simulation software suite.
          - **version** *(string) --*
            The version of the simulation software suite.
        :type robotSoftwareSuite: dict
        :param robotSoftwareSuite: **[REQUIRED]**
          The robot software suite of the simulation application.
          - **name** *(string) --*
            The name of the robot software suite.
          - **version** *(string) --*
            The version of the robot software suite.
        :type renderingEngine: dict
        :param renderingEngine: **[REQUIRED]**
          The rendering engine for the simulation application.
          - **name** *(string) --*
            The name of the rendering engine.
          - **version** *(string) --*
            The version of the rendering engine.
        :type tags: dict
        :param tags:
          A map that contains tag keys and tag values that are attached to the simulation application.
          - *(string) --*
            - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def create_simulation_application_version(self, application: str, currentRevisionId: str = None) -> Dict:
        """
        Creates a simulation application with a specific revision id.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/CreateSimulationApplicationVersion>`_
        
        **Request Syntax**
        ::
          response = client.create_simulation_application_version(
              application='string',
              currentRevisionId='string'
          )
        
        **Response Syntax**
        ::
            {
                'arn': 'string',
                'name': 'string',
                'version': 'string',
                'sources': [
                    {
                        's3Bucket': 'string',
                        's3Key': 'string',
                        'etag': 'string',
                        'architecture': 'X86_64'|'ARM64'|'ARMHF'
                    },
                ],
                'simulationSoftwareSuite': {
                    'name': 'Gazebo',
                    'version': 'string'
                },
                'robotSoftwareSuite': {
                    'name': 'ROS',
                    'version': 'Kinetic'
                },
                'renderingEngine': {
                    'name': 'OGRE',
                    'version': 'string'
                },
                'lastUpdatedAt': datetime(2015, 1, 1),
                'revisionId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **arn** *(string) --* 
              The Amazon Resource Name (ARN) of the simulation application.
            - **name** *(string) --* 
              The name of the simulation application.
            - **version** *(string) --* 
              The version of the simulation application.
            - **sources** *(list) --* 
              The sources of the simulation application.
              - *(dict) --* 
                Information about a source.
                - **s3Bucket** *(string) --* 
                  The s3 bucket name.
                - **s3Key** *(string) --* 
                  The s3 object key.
                - **etag** *(string) --* 
                  A hash of the object specified by ``s3Bucket`` and ``s3Key`` .
                - **architecture** *(string) --* 
                  The taget processor architecture for the application.
            - **simulationSoftwareSuite** *(dict) --* 
              The simulation software suite used by the simulation application.
              - **name** *(string) --* 
                The name of the simulation software suite.
              - **version** *(string) --* 
                The version of the simulation software suite.
            - **robotSoftwareSuite** *(dict) --* 
              Information about the robot software suite.
              - **name** *(string) --* 
                The name of the robot software suite.
              - **version** *(string) --* 
                The version of the robot software suite.
            - **renderingEngine** *(dict) --* 
              The rendering engine for the simulation application.
              - **name** *(string) --* 
                The name of the rendering engine.
              - **version** *(string) --* 
                The version of the rendering engine.
            - **lastUpdatedAt** *(datetime) --* 
              The time, in milliseconds since the epoch, when the simulation application was last updated.
            - **revisionId** *(string) --* 
              The revision ID of the simulation application.
        :type application: string
        :param application: **[REQUIRED]**
          The application information for the simulation application.
        :type currentRevisionId: string
        :param currentRevisionId:
          The current revision id for the simulation application. If you provide a value and it matches the latest revision ID, a new version will be created.
        :rtype: dict
        :returns:
        """
        pass

    def create_simulation_job(self, maxJobDurationInSeconds: int, iamRole: str, clientRequestToken: str = None, outputLocation: Dict = None, failureBehavior: str = None, robotApplications: List = None, simulationApplications: List = None, tags: Dict = None, vpcConfig: Dict = None) -> Dict:
        """
        Creates a simulation job.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/CreateSimulationJob>`_
        
        **Request Syntax**
        ::
          response = client.create_simulation_job(
              clientRequestToken='string',
              outputLocation={
                  's3Bucket': 'string',
                  's3Prefix': 'string'
              },
              maxJobDurationInSeconds=123,
              iamRole='string',
              failureBehavior='Fail'|'Continue',
              robotApplications=[
                  {
                      'application': 'string',
                      'applicationVersion': 'string',
                      'launchConfig': {
                          'packageName': 'string',
                          'launchFile': 'string',
                          'environmentVariables': {
                              'string': 'string'
                          }
                      }
                  },
              ],
              simulationApplications=[
                  {
                      'application': 'string',
                      'applicationVersion': 'string',
                      'launchConfig': {
                          'packageName': 'string',
                          'launchFile': 'string',
                          'environmentVariables': {
                              'string': 'string'
                          }
                      }
                  },
              ],
              tags={
                  'string': 'string'
              },
              vpcConfig={
                  'subnets': [
                      'string',
                  ],
                  'securityGroups': [
                      'string',
                  ],
                  'assignPublicIp': True|False
              }
          )
        
        **Response Syntax**
        ::
            {
                'arn': 'string',
                'status': 'Pending'|'Preparing'|'Running'|'Restarting'|'Completed'|'Failed'|'RunningFailed'|'Terminating'|'Terminated'|'Canceled',
                'lastUpdatedAt': datetime(2015, 1, 1),
                'failureBehavior': 'Fail'|'Continue',
                'failureCode': 'InternalServiceError'|'RobotApplicationCrash'|'SimulationApplicationCrash'|'BadPermissionsRobotApplication'|'BadPermissionsSimulationApplication'|'BadPermissionsS3Output'|'BadPermissionsCloudwatchLogs'|'SubnetIpLimitExceeded'|'ENILimitExceeded'|'BadPermissionsUserCredentials'|'InvalidBundleRobotApplication'|'InvalidBundleSimulationApplication'|'RobotApplicationVersionMismatchedEtag'|'SimulationApplicationVersionMismatchedEtag'|'WrongRegionS3Output'|'WrongRegionRobotApplication'|'WrongRegionSimulationApplication',
                'clientRequestToken': 'string',
                'outputLocation': {
                    's3Bucket': 'string',
                    's3Prefix': 'string'
                },
                'maxJobDurationInSeconds': 123,
                'simulationTimeMillis': 123,
                'iamRole': 'string',
                'robotApplications': [
                    {
                        'application': 'string',
                        'applicationVersion': 'string',
                        'launchConfig': {
                            'packageName': 'string',
                            'launchFile': 'string',
                            'environmentVariables': {
                                'string': 'string'
                            }
                        }
                    },
                ],
                'simulationApplications': [
                    {
                        'application': 'string',
                        'applicationVersion': 'string',
                        'launchConfig': {
                            'packageName': 'string',
                            'launchFile': 'string',
                            'environmentVariables': {
                                'string': 'string'
                            }
                        }
                    },
                ],
                'tags': {
                    'string': 'string'
                },
                'vpcConfig': {
                    'subnets': [
                        'string',
                    ],
                    'securityGroups': [
                        'string',
                    ],
                    'vpcId': 'string',
                    'assignPublicIp': True|False
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **arn** *(string) --* 
              The Amazon Resource Name (ARN) of the simulation job.
            - **status** *(string) --* 
              The status of the simulation job.
            - **lastUpdatedAt** *(datetime) --* 
              The time, in milliseconds since the epoch, when the simulation job was last updated.
            - **failureBehavior** *(string) --* 
              the failure behavior for the simulation job.
            - **failureCode** *(string) --* 
              The failure code of the simulation job if it failed:
                InternalServiceError  
              Internal service error.
                RobotApplicationCrash  
              Robot application exited abnormally.
                SimulationApplicationCrash  
              Simulation application exited abnormally.
                BadPermissionsRobotApplication  
              Robot application bundle could not be downloaded.
                BadPermissionsSimulationApplication  
              Simulation application bundle could not be downloaded.
                BadPermissionsS3Output  
              Unable to publish outputs to customer-provided S3 bucket.
                BadPermissionsCloudwatchLogs  
              Unable to publish logs to customer-provided CloudWatch Logs resource.
                SubnetIpLimitExceeded  
              Subnet IP limit exceeded.
                ENILimitExceeded  
              ENI limit exceeded.
                BadPermissionsUserCredentials  
              Unable to use the Role provided.
                InvalidBundleRobotApplication  
              Robot bundle cannot be extracted (invalid format, bundling error, or other issue).
                InvalidBundleSimulationApplication  
              Simulation bundle cannot be extracted (invalid format, bundling error, or other issue).
                RobotApplicationVersionMismatchedEtag  
              Etag for RobotApplication does not match value during version creation.
                SimulationApplicationVersionMismatchedEtag  
              Etag for SimulationApplication does not match value during version creation.
            - **clientRequestToken** *(string) --* 
              Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
            - **outputLocation** *(dict) --* 
              Simulation job output files location.
              - **s3Bucket** *(string) --* 
                The S3 bucket for output.
              - **s3Prefix** *(string) --* 
                The S3 folder in the ``s3Bucket`` where output files will be placed.
            - **maxJobDurationInSeconds** *(integer) --* 
              The maximum simulation job duration in seconds. The value must be 8 days (691,200 seconds) or less. 
            - **simulationTimeMillis** *(integer) --* 
              The simulation job execution duration in milliseconds.
            - **iamRole** *(string) --* 
              The IAM role that allows the simulation job to call the AWS APIs that are specified in its associated policies on your behalf.
            - **robotApplications** *(list) --* 
              The robot application used by the simulation job.
              - *(dict) --* 
                Application configuration information for a robot.
                - **application** *(string) --* 
                  The application information for the robot application.
                - **applicationVersion** *(string) --* 
                  The version of the robot application.
                - **launchConfig** *(dict) --* 
                  The launch configuration for the robot application.
                  - **packageName** *(string) --* 
                    The package name.
                  - **launchFile** *(string) --* 
                    The launch file name.
                  - **environmentVariables** *(dict) --* 
                    The environment variables for the application launch.
                    - *(string) --* 
                      - *(string) --* 
            - **simulationApplications** *(list) --* 
              The simulation application used by the simulation job.
              - *(dict) --* 
                Information about a simulation application configuration.
                - **application** *(string) --* 
                  The application information for the simulation application.
                - **applicationVersion** *(string) --* 
                  The version of the simulation application.
                - **launchConfig** *(dict) --* 
                  The launch configuration for the simulation application.
                  - **packageName** *(string) --* 
                    The package name.
                  - **launchFile** *(string) --* 
                    The launch file name.
                  - **environmentVariables** *(dict) --* 
                    The environment variables for the application launch.
                    - *(string) --* 
                      - *(string) --* 
            - **tags** *(dict) --* 
              The list of all tags added to the simulation job.
              - *(string) --* 
                - *(string) --* 
            - **vpcConfig** *(dict) --* 
              Information about the vpc configuration.
              - **subnets** *(list) --* 
                A list of subnet IDs associated with the simulation job.
                - *(string) --* 
              - **securityGroups** *(list) --* 
                A list of security group IDs associated with the simulation job.
                - *(string) --* 
              - **vpcId** *(string) --* 
                The VPC ID associated with your simulation job.
              - **assignPublicIp** *(boolean) --* 
                A boolean indicating if a public IP was assigned.
        :type clientRequestToken: string
        :param clientRequestToken:
          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
          This field is autopopulated if not provided.
        :type outputLocation: dict
        :param outputLocation:
          Location for output files generated by the simulation job.
          - **s3Bucket** *(string) --*
            The S3 bucket for output.
          - **s3Prefix** *(string) --*
            The S3 folder in the ``s3Bucket`` where output files will be placed.
        :type maxJobDurationInSeconds: integer
        :param maxJobDurationInSeconds: **[REQUIRED]**
          The maximum simulation job duration in seconds (up to 14 days or 1,209,600 seconds. When ``maxJobDurationInSeconds`` is reached, the simulation job will status will transition to ``Completed`` .
        :type iamRole: string
        :param iamRole: **[REQUIRED]**
          The IAM role name that allows the simulation instance to call the AWS APIs that are specified in its associated policies on your behalf. This is how credentials are passed in to your simulation job.
        :type failureBehavior: string
        :param failureBehavior:
          The failure behavior the simulation job.
            Continue
          Restart the simulation job in the same host instance.
            Fail
          Stop the simulation job and terminate the instance.
        :type robotApplications: list
        :param robotApplications:
          The robot application to use in the simulation job.
          - *(dict) --*
            Application configuration information for a robot.
            - **application** *(string) --* **[REQUIRED]**
              The application information for the robot application.
            - **applicationVersion** *(string) --*
              The version of the robot application.
            - **launchConfig** *(dict) --* **[REQUIRED]**
              The launch configuration for the robot application.
              - **packageName** *(string) --* **[REQUIRED]**
                The package name.
              - **launchFile** *(string) --* **[REQUIRED]**
                The launch file name.
              - **environmentVariables** *(dict) --*
                The environment variables for the application launch.
                - *(string) --*
                  - *(string) --*
        :type simulationApplications: list
        :param simulationApplications:
          The simulation application to use in the simulation job.
          - *(dict) --*
            Information about a simulation application configuration.
            - **application** *(string) --* **[REQUIRED]**
              The application information for the simulation application.
            - **applicationVersion** *(string) --*
              The version of the simulation application.
            - **launchConfig** *(dict) --* **[REQUIRED]**
              The launch configuration for the simulation application.
              - **packageName** *(string) --* **[REQUIRED]**
                The package name.
              - **launchFile** *(string) --* **[REQUIRED]**
                The launch file name.
              - **environmentVariables** *(dict) --*
                The environment variables for the application launch.
                - *(string) --*
                  - *(string) --*
        :type tags: dict
        :param tags:
          A map that contains tag keys and tag values that are attached to the simulation job.
          - *(string) --*
            - *(string) --*
        :type vpcConfig: dict
        :param vpcConfig:
          If your simulation job accesses resources in a VPC, you provide this parameter identifying the list of security group IDs and subnet IDs. These must belong to the same VPC. You must provide at least one security group and one subnet ID.
          - **subnets** *(list) --* **[REQUIRED]**
            A list of one or more subnet IDs in your VPC.
            - *(string) --*
          - **securityGroups** *(list) --*
            A list of one or more security groups IDs in your VPC.
            - *(string) --*
          - **assignPublicIp** *(boolean) --*
            A boolean indicating whether to assign a public IP address.
        :rtype: dict
        :returns:
        """
        pass

    def delete_fleet(self, fleet: str) -> Dict:
        """
        Deletes a fleet.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/DeleteFleet>`_
        
        **Request Syntax**
        ::
          response = client.delete_fleet(
              fleet='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type fleet: string
        :param fleet: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the fleet.
        :rtype: dict
        :returns:
        """
        pass

    def delete_robot(self, robot: str) -> Dict:
        """
        Deletes a robot.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/DeleteRobot>`_
        
        **Request Syntax**
        ::
          response = client.delete_robot(
              robot='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type robot: string
        :param robot: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the robot.
        :rtype: dict
        :returns:
        """
        pass

    def delete_robot_application(self, application: str, applicationVersion: str = None) -> Dict:
        """
        Deletes a robot application.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/DeleteRobotApplication>`_
        
        **Request Syntax**
        ::
          response = client.delete_robot_application(
              application='string',
              applicationVersion='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type application: string
        :param application: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the the robot application.
        :type applicationVersion: string
        :param applicationVersion:
          The version of the robot application to delete.
        :rtype: dict
        :returns:
        """
        pass

    def delete_simulation_application(self, application: str, applicationVersion: str = None) -> Dict:
        """
        Deletes a simulation application.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/DeleteSimulationApplication>`_
        
        **Request Syntax**
        ::
          response = client.delete_simulation_application(
              application='string',
              applicationVersion='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type application: string
        :param application: **[REQUIRED]**
          The application information for the simulation application to delete.
        :type applicationVersion: string
        :param applicationVersion:
          The version of the simulation application to delete.
        :rtype: dict
        :returns:
        """
        pass

    def deregister_robot(self, fleet: str, robot: str) -> Dict:
        """
        Deregisters a robot.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/DeregisterRobot>`_
        
        **Request Syntax**
        ::
          response = client.deregister_robot(
              fleet='string',
              robot='string'
          )
        
        **Response Syntax**
        ::
            {
                'fleet': 'string',
                'robot': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **fleet** *(string) --* 
              The Amazon Resource Name (ARN) of the fleet.
            - **robot** *(string) --* 
              The Amazon Resource Name (ARN) of the robot.
        :type fleet: string
        :param fleet: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the fleet.
        :type robot: string
        :param robot: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the robot.
        :rtype: dict
        :returns:
        """
        pass

    def describe_deployment_job(self, job: str) -> Dict:
        """
        Describes a deployment job. [Does it work regardless of deployment status, e.g. Failed?]
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/DescribeDeploymentJob>`_
        
        **Request Syntax**
        ::
          response = client.describe_deployment_job(
              job='string'
          )
        
        **Response Syntax**
        ::
            {
                'arn': 'string',
                'fleet': 'string',
                'status': 'Pending'|'Preparing'|'InProgress'|'Failed'|'Succeeded',
                'deploymentConfig': {
                    'concurrentDeploymentPercentage': 123,
                    'failureThresholdPercentage': 123
                },
                'deploymentApplicationConfigs': [
                    {
                        'application': 'string',
                        'applicationVersion': 'string',
                        'launchConfig': {
                            'packageName': 'string',
                            'preLaunchFile': 'string',
                            'launchFile': 'string',
                            'postLaunchFile': 'string',
                            'environmentVariables': {
                                'string': 'string'
                            }
                        }
                    },
                ],
                'failureReason': 'string',
                'failureCode': 'ResourceNotFound'|'FailureThresholdBreached'|'RobotDeploymentNoResponse'|'GreengrassDeploymentFailed'|'MissingRobotArchitecture'|'MissingRobotApplicationArchitecture'|'MissingRobotDeploymentResource'|'GreengrassGroupVersionDoesNotExist'|'ExtractingBundleFailure'|'PreLaunchFileFailure'|'PostLaunchFileFailure'|'BadPermissionError'|'InternalServerError',
                'createdAt': datetime(2015, 1, 1),
                'robotDeploymentSummary': [
                    {
                        'arn': 'string',
                        'deploymentStartTime': datetime(2015, 1, 1),
                        'deploymentFinishTime': datetime(2015, 1, 1),
                        'status': 'Available'|'Registered'|'PendingNewDeployment'|'Deploying'|'Failed'|'InSync'|'NoResponse',
                        'progressDetail': {
                            'currentProgress': 'string',
                            'targetResource': 'string'
                        },
                        'failureReason': 'string',
                        'failureCode': 'ResourceNotFound'|'FailureThresholdBreached'|'RobotDeploymentNoResponse'|'GreengrassDeploymentFailed'|'MissingRobotArchitecture'|'MissingRobotApplicationArchitecture'|'MissingRobotDeploymentResource'|'GreengrassGroupVersionDoesNotExist'|'ExtractingBundleFailure'|'PreLaunchFileFailure'|'PostLaunchFileFailure'|'BadPermissionError'|'InternalServerError'
                    },
                ],
                'tags': {
                    'string': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **arn** *(string) --* 
              The Amazon Resource Name (ARN) of the deployment job.
            - **fleet** *(string) --* 
              The Amazon Resource Name (ARN) of the fleet.
            - **status** *(string) --* 
              The status of the deployment job.
            - **deploymentConfig** *(dict) --* 
              The deployment configuration.
              - **concurrentDeploymentPercentage** *(integer) --* 
                The percentage of robots receiving the deployment at the same time.
              - **failureThresholdPercentage** *(integer) --* 
                The percentage of deployments that need to fail before stopping deployment.
            - **deploymentApplicationConfigs** *(list) --* 
              The deployment application configuration.
              - *(dict) --* 
                Information about a deployment application configuration.
                - **application** *(string) --* 
                  The Amazon Resource Name (ARN) of the robot application.
                - **applicationVersion** *(string) --* 
                  The version of the application.
                - **launchConfig** *(dict) --* 
                  The launch configuration.
                  - **packageName** *(string) --* 
                    The package name.
                  - **preLaunchFile** *(string) --* 
                    The deployment pre-launch file. This file will be executed prior to the launch file.
                  - **launchFile** *(string) --* 
                    The launch file name.
                  - **postLaunchFile** *(string) --* 
                    The deployment post-launch file. This file will be executed after the launch file.
                  - **environmentVariables** *(dict) --* 
                    An array of key/value pairs specifying environment variables for the robot application
                    - *(string) --* 
                      - *(string) --* 
            - **failureReason** *(string) --* 
              A short description of the reason why the deployment job failed.
            - **failureCode** *(string) --* 
              The deployment job failure code.
            - **createdAt** *(datetime) --* 
              The time, in milliseconds since the epoch, when the deployment job was created.
            - **robotDeploymentSummary** *(list) --* 
              A list of robot deployment summaries.
              - *(dict) --* 
                Information about a robot deployment.
                - **arn** *(string) --* 
                  The robot deployment Amazon Resource Name (ARN).
                - **deploymentStartTime** *(datetime) --* 
                  The time, in milliseconds since the epoch, when the deployment was started.
                - **deploymentFinishTime** *(datetime) --* 
                  The time, in milliseconds since the epoch, when the deployment finished.
                - **status** *(string) --* 
                  The status of the robot deployment.
                - **progressDetail** *(dict) --* 
                  Information about how the deployment is progressing.
                  - **currentProgress** *(string) --* 
                    The current progress status.
                  - **targetResource** *(string) --* 
                    The Amazon Resource Name (ARN) of the deployment job.
                - **failureReason** *(string) --* 
                  A short description of the reason why the robot deployment failed.
                - **failureCode** *(string) --* 
                  The robot deployment failure code.
            - **tags** *(dict) --* 
              The list of all tags added to the specified deployment job.
              - *(string) --* 
                - *(string) --* 
        :type job: string
        :param job: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the deployment job.
        :rtype: dict
        :returns:
        """
        pass

    def describe_fleet(self, fleet: str) -> Dict:
        """
        Describes a fleet.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/DescribeFleet>`_
        
        **Request Syntax**
        ::
          response = client.describe_fleet(
              fleet='string'
          )
        
        **Response Syntax**
        ::
            {
                'name': 'string',
                'arn': 'string',
                'robots': [
                    {
                        'arn': 'string',
                        'name': 'string',
                        'fleetArn': 'string',
                        'status': 'Available'|'Registered'|'PendingNewDeployment'|'Deploying'|'Failed'|'InSync'|'NoResponse',
                        'greenGrassGroupId': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'architecture': 'X86_64'|'ARM64'|'ARMHF',
                        'lastDeploymentJob': 'string',
                        'lastDeploymentTime': datetime(2015, 1, 1)
                    },
                ],
                'createdAt': datetime(2015, 1, 1),
                'lastDeploymentStatus': 'Pending'|'Preparing'|'InProgress'|'Failed'|'Succeeded',
                'lastDeploymentJob': 'string',
                'lastDeploymentTime': datetime(2015, 1, 1),
                'tags': {
                    'string': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **name** *(string) --* 
              The name of the fleet.
            - **arn** *(string) --* 
              The Amazon Resource Name (ARN) of the fleet.
            - **robots** *(list) --* 
              A list of robots.
              - *(dict) --* 
                Information about a robot.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the robot.
                - **name** *(string) --* 
                  The name of the robot.
                - **fleetArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the fleet.
                - **status** *(string) --* 
                  The status of the robot.
                - **greenGrassGroupId** *(string) --* 
                  The Greengrass group associated with the robot.
                - **createdAt** *(datetime) --* 
                  The time, in milliseconds since the epoch, when the robot was created.
                - **architecture** *(string) --* 
                  The architecture of the robot.
                - **lastDeploymentJob** *(string) --* 
                  The Amazon Resource Name (ARN) of the last deployment job.
                - **lastDeploymentTime** *(datetime) --* 
                  The time of the last deployment.
            - **createdAt** *(datetime) --* 
              The time, in milliseconds since the epoch, when the fleet was created.
            - **lastDeploymentStatus** *(string) --* 
              The status of the last deployment.
            - **lastDeploymentJob** *(string) --* 
              The Amazon Resource Name (ARN) of the last deployment job.
            - **lastDeploymentTime** *(datetime) --* 
              The time of the last deployment.
            - **tags** *(dict) --* 
              The list of all tags added to the specified fleet.
              - *(string) --* 
                - *(string) --* 
        :type fleet: string
        :param fleet: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the fleet.
        :rtype: dict
        :returns:
        """
        pass

    def describe_robot(self, robot: str) -> Dict:
        """
        Describes a robot.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/DescribeRobot>`_
        
        **Request Syntax**
        ::
          response = client.describe_robot(
              robot='string'
          )
        
        **Response Syntax**
        ::
            {
                'arn': 'string',
                'name': 'string',
                'fleetArn': 'string',
                'status': 'Available'|'Registered'|'PendingNewDeployment'|'Deploying'|'Failed'|'InSync'|'NoResponse',
                'greengrassGroupId': 'string',
                'createdAt': datetime(2015, 1, 1),
                'architecture': 'X86_64'|'ARM64'|'ARMHF',
                'lastDeploymentJob': 'string',
                'lastDeploymentTime': datetime(2015, 1, 1),
                'tags': {
                    'string': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **arn** *(string) --* 
              The Amazon Resource Name (ARN) of the robot.
            - **name** *(string) --* 
              The name of the robot.
            - **fleetArn** *(string) --* 
              The Amazon Resource Name (ARN) of the fleet.
            - **status** *(string) --* 
              The status of the fleet.
            - **greengrassGroupId** *(string) --* 
              The Greengrass group id.
            - **createdAt** *(datetime) --* 
              The time, in milliseconds since the epoch, when the robot was created.
            - **architecture** *(string) --* 
              The target architecture of the robot application.
            - **lastDeploymentJob** *(string) --* 
              The Amazon Resource Name (ARN) of the last deployment job.
            - **lastDeploymentTime** *(datetime) --* 
              The time of the last deployment job.
            - **tags** *(dict) --* 
              The list of all tags added to the specified robot.
              - *(string) --* 
                - *(string) --* 
        :type robot: string
        :param robot: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the robot to be described.
        :rtype: dict
        :returns:
        """
        pass

    def describe_robot_application(self, application: str, applicationVersion: str = None) -> Dict:
        """
        Describes a robot application.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/DescribeRobotApplication>`_
        
        **Request Syntax**
        ::
          response = client.describe_robot_application(
              application='string',
              applicationVersion='string'
          )
        
        **Response Syntax**
        ::
            {
                'arn': 'string',
                'name': 'string',
                'version': 'string',
                'sources': [
                    {
                        's3Bucket': 'string',
                        's3Key': 'string',
                        'etag': 'string',
                        'architecture': 'X86_64'|'ARM64'|'ARMHF'
                    },
                ],
                'robotSoftwareSuite': {
                    'name': 'ROS',
                    'version': 'Kinetic'
                },
                'revisionId': 'string',
                'lastUpdatedAt': datetime(2015, 1, 1),
                'tags': {
                    'string': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **arn** *(string) --* 
              The Amazon Resource Name (ARN) of the robot application.
            - **name** *(string) --* 
              The name of the robot application.
            - **version** *(string) --* 
              The version of the robot application.
            - **sources** *(list) --* 
              The sources of the robot application.
              - *(dict) --* 
                Information about a source.
                - **s3Bucket** *(string) --* 
                  The s3 bucket name.
                - **s3Key** *(string) --* 
                  The s3 object key.
                - **etag** *(string) --* 
                  A hash of the object specified by ``s3Bucket`` and ``s3Key`` .
                - **architecture** *(string) --* 
                  The taget processor architecture for the application.
            - **robotSoftwareSuite** *(dict) --* 
              The robot software suite used by the robot application.
              - **name** *(string) --* 
                The name of the robot software suite.
              - **version** *(string) --* 
                The version of the robot software suite.
            - **revisionId** *(string) --* 
              The revision id of the robot application.
            - **lastUpdatedAt** *(datetime) --* 
              The time, in milliseconds since the epoch, when the robot application was last updated.
            - **tags** *(dict) --* 
              The list of all tags added to the specified robot application.
              - *(string) --* 
                - *(string) --* 
        :type application: string
        :param application: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the robot application.
        :type applicationVersion: string
        :param applicationVersion:
          The version of the robot application to describe.
        :rtype: dict
        :returns:
        """
        pass

    def describe_simulation_application(self, application: str, applicationVersion: str = None) -> Dict:
        """
        Describes a simulation application.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/DescribeSimulationApplication>`_
        
        **Request Syntax**
        ::
          response = client.describe_simulation_application(
              application='string',
              applicationVersion='string'
          )
        
        **Response Syntax**
        ::
            {
                'arn': 'string',
                'name': 'string',
                'version': 'string',
                'sources': [
                    {
                        's3Bucket': 'string',
                        's3Key': 'string',
                        'etag': 'string',
                        'architecture': 'X86_64'|'ARM64'|'ARMHF'
                    },
                ],
                'simulationSoftwareSuite': {
                    'name': 'Gazebo',
                    'version': 'string'
                },
                'robotSoftwareSuite': {
                    'name': 'ROS',
                    'version': 'Kinetic'
                },
                'renderingEngine': {
                    'name': 'OGRE',
                    'version': 'string'
                },
                'revisionId': 'string',
                'lastUpdatedAt': datetime(2015, 1, 1),
                'tags': {
                    'string': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **arn** *(string) --* 
              The Amazon Resource Name (ARN) of the robot simulation application.
            - **name** *(string) --* 
              The name of the simulation application.
            - **version** *(string) --* 
              The version of the simulation application.
            - **sources** *(list) --* 
              The sources of the simulation application.
              - *(dict) --* 
                Information about a source.
                - **s3Bucket** *(string) --* 
                  The s3 bucket name.
                - **s3Key** *(string) --* 
                  The s3 object key.
                - **etag** *(string) --* 
                  A hash of the object specified by ``s3Bucket`` and ``s3Key`` .
                - **architecture** *(string) --* 
                  The taget processor architecture for the application.
            - **simulationSoftwareSuite** *(dict) --* 
              The simulation software suite used by the simulation application.
              - **name** *(string) --* 
                The name of the simulation software suite.
              - **version** *(string) --* 
                The version of the simulation software suite.
            - **robotSoftwareSuite** *(dict) --* 
              Information about the robot software suite.
              - **name** *(string) --* 
                The name of the robot software suite.
              - **version** *(string) --* 
                The version of the robot software suite.
            - **renderingEngine** *(dict) --* 
              The rendering engine for the simulation application.
              - **name** *(string) --* 
                The name of the rendering engine.
              - **version** *(string) --* 
                The version of the rendering engine.
            - **revisionId** *(string) --* 
              The revision id of the simulation application.
            - **lastUpdatedAt** *(datetime) --* 
              The time, in milliseconds since the epoch, when the simulation application was last updated.
            - **tags** *(dict) --* 
              The list of all tags added to the specified simulation application.
              - *(string) --* 
                - *(string) --* 
        :type application: string
        :param application: **[REQUIRED]**
          The application information for the simulation application.
        :type applicationVersion: string
        :param applicationVersion:
          The version of the simulation application to describe.
        :rtype: dict
        :returns:
        """
        pass

    def describe_simulation_job(self, job: str) -> Dict:
        """
        Describes a simulation job.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/DescribeSimulationJob>`_
        
        **Request Syntax**
        ::
          response = client.describe_simulation_job(
              job='string'
          )
        
        **Response Syntax**
        ::
            {
                'arn': 'string',
                'name': 'string',
                'status': 'Pending'|'Preparing'|'Running'|'Restarting'|'Completed'|'Failed'|'RunningFailed'|'Terminating'|'Terminated'|'Canceled',
                'lastUpdatedAt': datetime(2015, 1, 1),
                'failureBehavior': 'Fail'|'Continue',
                'failureCode': 'InternalServiceError'|'RobotApplicationCrash'|'SimulationApplicationCrash'|'BadPermissionsRobotApplication'|'BadPermissionsSimulationApplication'|'BadPermissionsS3Output'|'BadPermissionsCloudwatchLogs'|'SubnetIpLimitExceeded'|'ENILimitExceeded'|'BadPermissionsUserCredentials'|'InvalidBundleRobotApplication'|'InvalidBundleSimulationApplication'|'RobotApplicationVersionMismatchedEtag'|'SimulationApplicationVersionMismatchedEtag'|'WrongRegionS3Output'|'WrongRegionRobotApplication'|'WrongRegionSimulationApplication',
                'failureReason': 'string',
                'clientRequestToken': 'string',
                'outputLocation': {
                    's3Bucket': 'string',
                    's3Prefix': 'string'
                },
                'maxJobDurationInSeconds': 123,
                'simulationTimeMillis': 123,
                'iamRole': 'string',
                'robotApplications': [
                    {
                        'application': 'string',
                        'applicationVersion': 'string',
                        'launchConfig': {
                            'packageName': 'string',
                            'launchFile': 'string',
                            'environmentVariables': {
                                'string': 'string'
                            }
                        }
                    },
                ],
                'simulationApplications': [
                    {
                        'application': 'string',
                        'applicationVersion': 'string',
                        'launchConfig': {
                            'packageName': 'string',
                            'launchFile': 'string',
                            'environmentVariables': {
                                'string': 'string'
                            }
                        }
                    },
                ],
                'tags': {
                    'string': 'string'
                },
                'vpcConfig': {
                    'subnets': [
                        'string',
                    ],
                    'securityGroups': [
                        'string',
                    ],
                    'vpcId': 'string',
                    'assignPublicIp': True|False
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **arn** *(string) --* 
              The Amazon Resource Name (ARN) of the simulation job.
            - **name** *(string) --* 
              The name of the simulation job.
            - **status** *(string) --* 
              The status of the simulation job.
            - **lastUpdatedAt** *(datetime) --* 
              The time, in milliseconds since the epoch, when the simulation job was last updated.
            - **failureBehavior** *(string) --* 
              The failure behavior for the simulation job.
            - **failureCode** *(string) --* 
              The failure code of the simulation job if it failed:
                InternalServiceError  
              Internal service error.
                RobotApplicationCrash  
              Robot application exited abnormally.
                SimulationApplicationCrash  
              Simulation application exited abnormally.
                BadPermissionsRobotApplication  
              Robot application bundle could not be downloaded.
                BadPermissionsSimulationApplication  
              Simulation application bundle could not be downloaded.
                BadPermissionsS3Output  
              Unable to publish outputs to customer-provided S3 bucket.
                BadPermissionsCloudwatchLogs  
              Unable to publish logs to customer-provided CloudWatch Logs resource.
                SubnetIpLimitExceeded  
              Subnet IP limit exceeded.
                ENILimitExceeded  
              ENI limit exceeded.
                BadPermissionsUserCredentials  
              Unable to use the Role provided.
                InvalidBundleRobotApplication  
              Robot bundle cannot be extracted (invalid format, bundling error, or other issue).
                InvalidBundleSimulationApplication  
              Simulation bundle cannot be extracted (invalid format, bundling error, or other issue).
                RobotApplicationVersionMismatchedEtag  
              Etag for RobotApplication does not match value during version creation.
                SimulationApplicationVersionMismatchedEtag  
              Etag for SimulationApplication does not match value during version creation.
            - **failureReason** *(string) --* 
              Details about why the simulation job failed. For more information about troubleshooting, see `Troubleshooting <https://docs.aws.amazon.com/robomaker/latest/dg/troubleshooting.html>`__ .
            - **clientRequestToken** *(string) --* 
              Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
            - **outputLocation** *(dict) --* 
              Location for output files generated by the simulation job.
              - **s3Bucket** *(string) --* 
                The S3 bucket for output.
              - **s3Prefix** *(string) --* 
                The S3 folder in the ``s3Bucket`` where output files will be placed.
            - **maxJobDurationInSeconds** *(integer) --* 
              The maximum job duration in seconds. The value must be 8 days (691,200 seconds) or less.
            - **simulationTimeMillis** *(integer) --* 
              The simulation job execution duration in milliseconds.
            - **iamRole** *(string) --* 
              The IAM role that allows the simulation instance to call the AWS APIs that are specified in its associated policies on your behalf.
            - **robotApplications** *(list) --* 
              A list of robot applications.
              - *(dict) --* 
                Application configuration information for a robot.
                - **application** *(string) --* 
                  The application information for the robot application.
                - **applicationVersion** *(string) --* 
                  The version of the robot application.
                - **launchConfig** *(dict) --* 
                  The launch configuration for the robot application.
                  - **packageName** *(string) --* 
                    The package name.
                  - **launchFile** *(string) --* 
                    The launch file name.
                  - **environmentVariables** *(dict) --* 
                    The environment variables for the application launch.
                    - *(string) --* 
                      - *(string) --* 
            - **simulationApplications** *(list) --* 
              A list of simulation applications.
              - *(dict) --* 
                Information about a simulation application configuration.
                - **application** *(string) --* 
                  The application information for the simulation application.
                - **applicationVersion** *(string) --* 
                  The version of the simulation application.
                - **launchConfig** *(dict) --* 
                  The launch configuration for the simulation application.
                  - **packageName** *(string) --* 
                    The package name.
                  - **launchFile** *(string) --* 
                    The launch file name.
                  - **environmentVariables** *(dict) --* 
                    The environment variables for the application launch.
                    - *(string) --* 
                      - *(string) --* 
            - **tags** *(dict) --* 
              The list of all tags added to the specified simulation job.
              - *(string) --* 
                - *(string) --* 
            - **vpcConfig** *(dict) --* 
              The VPC configuration.
              - **subnets** *(list) --* 
                A list of subnet IDs associated with the simulation job.
                - *(string) --* 
              - **securityGroups** *(list) --* 
                A list of security group IDs associated with the simulation job.
                - *(string) --* 
              - **vpcId** *(string) --* 
                The VPC ID associated with your simulation job.
              - **assignPublicIp** *(boolean) --* 
                A boolean indicating if a public IP was assigned.
        :type job: string
        :param job: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the simulation job to be described.
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

    def list_deployment_jobs(self, filters: List = None, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Returns a list of deployment jobs for a fleet. You can optionally provide filters to retrieve specific deployment jobs.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/ListDeploymentJobs>`_
        
        **Request Syntax**
        ::
          response = client.list_deployment_jobs(
              filters=[
                  {
                      'name': 'string',
                      'values': [
                          'string',
                      ]
                  },
              ],
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'deploymentJobs': [
                    {
                        'arn': 'string',
                        'fleet': 'string',
                        'status': 'Pending'|'Preparing'|'InProgress'|'Failed'|'Succeeded',
                        'deploymentApplicationConfigs': [
                            {
                                'application': 'string',
                                'applicationVersion': 'string',
                                'launchConfig': {
                                    'packageName': 'string',
                                    'preLaunchFile': 'string',
                                    'launchFile': 'string',
                                    'postLaunchFile': 'string',
                                    'environmentVariables': {
                                        'string': 'string'
                                    }
                                }
                            },
                        ],
                        'deploymentConfig': {
                            'concurrentDeploymentPercentage': 123,
                            'failureThresholdPercentage': 123
                        },
                        'failureReason': 'string',
                        'failureCode': 'ResourceNotFound'|'FailureThresholdBreached'|'RobotDeploymentNoResponse'|'GreengrassDeploymentFailed'|'MissingRobotArchitecture'|'MissingRobotApplicationArchitecture'|'MissingRobotDeploymentResource'|'GreengrassGroupVersionDoesNotExist'|'ExtractingBundleFailure'|'PreLaunchFileFailure'|'PostLaunchFileFailure'|'BadPermissionError'|'InternalServerError',
                        'createdAt': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **deploymentJobs** *(list) --* 
              A list of deployment jobs that meet the criteria of the request.
              - *(dict) --* 
                Information about a deployment job.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the deployment job.
                - **fleet** *(string) --* 
                  The Amazon Resource Name (ARN) of the fleet.
                - **status** *(string) --* 
                  The status of the deployment job.
                - **deploymentApplicationConfigs** *(list) --* 
                  The deployment application configuration.
                  - *(dict) --* 
                    Information about a deployment application configuration.
                    - **application** *(string) --* 
                      The Amazon Resource Name (ARN) of the robot application.
                    - **applicationVersion** *(string) --* 
                      The version of the application.
                    - **launchConfig** *(dict) --* 
                      The launch configuration.
                      - **packageName** *(string) --* 
                        The package name.
                      - **preLaunchFile** *(string) --* 
                        The deployment pre-launch file. This file will be executed prior to the launch file.
                      - **launchFile** *(string) --* 
                        The launch file name.
                      - **postLaunchFile** *(string) --* 
                        The deployment post-launch file. This file will be executed after the launch file.
                      - **environmentVariables** *(dict) --* 
                        An array of key/value pairs specifying environment variables for the robot application
                        - *(string) --* 
                          - *(string) --* 
                - **deploymentConfig** *(dict) --* 
                  The deployment configuration.
                  - **concurrentDeploymentPercentage** *(integer) --* 
                    The percentage of robots receiving the deployment at the same time.
                  - **failureThresholdPercentage** *(integer) --* 
                    The percentage of deployments that need to fail before stopping deployment.
                - **failureReason** *(string) --* 
                  A short description of the reason why the deployment job failed.
                - **failureCode** *(string) --* 
                  The deployment job failure code.
                - **createdAt** *(datetime) --* 
                  The time, in milliseconds since the epoch, when the deployment job was created.
            - **nextToken** *(string) --* 
              The ``nextToken`` value to include in a future ``ListDeploymentJobs`` request. When the results of a ``ListDeploymentJobs`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return. 
        :type filters: list
        :param filters:
          Optional filters to limit results.
          - *(dict) --*
            Information about a filter.
            - **name** *(string) --*
              The name of the filter.
            - **values** *(list) --*
              A list of values.
              - *(string) --*
        :type nextToken: string
        :param nextToken:
          The ``nextToken`` value returned from a previous paginated ``ListDeploymentJobs`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value.
          .. note::
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
        :type maxResults: integer
        :param maxResults:
          The maximum number of deployment job results returned by ``ListDeploymentJobs`` in paginated output. When this parameter is used, ``ListDeploymentJobs`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListDeploymentJobs`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListDeploymentJobs`` returns up to 100 results and a ``nextToken`` value if applicable.
        :rtype: dict
        :returns:
        """
        pass

    def list_fleets(self, nextToken: str = None, maxResults: int = None, filters: List = None) -> Dict:
        """
        Returns a list of fleets. You can optionally provide filters to retrieve specific fleets.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/ListFleets>`_
        
        **Request Syntax**
        ::
          response = client.list_fleets(
              nextToken='string',
              maxResults=123,
              filters=[
                  {
                      'name': 'string',
                      'values': [
                          'string',
                      ]
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'fleetDetails': [
                    {
                        'name': 'string',
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastDeploymentStatus': 'Pending'|'Preparing'|'InProgress'|'Failed'|'Succeeded',
                        'lastDeploymentJob': 'string',
                        'lastDeploymentTime': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **fleetDetails** *(list) --* 
              A list of fleet details meeting the request criteria.
              - *(dict) --* 
                Information about a fleet.
                - **name** *(string) --* 
                  The name of the fleet.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the fleet.
                - **createdAt** *(datetime) --* 
                  The time, in milliseconds since the epoch, when the fleet was created.
                - **lastDeploymentStatus** *(string) --* 
                  The status of the last fleet deployment.
                - **lastDeploymentJob** *(string) --* 
                  The Amazon Resource Name (ARN) of the last deployment job.
                - **lastDeploymentTime** *(datetime) --* 
                  The time of the last deployment.
            - **nextToken** *(string) --* 
              The ``nextToken`` value to include in a future ``ListDeploymentJobs`` request. When the results of a ``ListFleets`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return. 
        :type nextToken: string
        :param nextToken:
          The ``nextToken`` value returned from a previous paginated ``ListFleets`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value.
          .. note::
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
        :type maxResults: integer
        :param maxResults:
          The maximum number of deployment job results returned by ``ListFleets`` in paginated output. When this parameter is used, ``ListFleets`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListFleets`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListFleets`` returns up to 100 results and a ``nextToken`` value if applicable.
        :type filters: list
        :param filters:
          Optional filters to limit results.
          - *(dict) --*
            Information about a filter.
            - **name** *(string) --*
              The name of the filter.
            - **values** *(list) --*
              A list of values.
              - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def list_robot_applications(self, versionQualifier: str = None, nextToken: str = None, maxResults: int = None, filters: List = None) -> Dict:
        """
        Returns a list of robot application. You can optionally provide filters to retrieve specific robot applications.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/ListRobotApplications>`_
        
        **Request Syntax**
        ::
          response = client.list_robot_applications(
              versionQualifier='string',
              nextToken='string',
              maxResults=123,
              filters=[
                  {
                      'name': 'string',
                      'values': [
                          'string',
                      ]
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'robotApplicationSummaries': [
                    {
                        'name': 'string',
                        'arn': 'string',
                        'version': 'string',
                        'lastUpdatedAt': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **robotApplicationSummaries** *(list) --* 
              A list of robot application summaries that meet the criteria of the request.
              - *(dict) --* 
                Summary information for a robot application.
                - **name** *(string) --* 
                  The name of the robot application.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the robot.
                - **version** *(string) --* 
                  The version of the robot application.
                - **lastUpdatedAt** *(datetime) --* 
                  The time, in milliseconds since the epoch, when the robot application was last updated.
            - **nextToken** *(string) --* 
              The ``nextToken`` value to include in a future ``ListRobotApplications`` request. When the results of a ``ListRobotApplications`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return. 
        :type versionQualifier: string
        :param versionQualifier:
          The version qualifier of the robot application.
        :type nextToken: string
        :param nextToken:
          The ``nextToken`` value returned from a previous paginated ``ListRobotApplications`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value.
          .. note::
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
        :type maxResults: integer
        :param maxResults:
          The maximum number of deployment job results returned by ``ListRobotApplications`` in paginated output. When this parameter is used, ``ListRobotApplications`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListFleets`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListRobotApplications`` returns up to 100 results and a ``nextToken`` value if applicable.
        :type filters: list
        :param filters:
          Optional filters to limit results.
          - *(dict) --*
            Information about a filter.
            - **name** *(string) --*
              The name of the filter.
            - **values** *(list) --*
              A list of values.
              - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def list_robots(self, nextToken: str = None, maxResults: int = None, filters: List = None) -> Dict:
        """
        Returns a list of robots. You can optionally provide filters to retrieve specific robots.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/ListRobots>`_
        
        **Request Syntax**
        ::
          response = client.list_robots(
              nextToken='string',
              maxResults=123,
              filters=[
                  {
                      'name': 'string',
                      'values': [
                          'string',
                      ]
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'robots': [
                    {
                        'arn': 'string',
                        'name': 'string',
                        'fleetArn': 'string',
                        'status': 'Available'|'Registered'|'PendingNewDeployment'|'Deploying'|'Failed'|'InSync'|'NoResponse',
                        'greenGrassGroupId': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'architecture': 'X86_64'|'ARM64'|'ARMHF',
                        'lastDeploymentJob': 'string',
                        'lastDeploymentTime': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **robots** *(list) --* 
              A list of robots that meet the criteria of the request.
              - *(dict) --* 
                Information about a robot.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the robot.
                - **name** *(string) --* 
                  The name of the robot.
                - **fleetArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the fleet.
                - **status** *(string) --* 
                  The status of the robot.
                - **greenGrassGroupId** *(string) --* 
                  The Greengrass group associated with the robot.
                - **createdAt** *(datetime) --* 
                  The time, in milliseconds since the epoch, when the robot was created.
                - **architecture** *(string) --* 
                  The architecture of the robot.
                - **lastDeploymentJob** *(string) --* 
                  The Amazon Resource Name (ARN) of the last deployment job.
                - **lastDeploymentTime** *(datetime) --* 
                  The time of the last deployment.
            - **nextToken** *(string) --* 
              The ``nextToken`` value to include in a future ``ListRobots`` request. When the results of a ``ListRobot`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return. 
        :type nextToken: string
        :param nextToken:
          The ``nextToken`` value returned from a previous paginated ``ListRobots`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value.
          .. note::
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
        :type maxResults: integer
        :param maxResults:
          The maximum number of deployment job results returned by ``ListRobots`` in paginated output. When this parameter is used, ``ListRobots`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListFleets`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListRobots`` returns up to 100 results and a ``nextToken`` value if applicable.
        :type filters: list
        :param filters:
          Optional filters to limit results.
          - *(dict) --*
            Information about a filter.
            - **name** *(string) --*
              The name of the filter.
            - **values** *(list) --*
              A list of values.
              - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def list_simulation_applications(self, versionQualifier: str = None, nextToken: str = None, maxResults: int = None, filters: List = None) -> Dict:
        """
        Returns a list of simulation applications. You can optionally provide filters to retrieve specific simulation applications.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/ListSimulationApplications>`_
        
        **Request Syntax**
        ::
          response = client.list_simulation_applications(
              versionQualifier='string',
              nextToken='string',
              maxResults=123,
              filters=[
                  {
                      'name': 'string',
                      'values': [
                          'string',
                      ]
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'simulationApplicationSummaries': [
                    {
                        'name': 'string',
                        'arn': 'string',
                        'version': 'string',
                        'lastUpdatedAt': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **simulationApplicationSummaries** *(list) --* 
              A list of simulation application summaries that meet the criteria of the request.
              - *(dict) --* 
                Summary information for a simulation application.
                - **name** *(string) --* 
                  The name of the simulation application.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the simulation application.
                - **version** *(string) --* 
                  The version of the simulation application.
                - **lastUpdatedAt** *(datetime) --* 
                  The time, in milliseconds since the epoch, when the simulation application was last updated.
            - **nextToken** *(string) --* 
              The ``nextToken`` value to include in a future ``ListSimulationApplications`` request. When the results of a ``ListRobot`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return. 
        :type versionQualifier: string
        :param versionQualifier:
          The version qualifier of the simulation application.
        :type nextToken: string
        :param nextToken:
          The ``nextToken`` value returned from a previous paginated ``ListSimulationApplications`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value.
          .. note::
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
        :type maxResults: integer
        :param maxResults:
          The maximum number of deployment job results returned by ``ListSimulationApplications`` in paginated output. When this parameter is used, ``ListSimulationApplications`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListFleets`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListSimulationApplications`` returns up to 100 results and a ``nextToken`` value if applicable.
        :type filters: list
        :param filters:
          Optional list of filters to limit results. The only valid filter name is ``name`` .
          - *(dict) --*
            Information about a filter.
            - **name** *(string) --*
              The name of the filter.
            - **values** *(list) --*
              A list of values.
              - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def list_simulation_jobs(self, nextToken: str = None, maxResults: int = None, filters: List = None) -> Dict:
        """
        Returns a list of simulation jobs. You can optionally provide filters to retrieve specific simulation jobs.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/ListSimulationJobs>`_
        
        **Request Syntax**
        ::
          response = client.list_simulation_jobs(
              nextToken='string',
              maxResults=123,
              filters=[
                  {
                      'name': 'string',
                      'values': [
                          'string',
                      ]
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'simulationJobSummaries': [
                    {
                        'arn': 'string',
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'name': 'string',
                        'status': 'Pending'|'Preparing'|'Running'|'Restarting'|'Completed'|'Failed'|'RunningFailed'|'Terminating'|'Terminated'|'Canceled',
                        'simulationApplicationNames': [
                            'string',
                        ],
                        'robotApplicationNames': [
                            'string',
                        ]
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **simulationJobSummaries** *(list) --* 
              A list of simulation job summaries that meet the criteria of the request.
              - *(dict) --* 
                Summary information for a simulation job.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the simulation job.
                - **lastUpdatedAt** *(datetime) --* 
                  The time, in milliseconds since the epoch, when the simulation job was last updated.
                - **name** *(string) --* 
                  The name of the simulation job.
                - **status** *(string) --* 
                  The status of the simulation job.
                - **simulationApplicationNames** *(list) --* 
                  A list of simulation job simulation application names.
                  - *(string) --* 
                - **robotApplicationNames** *(list) --* 
                  A list of simulation job robot application names.
                  - *(string) --* 
            - **nextToken** *(string) --* 
              The ``nextToken`` value to include in a future ``ListSimulationJobs`` request. When the results of a ``ListRobot`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return. 
        :type nextToken: string
        :param nextToken:
          The ``nextToken`` value returned from a previous paginated ``ListSimulationJobs`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value.
          .. note::
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
        :type maxResults: integer
        :param maxResults:
          The maximum number of deployment job results returned by ``ListSimulationJobs`` in paginated output. When this parameter is used, ``ListSimulationJobs`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListFleets`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListSimulationJobs`` returns up to 100 results and a ``nextToken`` value if applicable.
        :type filters: list
        :param filters:
          Optional filters to limit results.
          - *(dict) --*
            Information about a filter.
            - **name** *(string) --*
              The name of the filter.
            - **values** *(list) --*
              A list of values.
              - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def list_tags_for_resource(self, resourceArn: str) -> Dict:
        """
        Lists all tags on a AWS RoboMaker resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/ListTagsForResource>`_
        
        **Request Syntax**
        ::
          response = client.list_tags_for_resource(
              resourceArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'tags': {
                    'string': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **tags** *(dict) --* 
              The list of all tags added to the specified resource.
              - *(string) --* 
                - *(string) --* 
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**
          The AWS RoboMaker Amazon Resource Name (ARN) with tags to be listed.
        :rtype: dict
        :returns:
        """
        pass

    def register_robot(self, fleet: str, robot: str) -> Dict:
        """
        Registers a robot with a fleet.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/RegisterRobot>`_
        
        **Request Syntax**
        ::
          response = client.register_robot(
              fleet='string',
              robot='string'
          )
        
        **Response Syntax**
        ::
            {
                'fleet': 'string',
                'robot': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **fleet** *(string) --* 
              The Amazon Resource Name (ARN) of the fleet that the robot will join.
            - **robot** *(string) --* 
              Information about the robot registration.
        :type fleet: string
        :param fleet: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the fleet.
        :type robot: string
        :param robot: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the robot.
        :rtype: dict
        :returns:
        """
        pass

    def restart_simulation_job(self, job: str) -> Dict:
        """
        Restarts a running simulation job.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/RestartSimulationJob>`_
        
        **Request Syntax**
        ::
          response = client.restart_simulation_job(
              job='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type job: string
        :param job: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the simulation job.
        :rtype: dict
        :returns:
        """
        pass

    def sync_deployment_job(self, clientRequestToken: str, fleet: str) -> Dict:
        """
        Syncrhonizes robots in a fleet to the latest deployment. This is helpful if robots were added after a deployment.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/SyncDeploymentJob>`_
        
        **Request Syntax**
        ::
          response = client.sync_deployment_job(
              clientRequestToken='string',
              fleet='string'
          )
        
        **Response Syntax**
        ::
            {
                'arn': 'string',
                'fleet': 'string',
                'status': 'Pending'|'Preparing'|'InProgress'|'Failed'|'Succeeded',
                'deploymentConfig': {
                    'concurrentDeploymentPercentage': 123,
                    'failureThresholdPercentage': 123
                },
                'deploymentApplicationConfigs': [
                    {
                        'application': 'string',
                        'applicationVersion': 'string',
                        'launchConfig': {
                            'packageName': 'string',
                            'preLaunchFile': 'string',
                            'launchFile': 'string',
                            'postLaunchFile': 'string',
                            'environmentVariables': {
                                'string': 'string'
                            }
                        }
                    },
                ],
                'failureReason': 'string',
                'failureCode': 'ResourceNotFound'|'FailureThresholdBreached'|'RobotDeploymentNoResponse'|'GreengrassDeploymentFailed'|'MissingRobotArchitecture'|'MissingRobotApplicationArchitecture'|'MissingRobotDeploymentResource'|'GreengrassGroupVersionDoesNotExist'|'ExtractingBundleFailure'|'PreLaunchFileFailure'|'PostLaunchFileFailure'|'BadPermissionError'|'InternalServerError',
                'createdAt': datetime(2015, 1, 1)
            }
        
        **Response Structure**
          - *(dict) --* 
            - **arn** *(string) --* 
              The Amazon Resource Name (ARN) of the synchronization request.
            - **fleet** *(string) --* 
              The Amazon Resource Name (ARN) of the fleet.
            - **status** *(string) --* 
              The status of the synchronization job.
            - **deploymentConfig** *(dict) --* 
              Information about the deployment configuration.
              - **concurrentDeploymentPercentage** *(integer) --* 
                The percentage of robots receiving the deployment at the same time.
              - **failureThresholdPercentage** *(integer) --* 
                The percentage of deployments that need to fail before stopping deployment.
            - **deploymentApplicationConfigs** *(list) --* 
              Information about the deployment application configurations.
              - *(dict) --* 
                Information about a deployment application configuration.
                - **application** *(string) --* 
                  The Amazon Resource Name (ARN) of the robot application.
                - **applicationVersion** *(string) --* 
                  The version of the application.
                - **launchConfig** *(dict) --* 
                  The launch configuration.
                  - **packageName** *(string) --* 
                    The package name.
                  - **preLaunchFile** *(string) --* 
                    The deployment pre-launch file. This file will be executed prior to the launch file.
                  - **launchFile** *(string) --* 
                    The launch file name.
                  - **postLaunchFile** *(string) --* 
                    The deployment post-launch file. This file will be executed after the launch file.
                  - **environmentVariables** *(dict) --* 
                    An array of key/value pairs specifying environment variables for the robot application
                    - *(string) --* 
                      - *(string) --* 
            - **failureReason** *(string) --* 
              The failure reason if the job fails.
            - **failureCode** *(string) --* 
              The failure code if the job fails:
                InternalServiceError  
              Internal service error.
                RobotApplicationCrash  
              Robot application exited abnormally.
                SimulationApplicationCrash  
              Simulation application exited abnormally.
                BadPermissionsRobotApplication  
              Robot application bundle could not be downloaded.
                BadPermissionsSimulationApplication  
              Simulation application bundle could not be downloaded.
                BadPermissionsS3Output  
              Unable to publish outputs to customer-provided S3 bucket.
                BadPermissionsCloudwatchLogs  
              Unable to publish logs to customer-provided CloudWatch Logs resource.
                SubnetIpLimitExceeded  
              Subnet IP limit exceeded.
                ENILimitExceeded  
              ENI limit exceeded.
                BadPermissionsUserCredentials  
              Unable to use the Role provided.
                InvalidBundleRobotApplication  
              Robot bundle cannot be extracted (invalid format, bundling error, or other issue).
                InvalidBundleSimulationApplication  
              Simulation bundle cannot be extracted (invalid format, bundling error, or other issue).
                RobotApplicationVersionMismatchedEtag  
              Etag for RobotApplication does not match value during version creation.
                SimulationApplicationVersionMismatchedEtag  
              Etag for SimulationApplication does not match value during version creation.
            - **createdAt** *(datetime) --* 
              The time, in milliseconds since the epoch, when the fleet was created.
        :type clientRequestToken: string
        :param clientRequestToken: **[REQUIRED]**
          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
          This field is autopopulated if not provided.
        :type fleet: string
        :param fleet: **[REQUIRED]**
          The target fleet for the synchronization.
        :rtype: dict
        :returns:
        """
        pass

    def tag_resource(self, resourceArn: str, tags: Dict) -> Dict:
        """
        Adds or edits tags for a AWS RoboMaker resource.
        Each tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty strings. 
        For information about the rules that apply to tag keys and tag values, see `User-Defined Tag Restrictions <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html>`__ in the *AWS Billing and Cost Management User Guide* . 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/TagResource>`_
        
        **Request Syntax**
        ::
          response = client.tag_resource(
              resourceArn='string',
              tags={
                  'string': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the AWS RoboMaker resource you are tagging.
        :type tags: dict
        :param tags: **[REQUIRED]**
          A map that contains tag keys and tag values that are attached to the resource.
          - *(string) --*
            - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def untag_resource(self, resourceArn: str, tagKeys: List) -> Dict:
        """
        .. _https://docs.aws.amazon.com/robomaker/latest/dg//API_Reference.htmlAPI_TagResource.html: https://docs.aws.amazon.com/robomaker/latest/dg//API_Reference.htmlAPI_TagResource.html
        Removes the specified tags from the specified AWS RoboMaker resource.
        To remove a tag, specify the tag key. To change the tag value of an existing tag key, use ` ``TagResource`` https://docs.aws.amazon.com/robomaker/latest/dg//API_Reference.htmlAPI_TagResource.html`__ . 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/UntagResource>`_
        
        **Request Syntax**
        ::
          response = client.untag_resource(
              resourceArn='string',
              tagKeys=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the AWS RoboMaker resource you are removing tags.
        :type tagKeys: list
        :param tagKeys: **[REQUIRED]**
          A map that contains tag keys and tag values that will be unattached from the resource.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def update_robot_application(self, application: str, sources: List, robotSoftwareSuite: Dict, currentRevisionId: str = None) -> Dict:
        """
        Updates a robot application.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/UpdateRobotApplication>`_
        
        **Request Syntax**
        ::
          response = client.update_robot_application(
              application='string',
              sources=[
                  {
                      's3Bucket': 'string',
                      's3Key': 'string',
                      'architecture': 'X86_64'|'ARM64'|'ARMHF'
                  },
              ],
              robotSoftwareSuite={
                  'name': 'ROS',
                  'version': 'Kinetic'
              },
              currentRevisionId='string'
          )
        
        **Response Syntax**
        ::
            {
                'arn': 'string',
                'name': 'string',
                'version': 'string',
                'sources': [
                    {
                        's3Bucket': 'string',
                        's3Key': 'string',
                        'etag': 'string',
                        'architecture': 'X86_64'|'ARM64'|'ARMHF'
                    },
                ],
                'robotSoftwareSuite': {
                    'name': 'ROS',
                    'version': 'Kinetic'
                },
                'lastUpdatedAt': datetime(2015, 1, 1),
                'revisionId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **arn** *(string) --* 
              The Amazon Resource Name (ARN) of the updated robot application.
            - **name** *(string) --* 
              The name of the robot application.
            - **version** *(string) --* 
              The version of the robot application.
            - **sources** *(list) --* 
              The sources of the robot application.
              - *(dict) --* 
                Information about a source.
                - **s3Bucket** *(string) --* 
                  The s3 bucket name.
                - **s3Key** *(string) --* 
                  The s3 object key.
                - **etag** *(string) --* 
                  A hash of the object specified by ``s3Bucket`` and ``s3Key`` .
                - **architecture** *(string) --* 
                  The taget processor architecture for the application.
            - **robotSoftwareSuite** *(dict) --* 
              The robot software suite used by the robot application.
              - **name** *(string) --* 
                The name of the robot software suite.
              - **version** *(string) --* 
                The version of the robot software suite.
            - **lastUpdatedAt** *(datetime) --* 
              The time, in milliseconds since the epoch, when the robot application was last updated.
            - **revisionId** *(string) --* 
              The revision id of the robot application.
        :type application: string
        :param application: **[REQUIRED]**
          The application information for the robot application.
        :type sources: list
        :param sources: **[REQUIRED]**
          The sources of the robot application.
          - *(dict) --*
            Information about a source configuration.
            - **s3Bucket** *(string) --*
              The Amazon S3 bucket name.
            - **s3Key** *(string) --*
              The s3 object key.
            - **architecture** *(string) --*
              The target processor architecture for the application.
        :type robotSoftwareSuite: dict
        :param robotSoftwareSuite: **[REQUIRED]**
          The robot software suite used by the robot application.
          - **name** *(string) --*
            The name of the robot software suite.
          - **version** *(string) --*
            The version of the robot software suite.
        :type currentRevisionId: string
        :param currentRevisionId:
          The revision id for the robot application.
        :rtype: dict
        :returns:
        """
        pass

    def update_simulation_application(self, application: str, sources: List, simulationSoftwareSuite: Dict, robotSoftwareSuite: Dict, renderingEngine: Dict, currentRevisionId: str = None) -> Dict:
        """
        Updates a simulation application.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/UpdateSimulationApplication>`_
        
        **Request Syntax**
        ::
          response = client.update_simulation_application(
              application='string',
              sources=[
                  {
                      's3Bucket': 'string',
                      's3Key': 'string',
                      'architecture': 'X86_64'|'ARM64'|'ARMHF'
                  },
              ],
              simulationSoftwareSuite={
                  'name': 'Gazebo',
                  'version': 'string'
              },
              robotSoftwareSuite={
                  'name': 'ROS',
                  'version': 'Kinetic'
              },
              renderingEngine={
                  'name': 'OGRE',
                  'version': 'string'
              },
              currentRevisionId='string'
          )
        
        **Response Syntax**
        ::
            {
                'arn': 'string',
                'name': 'string',
                'version': 'string',
                'sources': [
                    {
                        's3Bucket': 'string',
                        's3Key': 'string',
                        'etag': 'string',
                        'architecture': 'X86_64'|'ARM64'|'ARMHF'
                    },
                ],
                'simulationSoftwareSuite': {
                    'name': 'Gazebo',
                    'version': 'string'
                },
                'robotSoftwareSuite': {
                    'name': 'ROS',
                    'version': 'Kinetic'
                },
                'renderingEngine': {
                    'name': 'OGRE',
                    'version': 'string'
                },
                'lastUpdatedAt': datetime(2015, 1, 1),
                'revisionId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **arn** *(string) --* 
              The Amazon Resource Name (ARN) of the updated simulation application.
            - **name** *(string) --* 
              The name of the simulation application.
            - **version** *(string) --* 
              The version of the robot application.
            - **sources** *(list) --* 
              The sources of the simulation application.
              - *(dict) --* 
                Information about a source.
                - **s3Bucket** *(string) --* 
                  The s3 bucket name.
                - **s3Key** *(string) --* 
                  The s3 object key.
                - **etag** *(string) --* 
                  A hash of the object specified by ``s3Bucket`` and ``s3Key`` .
                - **architecture** *(string) --* 
                  The taget processor architecture for the application.
            - **simulationSoftwareSuite** *(dict) --* 
              The simulation software suite used by the simulation application.
              - **name** *(string) --* 
                The name of the simulation software suite.
              - **version** *(string) --* 
                The version of the simulation software suite.
            - **robotSoftwareSuite** *(dict) --* 
              Information about the robot software suite.
              - **name** *(string) --* 
                The name of the robot software suite.
              - **version** *(string) --* 
                The version of the robot software suite.
            - **renderingEngine** *(dict) --* 
              The rendering engine for the simulation application.
              - **name** *(string) --* 
                The name of the rendering engine.
              - **version** *(string) --* 
                The version of the rendering engine.
            - **lastUpdatedAt** *(datetime) --* 
              The time, in milliseconds since the epoch, when the simulation application was last updated.
            - **revisionId** *(string) --* 
              The revision id of the simulation application.
        :type application: string
        :param application: **[REQUIRED]**
          The application information for the simulation application.
        :type sources: list
        :param sources: **[REQUIRED]**
          The sources of the simulation application.
          - *(dict) --*
            Information about a source configuration.
            - **s3Bucket** *(string) --*
              The Amazon S3 bucket name.
            - **s3Key** *(string) --*
              The s3 object key.
            - **architecture** *(string) --*
              The target processor architecture for the application.
        :type simulationSoftwareSuite: dict
        :param simulationSoftwareSuite: **[REQUIRED]**
          The simulation software suite used by the simulation application.
          - **name** *(string) --*
            The name of the simulation software suite.
          - **version** *(string) --*
            The version of the simulation software suite.
        :type robotSoftwareSuite: dict
        :param robotSoftwareSuite: **[REQUIRED]**
          Information about the robot software suite.
          - **name** *(string) --*
            The name of the robot software suite.
          - **version** *(string) --*
            The version of the robot software suite.
        :type renderingEngine: dict
        :param renderingEngine: **[REQUIRED]**
          The rendering engine for the simulation application.
          - **name** *(string) --*
            The name of the rendering engine.
          - **version** *(string) --*
            The version of the rendering engine.
        :type currentRevisionId: string
        :param currentRevisionId:
          The revision id for the robot application.
        :rtype: dict
        :returns:
        """
        pass
