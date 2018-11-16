from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def associate_role_to_group(self, GroupId: str, RoleArn: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/AssociateRoleToGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.associate_role_to_group(
              GroupId=\'string\',
              RoleArn=\'string\'
          )
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the AWS Greengrass group.
        
        :type RoleArn: string
        :param RoleArn: The ARN of the role you wish to associate with this group.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AssociatedAt\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* success
            
            - **AssociatedAt** *(string) --* The time, in milliseconds since the epoch, when the role ARN was associated with the group.
        """
        pass

    def associate_service_role_to_account(self, RoleArn: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/AssociateServiceRoleToAccount>`_
        
        **Request Syntax** 
        ::
        
          response = client.associate_service_role_to_account(
              RoleArn=\'string\'
          )
        :type RoleArn: string
        :param RoleArn: The ARN of the service role you wish to associate with your account.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AssociatedAt\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* success
            
            - **AssociatedAt** *(string) --* The time when the service role was associated with the account.
        """
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
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

    def create_core_definition(self, AmznClientToken: str = None, InitialVersion: Dict = None, Name: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateCoreDefinition>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_core_definition(
              AmznClientToken=\'string\',
              InitialVersion={
                  \'Cores\': [
                      {
                          \'CertificateArn\': \'string\',
                          \'Id\': \'string\',
                          \'SyncShadow\': True|False,
                          \'ThingArn\': \'string\'
                      },
                  ]
              },
              Name=\'string\'
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.
        
        :type InitialVersion: dict
        :param InitialVersion: Information about the initial version of the core definition.
        
          - **Cores** *(list) --* A list of cores in the core definition version.
        
            - *(dict) --* Information about a core.
        
              - **CertificateArn** *(string) --* The ARN of the certificate associated with the core.
        
              - **Id** *(string) --* A descriptive or arbitrary ID for the core. This value must be unique within the core definition version. Max length is 128 characters with pattern \'\'[a‑zA‑Z0‑9:_‑]+\'\'.
        
              - **SyncShadow** *(boolean) --* If true, the core\'s local shadow is automatically synced with the cloud.
        
              - **ThingArn** *(string) --* The ARN of the thing which is the core.
        
        :type Name: string
        :param Name: The name of the core definition.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Id\': \'string\',
                \'LastUpdatedTimestamp\': \'string\',
                \'LatestVersion\': \'string\',
                \'LatestVersionArn\': \'string\',
                \'Name\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Arn** *(string) --* The ARN of the definition.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was created.
            
            - **Id** *(string) --* The ID of the definition.
            
            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was last updated.
            
            - **LatestVersion** *(string) --* The latest version of the definition.
            
            - **LatestVersionArn** *(string) --* The ARN of the latest version of the definition.
            
            - **Name** *(string) --* The name of the definition.
        """
        pass

    def create_core_definition_version(self, CoreDefinitionId: str, AmznClientToken: str = None, Cores: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateCoreDefinitionVersion>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_core_definition_version(
              AmznClientToken=\'string\',
              CoreDefinitionId=\'string\',
              Cores=[
                  {
                      \'CertificateArn\': \'string\',
                      \'Id\': \'string\',
                      \'SyncShadow\': True|False,
                      \'ThingArn\': \'string\'
                  },
              ]
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.
        
        :type CoreDefinitionId: string
        :param CoreDefinitionId: **[REQUIRED]** The ID of the core definition.
        
        :type Cores: list
        :param Cores: A list of cores in the core definition version.
        
          - *(dict) --* Information about a core.
        
            - **CertificateArn** *(string) --* The ARN of the certificate associated with the core.
        
            - **Id** *(string) --* A descriptive or arbitrary ID for the core. This value must be unique within the core definition version. Max length is 128 characters with pattern \'\'[a‑zA‑Z0‑9:_‑]+\'\'.
        
            - **SyncShadow** *(boolean) --* If true, the core\'s local shadow is automatically synced with the cloud.
        
            - **ThingArn** *(string) --* The ARN of the thing which is the core.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Id\': \'string\',
                \'Version\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Arn** *(string) --* The ARN of the version.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the version was created.
            
            - **Id** *(string) --* The ID of the version.
            
            - **Version** *(string) --* The unique ID of the version.
        """
        pass

    def create_deployment(self, GroupId: str, AmznClientToken: str = None, DeploymentId: str = None, DeploymentType: str = None, GroupVersionId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateDeployment>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_deployment(
              AmznClientToken=\'string\',
              DeploymentId=\'string\',
              DeploymentType=\'NewDeployment\'|\'Redeployment\'|\'ResetDeployment\'|\'ForceResetDeployment\',
              GroupId=\'string\',
              GroupVersionId=\'string\'
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.
        
        :type DeploymentId: string
        :param DeploymentId: The ID of the deployment if you wish to redeploy a previous deployment.
        
        :type DeploymentType: string
        :param DeploymentType: The type of deployment. When used in \'\'CreateDeployment\'\', only \'\'NewDeployment\'\' and \'\'Redeployment\'\' are valid.
        
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the AWS Greengrass group.
        
        :type GroupVersionId: string
        :param GroupVersionId: The ID of the group version to be deployed.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DeploymentArn\': \'string\',
                \'DeploymentId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* Success. The group was deployed.
            
            - **DeploymentArn** *(string) --* The ARN of the deployment.
            
            - **DeploymentId** *(string) --* The ID of the deployment.
        """
        pass

    def create_device_definition(self, AmznClientToken: str = None, InitialVersion: Dict = None, Name: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateDeviceDefinition>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_device_definition(
              AmznClientToken=\'string\',
              InitialVersion={
                  \'Devices\': [
                      {
                          \'CertificateArn\': \'string\',
                          \'Id\': \'string\',
                          \'SyncShadow\': True|False,
                          \'ThingArn\': \'string\'
                      },
                  ]
              },
              Name=\'string\'
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.
        
        :type InitialVersion: dict
        :param InitialVersion: Information about the initial version of the device definition.
        
          - **Devices** *(list) --* A list of devices in the definition version.
        
            - *(dict) --* Information about a device.
        
              - **CertificateArn** *(string) --* The ARN of the certificate associated with the device.
        
              - **Id** *(string) --* A descriptive or arbitrary ID for the device. This value must be unique within the device definition version. Max length is 128 characters with pattern \'\'[a‑zA‑Z0‑9:_‑]+\'\'.
        
              - **SyncShadow** *(boolean) --* If true, the device\'s local shadow will be automatically synced with the cloud.
        
              - **ThingArn** *(string) --* The thing ARN of the device.
        
        :type Name: string
        :param Name: The name of the device definition.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Id\': \'string\',
                \'LastUpdatedTimestamp\': \'string\',
                \'LatestVersion\': \'string\',
                \'LatestVersionArn\': \'string\',
                \'Name\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Arn** *(string) --* The ARN of the definition.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was created.
            
            - **Id** *(string) --* The ID of the definition.
            
            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was last updated.
            
            - **LatestVersion** *(string) --* The latest version of the definition.
            
            - **LatestVersionArn** *(string) --* The ARN of the latest version of the definition.
            
            - **Name** *(string) --* The name of the definition.
        """
        pass

    def create_device_definition_version(self, DeviceDefinitionId: str, AmznClientToken: str = None, Devices: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateDeviceDefinitionVersion>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_device_definition_version(
              AmznClientToken=\'string\',
              DeviceDefinitionId=\'string\',
              Devices=[
                  {
                      \'CertificateArn\': \'string\',
                      \'Id\': \'string\',
                      \'SyncShadow\': True|False,
                      \'ThingArn\': \'string\'
                  },
              ]
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.
        
        :type DeviceDefinitionId: string
        :param DeviceDefinitionId: **[REQUIRED]** The ID of the device definition.
        
        :type Devices: list
        :param Devices: A list of devices in the definition version.
        
          - *(dict) --* Information about a device.
        
            - **CertificateArn** *(string) --* The ARN of the certificate associated with the device.
        
            - **Id** *(string) --* A descriptive or arbitrary ID for the device. This value must be unique within the device definition version. Max length is 128 characters with pattern \'\'[a‑zA‑Z0‑9:_‑]+\'\'.
        
            - **SyncShadow** *(boolean) --* If true, the device\'s local shadow will be automatically synced with the cloud.
        
            - **ThingArn** *(string) --* The thing ARN of the device.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Id\': \'string\',
                \'Version\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Arn** *(string) --* The ARN of the version.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the version was created.
            
            - **Id** *(string) --* The ID of the version.
            
            - **Version** *(string) --* The unique ID of the version.
        """
        pass

    def create_function_definition(self, AmznClientToken: str = None, InitialVersion: Dict = None, Name: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateFunctionDefinition>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_function_definition(
              AmznClientToken=\'string\',
              InitialVersion={
                  \'Functions\': [
                      {
                          \'FunctionArn\': \'string\',
                          \'FunctionConfiguration\': {
                              \'EncodingType\': \'binary\'|\'json\',
                              \'Environment\': {
                                  \'AccessSysfs\': True|False,
                                  \'ResourceAccessPolicies\': [
                                      {
                                          \'Permission\': \'ro\'|\'rw\',
                                          \'ResourceId\': \'string\'
                                      },
                                  ],
                                  \'Variables\': {
                                      \'string\': \'string\'
                                  }
                              },
                              \'ExecArgs\': \'string\',
                              \'Executable\': \'string\',
                              \'MemorySize\': 123,
                              \'Pinned\': True|False,
                              \'Timeout\': 123
                          },
                          \'Id\': \'string\'
                      },
                  ]
              },
              Name=\'string\'
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.
        
        :type InitialVersion: dict
        :param InitialVersion: Information about the initial version of the function definition.
        
          - **Functions** *(list) --* A list of Lambda functions in this function definition version.
        
            - *(dict) --* Information about a Lambda function.
        
              - **FunctionArn** *(string) --* The ARN of the Lambda function.
        
              - **FunctionConfiguration** *(dict) --* The configuration of the Lambda function.
        
                - **EncodingType** *(string) --* The expected encoding type of the input payload for the function. The default is \'\'json\'\'.
        
                - **Environment** *(dict) --* The environment configuration of the function.
        
                  - **AccessSysfs** *(boolean) --* If true, the Lambda function is allowed to access the host\'s /sys folder. Use this when the Lambda function needs to read device information from /sys.
        
                  - **ResourceAccessPolicies** *(list) --* A list of the resources, with their permissions, to which the Lambda function will be granted access. A Lambda function can have at most 10 resources.
        
                    - *(dict) --* A policy used by the function to access a resource.
        
                      - **Permission** *(string) --* The permissions that the Lambda function has to the resource. Can be one of \'\'rw\'\' (read/write) or \'\'ro\'\' (read-only).
        
                      - **ResourceId** *(string) --* The ID of the resource. (This ID is assigned to the resource when you create the resource definiton.)
        
                  - **Variables** *(dict) --* Environment variables for the Lambda function\'s configuration.
        
                    - *(string) --* 
        
                      - *(string) --* 
        
                - **ExecArgs** *(string) --* The execution arguments.
        
                - **Executable** *(string) --* The name of the function executable.
        
                - **MemorySize** *(integer) --* The memory size, in KB, which the function requires.
        
                - **Pinned** *(boolean) --* True if the function is pinned. Pinned means the function is long-lived and starts when the core starts.
        
                - **Timeout** *(integer) --* The allowed function execution time, after which Lambda should terminate the function. This timeout still applies to pinned lambdas for each request.
        
              - **Id** *(string) --* A descriptive or arbitrary ID for the function. This value must be unique within the function definition version. Max length is 128 characters with pattern \'\'[a‑zA‑Z0‑9:_‑]+\'\'.
        
        :type Name: string
        :param Name: The name of the function definition.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Id\': \'string\',
                \'LastUpdatedTimestamp\': \'string\',
                \'LatestVersion\': \'string\',
                \'LatestVersionArn\': \'string\',
                \'Name\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Arn** *(string) --* The ARN of the definition.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was created.
            
            - **Id** *(string) --* The ID of the definition.
            
            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was last updated.
            
            - **LatestVersion** *(string) --* The latest version of the definition.
            
            - **LatestVersionArn** *(string) --* The ARN of the latest version of the definition.
            
            - **Name** *(string) --* The name of the definition.
        """
        pass

    def create_function_definition_version(self, FunctionDefinitionId: str, AmznClientToken: str = None, Functions: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateFunctionDefinitionVersion>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_function_definition_version(
              AmznClientToken=\'string\',
              FunctionDefinitionId=\'string\',
              Functions=[
                  {
                      \'FunctionArn\': \'string\',
                      \'FunctionConfiguration\': {
                          \'EncodingType\': \'binary\'|\'json\',
                          \'Environment\': {
                              \'AccessSysfs\': True|False,
                              \'ResourceAccessPolicies\': [
                                  {
                                      \'Permission\': \'ro\'|\'rw\',
                                      \'ResourceId\': \'string\'
                                  },
                              ],
                              \'Variables\': {
                                  \'string\': \'string\'
                              }
                          },
                          \'ExecArgs\': \'string\',
                          \'Executable\': \'string\',
                          \'MemorySize\': 123,
                          \'Pinned\': True|False,
                          \'Timeout\': 123
                      },
                      \'Id\': \'string\'
                  },
              ]
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.
        
        :type FunctionDefinitionId: string
        :param FunctionDefinitionId: **[REQUIRED]** The ID of the Lambda function definition.
        
        :type Functions: list
        :param Functions: A list of Lambda functions in this function definition version.
        
          - *(dict) --* Information about a Lambda function.
        
            - **FunctionArn** *(string) --* The ARN of the Lambda function.
        
            - **FunctionConfiguration** *(dict) --* The configuration of the Lambda function.
        
              - **EncodingType** *(string) --* The expected encoding type of the input payload for the function. The default is \'\'json\'\'.
        
              - **Environment** *(dict) --* The environment configuration of the function.
        
                - **AccessSysfs** *(boolean) --* If true, the Lambda function is allowed to access the host\'s /sys folder. Use this when the Lambda function needs to read device information from /sys.
        
                - **ResourceAccessPolicies** *(list) --* A list of the resources, with their permissions, to which the Lambda function will be granted access. A Lambda function can have at most 10 resources.
        
                  - *(dict) --* A policy used by the function to access a resource.
        
                    - **Permission** *(string) --* The permissions that the Lambda function has to the resource. Can be one of \'\'rw\'\' (read/write) or \'\'ro\'\' (read-only).
        
                    - **ResourceId** *(string) --* The ID of the resource. (This ID is assigned to the resource when you create the resource definiton.)
        
                - **Variables** *(dict) --* Environment variables for the Lambda function\'s configuration.
        
                  - *(string) --* 
        
                    - *(string) --* 
        
              - **ExecArgs** *(string) --* The execution arguments.
        
              - **Executable** *(string) --* The name of the function executable.
        
              - **MemorySize** *(integer) --* The memory size, in KB, which the function requires.
        
              - **Pinned** *(boolean) --* True if the function is pinned. Pinned means the function is long-lived and starts when the core starts.
        
              - **Timeout** *(integer) --* The allowed function execution time, after which Lambda should terminate the function. This timeout still applies to pinned lambdas for each request.
        
            - **Id** *(string) --* A descriptive or arbitrary ID for the function. This value must be unique within the function definition version. Max length is 128 characters with pattern \'\'[a‑zA‑Z0‑9:_‑]+\'\'.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Id\': \'string\',
                \'Version\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Arn** *(string) --* The ARN of the version.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the version was created.
            
            - **Id** *(string) --* The ID of the version.
            
            - **Version** *(string) --* The unique ID of the version.
        """
        pass

    def create_group(self, AmznClientToken: str = None, InitialVersion: Dict = None, Name: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_group(
              AmznClientToken=\'string\',
              InitialVersion={
                  \'CoreDefinitionVersionArn\': \'string\',
                  \'DeviceDefinitionVersionArn\': \'string\',
                  \'FunctionDefinitionVersionArn\': \'string\',
                  \'LoggerDefinitionVersionArn\': \'string\',
                  \'ResourceDefinitionVersionArn\': \'string\',
                  \'SubscriptionDefinitionVersionArn\': \'string\'
              },
              Name=\'string\'
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.
        
        :type InitialVersion: dict
        :param InitialVersion: Information about the initial version of the group.
        
          - **CoreDefinitionVersionArn** *(string) --* The ARN of the core definition version for this group.
        
          - **DeviceDefinitionVersionArn** *(string) --* The ARN of the device definition version for this group.
        
          - **FunctionDefinitionVersionArn** *(string) --* The ARN of the function definition version for this group.
        
          - **LoggerDefinitionVersionArn** *(string) --* The ARN of the logger definition version for this group.
        
          - **ResourceDefinitionVersionArn** *(string) --* The resource definition version ARN for this group.
        
          - **SubscriptionDefinitionVersionArn** *(string) --* The ARN of the subscription definition version for this group.
        
        :type Name: string
        :param Name: The name of the group.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Id\': \'string\',
                \'LastUpdatedTimestamp\': \'string\',
                \'LatestVersion\': \'string\',
                \'LatestVersionArn\': \'string\',
                \'Name\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* Success. The group was created.
            
            - **Arn** *(string) --* The ARN of the definition.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was created.
            
            - **Id** *(string) --* The ID of the definition.
            
            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was last updated.
            
            - **LatestVersion** *(string) --* The latest version of the definition.
            
            - **LatestVersionArn** *(string) --* The ARN of the latest version of the definition.
            
            - **Name** *(string) --* The name of the definition.
        """
        pass

    def create_group_certificate_authority(self, GroupId: str, AmznClientToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateGroupCertificateAuthority>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_group_certificate_authority(
              AmznClientToken=\'string\',
              GroupId=\'string\'
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.
        
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the AWS Greengrass group.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'GroupCertificateAuthorityArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* Success. The response body contains the new active CA ARN.
            
            - **GroupCertificateAuthorityArn** *(string) --* The ARN of the group certificate authority.
        """
        pass

    def create_group_version(self, GroupId: str, AmznClientToken: str = None, CoreDefinitionVersionArn: str = None, DeviceDefinitionVersionArn: str = None, FunctionDefinitionVersionArn: str = None, LoggerDefinitionVersionArn: str = None, ResourceDefinitionVersionArn: str = None, SubscriptionDefinitionVersionArn: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateGroupVersion>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_group_version(
              AmznClientToken=\'string\',
              CoreDefinitionVersionArn=\'string\',
              DeviceDefinitionVersionArn=\'string\',
              FunctionDefinitionVersionArn=\'string\',
              GroupId=\'string\',
              LoggerDefinitionVersionArn=\'string\',
              ResourceDefinitionVersionArn=\'string\',
              SubscriptionDefinitionVersionArn=\'string\'
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.
        
        :type CoreDefinitionVersionArn: string
        :param CoreDefinitionVersionArn: The ARN of the core definition version for this group.
        
        :type DeviceDefinitionVersionArn: string
        :param DeviceDefinitionVersionArn: The ARN of the device definition version for this group.
        
        :type FunctionDefinitionVersionArn: string
        :param FunctionDefinitionVersionArn: The ARN of the function definition version for this group.
        
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the AWS Greengrass group.
        
        :type LoggerDefinitionVersionArn: string
        :param LoggerDefinitionVersionArn: The ARN of the logger definition version for this group.
        
        :type ResourceDefinitionVersionArn: string
        :param ResourceDefinitionVersionArn: The resource definition version ARN for this group.
        
        :type SubscriptionDefinitionVersionArn: string
        :param SubscriptionDefinitionVersionArn: The ARN of the subscription definition version for this group.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Id\': \'string\',
                \'Version\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* Success. The response contains information about the group version.
            
            - **Arn** *(string) --* The ARN of the version.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the version was created.
            
            - **Id** *(string) --* The ID of the version.
            
            - **Version** *(string) --* The unique ID of the version.
        """
        pass

    def create_logger_definition(self, AmznClientToken: str = None, InitialVersion: Dict = None, Name: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateLoggerDefinition>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_logger_definition(
              AmznClientToken=\'string\',
              InitialVersion={
                  \'Loggers\': [
                      {
                          \'Component\': \'GreengrassSystem\'|\'Lambda\',
                          \'Id\': \'string\',
                          \'Level\': \'DEBUG\'|\'INFO\'|\'WARN\'|\'ERROR\'|\'FATAL\',
                          \'Space\': 123,
                          \'Type\': \'FileSystem\'|\'AWSCloudWatch\'
                      },
                  ]
              },
              Name=\'string\'
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.
        
        :type InitialVersion: dict
        :param InitialVersion: Information about the initial version of the logger definition.
        
          - **Loggers** *(list) --* A list of loggers.
        
            - *(dict) --* Information about a logger
        
              - **Component** *(string) --* The component that will be subject to logging.
        
              - **Id** *(string) --* A descriptive or arbitrary ID for the logger. This value must be unique within the logger definition version. Max length is 128 characters with pattern \'\'[a‑zA‑Z0‑9:_‑]+\'\'.
        
              - **Level** *(string) --* The level of the logs.
        
              - **Space** *(integer) --* The amount of file space, in KB, to use if the local file system is used for logging purposes.
        
              - **Type** *(string) --* The type of log output which will be used.
        
        :type Name: string
        :param Name: The name of the logger definition.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Id\': \'string\',
                \'LastUpdatedTimestamp\': \'string\',
                \'LatestVersion\': \'string\',
                \'LatestVersionArn\': \'string\',
                \'Name\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Arn** *(string) --* The ARN of the definition.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was created.
            
            - **Id** *(string) --* The ID of the definition.
            
            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was last updated.
            
            - **LatestVersion** *(string) --* The latest version of the definition.
            
            - **LatestVersionArn** *(string) --* The ARN of the latest version of the definition.
            
            - **Name** *(string) --* The name of the definition.
        """
        pass

    def create_logger_definition_version(self, LoggerDefinitionId: str, AmznClientToken: str = None, Loggers: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateLoggerDefinitionVersion>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_logger_definition_version(
              AmznClientToken=\'string\',
              LoggerDefinitionId=\'string\',
              Loggers=[
                  {
                      \'Component\': \'GreengrassSystem\'|\'Lambda\',
                      \'Id\': \'string\',
                      \'Level\': \'DEBUG\'|\'INFO\'|\'WARN\'|\'ERROR\'|\'FATAL\',
                      \'Space\': 123,
                      \'Type\': \'FileSystem\'|\'AWSCloudWatch\'
                  },
              ]
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.
        
        :type LoggerDefinitionId: string
        :param LoggerDefinitionId: **[REQUIRED]** The ID of the logger definition.
        
        :type Loggers: list
        :param Loggers: A list of loggers.
        
          - *(dict) --* Information about a logger
        
            - **Component** *(string) --* The component that will be subject to logging.
        
            - **Id** *(string) --* A descriptive or arbitrary ID for the logger. This value must be unique within the logger definition version. Max length is 128 characters with pattern \'\'[a‑zA‑Z0‑9:_‑]+\'\'.
        
            - **Level** *(string) --* The level of the logs.
        
            - **Space** *(integer) --* The amount of file space, in KB, to use if the local file system is used for logging purposes.
        
            - **Type** *(string) --* The type of log output which will be used.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Id\': \'string\',
                \'Version\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Arn** *(string) --* The ARN of the version.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the version was created.
            
            - **Id** *(string) --* The ID of the version.
            
            - **Version** *(string) --* The unique ID of the version.
        """
        pass

    def create_resource_definition(self, AmznClientToken: str = None, InitialVersion: Dict = None, Name: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateResourceDefinition>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_resource_definition(
              AmznClientToken=\'string\',
              InitialVersion={
                  \'Resources\': [
                      {
                          \'Id\': \'string\',
                          \'Name\': \'string\',
                          \'ResourceDataContainer\': {
                              \'LocalDeviceResourceData\': {
                                  \'GroupOwnerSetting\': {
                                      \'AutoAddGroupOwner\': True|False,
                                      \'GroupOwner\': \'string\'
                                  },
                                  \'SourcePath\': \'string\'
                              },
                              \'LocalVolumeResourceData\': {
                                  \'DestinationPath\': \'string\',
                                  \'GroupOwnerSetting\': {
                                      \'AutoAddGroupOwner\': True|False,
                                      \'GroupOwner\': \'string\'
                                  },
                                  \'SourcePath\': \'string\'
                              },
                              \'S3MachineLearningModelResourceData\': {
                                  \'DestinationPath\': \'string\',
                                  \'S3Uri\': \'string\'
                              },
                              \'SageMakerMachineLearningModelResourceData\': {
                                  \'DestinationPath\': \'string\',
                                  \'SageMakerJobArn\': \'string\'
                              }
                          }
                      },
                  ]
              },
              Name=\'string\'
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.
        
        :type InitialVersion: dict
        :param InitialVersion: Information about the initial version of the resource definition.
        
          - **Resources** *(list) --* A list of resources.
        
            - *(dict) --* Information about a resource.
        
              - **Id** *(string) --* The resource ID, used to refer to a resource in the Lambda function configuration. Max length is 128 characters with pattern \'\'[a-zA-Z0-9:_-]+\'\'. This must be unique within a Greengrass group.
        
              - **Name** *(string) --* The descriptive resource name, which is displayed on the Greengrass console. Max length 128 characters with pattern \'\'[a-zA-Z0-9:_-]+\'\'. This must be unique within a Greengrass group.
        
              - **ResourceDataContainer** *(dict) --* A container of data for all resource types.
        
                - **LocalDeviceResourceData** *(dict) --* Attributes that define the local device resource.
        
                  - **GroupOwnerSetting** *(dict) --* Group/owner related settings for local resources.
        
                    - **AutoAddGroupOwner** *(boolean) --* If true, GreenGrass automatically adds the specified Linux OS group owner of the resource to the Lambda process privileges. Thus the Lambda process will have the file access permissions of the added Linux group.
        
                    - **GroupOwner** *(string) --* The name of the Linux OS group whose privileges will be added to the Lambda process. This field is optional.
        
                  - **SourcePath** *(string) --* The local absolute path of the device resource. The source path for a device resource can refer only to a character device or block device under \'\'/dev\'\'.
        
                - **LocalVolumeResourceData** *(dict) --* Attributes that define the local volume resource.
        
                  - **DestinationPath** *(string) --* The absolute local path of the resource inside the lambda environment.
        
                  - **GroupOwnerSetting** *(dict) --* Allows you to configure additional group privileges for the Lambda process. This field is optional.
        
                    - **AutoAddGroupOwner** *(boolean) --* If true, GreenGrass automatically adds the specified Linux OS group owner of the resource to the Lambda process privileges. Thus the Lambda process will have the file access permissions of the added Linux group.
        
                    - **GroupOwner** *(string) --* The name of the Linux OS group whose privileges will be added to the Lambda process. This field is optional.
        
                  - **SourcePath** *(string) --* The local absolute path of the volume resource on the host. The source path for a volume resource type cannot start with \'\'/proc\'\' or \'\'/sys\'\'.
        
                - **S3MachineLearningModelResourceData** *(dict) --* Attributes that define an S3 machine learning resource.
        
                  - **DestinationPath** *(string) --* The absolute local path of the resource inside the Lambda environment.
        
                  - **S3Uri** *(string) --* The URI of the source model in an S3 bucket. The model package must be in tar.gz or .zip format.
        
                - **SageMakerMachineLearningModelResourceData** *(dict) --* Attributes that define an SageMaker machine learning resource.
        
                  - **DestinationPath** *(string) --* The absolute local path of the resource inside the Lambda environment.
        
                  - **SageMakerJobArn** *(string) --* The ARN of the SageMaker training job that represents the source model.
        
        :type Name: string
        :param Name: The name of the resource definition.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Id\': \'string\',
                \'LastUpdatedTimestamp\': \'string\',
                \'LatestVersion\': \'string\',
                \'LatestVersionArn\': \'string\',
                \'Name\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Arn** *(string) --* The ARN of the definition.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was created.
            
            - **Id** *(string) --* The ID of the definition.
            
            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was last updated.
            
            - **LatestVersion** *(string) --* The latest version of the definition.
            
            - **LatestVersionArn** *(string) --* The ARN of the latest version of the definition.
            
            - **Name** *(string) --* The name of the definition.
        """
        pass

    def create_resource_definition_version(self, ResourceDefinitionId: str, AmznClientToken: str = None, Resources: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateResourceDefinitionVersion>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_resource_definition_version(
              AmznClientToken=\'string\',
              ResourceDefinitionId=\'string\',
              Resources=[
                  {
                      \'Id\': \'string\',
                      \'Name\': \'string\',
                      \'ResourceDataContainer\': {
                          \'LocalDeviceResourceData\': {
                              \'GroupOwnerSetting\': {
                                  \'AutoAddGroupOwner\': True|False,
                                  \'GroupOwner\': \'string\'
                              },
                              \'SourcePath\': \'string\'
                          },
                          \'LocalVolumeResourceData\': {
                              \'DestinationPath\': \'string\',
                              \'GroupOwnerSetting\': {
                                  \'AutoAddGroupOwner\': True|False,
                                  \'GroupOwner\': \'string\'
                              },
                              \'SourcePath\': \'string\'
                          },
                          \'S3MachineLearningModelResourceData\': {
                              \'DestinationPath\': \'string\',
                              \'S3Uri\': \'string\'
                          },
                          \'SageMakerMachineLearningModelResourceData\': {
                              \'DestinationPath\': \'string\',
                              \'SageMakerJobArn\': \'string\'
                          }
                      }
                  },
              ]
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.
        
        :type ResourceDefinitionId: string
        :param ResourceDefinitionId: **[REQUIRED]** The ID of the resource definition.
        
        :type Resources: list
        :param Resources: A list of resources.
        
          - *(dict) --* Information about a resource.
        
            - **Id** *(string) --* The resource ID, used to refer to a resource in the Lambda function configuration. Max length is 128 characters with pattern \'\'[a-zA-Z0-9:_-]+\'\'. This must be unique within a Greengrass group.
        
            - **Name** *(string) --* The descriptive resource name, which is displayed on the Greengrass console. Max length 128 characters with pattern \'\'[a-zA-Z0-9:_-]+\'\'. This must be unique within a Greengrass group.
        
            - **ResourceDataContainer** *(dict) --* A container of data for all resource types.
        
              - **LocalDeviceResourceData** *(dict) --* Attributes that define the local device resource.
        
                - **GroupOwnerSetting** *(dict) --* Group/owner related settings for local resources.
        
                  - **AutoAddGroupOwner** *(boolean) --* If true, GreenGrass automatically adds the specified Linux OS group owner of the resource to the Lambda process privileges. Thus the Lambda process will have the file access permissions of the added Linux group.
        
                  - **GroupOwner** *(string) --* The name of the Linux OS group whose privileges will be added to the Lambda process. This field is optional.
        
                - **SourcePath** *(string) --* The local absolute path of the device resource. The source path for a device resource can refer only to a character device or block device under \'\'/dev\'\'.
        
              - **LocalVolumeResourceData** *(dict) --* Attributes that define the local volume resource.
        
                - **DestinationPath** *(string) --* The absolute local path of the resource inside the lambda environment.
        
                - **GroupOwnerSetting** *(dict) --* Allows you to configure additional group privileges for the Lambda process. This field is optional.
        
                  - **AutoAddGroupOwner** *(boolean) --* If true, GreenGrass automatically adds the specified Linux OS group owner of the resource to the Lambda process privileges. Thus the Lambda process will have the file access permissions of the added Linux group.
        
                  - **GroupOwner** *(string) --* The name of the Linux OS group whose privileges will be added to the Lambda process. This field is optional.
        
                - **SourcePath** *(string) --* The local absolute path of the volume resource on the host. The source path for a volume resource type cannot start with \'\'/proc\'\' or \'\'/sys\'\'.
        
              - **S3MachineLearningModelResourceData** *(dict) --* Attributes that define an S3 machine learning resource.
        
                - **DestinationPath** *(string) --* The absolute local path of the resource inside the Lambda environment.
        
                - **S3Uri** *(string) --* The URI of the source model in an S3 bucket. The model package must be in tar.gz or .zip format.
        
              - **SageMakerMachineLearningModelResourceData** *(dict) --* Attributes that define an SageMaker machine learning resource.
        
                - **DestinationPath** *(string) --* The absolute local path of the resource inside the Lambda environment.
        
                - **SageMakerJobArn** *(string) --* The ARN of the SageMaker training job that represents the source model.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Id\': \'string\',
                \'Version\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Arn** *(string) --* The ARN of the version.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the version was created.
            
            - **Id** *(string) --* The ID of the version.
            
            - **Version** *(string) --* The unique ID of the version.
        """
        pass

    def create_software_update_job(self, AmznClientToken: str = None, S3UrlSignerRole: str = None, SoftwareToUpdate: str = None, UpdateAgentLogLevel: str = None, UpdateTargets: List = None, UpdateTargetsArchitecture: str = None, UpdateTargetsOperatingSystem: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateSoftwareUpdateJob>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_software_update_job(
              AmznClientToken=\'string\',
              S3UrlSignerRole=\'string\',
              SoftwareToUpdate=\'core\'|\'ota_agent\',
              UpdateAgentLogLevel=\'NONE\'|\'TRACE\'|\'DEBUG\'|\'VERBOSE\'|\'INFO\'|\'WARN\'|\'ERROR\'|\'FATAL\',
              UpdateTargets=[
                  \'string\',
              ],
              UpdateTargetsArchitecture=\'armv7l\'|\'x86_64\'|\'aarch64\',
              UpdateTargetsOperatingSystem=\'ubuntu\'|\'raspbian\'|\'amazon_linux\'
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.
        
        :type S3UrlSignerRole: string
        :param S3UrlSignerRole: The IAM Role that Greengrass will use to create pre-signed URLs pointing towards the update artifact.
        
        :type SoftwareToUpdate: string
        :param SoftwareToUpdate: The piece of software on the Greengrass core that will be updated.
        
        :type UpdateAgentLogLevel: string
        :param UpdateAgentLogLevel: The minimum level of log statements that should be logged by the OTA Agent during an update.
        
        :type UpdateTargets: list
        :param UpdateTargets: The ARNs of the targets (IoT things or IoT thing groups) that this update will be applied to.
        
          - *(string) --* 
        
        :type UpdateTargetsArchitecture: string
        :param UpdateTargetsArchitecture: The architecture of the cores which are the targets of an update.
        
        :type UpdateTargetsOperatingSystem: string
        :param UpdateTargetsOperatingSystem: The operating system of the cores which are the targets of an update.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IotJobArn\': \'string\',
                \'IotJobId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* success
            
            - **IotJobArn** *(string) --* The IoT Job ARN corresponding to this update.
            
            - **IotJobId** *(string) --* The IoT Job Id corresponding to this update.
        """
        pass

    def create_subscription_definition(self, AmznClientToken: str = None, InitialVersion: Dict = None, Name: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateSubscriptionDefinition>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_subscription_definition(
              AmznClientToken=\'string\',
              InitialVersion={
                  \'Subscriptions\': [
                      {
                          \'Id\': \'string\',
                          \'Source\': \'string\',
                          \'Subject\': \'string\',
                          \'Target\': \'string\'
                      },
                  ]
              },
              Name=\'string\'
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.
        
        :type InitialVersion: dict
        :param InitialVersion: Information about the initial version of the subscription definition.
        
          - **Subscriptions** *(list) --* A list of subscriptions.
        
            - *(dict) --* Information about a subscription.
        
              - **Id** *(string) --* A descriptive or arbitrary ID for the subscription. This value must be unique within the subscription definition version. Max length is 128 characters with pattern \'\'[a‑zA‑Z0‑9:_‑]+\'\'.
        
              - **Source** *(string) --* The source of the subscription. Can be a thing ARN, a Lambda function ARN, \'cloud\' (which represents the IoT cloud), or \'GGShadowService\'.
        
              - **Subject** *(string) --* The subject of the message.
        
              - **Target** *(string) --* Where the message is sent to. Can be a thing ARN, a Lambda function ARN, \'cloud\' (which represents the IoT cloud), or \'GGShadowService\'.
        
        :type Name: string
        :param Name: The name of the subscription definition.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Id\': \'string\',
                \'LastUpdatedTimestamp\': \'string\',
                \'LatestVersion\': \'string\',
                \'LatestVersionArn\': \'string\',
                \'Name\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Arn** *(string) --* The ARN of the definition.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was created.
            
            - **Id** *(string) --* The ID of the definition.
            
            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was last updated.
            
            - **LatestVersion** *(string) --* The latest version of the definition.
            
            - **LatestVersionArn** *(string) --* The ARN of the latest version of the definition.
            
            - **Name** *(string) --* The name of the definition.
        """
        pass

    def create_subscription_definition_version(self, SubscriptionDefinitionId: str, AmznClientToken: str = None, Subscriptions: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/CreateSubscriptionDefinitionVersion>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_subscription_definition_version(
              AmznClientToken=\'string\',
              SubscriptionDefinitionId=\'string\',
              Subscriptions=[
                  {
                      \'Id\': \'string\',
                      \'Source\': \'string\',
                      \'Subject\': \'string\',
                      \'Target\': \'string\'
                  },
              ]
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.
        
        :type SubscriptionDefinitionId: string
        :param SubscriptionDefinitionId: **[REQUIRED]** The ID of the subscription definition.
        
        :type Subscriptions: list
        :param Subscriptions: A list of subscriptions.
        
          - *(dict) --* Information about a subscription.
        
            - **Id** *(string) --* A descriptive or arbitrary ID for the subscription. This value must be unique within the subscription definition version. Max length is 128 characters with pattern \'\'[a‑zA‑Z0‑9:_‑]+\'\'.
        
            - **Source** *(string) --* The source of the subscription. Can be a thing ARN, a Lambda function ARN, \'cloud\' (which represents the IoT cloud), or \'GGShadowService\'.
        
            - **Subject** *(string) --* The subject of the message.
        
            - **Target** *(string) --* Where the message is sent to. Can be a thing ARN, a Lambda function ARN, \'cloud\' (which represents the IoT cloud), or \'GGShadowService\'.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Id\': \'string\',
                \'Version\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Arn** *(string) --* The ARN of the version.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the version was created.
            
            - **Id** *(string) --* The ID of the version.
            
            - **Version** *(string) --* The unique ID of the version.
        """
        pass

    def delete_core_definition(self, CoreDefinitionId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DeleteCoreDefinition>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_core_definition(
              CoreDefinitionId=\'string\'
          )
        :type CoreDefinitionId: string
        :param CoreDefinitionId: **[REQUIRED]** The ID of the core definition.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* success
        """
        pass

    def delete_device_definition(self, DeviceDefinitionId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DeleteDeviceDefinition>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_device_definition(
              DeviceDefinitionId=\'string\'
          )
        :type DeviceDefinitionId: string
        :param DeviceDefinitionId: **[REQUIRED]** The ID of the device definition.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* success
        """
        pass

    def delete_function_definition(self, FunctionDefinitionId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DeleteFunctionDefinition>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_function_definition(
              FunctionDefinitionId=\'string\'
          )
        :type FunctionDefinitionId: string
        :param FunctionDefinitionId: **[REQUIRED]** The ID of the Lambda function definition.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* success
        """
        pass

    def delete_group(self, GroupId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DeleteGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_group(
              GroupId=\'string\'
          )
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the AWS Greengrass group.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* success
        """
        pass

    def delete_logger_definition(self, LoggerDefinitionId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DeleteLoggerDefinition>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_logger_definition(
              LoggerDefinitionId=\'string\'
          )
        :type LoggerDefinitionId: string
        :param LoggerDefinitionId: **[REQUIRED]** The ID of the logger definition.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* success
        """
        pass

    def delete_resource_definition(self, ResourceDefinitionId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DeleteResourceDefinition>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_resource_definition(
              ResourceDefinitionId=\'string\'
          )
        :type ResourceDefinitionId: string
        :param ResourceDefinitionId: **[REQUIRED]** The ID of the resource definition.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* success
        """
        pass

    def delete_subscription_definition(self, SubscriptionDefinitionId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DeleteSubscriptionDefinition>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_subscription_definition(
              SubscriptionDefinitionId=\'string\'
          )
        :type SubscriptionDefinitionId: string
        :param SubscriptionDefinitionId: **[REQUIRED]** The ID of the subscription definition.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* success
        """
        pass

    def disassociate_role_from_group(self, GroupId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DisassociateRoleFromGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.disassociate_role_from_group(
              GroupId=\'string\'
          )
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the AWS Greengrass group.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DisassociatedAt\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* success
            
            - **DisassociatedAt** *(string) --* The time, in milliseconds since the epoch, when the role was disassociated from the group.
        """
        pass

    def disassociate_service_role_from_account(self) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/DisassociateServiceRoleFromAccount>`_
        
        **Request Syntax** 
        ::
        
          response = client.disassociate_service_role_from_account()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DisassociatedAt\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* success
            
            - **DisassociatedAt** *(string) --* The time when the service role was disassociated from the account.
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
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

    def get_associated_role(self, GroupId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetAssociatedRole>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_associated_role(
              GroupId=\'string\'
          )
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the AWS Greengrass group.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AssociatedAt\': \'string\',
                \'RoleArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* success
            
            - **AssociatedAt** *(string) --* The time when the role was associated with the group.
            
            - **RoleArn** *(string) --* The ARN of the role that is associated with the group.
        """
        pass

    def get_bulk_deployment_status(self, BulkDeploymentId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetBulkDeploymentStatus>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_bulk_deployment_status(
              BulkDeploymentId=\'string\'
          )
        :type BulkDeploymentId: string
        :param BulkDeploymentId: **[REQUIRED]** The ID of the bulk deployment.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'BulkDeploymentMetrics\': {
                    \'InvalidInputRecords\': 123,
                    \'RecordsProcessed\': 123,
                    \'RetryAttempts\': 123
                },
                \'BulkDeploymentStatus\': \'Initializing\'|\'Running\'|\'Completed\'|\'Stopping\'|\'Stopped\'|\'Failed\',
                \'CreatedAt\': \'string\',
                \'ErrorDetails\': [
                    {
                        \'DetailedErrorCode\': \'string\',
                        \'DetailedErrorMessage\': \'string\'
                    },
                ],
                \'ErrorMessage\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* Success. The response body contains the status of the bulk deployment.
            
            - **BulkDeploymentMetrics** *(dict) --* Relevant metrics on input records processed during bulk deployment.
              
              - **InvalidInputRecords** *(integer) --* The total number of records that returned a non-retryable error. For example, this can occur if a group record from the input file uses an invalid format or specifies a nonexistent group version, or if the execution role doesn\'t grant permission to deploy a group or group version.
              
              - **RecordsProcessed** *(integer) --* The total number of group records from the input file that have been processed so far, or attempted.
              
              - **RetryAttempts** *(integer) --* The total number of deployment attempts that returned a retryable error. For example, a retry is triggered if the attempt to deploy a group returns a throttling error. \'\'StartBulkDeployment\'\' retries a group deployment up to five times.
          
            - **BulkDeploymentStatus** *(string) --* The status of the bulk deployment.
            
            - **CreatedAt** *(string) --* The time, in ISO format, when the deployment was created.
            
            - **ErrorDetails** *(list) --* Error details
              
              - *(dict) --* Details about the error.
                
                - **DetailedErrorCode** *(string) --* A detailed error code.
                
                - **DetailedErrorMessage** *(string) --* A detailed error message.
            
            - **ErrorMessage** *(string) --* Error message
        """
        pass

    def get_connectivity_info(self, ThingName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetConnectivityInfo>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_connectivity_info(
              ThingName=\'string\'
          )
        :type ThingName: string
        :param ThingName: **[REQUIRED]** The thing name.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ConnectivityInfo\': [
                    {
                        \'HostAddress\': \'string\',
                        \'Id\': \'string\',
                        \'Metadata\': \'string\',
                        \'PortNumber\': 123
                    },
                ],
                \'Message\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* success
            
            - **ConnectivityInfo** *(list) --* Connectivity info list.
              
              - *(dict) --* Information about a Greengrass core\'s connectivity.
                
                - **HostAddress** *(string) --* The endpoint for the Greengrass core. Can be an IP address or DNS.
                
                - **Id** *(string) --* The ID of the connectivity information.
                
                - **Metadata** *(string) --* Metadata for this endpoint.
                
                - **PortNumber** *(integer) --* The port of the Greengrass core. Usually 8883.
            
            - **Message** *(string) --* A message about the connectivity info request.
        """
        pass

    def get_core_definition(self, CoreDefinitionId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetCoreDefinition>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_core_definition(
              CoreDefinitionId=\'string\'
          )
        :type CoreDefinitionId: string
        :param CoreDefinitionId: **[REQUIRED]** The ID of the core definition.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Id\': \'string\',
                \'LastUpdatedTimestamp\': \'string\',
                \'LatestVersion\': \'string\',
                \'LatestVersionArn\': \'string\',
                \'Name\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Arn** *(string) --* The ARN of the definition.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was created.
            
            - **Id** *(string) --* The ID of the definition.
            
            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was last updated.
            
            - **LatestVersion** *(string) --* The latest version of the definition.
            
            - **LatestVersionArn** *(string) --* The ARN of the latest version of the definition.
            
            - **Name** *(string) --* The name of the definition.
        """
        pass

    def get_core_definition_version(self, CoreDefinitionId: str, CoreDefinitionVersionId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetCoreDefinitionVersion>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_core_definition_version(
              CoreDefinitionId=\'string\',
              CoreDefinitionVersionId=\'string\'
          )
        :type CoreDefinitionId: string
        :param CoreDefinitionId: **[REQUIRED]** The ID of the core definition.
        
        :type CoreDefinitionVersionId: string
        :param CoreDefinitionVersionId: **[REQUIRED]** The ID of the core definition version.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Definition\': {
                    \'Cores\': [
                        {
                            \'CertificateArn\': \'string\',
                            \'Id\': \'string\',
                            \'SyncShadow\': True|False,
                            \'ThingArn\': \'string\'
                        },
                    ]
                },
                \'Id\': \'string\',
                \'NextToken\': \'string\',
                \'Version\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* success
            
            - **Arn** *(string) --* The ARN of the core definition version.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the core definition version was created.
            
            - **Definition** *(dict) --* Information about the core definition version.
              
              - **Cores** *(list) --* A list of cores in the core definition version.
                
                - *(dict) --* Information about a core.
                  
                  - **CertificateArn** *(string) --* The ARN of the certificate associated with the core.
                  
                  - **Id** *(string) --* A descriptive or arbitrary ID for the core. This value must be unique within the core definition version. Max length is 128 characters with pattern \'\'[a‑zA‑Z0‑9:_‑]+\'\'.
                  
                  - **SyncShadow** *(boolean) --* If true, the core\'s local shadow is automatically synced with the cloud.
                  
                  - **ThingArn** *(string) --* The ARN of the thing which is the core.
              
            - **Id** *(string) --* The ID of the core definition version.
            
            - **NextToken** *(string) --* The token for the next set of results, or \'\'null\'\' if there are no additional results.
            
            - **Version** *(string) --* The version of the core definition version.
        """
        pass

    def get_deployment_status(self, DeploymentId: str, GroupId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetDeploymentStatus>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_deployment_status(
              DeploymentId=\'string\',
              GroupId=\'string\'
          )
        :type DeploymentId: string
        :param DeploymentId: **[REQUIRED]** The ID of the deployment.
        
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the AWS Greengrass group.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DeploymentStatus\': \'string\',
                \'DeploymentType\': \'NewDeployment\'|\'Redeployment\'|\'ResetDeployment\'|\'ForceResetDeployment\',
                \'ErrorDetails\': [
                    {
                        \'DetailedErrorCode\': \'string\',
                        \'DetailedErrorMessage\': \'string\'
                    },
                ],
                \'ErrorMessage\': \'string\',
                \'UpdatedAt\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* Success. The response body contains the status of the deployment for the group.
            
            - **DeploymentStatus** *(string) --* The status of the deployment: \'\'Pending\'\', \'\'InProgress\'\', \'\'Success\'\', or \'\'Failure\'\'.
            
            - **DeploymentType** *(string) --* The type of the deployment.
            
            - **ErrorDetails** *(list) --* Error details
              
              - *(dict) --* Details about the error.
                
                - **DetailedErrorCode** *(string) --* A detailed error code.
                
                - **DetailedErrorMessage** *(string) --* A detailed error message.
            
            - **ErrorMessage** *(string) --* Error message
            
            - **UpdatedAt** *(string) --* The time, in milliseconds since the epoch, when the deployment status was updated.
        """
        pass

    def get_device_definition(self, DeviceDefinitionId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetDeviceDefinition>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_device_definition(
              DeviceDefinitionId=\'string\'
          )
        :type DeviceDefinitionId: string
        :param DeviceDefinitionId: **[REQUIRED]** The ID of the device definition.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Id\': \'string\',
                \'LastUpdatedTimestamp\': \'string\',
                \'LatestVersion\': \'string\',
                \'LatestVersionArn\': \'string\',
                \'Name\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Arn** *(string) --* The ARN of the definition.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was created.
            
            - **Id** *(string) --* The ID of the definition.
            
            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was last updated.
            
            - **LatestVersion** *(string) --* The latest version of the definition.
            
            - **LatestVersionArn** *(string) --* The ARN of the latest version of the definition.
            
            - **Name** *(string) --* The name of the definition.
        """
        pass

    def get_device_definition_version(self, DeviceDefinitionId: str, DeviceDefinitionVersionId: str, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetDeviceDefinitionVersion>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_device_definition_version(
              DeviceDefinitionId=\'string\',
              DeviceDefinitionVersionId=\'string\',
              NextToken=\'string\'
          )
        :type DeviceDefinitionId: string
        :param DeviceDefinitionId: **[REQUIRED]** The ID of the device definition.
        
        :type DeviceDefinitionVersionId: string
        :param DeviceDefinitionVersionId: **[REQUIRED]** The ID of the device definition version.
        
        :type NextToken: string
        :param NextToken: The token for the next set of results, or \'\'null\'\' if there are no additional results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Definition\': {
                    \'Devices\': [
                        {
                            \'CertificateArn\': \'string\',
                            \'Id\': \'string\',
                            \'SyncShadow\': True|False,
                            \'ThingArn\': \'string\'
                        },
                    ]
                },
                \'Id\': \'string\',
                \'NextToken\': \'string\',
                \'Version\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Arn** *(string) --* The ARN of the device definition version.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the device definition version was created.
            
            - **Definition** *(dict) --* Information about the device definition version.
              
              - **Devices** *(list) --* A list of devices in the definition version.
                
                - *(dict) --* Information about a device.
                  
                  - **CertificateArn** *(string) --* The ARN of the certificate associated with the device.
                  
                  - **Id** *(string) --* A descriptive or arbitrary ID for the device. This value must be unique within the device definition version. Max length is 128 characters with pattern \'\'[a‑zA‑Z0‑9:_‑]+\'\'.
                  
                  - **SyncShadow** *(boolean) --* If true, the device\'s local shadow will be automatically synced with the cloud.
                  
                  - **ThingArn** *(string) --* The thing ARN of the device.
              
            - **Id** *(string) --* The ID of the device definition version.
            
            - **NextToken** *(string) --* The token for the next set of results, or \'\'null\'\' if there are no additional results.
            
            - **Version** *(string) --* The version of the device definition version.
        """
        pass

    def get_function_definition(self, FunctionDefinitionId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetFunctionDefinition>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_function_definition(
              FunctionDefinitionId=\'string\'
          )
        :type FunctionDefinitionId: string
        :param FunctionDefinitionId: **[REQUIRED]** The ID of the Lambda function definition.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Id\': \'string\',
                \'LastUpdatedTimestamp\': \'string\',
                \'LatestVersion\': \'string\',
                \'LatestVersionArn\': \'string\',
                \'Name\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* success
            
            - **Arn** *(string) --* The ARN of the definition.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was created.
            
            - **Id** *(string) --* The ID of the definition.
            
            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was last updated.
            
            - **LatestVersion** *(string) --* The latest version of the definition.
            
            - **LatestVersionArn** *(string) --* The ARN of the latest version of the definition.
            
            - **Name** *(string) --* The name of the definition.
        """
        pass

    def get_function_definition_version(self, FunctionDefinitionId: str, FunctionDefinitionVersionId: str, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetFunctionDefinitionVersion>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_function_definition_version(
              FunctionDefinitionId=\'string\',
              FunctionDefinitionVersionId=\'string\',
              NextToken=\'string\'
          )
        :type FunctionDefinitionId: string
        :param FunctionDefinitionId: **[REQUIRED]** The ID of the Lambda function definition.
        
        :type FunctionDefinitionVersionId: string
        :param FunctionDefinitionVersionId: **[REQUIRED]** The ID of the function definition version.
        
        :type NextToken: string
        :param NextToken: The token for the next set of results, or \'\'null\'\' if there are no additional results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Definition\': {
                    \'Functions\': [
                        {
                            \'FunctionArn\': \'string\',
                            \'FunctionConfiguration\': {
                                \'EncodingType\': \'binary\'|\'json\',
                                \'Environment\': {
                                    \'AccessSysfs\': True|False,
                                    \'ResourceAccessPolicies\': [
                                        {
                                            \'Permission\': \'ro\'|\'rw\',
                                            \'ResourceId\': \'string\'
                                        },
                                    ],
                                    \'Variables\': {
                                        \'string\': \'string\'
                                    }
                                },
                                \'ExecArgs\': \'string\',
                                \'Executable\': \'string\',
                                \'MemorySize\': 123,
                                \'Pinned\': True|False,
                                \'Timeout\': 123
                            },
                            \'Id\': \'string\'
                        },
                    ]
                },
                \'Id\': \'string\',
                \'NextToken\': \'string\',
                \'Version\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* success
            
            - **Arn** *(string) --* The ARN of the function definition version.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the function definition version was created.
            
            - **Definition** *(dict) --* Information on the definition.
              
              - **Functions** *(list) --* A list of Lambda functions in this function definition version.
                
                - *(dict) --* Information about a Lambda function.
                  
                  - **FunctionArn** *(string) --* The ARN of the Lambda function.
                  
                  - **FunctionConfiguration** *(dict) --* The configuration of the Lambda function.
                    
                    - **EncodingType** *(string) --* The expected encoding type of the input payload for the function. The default is \'\'json\'\'.
                    
                    - **Environment** *(dict) --* The environment configuration of the function.
                      
                      - **AccessSysfs** *(boolean) --* If true, the Lambda function is allowed to access the host\'s /sys folder. Use this when the Lambda function needs to read device information from /sys.
                      
                      - **ResourceAccessPolicies** *(list) --* A list of the resources, with their permissions, to which the Lambda function will be granted access. A Lambda function can have at most 10 resources.
                        
                        - *(dict) --* A policy used by the function to access a resource.
                          
                          - **Permission** *(string) --* The permissions that the Lambda function has to the resource. Can be one of \'\'rw\'\' (read/write) or \'\'ro\'\' (read-only).
                          
                          - **ResourceId** *(string) --* The ID of the resource. (This ID is assigned to the resource when you create the resource definiton.)
                      
                      - **Variables** *(dict) --* Environment variables for the Lambda function\'s configuration.
                        
                        - *(string) --* 
                          
                          - *(string) --* 
                    
                    - **ExecArgs** *(string) --* The execution arguments.
                    
                    - **Executable** *(string) --* The name of the function executable.
                    
                    - **MemorySize** *(integer) --* The memory size, in KB, which the function requires.
                    
                    - **Pinned** *(boolean) --* True if the function is pinned. Pinned means the function is long-lived and starts when the core starts.
                    
                    - **Timeout** *(integer) --* The allowed function execution time, after which Lambda should terminate the function. This timeout still applies to pinned lambdas for each request.
                
                  - **Id** *(string) --* A descriptive or arbitrary ID for the function. This value must be unique within the function definition version. Max length is 128 characters with pattern \'\'[a‑zA‑Z0‑9:_‑]+\'\'.
              
            - **Id** *(string) --* The ID of the function definition version.
            
            - **NextToken** *(string) --* The token for the next set of results, or \'\'null\'\' if there are no additional results.
            
            - **Version** *(string) --* The version of the function definition version.
        """
        pass

    def get_group(self, GroupId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_group(
              GroupId=\'string\'
          )
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the AWS Greengrass group.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Id\': \'string\',
                \'LastUpdatedTimestamp\': \'string\',
                \'LatestVersion\': \'string\',
                \'LatestVersionArn\': \'string\',
                \'Name\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* success
            
            - **Arn** *(string) --* The ARN of the definition.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was created.
            
            - **Id** *(string) --* The ID of the definition.
            
            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was last updated.
            
            - **LatestVersion** *(string) --* The latest version of the definition.
            
            - **LatestVersionArn** *(string) --* The ARN of the latest version of the definition.
            
            - **Name** *(string) --* The name of the definition.
        """
        pass

    def get_group_certificate_authority(self, CertificateAuthorityId: str, GroupId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetGroupCertificateAuthority>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_group_certificate_authority(
              CertificateAuthorityId=\'string\',
              GroupId=\'string\'
          )
        :type CertificateAuthorityId: string
        :param CertificateAuthorityId: **[REQUIRED]** The ID of the certificate authority.
        
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the AWS Greengrass group.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'GroupCertificateAuthorityArn\': \'string\',
                \'GroupCertificateAuthorityId\': \'string\',
                \'PemEncodedCertificate\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* Success. The response body contains the PKI Configuration.
            
            - **GroupCertificateAuthorityArn** *(string) --* The ARN of the certificate authority for the group.
            
            - **GroupCertificateAuthorityId** *(string) --* The ID of the certificate authority for the group.
            
            - **PemEncodedCertificate** *(string) --* The PEM encoded certificate for the group.
        """
        pass

    def get_group_certificate_configuration(self, GroupId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetGroupCertificateConfiguration>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_group_certificate_configuration(
              GroupId=\'string\'
          )
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the AWS Greengrass group.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'CertificateAuthorityExpiryInMilliseconds\': \'string\',
                \'CertificateExpiryInMilliseconds\': \'string\',
                \'GroupId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* Success. The response body contains the PKI Configuration.
            
            - **CertificateAuthorityExpiryInMilliseconds** *(string) --* The amount of time remaining before the certificate authority expires, in milliseconds.
            
            - **CertificateExpiryInMilliseconds** *(string) --* The amount of time remaining before the certificate expires, in milliseconds.
            
            - **GroupId** *(string) --* The ID of the group certificate configuration.
        """
        pass

    def get_group_version(self, GroupId: str, GroupVersionId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetGroupVersion>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_group_version(
              GroupId=\'string\',
              GroupVersionId=\'string\'
          )
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the AWS Greengrass group.
        
        :type GroupVersionId: string
        :param GroupVersionId: **[REQUIRED]** The ID of the group version.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Definition\': {
                    \'CoreDefinitionVersionArn\': \'string\',
                    \'DeviceDefinitionVersionArn\': \'string\',
                    \'FunctionDefinitionVersionArn\': \'string\',
                    \'LoggerDefinitionVersionArn\': \'string\',
                    \'ResourceDefinitionVersionArn\': \'string\',
                    \'SubscriptionDefinitionVersionArn\': \'string\'
                },
                \'Id\': \'string\',
                \'Version\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* success
            
            - **Arn** *(string) --* The ARN of the group version.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the group version was created.
            
            - **Definition** *(dict) --* Information about the group version definition.
              
              - **CoreDefinitionVersionArn** *(string) --* The ARN of the core definition version for this group.
              
              - **DeviceDefinitionVersionArn** *(string) --* The ARN of the device definition version for this group.
              
              - **FunctionDefinitionVersionArn** *(string) --* The ARN of the function definition version for this group.
              
              - **LoggerDefinitionVersionArn** *(string) --* The ARN of the logger definition version for this group.
              
              - **ResourceDefinitionVersionArn** *(string) --* The resource definition version ARN for this group.
              
              - **SubscriptionDefinitionVersionArn** *(string) --* The ARN of the subscription definition version for this group.
          
            - **Id** *(string) --* The ID of the group version.
            
            - **Version** *(string) --* The unique ID for the version of the group.
        """
        pass

    def get_logger_definition(self, LoggerDefinitionId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetLoggerDefinition>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_logger_definition(
              LoggerDefinitionId=\'string\'
          )
        :type LoggerDefinitionId: string
        :param LoggerDefinitionId: **[REQUIRED]** The ID of the logger definition.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Id\': \'string\',
                \'LastUpdatedTimestamp\': \'string\',
                \'LatestVersion\': \'string\',
                \'LatestVersionArn\': \'string\',
                \'Name\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Arn** *(string) --* The ARN of the definition.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was created.
            
            - **Id** *(string) --* The ID of the definition.
            
            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was last updated.
            
            - **LatestVersion** *(string) --* The latest version of the definition.
            
            - **LatestVersionArn** *(string) --* The ARN of the latest version of the definition.
            
            - **Name** *(string) --* The name of the definition.
        """
        pass

    def get_logger_definition_version(self, LoggerDefinitionId: str, LoggerDefinitionVersionId: str, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetLoggerDefinitionVersion>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_logger_definition_version(
              LoggerDefinitionId=\'string\',
              LoggerDefinitionVersionId=\'string\',
              NextToken=\'string\'
          )
        :type LoggerDefinitionId: string
        :param LoggerDefinitionId: **[REQUIRED]** The ID of the logger definition.
        
        :type LoggerDefinitionVersionId: string
        :param LoggerDefinitionVersionId: **[REQUIRED]** The ID of the logger definition version.
        
        :type NextToken: string
        :param NextToken: The token for the next set of results, or \'\'null\'\' if there are no additional results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Definition\': {
                    \'Loggers\': [
                        {
                            \'Component\': \'GreengrassSystem\'|\'Lambda\',
                            \'Id\': \'string\',
                            \'Level\': \'DEBUG\'|\'INFO\'|\'WARN\'|\'ERROR\'|\'FATAL\',
                            \'Space\': 123,
                            \'Type\': \'FileSystem\'|\'AWSCloudWatch\'
                        },
                    ]
                },
                \'Id\': \'string\',
                \'Version\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* success
            
            - **Arn** *(string) --* The ARN of the logger definition version.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the logger definition version was created.
            
            - **Definition** *(dict) --* Information about the logger definition version.
              
              - **Loggers** *(list) --* A list of loggers.
                
                - *(dict) --* Information about a logger
                  
                  - **Component** *(string) --* The component that will be subject to logging.
                  
                  - **Id** *(string) --* A descriptive or arbitrary ID for the logger. This value must be unique within the logger definition version. Max length is 128 characters with pattern \'\'[a‑zA‑Z0‑9:_‑]+\'\'.
                  
                  - **Level** *(string) --* The level of the logs.
                  
                  - **Space** *(integer) --* The amount of file space, in KB, to use if the local file system is used for logging purposes.
                  
                  - **Type** *(string) --* The type of log output which will be used.
              
            - **Id** *(string) --* The ID of the logger definition version.
            
            - **Version** *(string) --* The version of the logger definition version.
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

    def get_resource_definition(self, ResourceDefinitionId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetResourceDefinition>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_resource_definition(
              ResourceDefinitionId=\'string\'
          )
        :type ResourceDefinitionId: string
        :param ResourceDefinitionId: **[REQUIRED]** The ID of the resource definition.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Id\': \'string\',
                \'LastUpdatedTimestamp\': \'string\',
                \'LatestVersion\': \'string\',
                \'LatestVersionArn\': \'string\',
                \'Name\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* success
            
            - **Arn** *(string) --* The ARN of the definition.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was created.
            
            - **Id** *(string) --* The ID of the definition.
            
            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was last updated.
            
            - **LatestVersion** *(string) --* The latest version of the definition.
            
            - **LatestVersionArn** *(string) --* The ARN of the latest version of the definition.
            
            - **Name** *(string) --* The name of the definition.
        """
        pass

    def get_resource_definition_version(self, ResourceDefinitionId: str, ResourceDefinitionVersionId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetResourceDefinitionVersion>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_resource_definition_version(
              ResourceDefinitionId=\'string\',
              ResourceDefinitionVersionId=\'string\'
          )
        :type ResourceDefinitionId: string
        :param ResourceDefinitionId: **[REQUIRED]** The ID of the resource definition.
        
        :type ResourceDefinitionVersionId: string
        :param ResourceDefinitionVersionId: **[REQUIRED]** The ID of the resource definition version.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Definition\': {
                    \'Resources\': [
                        {
                            \'Id\': \'string\',
                            \'Name\': \'string\',
                            \'ResourceDataContainer\': {
                                \'LocalDeviceResourceData\': {
                                    \'GroupOwnerSetting\': {
                                        \'AutoAddGroupOwner\': True|False,
                                        \'GroupOwner\': \'string\'
                                    },
                                    \'SourcePath\': \'string\'
                                },
                                \'LocalVolumeResourceData\': {
                                    \'DestinationPath\': \'string\',
                                    \'GroupOwnerSetting\': {
                                        \'AutoAddGroupOwner\': True|False,
                                        \'GroupOwner\': \'string\'
                                    },
                                    \'SourcePath\': \'string\'
                                },
                                \'S3MachineLearningModelResourceData\': {
                                    \'DestinationPath\': \'string\',
                                    \'S3Uri\': \'string\'
                                },
                                \'SageMakerMachineLearningModelResourceData\': {
                                    \'DestinationPath\': \'string\',
                                    \'SageMakerJobArn\': \'string\'
                                }
                            }
                        },
                    ]
                },
                \'Id\': \'string\',
                \'Version\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* success
            
            - **Arn** *(string) --* Arn of the resource definition version.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the resource definition version was created.
            
            - **Definition** *(dict) --* Information about the definition.
              
              - **Resources** *(list) --* A list of resources.
                
                - *(dict) --* Information about a resource.
                  
                  - **Id** *(string) --* The resource ID, used to refer to a resource in the Lambda function configuration. Max length is 128 characters with pattern \'\'[a-zA-Z0-9:_-]+\'\'. This must be unique within a Greengrass group.
                  
                  - **Name** *(string) --* The descriptive resource name, which is displayed on the Greengrass console. Max length 128 characters with pattern \'\'[a-zA-Z0-9:_-]+\'\'. This must be unique within a Greengrass group.
                  
                  - **ResourceDataContainer** *(dict) --* A container of data for all resource types.
                    
                    - **LocalDeviceResourceData** *(dict) --* Attributes that define the local device resource.
                      
                      - **GroupOwnerSetting** *(dict) --* Group/owner related settings for local resources.
                        
                        - **AutoAddGroupOwner** *(boolean) --* If true, GreenGrass automatically adds the specified Linux OS group owner of the resource to the Lambda process privileges. Thus the Lambda process will have the file access permissions of the added Linux group.
                        
                        - **GroupOwner** *(string) --* The name of the Linux OS group whose privileges will be added to the Lambda process. This field is optional.
                    
                      - **SourcePath** *(string) --* The local absolute path of the device resource. The source path for a device resource can refer only to a character device or block device under \'\'/dev\'\'.
                  
                    - **LocalVolumeResourceData** *(dict) --* Attributes that define the local volume resource.
                      
                      - **DestinationPath** *(string) --* The absolute local path of the resource inside the lambda environment.
                      
                      - **GroupOwnerSetting** *(dict) --* Allows you to configure additional group privileges for the Lambda process. This field is optional.
                        
                        - **AutoAddGroupOwner** *(boolean) --* If true, GreenGrass automatically adds the specified Linux OS group owner of the resource to the Lambda process privileges. Thus the Lambda process will have the file access permissions of the added Linux group.
                        
                        - **GroupOwner** *(string) --* The name of the Linux OS group whose privileges will be added to the Lambda process. This field is optional.
                    
                      - **SourcePath** *(string) --* The local absolute path of the volume resource on the host. The source path for a volume resource type cannot start with \'\'/proc\'\' or \'\'/sys\'\'.
                  
                    - **S3MachineLearningModelResourceData** *(dict) --* Attributes that define an S3 machine learning resource.
                      
                      - **DestinationPath** *(string) --* The absolute local path of the resource inside the Lambda environment.
                      
                      - **S3Uri** *(string) --* The URI of the source model in an S3 bucket. The model package must be in tar.gz or .zip format.
                  
                    - **SageMakerMachineLearningModelResourceData** *(dict) --* Attributes that define an SageMaker machine learning resource.
                      
                      - **DestinationPath** *(string) --* The absolute local path of the resource inside the Lambda environment.
                      
                      - **SageMakerJobArn** *(string) --* The ARN of the SageMaker training job that represents the source model.
                  
            - **Id** *(string) --* The ID of the resource definition version.
            
            - **Version** *(string) --* The version of the resource definition version.
        """
        pass

    def get_service_role_for_account(self) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetServiceRoleForAccount>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_service_role_for_account()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AssociatedAt\': \'string\',
                \'RoleArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* success
            
            - **AssociatedAt** *(string) --* The time when the service role was associated with the account.
            
            - **RoleArn** *(string) --* The ARN of the role which is associated with the account.
        """
        pass

    def get_subscription_definition(self, SubscriptionDefinitionId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetSubscriptionDefinition>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_subscription_definition(
              SubscriptionDefinitionId=\'string\'
          )
        :type SubscriptionDefinitionId: string
        :param SubscriptionDefinitionId: **[REQUIRED]** The ID of the subscription definition.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Id\': \'string\',
                \'LastUpdatedTimestamp\': \'string\',
                \'LatestVersion\': \'string\',
                \'LatestVersionArn\': \'string\',
                \'Name\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Arn** *(string) --* The ARN of the definition.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was created.
            
            - **Id** *(string) --* The ID of the definition.
            
            - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was last updated.
            
            - **LatestVersion** *(string) --* The latest version of the definition.
            
            - **LatestVersionArn** *(string) --* The ARN of the latest version of the definition.
            
            - **Name** *(string) --* The name of the definition.
        """
        pass

    def get_subscription_definition_version(self, SubscriptionDefinitionId: str, SubscriptionDefinitionVersionId: str, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/GetSubscriptionDefinitionVersion>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_subscription_definition_version(
              NextToken=\'string\',
              SubscriptionDefinitionId=\'string\',
              SubscriptionDefinitionVersionId=\'string\'
          )
        :type NextToken: string
        :param NextToken: The token for the next set of results, or \'\'null\'\' if there are no additional results.
        
        :type SubscriptionDefinitionId: string
        :param SubscriptionDefinitionId: **[REQUIRED]** The ID of the subscription definition.
        
        :type SubscriptionDefinitionVersionId: string
        :param SubscriptionDefinitionVersionId: **[REQUIRED]** The ID of the subscription definition version.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Arn\': \'string\',
                \'CreationTimestamp\': \'string\',
                \'Definition\': {
                    \'Subscriptions\': [
                        {
                            \'Id\': \'string\',
                            \'Source\': \'string\',
                            \'Subject\': \'string\',
                            \'Target\': \'string\'
                        },
                    ]
                },
                \'Id\': \'string\',
                \'NextToken\': \'string\',
                \'Version\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Arn** *(string) --* The ARN of the subscription definition version.
            
            - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the subscription definition version was created.
            
            - **Definition** *(dict) --* Information about the subscription definition version.
              
              - **Subscriptions** *(list) --* A list of subscriptions.
                
                - *(dict) --* Information about a subscription.
                  
                  - **Id** *(string) --* A descriptive or arbitrary ID for the subscription. This value must be unique within the subscription definition version. Max length is 128 characters with pattern \'\'[a‑zA‑Z0‑9:_‑]+\'\'.
                  
                  - **Source** *(string) --* The source of the subscription. Can be a thing ARN, a Lambda function ARN, \'cloud\' (which represents the IoT cloud), or \'GGShadowService\'.
                  
                  - **Subject** *(string) --* The subject of the message.
                  
                  - **Target** *(string) --* Where the message is sent to. Can be a thing ARN, a Lambda function ARN, \'cloud\' (which represents the IoT cloud), or \'GGShadowService\'.
              
            - **Id** *(string) --* The ID of the subscription definition version.
            
            - **NextToken** *(string) --* The token for the next set of results, or \'\'null\'\' if there are no additional results.
            
            - **Version** *(string) --* The version of the subscription definition version.
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

    def list_bulk_deployment_detailed_reports(self, BulkDeploymentId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListBulkDeploymentDetailedReports>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_bulk_deployment_detailed_reports(
              BulkDeploymentId=\'string\',
              MaxResults=\'string\',
              NextToken=\'string\'
          )
        :type BulkDeploymentId: string
        :param BulkDeploymentId: **[REQUIRED]** The ID of the bulk deployment.
        
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.
        
        :type NextToken: string
        :param NextToken: The token for the next set of results, or \'\'null\'\' if there are no additional results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Deployments\': [
                    {
                        \'CreatedAt\': \'string\',
                        \'DeploymentArn\': \'string\',
                        \'DeploymentId\': \'string\',
                        \'DeploymentStatus\': \'string\',
                        \'DeploymentType\': \'NewDeployment\'|\'Redeployment\'|\'ResetDeployment\'|\'ForceResetDeployment\',
                        \'ErrorDetails\': [
                            {
                                \'DetailedErrorCode\': \'string\',
                                \'DetailedErrorMessage\': \'string\'
                            },
                        ],
                        \'ErrorMessage\': \'string\',
                        \'GroupArn\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* Success. The response body contains the list of deployments for the given group.
            
            - **Deployments** *(list) --* A list of the individual group deployments in the bulk deployment operation.
              
              - *(dict) --* Information about an individual group deployment in a bulk deployment operation.
                
                - **CreatedAt** *(string) --* The time, in ISO format, when the deployment was created.
                
                - **DeploymentArn** *(string) --* The ARN of the group deployment.
                
                - **DeploymentId** *(string) --* The ID of the group deployment.
                
                - **DeploymentStatus** *(string) --* The current status of the group deployment: \'\'Pending\'\', \'\'InProgress\'\', \'\'Success\'\', or \'\'Failure\'\'.
                
                - **DeploymentType** *(string) --* The type of the deployment.
                
                - **ErrorDetails** *(list) --* Details about the error.
                  
                  - *(dict) --* Details about the error.
                    
                    - **DetailedErrorCode** *(string) --* A detailed error code.
                    
                    - **DetailedErrorMessage** *(string) --* A detailed error message.
                
                - **ErrorMessage** *(string) --* The error message for a failed deployment
                
                - **GroupArn** *(string) --* The ARN of the Greengrass group.
            
            - **NextToken** *(string) --* The token for the next set of results, or \'\'null\'\' if there are no additional results.
        """
        pass

    def list_bulk_deployments(self, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListBulkDeployments>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_bulk_deployments(
              MaxResults=\'string\',
              NextToken=\'string\'
          )
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.
        
        :type NextToken: string
        :param NextToken: The token for the next set of results, or \'\'null\'\' if there are no additional results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'BulkDeployments\': [
                    {
                        \'BulkDeploymentArn\': \'string\',
                        \'BulkDeploymentId\': \'string\',
                        \'CreatedAt\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* Success. The response body contains the list of bulk deployments.
            
            - **BulkDeployments** *(list) --* A list of bulk deployments.
              
              - *(dict) --* Information about a bulk deployment.
                
                - **BulkDeploymentArn** *(string) --* The ARN of the bulk deployment.
                
                - **BulkDeploymentId** *(string) --* The ID of the bulk deployment.
                
                - **CreatedAt** *(string) --* The time, in ISO format, when the deployment was created.
            
            - **NextToken** *(string) --* The token for the next set of results, or \'\'null\'\' if there are no additional results.
        """
        pass

    def list_core_definition_versions(self, CoreDefinitionId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListCoreDefinitionVersions>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_core_definition_versions(
              CoreDefinitionId=\'string\',
              MaxResults=\'string\',
              NextToken=\'string\'
          )
        :type CoreDefinitionId: string
        :param CoreDefinitionId: **[REQUIRED]** The ID of the core definition.
        
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.
        
        :type NextToken: string
        :param NextToken: The token for the next set of results, or \'\'null\'\' if there are no additional results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextToken\': \'string\',
                \'Versions\': [
                    {
                        \'Arn\': \'string\',
                        \'CreationTimestamp\': \'string\',
                        \'Id\': \'string\',
                        \'Version\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NextToken** *(string) --* The token for the next set of results, or \'\'null\'\' if there are no additional results.
            
            - **Versions** *(list) --* Information about a version.
              
              - *(dict) --* Information about a version.
                
                - **Arn** *(string) --* The ARN of the version.
                
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the version was created.
                
                - **Id** *(string) --* The ID of the version.
                
                - **Version** *(string) --* The unique ID of the version.
            
        """
        pass

    def list_core_definitions(self, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListCoreDefinitions>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_core_definitions(
              MaxResults=\'string\',
              NextToken=\'string\'
          )
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.
        
        :type NextToken: string
        :param NextToken: The token for the next set of results, or \'\'null\'\' if there are no additional results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Definitions\': [
                    {
                        \'Arn\': \'string\',
                        \'CreationTimestamp\': \'string\',
                        \'Id\': \'string\',
                        \'LastUpdatedTimestamp\': \'string\',
                        \'LatestVersion\': \'string\',
                        \'LatestVersionArn\': \'string\',
                        \'Name\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Definitions** *(list) --* Information about a definition.
              
              - *(dict) --* Information about a definition.
                
                - **Arn** *(string) --* The ARN of the definition.
                
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was created.
                
                - **Id** *(string) --* The ID of the definition.
                
                - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was last updated.
                
                - **LatestVersion** *(string) --* The latest version of the definition.
                
                - **LatestVersionArn** *(string) --* The ARN of the latest version of the definition.
                
                - **Name** *(string) --* The name of the definition.
            
            - **NextToken** *(string) --* The token for the next set of results, or \'\'null\'\' if there are no additional results.
        """
        pass

    def list_deployments(self, GroupId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListDeployments>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_deployments(
              GroupId=\'string\',
              MaxResults=\'string\',
              NextToken=\'string\'
          )
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the AWS Greengrass group.
        
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.
        
        :type NextToken: string
        :param NextToken: The token for the next set of results, or \'\'null\'\' if there are no additional results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Deployments\': [
                    {
                        \'CreatedAt\': \'string\',
                        \'DeploymentArn\': \'string\',
                        \'DeploymentId\': \'string\',
                        \'DeploymentType\': \'NewDeployment\'|\'Redeployment\'|\'ResetDeployment\'|\'ForceResetDeployment\',
                        \'GroupArn\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* Success. The response body contains the list of deployments for the given group.
            
            - **Deployments** *(list) --* A list of deployments for the requested groups.
              
              - *(dict) --* Information about a deployment.
                
                - **CreatedAt** *(string) --* The time, in milliseconds since the epoch, when the deployment was created.
                
                - **DeploymentArn** *(string) --* The ARN of the deployment.
                
                - **DeploymentId** *(string) --* The ID of the deployment.
                
                - **DeploymentType** *(string) --* The type of the deployment.
                
                - **GroupArn** *(string) --* The ARN of the group for this deployment.
            
            - **NextToken** *(string) --* The token for the next set of results, or \'\'null\'\' if there are no additional results.
        """
        pass

    def list_device_definition_versions(self, DeviceDefinitionId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListDeviceDefinitionVersions>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_device_definition_versions(
              DeviceDefinitionId=\'string\',
              MaxResults=\'string\',
              NextToken=\'string\'
          )
        :type DeviceDefinitionId: string
        :param DeviceDefinitionId: **[REQUIRED]** The ID of the device definition.
        
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.
        
        :type NextToken: string
        :param NextToken: The token for the next set of results, or \'\'null\'\' if there are no additional results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextToken\': \'string\',
                \'Versions\': [
                    {
                        \'Arn\': \'string\',
                        \'CreationTimestamp\': \'string\',
                        \'Id\': \'string\',
                        \'Version\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NextToken** *(string) --* The token for the next set of results, or \'\'null\'\' if there are no additional results.
            
            - **Versions** *(list) --* Information about a version.
              
              - *(dict) --* Information about a version.
                
                - **Arn** *(string) --* The ARN of the version.
                
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the version was created.
                
                - **Id** *(string) --* The ID of the version.
                
                - **Version** *(string) --* The unique ID of the version.
            
        """
        pass

    def list_device_definitions(self, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListDeviceDefinitions>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_device_definitions(
              MaxResults=\'string\',
              NextToken=\'string\'
          )
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.
        
        :type NextToken: string
        :param NextToken: The token for the next set of results, or \'\'null\'\' if there are no additional results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Definitions\': [
                    {
                        \'Arn\': \'string\',
                        \'CreationTimestamp\': \'string\',
                        \'Id\': \'string\',
                        \'LastUpdatedTimestamp\': \'string\',
                        \'LatestVersion\': \'string\',
                        \'LatestVersionArn\': \'string\',
                        \'Name\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Definitions** *(list) --* Information about a definition.
              
              - *(dict) --* Information about a definition.
                
                - **Arn** *(string) --* The ARN of the definition.
                
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was created.
                
                - **Id** *(string) --* The ID of the definition.
                
                - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was last updated.
                
                - **LatestVersion** *(string) --* The latest version of the definition.
                
                - **LatestVersionArn** *(string) --* The ARN of the latest version of the definition.
                
                - **Name** *(string) --* The name of the definition.
            
            - **NextToken** *(string) --* The token for the next set of results, or \'\'null\'\' if there are no additional results.
        """
        pass

    def list_function_definition_versions(self, FunctionDefinitionId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListFunctionDefinitionVersions>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_function_definition_versions(
              FunctionDefinitionId=\'string\',
              MaxResults=\'string\',
              NextToken=\'string\'
          )
        :type FunctionDefinitionId: string
        :param FunctionDefinitionId: **[REQUIRED]** The ID of the Lambda function definition.
        
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.
        
        :type NextToken: string
        :param NextToken: The token for the next set of results, or \'\'null\'\' if there are no additional results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextToken\': \'string\',
                \'Versions\': [
                    {
                        \'Arn\': \'string\',
                        \'CreationTimestamp\': \'string\',
                        \'Id\': \'string\',
                        \'Version\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* success
            
            - **NextToken** *(string) --* The token for the next set of results, or \'\'null\'\' if there are no additional results.
            
            - **Versions** *(list) --* Information about a version.
              
              - *(dict) --* Information about a version.
                
                - **Arn** *(string) --* The ARN of the version.
                
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the version was created.
                
                - **Id** *(string) --* The ID of the version.
                
                - **Version** *(string) --* The unique ID of the version.
            
        """
        pass

    def list_function_definitions(self, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListFunctionDefinitions>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_function_definitions(
              MaxResults=\'string\',
              NextToken=\'string\'
          )
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.
        
        :type NextToken: string
        :param NextToken: The token for the next set of results, or \'\'null\'\' if there are no additional results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Definitions\': [
                    {
                        \'Arn\': \'string\',
                        \'CreationTimestamp\': \'string\',
                        \'Id\': \'string\',
                        \'LastUpdatedTimestamp\': \'string\',
                        \'LatestVersion\': \'string\',
                        \'LatestVersionArn\': \'string\',
                        \'Name\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* Success. The response contains the IDs of all the Greengrass Lambda function definitions in this account.
            
            - **Definitions** *(list) --* Information about a definition.
              
              - *(dict) --* Information about a definition.
                
                - **Arn** *(string) --* The ARN of the definition.
                
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was created.
                
                - **Id** *(string) --* The ID of the definition.
                
                - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was last updated.
                
                - **LatestVersion** *(string) --* The latest version of the definition.
                
                - **LatestVersionArn** *(string) --* The ARN of the latest version of the definition.
                
                - **Name** *(string) --* The name of the definition.
            
            - **NextToken** *(string) --* The token for the next set of results, or \'\'null\'\' if there are no additional results.
        """
        pass

    def list_group_certificate_authorities(self, GroupId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListGroupCertificateAuthorities>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_group_certificate_authorities(
              GroupId=\'string\'
          )
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the AWS Greengrass group.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'GroupCertificateAuthorities\': [
                    {
                        \'GroupCertificateAuthorityArn\': \'string\',
                        \'GroupCertificateAuthorityId\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* Success. The response body contains the PKI Configuration.
            
            - **GroupCertificateAuthorities** *(list) --* A list of certificate authorities associated with the group.
              
              - *(dict) --* Information about a certificate authority for a group.
                
                - **GroupCertificateAuthorityArn** *(string) --* The ARN of the certificate authority for the group.
                
                - **GroupCertificateAuthorityId** *(string) --* The ID of the certificate authority for the group.
            
        """
        pass

    def list_group_versions(self, GroupId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListGroupVersions>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_group_versions(
              GroupId=\'string\',
              MaxResults=\'string\',
              NextToken=\'string\'
          )
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the AWS Greengrass group.
        
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.
        
        :type NextToken: string
        :param NextToken: The token for the next set of results, or \'\'null\'\' if there are no additional results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextToken\': \'string\',
                \'Versions\': [
                    {
                        \'Arn\': \'string\',
                        \'CreationTimestamp\': \'string\',
                        \'Id\': \'string\',
                        \'Version\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* Success. The response contains the list of versions and metadata for the given group.
            
            - **NextToken** *(string) --* The token for the next set of results, or \'\'null\'\' if there are no additional results.
            
            - **Versions** *(list) --* Information about a version.
              
              - *(dict) --* Information about a version.
                
                - **Arn** *(string) --* The ARN of the version.
                
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the version was created.
                
                - **Id** *(string) --* The ID of the version.
                
                - **Version** *(string) --* The unique ID of the version.
            
        """
        pass

    def list_groups(self, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListGroups>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_groups(
              MaxResults=\'string\',
              NextToken=\'string\'
          )
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.
        
        :type NextToken: string
        :param NextToken: The token for the next set of results, or \'\'null\'\' if there are no additional results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Groups\': [
                    {
                        \'Arn\': \'string\',
                        \'CreationTimestamp\': \'string\',
                        \'Id\': \'string\',
                        \'LastUpdatedTimestamp\': \'string\',
                        \'LatestVersion\': \'string\',
                        \'LatestVersionArn\': \'string\',
                        \'Name\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Groups** *(list) --* Information about a group.
              
              - *(dict) --* Information about a group.
                
                - **Arn** *(string) --* The ARN of the group.
                
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the group was created.
                
                - **Id** *(string) --* The ID of the group.
                
                - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the group was last updated.
                
                - **LatestVersion** *(string) --* The latest version of the group.
                
                - **LatestVersionArn** *(string) --* The ARN of the latest version of the group.
                
                - **Name** *(string) --* The name of the group.
            
            - **NextToken** *(string) --* The token for the next set of results, or \'\'null\'\' if there are no additional results.
        """
        pass

    def list_logger_definition_versions(self, LoggerDefinitionId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListLoggerDefinitionVersions>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_logger_definition_versions(
              LoggerDefinitionId=\'string\',
              MaxResults=\'string\',
              NextToken=\'string\'
          )
        :type LoggerDefinitionId: string
        :param LoggerDefinitionId: **[REQUIRED]** The ID of the logger definition.
        
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.
        
        :type NextToken: string
        :param NextToken: The token for the next set of results, or \'\'null\'\' if there are no additional results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextToken\': \'string\',
                \'Versions\': [
                    {
                        \'Arn\': \'string\',
                        \'CreationTimestamp\': \'string\',
                        \'Id\': \'string\',
                        \'Version\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NextToken** *(string) --* The token for the next set of results, or \'\'null\'\' if there are no additional results.
            
            - **Versions** *(list) --* Information about a version.
              
              - *(dict) --* Information about a version.
                
                - **Arn** *(string) --* The ARN of the version.
                
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the version was created.
                
                - **Id** *(string) --* The ID of the version.
                
                - **Version** *(string) --* The unique ID of the version.
            
        """
        pass

    def list_logger_definitions(self, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListLoggerDefinitions>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_logger_definitions(
              MaxResults=\'string\',
              NextToken=\'string\'
          )
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.
        
        :type NextToken: string
        :param NextToken: The token for the next set of results, or \'\'null\'\' if there are no additional results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Definitions\': [
                    {
                        \'Arn\': \'string\',
                        \'CreationTimestamp\': \'string\',
                        \'Id\': \'string\',
                        \'LastUpdatedTimestamp\': \'string\',
                        \'LatestVersion\': \'string\',
                        \'LatestVersionArn\': \'string\',
                        \'Name\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Definitions** *(list) --* Information about a definition.
              
              - *(dict) --* Information about a definition.
                
                - **Arn** *(string) --* The ARN of the definition.
                
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was created.
                
                - **Id** *(string) --* The ID of the definition.
                
                - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was last updated.
                
                - **LatestVersion** *(string) --* The latest version of the definition.
                
                - **LatestVersionArn** *(string) --* The ARN of the latest version of the definition.
                
                - **Name** *(string) --* The name of the definition.
            
            - **NextToken** *(string) --* The token for the next set of results, or \'\'null\'\' if there are no additional results.
        """
        pass

    def list_resource_definition_versions(self, ResourceDefinitionId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListResourceDefinitionVersions>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_resource_definition_versions(
              MaxResults=\'string\',
              NextToken=\'string\',
              ResourceDefinitionId=\'string\'
          )
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.
        
        :type NextToken: string
        :param NextToken: The token for the next set of results, or \'\'null\'\' if there are no additional results.
        
        :type ResourceDefinitionId: string
        :param ResourceDefinitionId: **[REQUIRED]** The ID of the resource definition.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextToken\': \'string\',
                \'Versions\': [
                    {
                        \'Arn\': \'string\',
                        \'CreationTimestamp\': \'string\',
                        \'Id\': \'string\',
                        \'Version\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* success
            
            - **NextToken** *(string) --* The token for the next set of results, or \'\'null\'\' if there are no additional results.
            
            - **Versions** *(list) --* Information about a version.
              
              - *(dict) --* Information about a version.
                
                - **Arn** *(string) --* The ARN of the version.
                
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the version was created.
                
                - **Id** *(string) --* The ID of the version.
                
                - **Version** *(string) --* The unique ID of the version.
            
        """
        pass

    def list_resource_definitions(self, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListResourceDefinitions>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_resource_definitions(
              MaxResults=\'string\',
              NextToken=\'string\'
          )
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.
        
        :type NextToken: string
        :param NextToken: The token for the next set of results, or \'\'null\'\' if there are no additional results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Definitions\': [
                    {
                        \'Arn\': \'string\',
                        \'CreationTimestamp\': \'string\',
                        \'Id\': \'string\',
                        \'LastUpdatedTimestamp\': \'string\',
                        \'LatestVersion\': \'string\',
                        \'LatestVersionArn\': \'string\',
                        \'Name\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* The IDs of all the Greengrass resource definitions in this account.
            
            - **Definitions** *(list) --* Information about a definition.
              
              - *(dict) --* Information about a definition.
                
                - **Arn** *(string) --* The ARN of the definition.
                
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was created.
                
                - **Id** *(string) --* The ID of the definition.
                
                - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was last updated.
                
                - **LatestVersion** *(string) --* The latest version of the definition.
                
                - **LatestVersionArn** *(string) --* The ARN of the latest version of the definition.
                
                - **Name** *(string) --* The name of the definition.
            
            - **NextToken** *(string) --* The token for the next set of results, or \'\'null\'\' if there are no additional results.
        """
        pass

    def list_subscription_definition_versions(self, SubscriptionDefinitionId: str, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListSubscriptionDefinitionVersions>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_subscription_definition_versions(
              MaxResults=\'string\',
              NextToken=\'string\',
              SubscriptionDefinitionId=\'string\'
          )
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.
        
        :type NextToken: string
        :param NextToken: The token for the next set of results, or \'\'null\'\' if there are no additional results.
        
        :type SubscriptionDefinitionId: string
        :param SubscriptionDefinitionId: **[REQUIRED]** The ID of the subscription definition.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextToken\': \'string\',
                \'Versions\': [
                    {
                        \'Arn\': \'string\',
                        \'CreationTimestamp\': \'string\',
                        \'Id\': \'string\',
                        \'Version\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NextToken** *(string) --* The token for the next set of results, or \'\'null\'\' if there are no additional results.
            
            - **Versions** *(list) --* Information about a version.
              
              - *(dict) --* Information about a version.
                
                - **Arn** *(string) --* The ARN of the version.
                
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the version was created.
                
                - **Id** *(string) --* The ID of the version.
                
                - **Version** *(string) --* The unique ID of the version.
            
        """
        pass

    def list_subscription_definitions(self, MaxResults: str = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ListSubscriptionDefinitions>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_subscription_definitions(
              MaxResults=\'string\',
              NextToken=\'string\'
          )
        :type MaxResults: string
        :param MaxResults: The maximum number of results to be returned per request.
        
        :type NextToken: string
        :param NextToken: The token for the next set of results, or \'\'null\'\' if there are no additional results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Definitions\': [
                    {
                        \'Arn\': \'string\',
                        \'CreationTimestamp\': \'string\',
                        \'Id\': \'string\',
                        \'LastUpdatedTimestamp\': \'string\',
                        \'LatestVersion\': \'string\',
                        \'LatestVersionArn\': \'string\',
                        \'Name\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Definitions** *(list) --* Information about a definition.
              
              - *(dict) --* Information about a definition.
                
                - **Arn** *(string) --* The ARN of the definition.
                
                - **CreationTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was created.
                
                - **Id** *(string) --* The ID of the definition.
                
                - **LastUpdatedTimestamp** *(string) --* The time, in milliseconds since the epoch, when the definition was last updated.
                
                - **LatestVersion** *(string) --* The latest version of the definition.
                
                - **LatestVersionArn** *(string) --* The ARN of the latest version of the definition.
                
                - **Name** *(string) --* The name of the definition.
            
            - **NextToken** *(string) --* The token for the next set of results, or \'\'null\'\' if there are no additional results.
        """
        pass

    def reset_deployments(self, GroupId: str, AmznClientToken: str = None, Force: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/ResetDeployments>`_
        
        **Request Syntax** 
        ::
        
          response = client.reset_deployments(
              AmznClientToken=\'string\',
              Force=True|False,
              GroupId=\'string\'
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.
        
        :type Force: boolean
        :param Force: If true, performs a best-effort only core reset.
        
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the AWS Greengrass group.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DeploymentArn\': \'string\',
                \'DeploymentId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* Success. The group\'s deployments were reset.
            
            - **DeploymentArn** *(string) --* The ARN of the deployment.
            
            - **DeploymentId** *(string) --* The ID of the deployment.
        """
        pass

    def start_bulk_deployment(self, AmznClientToken: str = None, ExecutionRoleArn: str = None, InputFileUri: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/StartBulkDeployment>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_bulk_deployment(
              AmznClientToken=\'string\',
              ExecutionRoleArn=\'string\',
              InputFileUri=\'string\'
          )
        :type AmznClientToken: string
        :param AmznClientToken: A client token used to correlate requests and responses.
        
        :type ExecutionRoleArn: string
        :param ExecutionRoleArn: The ARN of the execution role to associate with the bulk deployment operation. This IAM role must allow the \'\'greengrass:CreateDeployment\'\' action for all group versions that are listed in the input file. This IAM role must have access to the S3 bucket containing the input file.
        
        :type InputFileUri: string
        :param InputFileUri: The URI of the input file contained in the S3 bucket. The execution role must have \'\'getObject\'\' permissions on this bucket to access the input file. The input file is a JSON-serialized, line delimited file with UTF-8 encoding that provides a list of group and version IDs and the deployment type. This file must be less than 100MB. Currently, Greengrass; supports only \'\'NewDeployment\'\' deployment types.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'BulkDeploymentArn\': \'string\',
                \'BulkDeploymentId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* success
            
            - **BulkDeploymentArn** *(string) --* The ARN of the bulk deployment.
            
            - **BulkDeploymentId** *(string) --* The ID of the bulk deployment.
        """
        pass

    def stop_bulk_deployment(self, BulkDeploymentId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/StopBulkDeployment>`_
        
        **Request Syntax** 
        ::
        
          response = client.stop_bulk_deployment(
              BulkDeploymentId=\'string\'
          )
        :type BulkDeploymentId: string
        :param BulkDeploymentId: **[REQUIRED]** The ID of the bulk deployment.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* Success. The bulk deployment is being stopped.
        """
        pass

    def update_connectivity_info(self, ThingName: str, ConnectivityInfo: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateConnectivityInfo>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_connectivity_info(
              ConnectivityInfo=[
                  {
                      \'HostAddress\': \'string\',
                      \'Id\': \'string\',
                      \'Metadata\': \'string\',
                      \'PortNumber\': 123
                  },
              ],
              ThingName=\'string\'
          )
        :type ConnectivityInfo: list
        :param ConnectivityInfo: A list of connectivity info.
        
          - *(dict) --* Information about a Greengrass core\'s connectivity.
        
            - **HostAddress** *(string) --* The endpoint for the Greengrass core. Can be an IP address or DNS.
        
            - **Id** *(string) --* The ID of the connectivity information.
        
            - **Metadata** *(string) --* Metadata for this endpoint.
        
            - **PortNumber** *(integer) --* The port of the Greengrass core. Usually 8883.
        
        :type ThingName: string
        :param ThingName: **[REQUIRED]** The thing name.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Message\': \'string\',
                \'Version\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* success
            
            - **Message** *(string) --* A message about the connectivity info update request.
            
            - **Version** *(string) --* The new version of the connectivity info.
        """
        pass

    def update_core_definition(self, CoreDefinitionId: str, Name: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateCoreDefinition>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_core_definition(
              CoreDefinitionId=\'string\',
              Name=\'string\'
          )
        :type CoreDefinitionId: string
        :param CoreDefinitionId: **[REQUIRED]** The ID of the core definition.
        
        :type Name: string
        :param Name: The name of the definition.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* success
        """
        pass

    def update_device_definition(self, DeviceDefinitionId: str, Name: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateDeviceDefinition>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_device_definition(
              DeviceDefinitionId=\'string\',
              Name=\'string\'
          )
        :type DeviceDefinitionId: string
        :param DeviceDefinitionId: **[REQUIRED]** The ID of the device definition.
        
        :type Name: string
        :param Name: The name of the definition.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* success
        """
        pass

    def update_function_definition(self, FunctionDefinitionId: str, Name: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateFunctionDefinition>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_function_definition(
              FunctionDefinitionId=\'string\',
              Name=\'string\'
          )
        :type FunctionDefinitionId: string
        :param FunctionDefinitionId: **[REQUIRED]** The ID of the Lambda function definition.
        
        :type Name: string
        :param Name: The name of the definition.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* success
        """
        pass

    def update_group(self, GroupId: str, Name: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateGroup>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_group(
              GroupId=\'string\',
              Name=\'string\'
          )
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the AWS Greengrass group.
        
        :type Name: string
        :param Name: The name of the definition.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* success
        """
        pass

    def update_group_certificate_configuration(self, GroupId: str, CertificateExpiryInMilliseconds: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateGroupCertificateConfiguration>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_group_certificate_configuration(
              CertificateExpiryInMilliseconds=\'string\',
              GroupId=\'string\'
          )
        :type CertificateExpiryInMilliseconds: string
        :param CertificateExpiryInMilliseconds: The amount of time remaining before the certificate expires, in milliseconds.
        
        :type GroupId: string
        :param GroupId: **[REQUIRED]** The ID of the AWS Greengrass group.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'CertificateAuthorityExpiryInMilliseconds\': \'string\',
                \'CertificateExpiryInMilliseconds\': \'string\',
                \'GroupId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* Success. The response body contains the PKI Configuration.
            
            - **CertificateAuthorityExpiryInMilliseconds** *(string) --* The amount of time remaining before the certificate authority expires, in milliseconds.
            
            - **CertificateExpiryInMilliseconds** *(string) --* The amount of time remaining before the certificate expires, in milliseconds.
            
            - **GroupId** *(string) --* The ID of the group certificate configuration.
        """
        pass

    def update_logger_definition(self, LoggerDefinitionId: str, Name: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateLoggerDefinition>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_logger_definition(
              LoggerDefinitionId=\'string\',
              Name=\'string\'
          )
        :type LoggerDefinitionId: string
        :param LoggerDefinitionId: **[REQUIRED]** The ID of the logger definition.
        
        :type Name: string
        :param Name: The name of the definition.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* success
        """
        pass

    def update_resource_definition(self, ResourceDefinitionId: str, Name: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateResourceDefinition>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_resource_definition(
              Name=\'string\',
              ResourceDefinitionId=\'string\'
          )
        :type Name: string
        :param Name: The name of the definition.
        
        :type ResourceDefinitionId: string
        :param ResourceDefinitionId: **[REQUIRED]** The ID of the resource definition.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* success
        """
        pass

    def update_subscription_definition(self, SubscriptionDefinitionId: str, Name: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/greengrass-2017-06-07/UpdateSubscriptionDefinition>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_subscription_definition(
              Name=\'string\',
              SubscriptionDefinitionId=\'string\'
          )
        :type Name: string
        :param Name: The name of the definition.
        
        :type SubscriptionDefinitionId: string
        :param SubscriptionDefinitionId: **[REQUIRED]** The ID of the subscription definition.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* success
        """
        pass
