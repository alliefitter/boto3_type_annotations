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

    def create_device_pool(self, projectArn: str, name: str, rules: List, description: str = None, maxDevices: int = None) -> Dict:
        """
        Creates a device pool.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/CreateDevicePool>`_
        
        **Request Syntax**
        ::
          response = client.create_device_pool(
              projectArn='string',
              name='string',
              description='string',
              rules=[
                  {
                      'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE'|'OS_VERSION'|'MODEL'|'AVAILABILITY',
                      'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                      'value': 'string'
                  },
              ],
              maxDevices=123
          )
        
        **Response Syntax**
        ::
            {
                'devicePool': {
                    'arn': 'string',
                    'name': 'string',
                    'description': 'string',
                    'type': 'CURATED'|'PRIVATE',
                    'rules': [
                        {
                            'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE'|'OS_VERSION'|'MODEL'|'AVAILABILITY',
                            'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                            'value': 'string'
                        },
                    ],
                    'maxDevices': 123
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of a create device pool request.
            - **devicePool** *(dict) --* 
              The newly created device pool.
              - **arn** *(string) --* 
                The device pool's ARN.
              - **name** *(string) --* 
                The device pool's name.
              - **description** *(string) --* 
                The device pool's description.
              - **type** *(string) --* 
                The device pool's type.
                Allowed values include:
                * CURATED: A device pool that is created and managed by AWS Device Farm. 
                * PRIVATE: A device pool that is created and managed by the device pool developer. 
              - **rules** *(list) --* 
                Information about the device pool's rules.
                - *(dict) --* 
                  Represents a condition for a device pool.
                  - **attribute** *(string) --* 
                    The rule's stringified attribute. For example, specify the value as ``"\"abc\""`` .
                    The supported operators for each attribute are provided in the following list.
                      APPIUM_VERSION  
                    The Appium version for the test.
                     *Supported operators* : ``CONTAINS``  
                      ARN  
                    The Amazon Resource Name (ARN) of the device. For example, "arn:aws:devicefarm:us-west-2::device:12345Example".
                     *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                      AVAILABILITY  
                    The current availability of the device. Valid values are "AVAILABLE", "HIGHLY_AVAILABLE", "BUSY", or "TEMPORARY_NOT_AVAILABLE".
                     *Supported operators* : ``EQUALS``  
                      FLEET_TYPE  
                    The fleet type. Valid values are "PUBLIC" or "PRIVATE".
                     *Supported operators* : ``EQUALS``  
                      FORM_FACTOR  
                    The device form factor. Valid values are "PHONE" or "TABLET".
                     *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                      INSTANCE_ARN  
                    The Amazon Resource Name (ARN) of the device instance.
                     *Supported operators* : ``IN`` , ``NOT_IN``  
                      INSTANCE_LABELS  
                    The label of the device instance.
                     *Supported operators* : ``CONTAINS``  
                      MANUFACTURER  
                    The device manufacturer. For example, "Apple".
                     *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                      MODEL  
                    The device model, such as "Apple iPad Air 2" or "Google Pixel".
                     *Supported operators* : ``CONTAINS`` , ``EQUALS`` , ``IN`` , ``NOT_IN``  
                      OS_VERSION  
                    The operating system version. For example, "10.3.2".
                     *Supported operators* : ``EQUALS`` , ``GREATER_THAN`` , ``GREATER_THAN_OR_EQUALS`` , ``IN`` , ``LESS_THAN`` , ``LESS_THAN_OR_EQUALS`` , ``NOT_IN``  
                      PLATFORM  
                    The device platform. Valid values are "ANDROID" or "IOS".
                     *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                      REMOTE_ACCESS_ENABLED  
                    Whether the device is enabled for remote access. Valid values are "TRUE" or "FALSE".
                     *Supported operators* : ``EQUALS``  
                      REMOTE_DEBUG_ENABLED  
                    Whether the device is enabled for remote debugging. Valid values are "TRUE" or "FALSE".
                     *Supported operators* : ``EQUALS``  
                  - **operator** *(string) --* 
                    Specifies how Device Farm compares the rule's attribute to the value. For the operators that are supported by each attribute, see the attribute descriptions.
                  - **value** *(string) --* 
                    The rule's value.
              - **maxDevices** *(integer) --* 
                The number of devices that Device Farm can add to your device pool. Device Farm adds devices that are available and that meet the criteria that you assign for the ``rules`` parameter. Depending on how many devices meet these constraints, your device pool might contain fewer devices than the value for this parameter.
                By specifying the maximum number of devices, you can control the costs that you incur by running tests.
        :type projectArn: string
        :param projectArn: **[REQUIRED]**
          The ARN of the project for the device pool.
        :type name: string
        :param name: **[REQUIRED]**
          The device pool\'s name.
        :type description: string
        :param description:
          The device pool\'s description.
        :type rules: list
        :param rules: **[REQUIRED]**
          The device pool\'s rules.
          - *(dict) --*
            Represents a condition for a device pool.
            - **attribute** *(string) --*
              The rule\'s stringified attribute. For example, specify the value as ``\"\\"abc\\"\"`` .
              The supported operators for each attribute are provided in the following list.
                APPIUM_VERSION
              The Appium version for the test.
               *Supported operators* : ``CONTAINS``
                ARN
              The Amazon Resource Name (ARN) of the device. For example, \"arn:aws:devicefarm:us-west-2::device:12345Example\".
               *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``
                AVAILABILITY
              The current availability of the device. Valid values are \"AVAILABLE\", \"HIGHLY_AVAILABLE\", \"BUSY\", or \"TEMPORARY_NOT_AVAILABLE\".
               *Supported operators* : ``EQUALS``
                FLEET_TYPE
              The fleet type. Valid values are \"PUBLIC\" or \"PRIVATE\".
               *Supported operators* : ``EQUALS``
                FORM_FACTOR
              The device form factor. Valid values are \"PHONE\" or \"TABLET\".
               *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``
                INSTANCE_ARN
              The Amazon Resource Name (ARN) of the device instance.
               *Supported operators* : ``IN`` , ``NOT_IN``
                INSTANCE_LABELS
              The label of the device instance.
               *Supported operators* : ``CONTAINS``
                MANUFACTURER
              The device manufacturer. For example, \"Apple\".
               *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``
                MODEL
              The device model, such as \"Apple iPad Air 2\" or \"Google Pixel\".
               *Supported operators* : ``CONTAINS`` , ``EQUALS`` , ``IN`` , ``NOT_IN``
                OS_VERSION
              The operating system version. For example, \"10.3.2\".
               *Supported operators* : ``EQUALS`` , ``GREATER_THAN`` , ``GREATER_THAN_OR_EQUALS`` , ``IN`` , ``LESS_THAN`` , ``LESS_THAN_OR_EQUALS`` , ``NOT_IN``
                PLATFORM
              The device platform. Valid values are \"ANDROID\" or \"IOS\".
               *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``
                REMOTE_ACCESS_ENABLED
              Whether the device is enabled for remote access. Valid values are \"TRUE\" or \"FALSE\".
               *Supported operators* : ``EQUALS``
                REMOTE_DEBUG_ENABLED
              Whether the device is enabled for remote debugging. Valid values are \"TRUE\" or \"FALSE\".
               *Supported operators* : ``EQUALS``
            - **operator** *(string) --*
              Specifies how Device Farm compares the rule\'s attribute to the value. For the operators that are supported by each attribute, see the attribute descriptions.
            - **value** *(string) --*
              The rule\'s value.
        :type maxDevices: integer
        :param maxDevices:
          The number of devices that Device Farm can add to your device pool. Device Farm adds devices that are available and that meet the criteria that you assign for the ``rules`` parameter. Depending on how many devices meet these constraints, your device pool might contain fewer devices than the value for this parameter.
          By specifying the maximum number of devices, you can control the costs that you incur by running tests.
        :rtype: dict
        :returns:
        """
        pass

    def create_instance_profile(self, name: str, description: str = None, packageCleanup: bool = None, excludeAppPackagesFromCleanup: List = None, rebootAfterUse: bool = None) -> Dict:
        """
        Creates a profile that can be applied to one or more private fleet device instances.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/CreateInstanceProfile>`_
        
        **Request Syntax**
        ::
          response = client.create_instance_profile(
              name='string',
              description='string',
              packageCleanup=True|False,
              excludeAppPackagesFromCleanup=[
                  'string',
              ],
              rebootAfterUse=True|False
          )
        
        **Response Syntax**
        ::
            {
                'instanceProfile': {
                    'arn': 'string',
                    'packageCleanup': True|False,
                    'excludeAppPackagesFromCleanup': [
                        'string',
                    ],
                    'rebootAfterUse': True|False,
                    'name': 'string',
                    'description': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **instanceProfile** *(dict) --* 
              An object containing information about your instance profile.
              - **arn** *(string) --* 
                The Amazon Resource Name (ARN) of the instance profile.
              - **packageCleanup** *(boolean) --* 
                When set to ``true`` , Device Farm will remove app packages after a test run. The default value is ``false`` for private devices.
              - **excludeAppPackagesFromCleanup** *(list) --* 
                An array of strings specifying the list of app packages that should not be cleaned up from the device after a test run is over.
                The list of packages is only considered if you set ``packageCleanup`` to ``true`` .
                - *(string) --* 
              - **rebootAfterUse** *(boolean) --* 
                When set to ``true`` , Device Farm will reboot the instance after a test run. The default value is ``true`` .
              - **name** *(string) --* 
                The name of the instance profile.
              - **description** *(string) --* 
                The description of the instance profile.
        :type name: string
        :param name: **[REQUIRED]**
          The name of your instance profile.
        :type description: string
        :param description:
          The description of your instance profile.
        :type packageCleanup: boolean
        :param packageCleanup:
          When set to ``true`` , Device Farm will remove app packages after a test run. The default value is ``false`` for private devices.
        :type excludeAppPackagesFromCleanup: list
        :param excludeAppPackagesFromCleanup:
          An array of strings specifying the list of app packages that should not be cleaned up from the device after a test run is over.
          The list of packages is only considered if you set ``packageCleanup`` to ``true`` .
          - *(string) --*
        :type rebootAfterUse: boolean
        :param rebootAfterUse:
          When set to ``true`` , Device Farm will reboot the instance after a test run. The default value is ``true`` .
        :rtype: dict
        :returns:
        """
        pass

    def create_network_profile(self, projectArn: str, name: str, description: str = None, type: str = None, uplinkBandwidthBits: int = None, downlinkBandwidthBits: int = None, uplinkDelayMs: int = None, downlinkDelayMs: int = None, uplinkJitterMs: int = None, downlinkJitterMs: int = None, uplinkLossPercent: int = None, downlinkLossPercent: int = None) -> Dict:
        """
        Creates a network profile.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/CreateNetworkProfile>`_
        
        **Request Syntax**
        ::
          response = client.create_network_profile(
              projectArn='string',
              name='string',
              description='string',
              type='CURATED'|'PRIVATE',
              uplinkBandwidthBits=123,
              downlinkBandwidthBits=123,
              uplinkDelayMs=123,
              downlinkDelayMs=123,
              uplinkJitterMs=123,
              downlinkJitterMs=123,
              uplinkLossPercent=123,
              downlinkLossPercent=123
          )
        
        **Response Syntax**
        ::
            {
                'networkProfile': {
                    'arn': 'string',
                    'name': 'string',
                    'description': 'string',
                    'type': 'CURATED'|'PRIVATE',
                    'uplinkBandwidthBits': 123,
                    'downlinkBandwidthBits': 123,
                    'uplinkDelayMs': 123,
                    'downlinkDelayMs': 123,
                    'uplinkJitterMs': 123,
                    'downlinkJitterMs': 123,
                    'uplinkLossPercent': 123,
                    'downlinkLossPercent': 123
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **networkProfile** *(dict) --* 
              The network profile that is returned by the create network profile request.
              - **arn** *(string) --* 
                The Amazon Resource Name (ARN) of the network profile.
              - **name** *(string) --* 
                The name of the network profile.
              - **description** *(string) --* 
                The description of the network profile.
              - **type** *(string) --* 
                The type of network profile. Valid values are listed below.
              - **uplinkBandwidthBits** *(integer) --* 
                The data throughput rate in bits per second, as an integer from 0 to 104857600.
              - **downlinkBandwidthBits** *(integer) --* 
                The data throughput rate in bits per second, as an integer from 0 to 104857600.
              - **uplinkDelayMs** *(integer) --* 
                Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
              - **downlinkDelayMs** *(integer) --* 
                Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
              - **uplinkJitterMs** *(integer) --* 
                Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
              - **downlinkJitterMs** *(integer) --* 
                Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
              - **uplinkLossPercent** *(integer) --* 
                Proportion of transmitted packets that fail to arrive from 0 to 100 percent.
              - **downlinkLossPercent** *(integer) --* 
                Proportion of received packets that fail to arrive from 0 to 100 percent.
        :type projectArn: string
        :param projectArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the project for which you want to create a network profile.
        :type name: string
        :param name: **[REQUIRED]**
          The name you wish to specify for the new network profile.
        :type description: string
        :param description:
          The description of the network profile.
        :type type: string
        :param type:
          The type of network profile you wish to create. Valid values are listed below.
        :type uplinkBandwidthBits: integer
        :param uplinkBandwidthBits:
          The data throughput rate in bits per second, as an integer from 0 to 104857600.
        :type downlinkBandwidthBits: integer
        :param downlinkBandwidthBits:
          The data throughput rate in bits per second, as an integer from 0 to 104857600.
        :type uplinkDelayMs: integer
        :param uplinkDelayMs:
          Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
        :type downlinkDelayMs: integer
        :param downlinkDelayMs:
          Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
        :type uplinkJitterMs: integer
        :param uplinkJitterMs:
          Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
        :type downlinkJitterMs: integer
        :param downlinkJitterMs:
          Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
        :type uplinkLossPercent: integer
        :param uplinkLossPercent:
          Proportion of transmitted packets that fail to arrive from 0 to 100 percent.
        :type downlinkLossPercent: integer
        :param downlinkLossPercent:
          Proportion of received packets that fail to arrive from 0 to 100 percent.
        :rtype: dict
        :returns:
        """
        pass

    def create_project(self, name: str, defaultJobTimeoutMinutes: int = None) -> Dict:
        """
        Creates a new project.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/CreateProject>`_
        
        **Request Syntax**
        ::
          response = client.create_project(
              name='string',
              defaultJobTimeoutMinutes=123
          )
        
        **Response Syntax**
        ::
            {
                'project': {
                    'arn': 'string',
                    'name': 'string',
                    'defaultJobTimeoutMinutes': 123,
                    'created': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of a create project request.
            - **project** *(dict) --* 
              The newly created project.
              - **arn** *(string) --* 
                The project's ARN.
              - **name** *(string) --* 
                The project's name.
              - **defaultJobTimeoutMinutes** *(integer) --* 
                The default number of minutes (at the project level) a test run will execute before it times out. Default value is 60 minutes.
              - **created** *(datetime) --* 
                When the project was created.
        :type name: string
        :param name: **[REQUIRED]**
          The project\'s name.
        :type defaultJobTimeoutMinutes: integer
        :param defaultJobTimeoutMinutes:
          Sets the execution timeout value (in minutes) for a project. All test runs in this project will use the specified execution timeout value unless overridden when scheduling a run.
        :rtype: dict
        :returns:
        """
        pass

    def create_remote_access_session(self, projectArn: str, deviceArn: str, instanceArn: str = None, sshPublicKey: str = None, remoteDebugEnabled: bool = None, remoteRecordEnabled: bool = None, remoteRecordAppArn: str = None, name: str = None, clientId: str = None, configuration: Dict = None, interactionMode: str = None, skipAppResign: bool = None) -> Dict:
        """
        Specifies and starts a remote access session.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/CreateRemoteAccessSession>`_
        
        **Request Syntax**
        ::
          response = client.create_remote_access_session(
              projectArn='string',
              deviceArn='string',
              instanceArn='string',
              sshPublicKey='string',
              remoteDebugEnabled=True|False,
              remoteRecordEnabled=True|False,
              remoteRecordAppArn='string',
              name='string',
              clientId='string',
              configuration={
                  'billingMethod': 'METERED'|'UNMETERED',
                  'vpceConfigurationArns': [
                      'string',
                  ]
              },
              interactionMode='INTERACTIVE'|'NO_VIDEO'|'VIDEO_ONLY',
              skipAppResign=True|False
          )
        
        **Response Syntax**
        ::
            {
                'remoteAccessSession': {
                    'arn': 'string',
                    'name': 'string',
                    'created': datetime(2015, 1, 1),
                    'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                    'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                    'message': 'string',
                    'started': datetime(2015, 1, 1),
                    'stopped': datetime(2015, 1, 1),
                    'device': {
                        'arn': 'string',
                        'name': 'string',
                        'manufacturer': 'string',
                        'model': 'string',
                        'modelId': 'string',
                        'formFactor': 'PHONE'|'TABLET',
                        'platform': 'ANDROID'|'IOS',
                        'os': 'string',
                        'cpu': {
                            'frequency': 'string',
                            'architecture': 'string',
                            'clock': 123.0
                        },
                        'resolution': {
                            'width': 123,
                            'height': 123
                        },
                        'heapSize': 123,
                        'memory': 123,
                        'image': 'string',
                        'carrier': 'string',
                        'radio': 'string',
                        'remoteAccessEnabled': True|False,
                        'remoteDebugEnabled': True|False,
                        'fleetType': 'string',
                        'fleetName': 'string',
                        'instances': [
                            {
                                'arn': 'string',
                                'deviceArn': 'string',
                                'labels': [
                                    'string',
                                ],
                                'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                                'udid': 'string',
                                'instanceProfile': {
                                    'arn': 'string',
                                    'packageCleanup': True|False,
                                    'excludeAppPackagesFromCleanup': [
                                        'string',
                                    ],
                                    'rebootAfterUse': True|False,
                                    'name': 'string',
                                    'description': 'string'
                                }
                            },
                        ],
                        'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
                    },
                    'instanceArn': 'string',
                    'remoteDebugEnabled': True|False,
                    'remoteRecordEnabled': True|False,
                    'remoteRecordAppArn': 'string',
                    'hostAddress': 'string',
                    'clientId': 'string',
                    'billingMethod': 'METERED'|'UNMETERED',
                    'deviceMinutes': {
                        'total': 123.0,
                        'metered': 123.0,
                        'unmetered': 123.0
                    },
                    'endpoint': 'string',
                    'deviceUdid': 'string',
                    'interactionMode': 'INTERACTIVE'|'NO_VIDEO'|'VIDEO_ONLY',
                    'skipAppResign': True|False
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the server response from a request to create a remote access session.
            - **remoteAccessSession** *(dict) --* 
              A container that describes the remote access session when the request to create a remote access session is sent.
              - **arn** *(string) --* 
                The Amazon Resource Name (ARN) of the remote access session.
              - **name** *(string) --* 
                The name of the remote access session.
              - **created** *(datetime) --* 
                The date and time the remote access session was created.
              - **status** *(string) --* 
                The status of the remote access session. Can be any of the following:
                * PENDING: A pending status. 
                * PENDING_CONCURRENCY: A pending concurrency status. 
                * PENDING_DEVICE: A pending device status. 
                * PROCESSING: A processing status. 
                * SCHEDULING: A scheduling status. 
                * PREPARING: A preparing status. 
                * RUNNING: A running status. 
                * COMPLETED: A completed status. 
                * STOPPING: A stopping status. 
              - **result** *(string) --* 
                The result of the remote access session. Can be any of the following:
                * PENDING: A pending condition. 
                * PASSED: A passing condition. 
                * WARNED: A warning condition. 
                * FAILED: A failed condition. 
                * SKIPPED: A skipped condition. 
                * ERRORED: An error condition. 
                * STOPPED: A stopped condition. 
              - **message** *(string) --* 
                A message about the remote access session.
              - **started** *(datetime) --* 
                The date and time the remote access session was started.
              - **stopped** *(datetime) --* 
                The date and time the remote access session was stopped.
              - **device** *(dict) --* 
                The device (phone or tablet) used in the remote access session.
                - **arn** *(string) --* 
                  The device's ARN.
                - **name** *(string) --* 
                  The device's display name.
                - **manufacturer** *(string) --* 
                  The device's manufacturer name.
                - **model** *(string) --* 
                  The device's model name.
                - **modelId** *(string) --* 
                  The device's model ID.
                - **formFactor** *(string) --* 
                  The device's form factor.
                  Allowed values include:
                  * PHONE: The phone form factor. 
                  * TABLET: The tablet form factor. 
                - **platform** *(string) --* 
                  The device's platform.
                  Allowed values include:
                  * ANDROID: The Android platform. 
                  * IOS: The iOS platform. 
                - **os** *(string) --* 
                  The device's operating system type.
                - **cpu** *(dict) --* 
                  Information about the device's CPU.
                  - **frequency** *(string) --* 
                    The CPU's frequency.
                  - **architecture** *(string) --* 
                    The CPU's architecture, for example x86 or ARM.
                  - **clock** *(float) --* 
                    The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.
                - **resolution** *(dict) --* 
                  The resolution of the device.
                  - **width** *(integer) --* 
                    The screen resolution's width, expressed in pixels.
                  - **height** *(integer) --* 
                    The screen resolution's height, expressed in pixels.
                - **heapSize** *(integer) --* 
                  The device's heap size, expressed in bytes.
                - **memory** *(integer) --* 
                  The device's total memory size, expressed in bytes.
                - **image** *(string) --* 
                  The device's image name.
                - **carrier** *(string) --* 
                  The device's carrier.
                - **radio** *(string) --* 
                  The device's radio.
                - **remoteAccessEnabled** *(boolean) --* 
                  Specifies whether remote access has been enabled for the specified device.
                - **remoteDebugEnabled** *(boolean) --* 
                  This flag is set to ``true`` if remote debugging is enabled for the device.
                - **fleetType** *(string) --* 
                  The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.
                - **fleetName** *(string) --* 
                  The name of the fleet to which this device belongs.
                - **instances** *(list) --* 
                  The instances belonging to this device.
                  - *(dict) --* 
                    Represents the device instance.
                    - **arn** *(string) --* 
                      The Amazon Resource Name (ARN) of the device instance.
                    - **deviceArn** *(string) --* 
                      The Amazon Resource Name (ARN) of the device.
                    - **labels** *(list) --* 
                      An array of strings describing the device instance.
                      - *(string) --* 
                    - **status** *(string) --* 
                      The status of the device instance. Valid values are listed below.
                    - **udid** *(string) --* 
                      Unique device identifier for the device instance.
                    - **instanceProfile** *(dict) --* 
                      A object containing information about the instance profile.
                      - **arn** *(string) --* 
                        The Amazon Resource Name (ARN) of the instance profile.
                      - **packageCleanup** *(boolean) --* 
                        When set to ``true`` , Device Farm will remove app packages after a test run. The default value is ``false`` for private devices.
                      - **excludeAppPackagesFromCleanup** *(list) --* 
                        An array of strings specifying the list of app packages that should not be cleaned up from the device after a test run is over.
                        The list of packages is only considered if you set ``packageCleanup`` to ``true`` .
                        - *(string) --* 
                      - **rebootAfterUse** *(boolean) --* 
                        When set to ``true`` , Device Farm will reboot the instance after a test run. The default value is ``true`` .
                      - **name** *(string) --* 
                        The name of the instance profile.
                      - **description** *(string) --* 
                        The description of the instance profile.
                - **availability** *(string) --* 
                  Reflects how likely a device will be available for a test run. It is currently available in the ListDevices and GetDevice API methods.
              - **instanceArn** *(string) --* 
                The Amazon Resource Name (ARN) of the instance.
              - **remoteDebugEnabled** *(boolean) --* 
                This flag is set to ``true`` if remote debugging is enabled for the remote access session.
              - **remoteRecordEnabled** *(boolean) --* 
                This flag is set to ``true`` if remote recording is enabled for the remote access session.
              - **remoteRecordAppArn** *(string) --* 
                The Amazon Resource Name (ARN) for the app to be recorded in the remote access session.
              - **hostAddress** *(string) --* 
                IP address of the EC2 host where you need to connect to remotely debug devices. Only returned if remote debugging is enabled for the remote access session.
              - **clientId** *(string) --* 
                Unique identifier of your client for the remote access session. Only returned if remote debugging is enabled for the remote access session.
              - **billingMethod** *(string) --* 
                The billing method of the remote access session. Possible values include ``METERED`` or ``UNMETERED`` . For more information about metered devices, see `AWS Device Farm terminology <https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html#welcome-terminology>`__ ."
              - **deviceMinutes** *(dict) --* 
                The number of minutes a device is used in a remote access sesssion (including setup and teardown minutes).
                - **total** *(float) --* 
                  When specified, represents the total minutes used by the resource to run tests.
                - **metered** *(float) --* 
                  When specified, represents only the sum of metered minutes used by the resource to run tests.
                - **unmetered** *(float) --* 
                  When specified, represents only the sum of unmetered minutes used by the resource to run tests.
              - **endpoint** *(string) --* 
                The endpoint for the remote access sesssion.
              - **deviceUdid** *(string) --* 
                Unique device identifier for the remote device. Only returned if remote debugging is enabled for the remote access session.
              - **interactionMode** *(string) --* 
                The interaction mode of the remote access session. Valid values are:
                * INTERACTIVE: You can interact with the iOS device by viewing, touching, and rotating the screen. You **cannot** run XCUITest framework-based tests in this mode. 
                * NO_VIDEO: You are connected to the device but cannot interact with it or view the screen. This mode has the fastest test execution speed. You **can** run XCUITest framework-based tests in this mode. 
                * VIDEO_ONLY: You can view the screen but cannot touch or rotate it. You **can** run XCUITest framework-based tests and watch the screen in this mode. 
              - **skipAppResign** *(boolean) --* 
                When set to ``true`` , for private devices, Device Farm will not sign your app again. For public devices, Device Farm always signs your apps again and this parameter has no effect.
                For more information about how Device Farm re-signs your app(s), see `Do you modify my app? <https://aws.amazon.com/device-farm/faq/>`__ in the *AWS Device Farm FAQs* .
        :type projectArn: string
        :param projectArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the project for which you want to create a remote access session.
        :type deviceArn: string
        :param deviceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the device for which you want to create a remote access session.
        :type instanceArn: string
        :param instanceArn:
          The Amazon Resource Name (ARN) of the device instance for which you want to create a remote access session.
        :type sshPublicKey: string
        :param sshPublicKey:
          The public key of the ``ssh`` key pair you want to use for connecting to remote devices in your remote debugging session. This is only required if ``remoteDebugEnabled`` is set to ``true`` .
        :type remoteDebugEnabled: boolean
        :param remoteDebugEnabled:
          Set to ``true`` if you want to access devices remotely for debugging in your remote access session.
        :type remoteRecordEnabled: boolean
        :param remoteRecordEnabled:
          Set to ``true`` to enable remote recording for the remote access session.
        :type remoteRecordAppArn: string
        :param remoteRecordAppArn:
          The Amazon Resource Name (ARN) for the app to be recorded in the remote access session.
        :type name: string
        :param name:
          The name of the remote access session that you wish to create.
        :type clientId: string
        :param clientId:
          Unique identifier for the client. If you want access to multiple devices on the same client, you should pass the same ``clientId`` value in each call to ``CreateRemoteAccessSession`` . This is required only if ``remoteDebugEnabled`` is set to ``true`` .
        :type configuration: dict
        :param configuration:
          The configuration information for the remote access session request.
          - **billingMethod** *(string) --*
            The billing method for the remote access session.
          - **vpceConfigurationArns** *(list) --*
            An array of Amazon Resource Names (ARNs) included in the VPC endpoint configuration.
            - *(string) --*
        :type interactionMode: string
        :param interactionMode:
          The interaction mode of the remote access session. Valid values are:
          * INTERACTIVE: You can interact with the iOS device by viewing, touching, and rotating the screen. You **cannot** run XCUITest framework-based tests in this mode.
          * NO_VIDEO: You are connected to the device but cannot interact with it or view the screen. This mode has the fastest test execution speed. You **can** run XCUITest framework-based tests in this mode.
          * VIDEO_ONLY: You can view the screen but cannot touch or rotate it. You **can** run XCUITest framework-based tests and watch the screen in this mode.
        :type skipAppResign: boolean
        :param skipAppResign:
          When set to ``true`` , for private devices, Device Farm will not sign your app again. For public devices, Device Farm always signs your apps again and this parameter has no effect.
          For more information about how Device Farm re-signs your app(s), see `Do you modify my app? <https://aws.amazon.com/device-farm/faq/>`__ in the *AWS Device Farm FAQs* .
        :rtype: dict
        :returns:
        """
        pass

    def create_upload(self, projectArn: str, name: str, type: str, contentType: str = None) -> Dict:
        """
        Uploads an app or test scripts.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/CreateUpload>`_
        
        **Request Syntax**
        ::
          response = client.create_upload(
              projectArn='string',
              name='string',
              type='ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_NODE_TEST_PACKAGE'|'APPIUM_RUBY_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_NODE_TEST_PACKAGE'|'APPIUM_WEB_RUBY_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE'|'APPIUM_JAVA_JUNIT_TEST_SPEC'|'APPIUM_JAVA_TESTNG_TEST_SPEC'|'APPIUM_PYTHON_TEST_SPEC'|'APPIUM_NODE_TEST_SPEC'|'APPIUM_RUBY_TEST_SPEC'|'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC'|'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC'|'APPIUM_WEB_PYTHON_TEST_SPEC'|'APPIUM_WEB_NODE_TEST_SPEC'|'APPIUM_WEB_RUBY_TEST_SPEC'|'INSTRUMENTATION_TEST_SPEC'|'XCTEST_UI_TEST_SPEC',
              contentType='string'
          )
        
        **Response Syntax**
        ::
            {
                'upload': {
                    'arn': 'string',
                    'name': 'string',
                    'created': datetime(2015, 1, 1),
                    'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_NODE_TEST_PACKAGE'|'APPIUM_RUBY_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_NODE_TEST_PACKAGE'|'APPIUM_WEB_RUBY_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE'|'APPIUM_JAVA_JUNIT_TEST_SPEC'|'APPIUM_JAVA_TESTNG_TEST_SPEC'|'APPIUM_PYTHON_TEST_SPEC'|'APPIUM_NODE_TEST_SPEC'|'APPIUM_RUBY_TEST_SPEC'|'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC'|'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC'|'APPIUM_WEB_PYTHON_TEST_SPEC'|'APPIUM_WEB_NODE_TEST_SPEC'|'APPIUM_WEB_RUBY_TEST_SPEC'|'INSTRUMENTATION_TEST_SPEC'|'XCTEST_UI_TEST_SPEC',
                    'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
                    'url': 'string',
                    'metadata': 'string',
                    'contentType': 'string',
                    'message': 'string',
                    'category': 'CURATED'|'PRIVATE'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of a create upload request.
            - **upload** *(dict) --* 
              The newly created upload.
              - **arn** *(string) --* 
                The upload's ARN.
              - **name** *(string) --* 
                The upload's file name.
              - **created** *(datetime) --* 
                When the upload was created.
              - **type** *(string) --* 
                The upload's type.
                Must be one of the following values:
                * ANDROID_APP: An Android upload. 
                * IOS_APP: An iOS upload. 
                * WEB_APP: A web appliction upload. 
                * EXTERNAL_DATA: An external data upload. 
                * APPIUM_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload. 
                * APPIUM_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload. 
                * APPIUM_PYTHON_TEST_PACKAGE: An Appium Python test package upload. 
                * APPIUM_NODE_TEST_PACKAGE: An Appium Node.js test package upload. 
                * APPIUM_RUBY_TEST_PACKAGE: An Appium Ruby test package upload. 
                * APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload for web apps. 
                * APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload for web apps. 
                * APPIUM_WEB_PYTHON_TEST_PACKAGE: An Appium Python test package upload for web apps. 
                * APPIUM_WEB_NODE_TEST_PACKAGE: An Appium Node.js test package upload for web apps. 
                * APPIUM_WEB_RUBY_TEST_PACKAGE: An Appium Ruby test package upload for web apps. 
                * CALABASH_TEST_PACKAGE: A Calabash test package upload. 
                * INSTRUMENTATION_TEST_PACKAGE: An instrumentation upload. 
                * UIAUTOMATION_TEST_PACKAGE: A uiautomation test package upload. 
                * UIAUTOMATOR_TEST_PACKAGE: A uiautomator test package upload. 
                * XCTEST_TEST_PACKAGE: An XCode test package upload. 
                * XCTEST_UI_TEST_PACKAGE: An XCode UI test package upload. 
                * APPIUM_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload. 
                * APPIUM_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload. 
                * APPIUM_PYTHON_TEST_SPEC: An Appium Python test spec upload. 
                * APPIUM_NODE_TEST_SPEC: An Appium Node.js test spec upload. 
                * APPIUM_RUBY_TEST_SPEC: An Appium Ruby test spec upload. 
                * APPIUM_WEB_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload for a web app. 
                * APPIUM_WEB_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload for a web app. 
                * APPIUM_WEB_PYTHON_TEST_SPEC: An Appium Python test spec upload for a web app. 
                * APPIUM_WEB_NODE_TEST_SPEC: An Appium Node.js test spec upload for a web app. 
                * APPIUM_WEB_RUBY_TEST_SPEC: An Appium Ruby test spec upload for a web app. 
                * INSTRUMENTATION_TEST_SPEC: An instrumentation test spec upload. 
                * XCTEST_UI_TEST_SPEC: An XCode UI test spec upload. 
              - **status** *(string) --* 
                The upload's status.
                Must be one of the following values:
                * FAILED: A failed status. 
                * INITIALIZED: An initialized status. 
                * PROCESSING: A processing status. 
                * SUCCEEDED: A succeeded status. 
              - **url** *(string) --* 
                The pre-signed Amazon S3 URL that was used to store a file through a corresponding PUT request.
              - **metadata** *(string) --* 
                The upload's metadata. For example, for Android, this contains information that is parsed from the manifest and is displayed in the AWS Device Farm console after the associated app is uploaded.
              - **contentType** *(string) --* 
                The upload's content type (for example, "application/octet-stream").
              - **message** *(string) --* 
                A message about the upload's result.
              - **category** *(string) --* 
                The upload's category. Allowed values include:
                * CURATED: An upload managed by AWS Device Farm. 
                * PRIVATE: An upload managed by the AWS Device Farm customer. 
        :type projectArn: string
        :param projectArn: **[REQUIRED]**
          The ARN of the project for the upload.
        :type name: string
        :param name: **[REQUIRED]**
          The upload\'s file name. The name should not contain the \'/\' character. If uploading an iOS app, the file name needs to end with the ``.ipa`` extension. If uploading an Android app, the file name needs to end with the ``.apk`` extension. For all others, the file name must end with the ``.zip`` file extension.
        :type type: string
        :param type: **[REQUIRED]**
          The upload\'s upload type.
          Must be one of the following values:
          * ANDROID_APP: An Android upload.
          * IOS_APP: An iOS upload.
          * WEB_APP: A web application upload.
          * EXTERNAL_DATA: An external data upload.
          * APPIUM_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload.
          * APPIUM_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload.
          * APPIUM_PYTHON_TEST_PACKAGE: An Appium Python test package upload.
          * APPIUM_NODE_TEST_PACKAGE: An Appium Node.js test package upload.
          * APPIUM_RUBY_TEST_PACKAGE: An Appium Ruby test package upload.
          * APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload for a web app.
          * APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload for a web app.
          * APPIUM_WEB_PYTHON_TEST_PACKAGE: An Appium Python test package upload for a web app.
          * APPIUM_WEB_NODE_TEST_PACKAGE: An Appium Node.js test package upload for a web app.
          * APPIUM_WEB_RUBY_TEST_PACKAGE: An Appium Ruby test package upload for a web app.
          * CALABASH_TEST_PACKAGE: A Calabash test package upload.
          * INSTRUMENTATION_TEST_PACKAGE: An instrumentation upload.
          * UIAUTOMATION_TEST_PACKAGE: A uiautomation test package upload.
          * UIAUTOMATOR_TEST_PACKAGE: A uiautomator test package upload.
          * XCTEST_TEST_PACKAGE: An XCode test package upload.
          * XCTEST_UI_TEST_PACKAGE: An XCode UI test package upload.
          * APPIUM_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload.
          * APPIUM_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload.
          * APPIUM_PYTHON_TEST_SPEC: An Appium Python test spec upload.
          * APPIUM_NODE_TEST_SPEC: An Appium Node.js test spec upload.
          * APPIUM_RUBY_TEST_SPEC: An Appium Ruby test spec upload.
          * APPIUM_WEB_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload for a web app.
          * APPIUM_WEB_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload for a web app.
          * APPIUM_WEB_PYTHON_TEST_SPEC: An Appium Python test spec upload for a web app.
          * APPIUM_WEB_NODE_TEST_SPEC: An Appium Node.js test spec upload for a web app.
          * APPIUM_WEB_RUBY_TEST_SPEC: An Appium Ruby test spec upload for a web app.
          * INSTRUMENTATION_TEST_SPEC: An instrumentation test spec upload.
          * XCTEST_UI_TEST_SPEC: An XCode UI test spec upload.
           **Note** If you call ``CreateUpload`` with ``WEB_APP`` specified, AWS Device Farm throws an ``ArgumentException`` error.
        :type contentType: string
        :param contentType:
          The upload\'s content type (for example, \"application/octet-stream\").
        :rtype: dict
        :returns:
        """
        pass

    def create_vpce_configuration(self, vpceConfigurationName: str, vpceServiceName: str, serviceDnsName: str, vpceConfigurationDescription: str = None) -> Dict:
        """
        Creates a configuration record in Device Farm for your Amazon Virtual Private Cloud (VPC) endpoint.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/CreateVPCEConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.create_vpce_configuration(
              vpceConfigurationName='string',
              vpceServiceName='string',
              serviceDnsName='string',
              vpceConfigurationDescription='string'
          )
        
        **Response Syntax**
        ::
            {
                'vpceConfiguration': {
                    'arn': 'string',
                    'vpceConfigurationName': 'string',
                    'vpceServiceName': 'string',
                    'serviceDnsName': 'string',
                    'vpceConfigurationDescription': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **vpceConfiguration** *(dict) --* 
              An object containing information about your VPC endpoint configuration.
              - **arn** *(string) --* 
                The Amazon Resource Name (ARN) of the VPC endpoint configuration.
              - **vpceConfigurationName** *(string) --* 
                The friendly name you give to your VPC endpoint configuration, to manage your configurations more easily.
              - **vpceServiceName** *(string) --* 
                The name of the VPC endpoint service running inside your AWS account that you want Device Farm to test.
              - **serviceDnsName** *(string) --* 
                The DNS name that maps to the private IP address of the service you want to access.
              - **vpceConfigurationDescription** *(string) --* 
                An optional description, providing more details about your VPC endpoint configuration.
        :type vpceConfigurationName: string
        :param vpceConfigurationName: **[REQUIRED]**
          The friendly name you give to your VPC endpoint configuration, to manage your configurations more easily.
        :type vpceServiceName: string
        :param vpceServiceName: **[REQUIRED]**
          The name of the VPC endpoint service running inside your AWS account that you want Device Farm to test.
        :type serviceDnsName: string
        :param serviceDnsName: **[REQUIRED]**
          The DNS name of the service running in your VPC that you want Device Farm to test.
        :type vpceConfigurationDescription: string
        :param vpceConfigurationDescription:
          An optional description, providing more details about your VPC endpoint configuration.
        :rtype: dict
        :returns:
        """
        pass

    def delete_device_pool(self, arn: str) -> Dict:
        """
        Deletes a device pool given the pool ARN. Does not allow deletion of curated pools owned by the system.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/DeleteDevicePool>`_
        
        **Request Syntax**
        ::
          response = client.delete_device_pool(
              arn='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of a delete device pool request.
        :type arn: string
        :param arn: **[REQUIRED]**
          Represents the Amazon Resource Name (ARN) of the Device Farm device pool you wish to delete.
        :rtype: dict
        :returns:
        """
        pass

    def delete_instance_profile(self, arn: str) -> Dict:
        """
        Deletes a profile that can be applied to one or more private device instances.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/DeleteInstanceProfile>`_
        
        **Request Syntax**
        ::
          response = client.delete_instance_profile(
              arn='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type arn: string
        :param arn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the instance profile you are requesting to delete.
        :rtype: dict
        :returns:
        """
        pass

    def delete_network_profile(self, arn: str) -> Dict:
        """
        Deletes a network profile.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/DeleteNetworkProfile>`_
        
        **Request Syntax**
        ::
          response = client.delete_network_profile(
              arn='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type arn: string
        :param arn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the network profile you want to delete.
        :rtype: dict
        :returns:
        """
        pass

    def delete_project(self, arn: str) -> Dict:
        """
        Deletes an AWS Device Farm project, given the project ARN.
         **Note** Deleting this resource does not stop an in-progress run.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/DeleteProject>`_
        
        **Request Syntax**
        ::
          response = client.delete_project(
              arn='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of a delete project request.
        :type arn: string
        :param arn: **[REQUIRED]**
          Represents the Amazon Resource Name (ARN) of the Device Farm project you wish to delete.
        :rtype: dict
        :returns:
        """
        pass

    def delete_remote_access_session(self, arn: str) -> Dict:
        """
        Deletes a completed remote access session and its results.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/DeleteRemoteAccessSession>`_
        
        **Request Syntax**
        ::
          response = client.delete_remote_access_session(
              arn='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            The response from the server when a request is made to delete the remote access session.
        :type arn: string
        :param arn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the sesssion for which you want to delete remote access.
        :rtype: dict
        :returns:
        """
        pass

    def delete_run(self, arn: str) -> Dict:
        """
        Deletes the run, given the run ARN.
         **Note** Deleting this resource does not stop an in-progress run.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/DeleteRun>`_
        
        **Request Syntax**
        ::
          response = client.delete_run(
              arn='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of a delete run request.
        :type arn: string
        :param arn: **[REQUIRED]**
          The Amazon Resource Name (ARN) for the run you wish to delete.
        :rtype: dict
        :returns:
        """
        pass

    def delete_upload(self, arn: str) -> Dict:
        """
        Deletes an upload given the upload ARN.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/DeleteUpload>`_
        
        **Request Syntax**
        ::
          response = client.delete_upload(
              arn='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of a delete upload request.
        :type arn: string
        :param arn: **[REQUIRED]**
          Represents the Amazon Resource Name (ARN) of the Device Farm upload you wish to delete.
        :rtype: dict
        :returns:
        """
        pass

    def delete_vpce_configuration(self, arn: str) -> Dict:
        """
        Deletes a configuration for your Amazon Virtual Private Cloud (VPC) endpoint.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/DeleteVPCEConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.delete_vpce_configuration(
              arn='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type arn: string
        :param arn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the VPC endpoint configuration you want to delete.
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

    def get_account_settings(self) -> Dict:
        """
        Returns the number of unmetered iOS and/or unmetered Android devices that have been purchased by the account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetAccountSettings>`_
        
        **Request Syntax**
        ::
          response = client.get_account_settings()
        
        **Response Syntax**
        ::
            {
                'accountSettings': {
                    'awsAccountNumber': 'string',
                    'unmeteredDevices': {
                        'string': 123
                    },
                    'unmeteredRemoteAccessDevices': {
                        'string': 123
                    },
                    'maxJobTimeoutMinutes': 123,
                    'trialMinutes': {
                        'total': 123.0,
                        'remaining': 123.0
                    },
                    'maxSlots': {
                        'string': 123
                    },
                    'defaultJobTimeoutMinutes': 123,
                    'skipAppResign': True|False
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the account settings return values from the ``GetAccountSettings`` request.
            - **accountSettings** *(dict) --* 
              The account settings.
              - **awsAccountNumber** *(string) --* 
                The AWS account number specified in the ``AccountSettings`` container.
              - **unmeteredDevices** *(dict) --* 
                Returns the unmetered devices you have purchased or want to purchase.
                - *(string) --* 
                  - *(integer) --* 
              - **unmeteredRemoteAccessDevices** *(dict) --* 
                Returns the unmetered remote access devices you have purchased or want to purchase.
                - *(string) --* 
                  - *(integer) --* 
              - **maxJobTimeoutMinutes** *(integer) --* 
                The maximum number of minutes a test run will execute before it times out.
              - **trialMinutes** *(dict) --* 
                Information about an AWS account's usage of free trial device minutes.
                - **total** *(float) --* 
                  The total number of free trial minutes that the account started with.
                - **remaining** *(float) --* 
                  The number of free trial minutes remaining in the account.
              - **maxSlots** *(dict) --* 
                The maximum number of device slots that the AWS account can purchase. Each maximum is expressed as an ``offering-id:number`` pair, where the ``offering-id`` represents one of the IDs returned by the ``ListOfferings`` command.
                - *(string) --* 
                  - *(integer) --* 
              - **defaultJobTimeoutMinutes** *(integer) --* 
                The default number of minutes (at the account level) a test run will execute before it times out. Default value is 60 minutes.
              - **skipAppResign** *(boolean) --* 
                When set to ``true`` , for private devices, Device Farm will not sign your app again. For public devices, Device Farm always signs your apps again and this parameter has no effect.
                For more information about how Device Farm re-signs your app(s), see `Do you modify my app? <https://aws.amazon.com/device-farm/faq/>`__ in the *AWS Device Farm FAQs* .
        :rtype: dict
        :returns:
        """
        pass

    def get_device(self, arn: str) -> Dict:
        """
        Gets information about a unique device type.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetDevice>`_
        
        **Request Syntax**
        ::
          response = client.get_device(
              arn='string'
          )
        
        **Response Syntax**
        ::
            {
                'device': {
                    'arn': 'string',
                    'name': 'string',
                    'manufacturer': 'string',
                    'model': 'string',
                    'modelId': 'string',
                    'formFactor': 'PHONE'|'TABLET',
                    'platform': 'ANDROID'|'IOS',
                    'os': 'string',
                    'cpu': {
                        'frequency': 'string',
                        'architecture': 'string',
                        'clock': 123.0
                    },
                    'resolution': {
                        'width': 123,
                        'height': 123
                    },
                    'heapSize': 123,
                    'memory': 123,
                    'image': 'string',
                    'carrier': 'string',
                    'radio': 'string',
                    'remoteAccessEnabled': True|False,
                    'remoteDebugEnabled': True|False,
                    'fleetType': 'string',
                    'fleetName': 'string',
                    'instances': [
                        {
                            'arn': 'string',
                            'deviceArn': 'string',
                            'labels': [
                                'string',
                            ],
                            'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                            'udid': 'string',
                            'instanceProfile': {
                                'arn': 'string',
                                'packageCleanup': True|False,
                                'excludeAppPackagesFromCleanup': [
                                    'string',
                                ],
                                'rebootAfterUse': True|False,
                                'name': 'string',
                                'description': 'string'
                            }
                        },
                    ],
                    'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of a get device request.
            - **device** *(dict) --* 
              An object containing information about the requested device.
              - **arn** *(string) --* 
                The device's ARN.
              - **name** *(string) --* 
                The device's display name.
              - **manufacturer** *(string) --* 
                The device's manufacturer name.
              - **model** *(string) --* 
                The device's model name.
              - **modelId** *(string) --* 
                The device's model ID.
              - **formFactor** *(string) --* 
                The device's form factor.
                Allowed values include:
                * PHONE: The phone form factor. 
                * TABLET: The tablet form factor. 
              - **platform** *(string) --* 
                The device's platform.
                Allowed values include:
                * ANDROID: The Android platform. 
                * IOS: The iOS platform. 
              - **os** *(string) --* 
                The device's operating system type.
              - **cpu** *(dict) --* 
                Information about the device's CPU.
                - **frequency** *(string) --* 
                  The CPU's frequency.
                - **architecture** *(string) --* 
                  The CPU's architecture, for example x86 or ARM.
                - **clock** *(float) --* 
                  The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.
              - **resolution** *(dict) --* 
                The resolution of the device.
                - **width** *(integer) --* 
                  The screen resolution's width, expressed in pixels.
                - **height** *(integer) --* 
                  The screen resolution's height, expressed in pixels.
              - **heapSize** *(integer) --* 
                The device's heap size, expressed in bytes.
              - **memory** *(integer) --* 
                The device's total memory size, expressed in bytes.
              - **image** *(string) --* 
                The device's image name.
              - **carrier** *(string) --* 
                The device's carrier.
              - **radio** *(string) --* 
                The device's radio.
              - **remoteAccessEnabled** *(boolean) --* 
                Specifies whether remote access has been enabled for the specified device.
              - **remoteDebugEnabled** *(boolean) --* 
                This flag is set to ``true`` if remote debugging is enabled for the device.
              - **fleetType** *(string) --* 
                The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.
              - **fleetName** *(string) --* 
                The name of the fleet to which this device belongs.
              - **instances** *(list) --* 
                The instances belonging to this device.
                - *(dict) --* 
                  Represents the device instance.
                  - **arn** *(string) --* 
                    The Amazon Resource Name (ARN) of the device instance.
                  - **deviceArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the device.
                  - **labels** *(list) --* 
                    An array of strings describing the device instance.
                    - *(string) --* 
                  - **status** *(string) --* 
                    The status of the device instance. Valid values are listed below.
                  - **udid** *(string) --* 
                    Unique device identifier for the device instance.
                  - **instanceProfile** *(dict) --* 
                    A object containing information about the instance profile.
                    - **arn** *(string) --* 
                      The Amazon Resource Name (ARN) of the instance profile.
                    - **packageCleanup** *(boolean) --* 
                      When set to ``true`` , Device Farm will remove app packages after a test run. The default value is ``false`` for private devices.
                    - **excludeAppPackagesFromCleanup** *(list) --* 
                      An array of strings specifying the list of app packages that should not be cleaned up from the device after a test run is over.
                      The list of packages is only considered if you set ``packageCleanup`` to ``true`` .
                      - *(string) --* 
                    - **rebootAfterUse** *(boolean) --* 
                      When set to ``true`` , Device Farm will reboot the instance after a test run. The default value is ``true`` .
                    - **name** *(string) --* 
                      The name of the instance profile.
                    - **description** *(string) --* 
                      The description of the instance profile.
              - **availability** *(string) --* 
                Reflects how likely a device will be available for a test run. It is currently available in the ListDevices and GetDevice API methods.
        :type arn: string
        :param arn: **[REQUIRED]**
          The device type\'s ARN.
        :rtype: dict
        :returns:
        """
        pass

    def get_device_instance(self, arn: str) -> Dict:
        """
        Returns information about a device instance belonging to a private device fleet.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetDeviceInstance>`_
        
        **Request Syntax**
        ::
          response = client.get_device_instance(
              arn='string'
          )
        
        **Response Syntax**
        ::
            {
                'deviceInstance': {
                    'arn': 'string',
                    'deviceArn': 'string',
                    'labels': [
                        'string',
                    ],
                    'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                    'udid': 'string',
                    'instanceProfile': {
                        'arn': 'string',
                        'packageCleanup': True|False,
                        'excludeAppPackagesFromCleanup': [
                            'string',
                        ],
                        'rebootAfterUse': True|False,
                        'name': 'string',
                        'description': 'string'
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **deviceInstance** *(dict) --* 
              An object containing information about your device instance.
              - **arn** *(string) --* 
                The Amazon Resource Name (ARN) of the device instance.
              - **deviceArn** *(string) --* 
                The Amazon Resource Name (ARN) of the device.
              - **labels** *(list) --* 
                An array of strings describing the device instance.
                - *(string) --* 
              - **status** *(string) --* 
                The status of the device instance. Valid values are listed below.
              - **udid** *(string) --* 
                Unique device identifier for the device instance.
              - **instanceProfile** *(dict) --* 
                A object containing information about the instance profile.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the instance profile.
                - **packageCleanup** *(boolean) --* 
                  When set to ``true`` , Device Farm will remove app packages after a test run. The default value is ``false`` for private devices.
                - **excludeAppPackagesFromCleanup** *(list) --* 
                  An array of strings specifying the list of app packages that should not be cleaned up from the device after a test run is over.
                  The list of packages is only considered if you set ``packageCleanup`` to ``true`` .
                  - *(string) --* 
                - **rebootAfterUse** *(boolean) --* 
                  When set to ``true`` , Device Farm will reboot the instance after a test run. The default value is ``true`` .
                - **name** *(string) --* 
                  The name of the instance profile.
                - **description** *(string) --* 
                  The description of the instance profile.
        :type arn: string
        :param arn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the instance you\'re requesting information about.
        :rtype: dict
        :returns:
        """
        pass

    def get_device_pool(self, arn: str) -> Dict:
        """
        Gets information about a device pool.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetDevicePool>`_
        
        **Request Syntax**
        ::
          response = client.get_device_pool(
              arn='string'
          )
        
        **Response Syntax**
        ::
            {
                'devicePool': {
                    'arn': 'string',
                    'name': 'string',
                    'description': 'string',
                    'type': 'CURATED'|'PRIVATE',
                    'rules': [
                        {
                            'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE'|'OS_VERSION'|'MODEL'|'AVAILABILITY',
                            'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                            'value': 'string'
                        },
                    ],
                    'maxDevices': 123
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of a get device pool request.
            - **devicePool** *(dict) --* 
              An object containing information about the requested device pool.
              - **arn** *(string) --* 
                The device pool's ARN.
              - **name** *(string) --* 
                The device pool's name.
              - **description** *(string) --* 
                The device pool's description.
              - **type** *(string) --* 
                The device pool's type.
                Allowed values include:
                * CURATED: A device pool that is created and managed by AWS Device Farm. 
                * PRIVATE: A device pool that is created and managed by the device pool developer. 
              - **rules** *(list) --* 
                Information about the device pool's rules.
                - *(dict) --* 
                  Represents a condition for a device pool.
                  - **attribute** *(string) --* 
                    The rule's stringified attribute. For example, specify the value as ``"\"abc\""`` .
                    The supported operators for each attribute are provided in the following list.
                      APPIUM_VERSION  
                    The Appium version for the test.
                     *Supported operators* : ``CONTAINS``  
                      ARN  
                    The Amazon Resource Name (ARN) of the device. For example, "arn:aws:devicefarm:us-west-2::device:12345Example".
                     *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                      AVAILABILITY  
                    The current availability of the device. Valid values are "AVAILABLE", "HIGHLY_AVAILABLE", "BUSY", or "TEMPORARY_NOT_AVAILABLE".
                     *Supported operators* : ``EQUALS``  
                      FLEET_TYPE  
                    The fleet type. Valid values are "PUBLIC" or "PRIVATE".
                     *Supported operators* : ``EQUALS``  
                      FORM_FACTOR  
                    The device form factor. Valid values are "PHONE" or "TABLET".
                     *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                      INSTANCE_ARN  
                    The Amazon Resource Name (ARN) of the device instance.
                     *Supported operators* : ``IN`` , ``NOT_IN``  
                      INSTANCE_LABELS  
                    The label of the device instance.
                     *Supported operators* : ``CONTAINS``  
                      MANUFACTURER  
                    The device manufacturer. For example, "Apple".
                     *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                      MODEL  
                    The device model, such as "Apple iPad Air 2" or "Google Pixel".
                     *Supported operators* : ``CONTAINS`` , ``EQUALS`` , ``IN`` , ``NOT_IN``  
                      OS_VERSION  
                    The operating system version. For example, "10.3.2".
                     *Supported operators* : ``EQUALS`` , ``GREATER_THAN`` , ``GREATER_THAN_OR_EQUALS`` , ``IN`` , ``LESS_THAN`` , ``LESS_THAN_OR_EQUALS`` , ``NOT_IN``  
                      PLATFORM  
                    The device platform. Valid values are "ANDROID" or "IOS".
                     *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                      REMOTE_ACCESS_ENABLED  
                    Whether the device is enabled for remote access. Valid values are "TRUE" or "FALSE".
                     *Supported operators* : ``EQUALS``  
                      REMOTE_DEBUG_ENABLED  
                    Whether the device is enabled for remote debugging. Valid values are "TRUE" or "FALSE".
                     *Supported operators* : ``EQUALS``  
                  - **operator** *(string) --* 
                    Specifies how Device Farm compares the rule's attribute to the value. For the operators that are supported by each attribute, see the attribute descriptions.
                  - **value** *(string) --* 
                    The rule's value.
              - **maxDevices** *(integer) --* 
                The number of devices that Device Farm can add to your device pool. Device Farm adds devices that are available and that meet the criteria that you assign for the ``rules`` parameter. Depending on how many devices meet these constraints, your device pool might contain fewer devices than the value for this parameter.
                By specifying the maximum number of devices, you can control the costs that you incur by running tests.
        :type arn: string
        :param arn: **[REQUIRED]**
          The device pool\'s ARN.
        :rtype: dict
        :returns:
        """
        pass

    def get_device_pool_compatibility(self, devicePoolArn: str, appArn: str = None, testType: str = None, test: Dict = None, configuration: Dict = None) -> Dict:
        """
        Gets information about compatibility with a device pool.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetDevicePoolCompatibility>`_
        
        **Request Syntax**
        ::
          response = client.get_device_pool_compatibility(
              devicePoolArn='string',
              appArn='string',
              testType='BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
              test={
                  'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
                  'testPackageArn': 'string',
                  'testSpecArn': 'string',
                  'filter': 'string',
                  'parameters': {
                      'string': 'string'
                  }
              },
              configuration={
                  'extraDataPackageArn': 'string',
                  'networkProfileArn': 'string',
                  'locale': 'string',
                  'location': {
                      'latitude': 123.0,
                      'longitude': 123.0
                  },
                  'vpceConfigurationArns': [
                      'string',
                  ],
                  'customerArtifactPaths': {
                      'iosPaths': [
                          'string',
                      ],
                      'androidPaths': [
                          'string',
                      ],
                      'deviceHostPaths': [
                          'string',
                      ]
                  },
                  'radios': {
                      'wifi': True|False,
                      'bluetooth': True|False,
                      'nfc': True|False,
                      'gps': True|False
                  },
                  'auxiliaryApps': [
                      'string',
                  ],
                  'billingMethod': 'METERED'|'UNMETERED'
              }
          )
        
        **Response Syntax**
        ::
            {
                'compatibleDevices': [
                    {
                        'device': {
                            'arn': 'string',
                            'name': 'string',
                            'manufacturer': 'string',
                            'model': 'string',
                            'modelId': 'string',
                            'formFactor': 'PHONE'|'TABLET',
                            'platform': 'ANDROID'|'IOS',
                            'os': 'string',
                            'cpu': {
                                'frequency': 'string',
                                'architecture': 'string',
                                'clock': 123.0
                            },
                            'resolution': {
                                'width': 123,
                                'height': 123
                            },
                            'heapSize': 123,
                            'memory': 123,
                            'image': 'string',
                            'carrier': 'string',
                            'radio': 'string',
                            'remoteAccessEnabled': True|False,
                            'remoteDebugEnabled': True|False,
                            'fleetType': 'string',
                            'fleetName': 'string',
                            'instances': [
                                {
                                    'arn': 'string',
                                    'deviceArn': 'string',
                                    'labels': [
                                        'string',
                                    ],
                                    'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                                    'udid': 'string',
                                    'instanceProfile': {
                                        'arn': 'string',
                                        'packageCleanup': True|False,
                                        'excludeAppPackagesFromCleanup': [
                                            'string',
                                        ],
                                        'rebootAfterUse': True|False,
                                        'name': 'string',
                                        'description': 'string'
                                    }
                                },
                            ],
                            'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
                        },
                        'compatible': True|False,
                        'incompatibilityMessages': [
                            {
                                'message': 'string',
                                'type': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE'|'OS_VERSION'|'MODEL'|'AVAILABILITY'
                            },
                        ]
                    },
                ],
                'incompatibleDevices': [
                    {
                        'device': {
                            'arn': 'string',
                            'name': 'string',
                            'manufacturer': 'string',
                            'model': 'string',
                            'modelId': 'string',
                            'formFactor': 'PHONE'|'TABLET',
                            'platform': 'ANDROID'|'IOS',
                            'os': 'string',
                            'cpu': {
                                'frequency': 'string',
                                'architecture': 'string',
                                'clock': 123.0
                            },
                            'resolution': {
                                'width': 123,
                                'height': 123
                            },
                            'heapSize': 123,
                            'memory': 123,
                            'image': 'string',
                            'carrier': 'string',
                            'radio': 'string',
                            'remoteAccessEnabled': True|False,
                            'remoteDebugEnabled': True|False,
                            'fleetType': 'string',
                            'fleetName': 'string',
                            'instances': [
                                {
                                    'arn': 'string',
                                    'deviceArn': 'string',
                                    'labels': [
                                        'string',
                                    ],
                                    'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                                    'udid': 'string',
                                    'instanceProfile': {
                                        'arn': 'string',
                                        'packageCleanup': True|False,
                                        'excludeAppPackagesFromCleanup': [
                                            'string',
                                        ],
                                        'rebootAfterUse': True|False,
                                        'name': 'string',
                                        'description': 'string'
                                    }
                                },
                            ],
                            'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
                        },
                        'compatible': True|False,
                        'incompatibilityMessages': [
                            {
                                'message': 'string',
                                'type': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE'|'OS_VERSION'|'MODEL'|'AVAILABILITY'
                            },
                        ]
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of describe device pool compatibility request.
            - **compatibleDevices** *(list) --* 
              Information about compatible devices.
              - *(dict) --* 
                Represents a device pool compatibility result.
                - **device** *(dict) --* 
                  The device (phone or tablet) that you wish to return information about.
                  - **arn** *(string) --* 
                    The device's ARN.
                  - **name** *(string) --* 
                    The device's display name.
                  - **manufacturer** *(string) --* 
                    The device's manufacturer name.
                  - **model** *(string) --* 
                    The device's model name.
                  - **modelId** *(string) --* 
                    The device's model ID.
                  - **formFactor** *(string) --* 
                    The device's form factor.
                    Allowed values include:
                    * PHONE: The phone form factor. 
                    * TABLET: The tablet form factor. 
                  - **platform** *(string) --* 
                    The device's platform.
                    Allowed values include:
                    * ANDROID: The Android platform. 
                    * IOS: The iOS platform. 
                  - **os** *(string) --* 
                    The device's operating system type.
                  - **cpu** *(dict) --* 
                    Information about the device's CPU.
                    - **frequency** *(string) --* 
                      The CPU's frequency.
                    - **architecture** *(string) --* 
                      The CPU's architecture, for example x86 or ARM.
                    - **clock** *(float) --* 
                      The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.
                  - **resolution** *(dict) --* 
                    The resolution of the device.
                    - **width** *(integer) --* 
                      The screen resolution's width, expressed in pixels.
                    - **height** *(integer) --* 
                      The screen resolution's height, expressed in pixels.
                  - **heapSize** *(integer) --* 
                    The device's heap size, expressed in bytes.
                  - **memory** *(integer) --* 
                    The device's total memory size, expressed in bytes.
                  - **image** *(string) --* 
                    The device's image name.
                  - **carrier** *(string) --* 
                    The device's carrier.
                  - **radio** *(string) --* 
                    The device's radio.
                  - **remoteAccessEnabled** *(boolean) --* 
                    Specifies whether remote access has been enabled for the specified device.
                  - **remoteDebugEnabled** *(boolean) --* 
                    This flag is set to ``true`` if remote debugging is enabled for the device.
                  - **fleetType** *(string) --* 
                    The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.
                  - **fleetName** *(string) --* 
                    The name of the fleet to which this device belongs.
                  - **instances** *(list) --* 
                    The instances belonging to this device.
                    - *(dict) --* 
                      Represents the device instance.
                      - **arn** *(string) --* 
                        The Amazon Resource Name (ARN) of the device instance.
                      - **deviceArn** *(string) --* 
                        The Amazon Resource Name (ARN) of the device.
                      - **labels** *(list) --* 
                        An array of strings describing the device instance.
                        - *(string) --* 
                      - **status** *(string) --* 
                        The status of the device instance. Valid values are listed below.
                      - **udid** *(string) --* 
                        Unique device identifier for the device instance.
                      - **instanceProfile** *(dict) --* 
                        A object containing information about the instance profile.
                        - **arn** *(string) --* 
                          The Amazon Resource Name (ARN) of the instance profile.
                        - **packageCleanup** *(boolean) --* 
                          When set to ``true`` , Device Farm will remove app packages after a test run. The default value is ``false`` for private devices.
                        - **excludeAppPackagesFromCleanup** *(list) --* 
                          An array of strings specifying the list of app packages that should not be cleaned up from the device after a test run is over.
                          The list of packages is only considered if you set ``packageCleanup`` to ``true`` .
                          - *(string) --* 
                        - **rebootAfterUse** *(boolean) --* 
                          When set to ``true`` , Device Farm will reboot the instance after a test run. The default value is ``true`` .
                        - **name** *(string) --* 
                          The name of the instance profile.
                        - **description** *(string) --* 
                          The description of the instance profile.
                  - **availability** *(string) --* 
                    Reflects how likely a device will be available for a test run. It is currently available in the ListDevices and GetDevice API methods.
                - **compatible** *(boolean) --* 
                  Whether the result was compatible with the device pool.
                - **incompatibilityMessages** *(list) --* 
                  Information about the compatibility.
                  - *(dict) --* 
                    Represents information about incompatibility.
                    - **message** *(string) --* 
                      A message about the incompatibility.
                    - **type** *(string) --* 
                      The type of incompatibility.
                      Allowed values include:
                      * ARN: The ARN. 
                      * FORM_FACTOR: The form factor (for example, phone or tablet). 
                      * MANUFACTURER: The manufacturer. 
                      * PLATFORM: The platform (for example, Android or iOS). 
                      * REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. 
                      * APPIUM_VERSION: The Appium version for the test. 
            - **incompatibleDevices** *(list) --* 
              Information about incompatible devices.
              - *(dict) --* 
                Represents a device pool compatibility result.
                - **device** *(dict) --* 
                  The device (phone or tablet) that you wish to return information about.
                  - **arn** *(string) --* 
                    The device's ARN.
                  - **name** *(string) --* 
                    The device's display name.
                  - **manufacturer** *(string) --* 
                    The device's manufacturer name.
                  - **model** *(string) --* 
                    The device's model name.
                  - **modelId** *(string) --* 
                    The device's model ID.
                  - **formFactor** *(string) --* 
                    The device's form factor.
                    Allowed values include:
                    * PHONE: The phone form factor. 
                    * TABLET: The tablet form factor. 
                  - **platform** *(string) --* 
                    The device's platform.
                    Allowed values include:
                    * ANDROID: The Android platform. 
                    * IOS: The iOS platform. 
                  - **os** *(string) --* 
                    The device's operating system type.
                  - **cpu** *(dict) --* 
                    Information about the device's CPU.
                    - **frequency** *(string) --* 
                      The CPU's frequency.
                    - **architecture** *(string) --* 
                      The CPU's architecture, for example x86 or ARM.
                    - **clock** *(float) --* 
                      The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.
                  - **resolution** *(dict) --* 
                    The resolution of the device.
                    - **width** *(integer) --* 
                      The screen resolution's width, expressed in pixels.
                    - **height** *(integer) --* 
                      The screen resolution's height, expressed in pixels.
                  - **heapSize** *(integer) --* 
                    The device's heap size, expressed in bytes.
                  - **memory** *(integer) --* 
                    The device's total memory size, expressed in bytes.
                  - **image** *(string) --* 
                    The device's image name.
                  - **carrier** *(string) --* 
                    The device's carrier.
                  - **radio** *(string) --* 
                    The device's radio.
                  - **remoteAccessEnabled** *(boolean) --* 
                    Specifies whether remote access has been enabled for the specified device.
                  - **remoteDebugEnabled** *(boolean) --* 
                    This flag is set to ``true`` if remote debugging is enabled for the device.
                  - **fleetType** *(string) --* 
                    The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.
                  - **fleetName** *(string) --* 
                    The name of the fleet to which this device belongs.
                  - **instances** *(list) --* 
                    The instances belonging to this device.
                    - *(dict) --* 
                      Represents the device instance.
                      - **arn** *(string) --* 
                        The Amazon Resource Name (ARN) of the device instance.
                      - **deviceArn** *(string) --* 
                        The Amazon Resource Name (ARN) of the device.
                      - **labels** *(list) --* 
                        An array of strings describing the device instance.
                        - *(string) --* 
                      - **status** *(string) --* 
                        The status of the device instance. Valid values are listed below.
                      - **udid** *(string) --* 
                        Unique device identifier for the device instance.
                      - **instanceProfile** *(dict) --* 
                        A object containing information about the instance profile.
                        - **arn** *(string) --* 
                          The Amazon Resource Name (ARN) of the instance profile.
                        - **packageCleanup** *(boolean) --* 
                          When set to ``true`` , Device Farm will remove app packages after a test run. The default value is ``false`` for private devices.
                        - **excludeAppPackagesFromCleanup** *(list) --* 
                          An array of strings specifying the list of app packages that should not be cleaned up from the device after a test run is over.
                          The list of packages is only considered if you set ``packageCleanup`` to ``true`` .
                          - *(string) --* 
                        - **rebootAfterUse** *(boolean) --* 
                          When set to ``true`` , Device Farm will reboot the instance after a test run. The default value is ``true`` .
                        - **name** *(string) --* 
                          The name of the instance profile.
                        - **description** *(string) --* 
                          The description of the instance profile.
                  - **availability** *(string) --* 
                    Reflects how likely a device will be available for a test run. It is currently available in the ListDevices and GetDevice API methods.
                - **compatible** *(boolean) --* 
                  Whether the result was compatible with the device pool.
                - **incompatibilityMessages** *(list) --* 
                  Information about the compatibility.
                  - *(dict) --* 
                    Represents information about incompatibility.
                    - **message** *(string) --* 
                      A message about the incompatibility.
                    - **type** *(string) --* 
                      The type of incompatibility.
                      Allowed values include:
                      * ARN: The ARN. 
                      * FORM_FACTOR: The form factor (for example, phone or tablet). 
                      * MANUFACTURER: The manufacturer. 
                      * PLATFORM: The platform (for example, Android or iOS). 
                      * REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. 
                      * APPIUM_VERSION: The Appium version for the test. 
        :type devicePoolArn: string
        :param devicePoolArn: **[REQUIRED]**
          The device pool\'s ARN.
        :type appArn: string
        :param appArn:
          The ARN of the app that is associated with the specified device pool.
        :type testType: string
        :param testType:
          The test type for the specified device pool.
          Allowed values include the following:
          * BUILTIN_FUZZ: The built-in fuzz type.
          * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time.
          * APPIUM_JAVA_JUNIT: The Appium Java JUnit type.
          * APPIUM_JAVA_TESTNG: The Appium Java TestNG type.
          * APPIUM_PYTHON: The Appium Python type.
          * APPIUM_NODE: The Appium Node.js type.
          * APPIUM_RUBY: The Appium Ruby type.
          * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for web apps.
          * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for web apps.
          * APPIUM_WEB_PYTHON: The Appium Python type for web apps.
          * APPIUM_WEB_NODE: The Appium Node.js type for web apps.
          * APPIUM_WEB_RUBY: The Appium Ruby type for web apps.
          * CALABASH: The Calabash type.
          * INSTRUMENTATION: The Instrumentation type.
          * UIAUTOMATION: The uiautomation type.
          * UIAUTOMATOR: The uiautomator type.
          * XCTEST: The XCode test type.
          * XCTEST_UI: The XCode UI test type.
        :type test: dict
        :param test:
          Information about the uploaded test to be run against the device pool.
          - **type** *(string) --* **[REQUIRED]**
            The test\'s type.
            Must be one of the following values:
            * BUILTIN_FUZZ: The built-in fuzz type.
            * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time.
            * APPIUM_JAVA_JUNIT: The Appium Java JUnit type.
            * APPIUM_JAVA_TESTNG: The Appium Java TestNG type.
            * APPIUM_PYTHON: The Appium Python type.
            * APPIUM_NODE: The Appium Node.js type.
            * APPIUM_RUBY: The Appium Ruby type.
            * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for web apps.
            * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for web apps.
            * APPIUM_WEB_PYTHON: The Appium Python type for web apps.
            * APPIUM_WEB_NODE: The Appium Node.js type for web apps.
            * APPIUM_WEB_RUBY: The Appium Ruby type for web apps.
            * CALABASH: The Calabash type.
            * INSTRUMENTATION: The Instrumentation type.
            * UIAUTOMATION: The uiautomation type.
            * UIAUTOMATOR: The uiautomator type.
            * XCTEST: The XCode test type.
            * XCTEST_UI: The XCode UI test type.
          - **testPackageArn** *(string) --*
            The ARN of the uploaded test that will be run.
          - **testSpecArn** *(string) --*
            The ARN of the YAML-formatted test specification.
          - **filter** *(string) --*
            The test\'s filter.
          - **parameters** *(dict) --*
            The test\'s parameters, such as test framework parameters and fixture settings. Parameters are represented by name-value pairs of strings.
            For all tests:
            * app_performance_monitoring: Performance monitoring is enabled by default. Set this parameter to \"false\" to disable it.
            For Calabash tests:
            * profile: A cucumber profile, for example, \"my_profile_name\".
            * tags: You can limit execution to features or scenarios that have (or don\'t have) certain tags, for example, \"@smoke\" or \"@smoke,~@wip\".
            For Appium tests (all types):
            * appium_version: The Appium version. Currently supported values are \"1.6.5\" (and higher), \"latest\", and \"default\".
              * “latest” will run the latest Appium version supported by Device Farm (1.9.1).
              * For “default”, Device Farm will choose a compatible version of Appium for the device. The current behavior is to run 1.7.2 on Android devices and iOS 9 and earlier, 1.7.2 for iOS 10 and later.
              * This behavior is subject to change.
            For Fuzz tests (Android only):
            * event_count: The number of events, between 1 and 10000, that the UI fuzz test should perform.
            * throttle: The time, in ms, between 0 and 1000, that the UI fuzz test should wait between events.
            * seed: A seed to use for randomizing the UI fuzz test. Using the same seed value between tests ensures identical event sequences.
            For Explorer tests:
            * username: A username to use if the Explorer encounters a login form. If not supplied, no username will be inserted.
            * password: A password to use if the Explorer encounters a login form. If not supplied, no password will be inserted.
            For Instrumentation:
            * filter: A test filter string. Examples:
              * Running a single test case: \"com.android.abc.Test1\"
              * Running a single test: \"com.android.abc.Test1#smoke\"
              * Running multiple tests: \"com.android.abc.Test1,com.android.abc.Test2\"
            For XCTest and XCTestUI:
            * filter: A test filter string. Examples:
              * Running a single test class: \"LoginTests\"
              * Running a multiple test classes: \"LoginTests,SmokeTests\"
              * Running a single test: \"LoginTests/testValid\"
              * Running multiple tests: \"LoginTests/testValid,LoginTests/testInvalid\"
            For UIAutomator:
            * filter: A test filter string. Examples:
              * Running a single test case: \"com.android.abc.Test1\"
              * Running a single test: \"com.android.abc.Test1#smoke\"
              * Running multiple tests: \"com.android.abc.Test1,com.android.abc.Test2\"
            - *(string) --*
              - *(string) --*
        :type configuration: dict
        :param configuration:
          An object containing information about the settings for a run.
          - **extraDataPackageArn** *(string) --*
            The ARN of the extra data for the run. The extra data is a .zip file that AWS Device Farm will extract to external data for Android or the app\'s sandbox for iOS.
          - **networkProfileArn** *(string) --*
            Reserved for internal use.
          - **locale** *(string) --*
            Information about the locale that is used for the run.
          - **location** *(dict) --*
            Information about the location that is used for the run.
            - **latitude** *(float) --* **[REQUIRED]**
              The latitude.
            - **longitude** *(float) --* **[REQUIRED]**
              The longitude.
          - **vpceConfigurationArns** *(list) --*
            An array of Amazon Resource Names (ARNs) for your VPC endpoint configurations.
            - *(string) --*
          - **customerArtifactPaths** *(dict) --*
            Input ``CustomerArtifactPaths`` object for the scheduled run configuration.
            - **iosPaths** *(list) --*
              Comma-separated list of paths on the iOS device where the artifacts generated by the customer\'s tests will be pulled from.
              - *(string) --*
            - **androidPaths** *(list) --*
              Comma-separated list of paths on the Android device where the artifacts generated by the customer\'s tests will be pulled from.
              - *(string) --*
            - **deviceHostPaths** *(list) --*
              Comma-separated list of paths in the test execution environment where the artifacts generated by the customer\'s tests will be pulled from.
              - *(string) --*
          - **radios** *(dict) --*
            Information about the radio states for the run.
            - **wifi** *(boolean) --*
              True if Wi-Fi is enabled at the beginning of the test; otherwise, false.
            - **bluetooth** *(boolean) --*
              True if Bluetooth is enabled at the beginning of the test; otherwise, false.
            - **nfc** *(boolean) --*
              True if NFC is enabled at the beginning of the test; otherwise, false.
            - **gps** *(boolean) --*
              True if GPS is enabled at the beginning of the test; otherwise, false.
          - **auxiliaryApps** *(list) --*
            A list of auxiliary apps for the run.
            - *(string) --*
          - **billingMethod** *(string) --*
            Specifies the billing method for a test run: ``metered`` or ``unmetered`` . If the parameter is not specified, the default value is ``metered`` .
        :rtype: dict
        :returns:
        """
        pass

    def get_instance_profile(self, arn: str) -> Dict:
        """
        Returns information about the specified instance profile.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetInstanceProfile>`_
        
        **Request Syntax**
        ::
          response = client.get_instance_profile(
              arn='string'
          )
        
        **Response Syntax**
        ::
            {
                'instanceProfile': {
                    'arn': 'string',
                    'packageCleanup': True|False,
                    'excludeAppPackagesFromCleanup': [
                        'string',
                    ],
                    'rebootAfterUse': True|False,
                    'name': 'string',
                    'description': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **instanceProfile** *(dict) --* 
              An object containing information about your instance profile.
              - **arn** *(string) --* 
                The Amazon Resource Name (ARN) of the instance profile.
              - **packageCleanup** *(boolean) --* 
                When set to ``true`` , Device Farm will remove app packages after a test run. The default value is ``false`` for private devices.
              - **excludeAppPackagesFromCleanup** *(list) --* 
                An array of strings specifying the list of app packages that should not be cleaned up from the device after a test run is over.
                The list of packages is only considered if you set ``packageCleanup`` to ``true`` .
                - *(string) --* 
              - **rebootAfterUse** *(boolean) --* 
                When set to ``true`` , Device Farm will reboot the instance after a test run. The default value is ``true`` .
              - **name** *(string) --* 
                The name of the instance profile.
              - **description** *(string) --* 
                The description of the instance profile.
        :type arn: string
        :param arn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of your instance profile.
        :rtype: dict
        :returns:
        """
        pass

    def get_job(self, arn: str) -> Dict:
        """
        Gets information about a job.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetJob>`_
        
        **Request Syntax**
        ::
          response = client.get_job(
              arn='string'
          )
        
        **Response Syntax**
        ::
            {
                'job': {
                    'arn': 'string',
                    'name': 'string',
                    'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
                    'created': datetime(2015, 1, 1),
                    'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                    'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                    'started': datetime(2015, 1, 1),
                    'stopped': datetime(2015, 1, 1),
                    'counters': {
                        'total': 123,
                        'passed': 123,
                        'failed': 123,
                        'warned': 123,
                        'errored': 123,
                        'stopped': 123,
                        'skipped': 123
                    },
                    'message': 'string',
                    'device': {
                        'arn': 'string',
                        'name': 'string',
                        'manufacturer': 'string',
                        'model': 'string',
                        'modelId': 'string',
                        'formFactor': 'PHONE'|'TABLET',
                        'platform': 'ANDROID'|'IOS',
                        'os': 'string',
                        'cpu': {
                            'frequency': 'string',
                            'architecture': 'string',
                            'clock': 123.0
                        },
                        'resolution': {
                            'width': 123,
                            'height': 123
                        },
                        'heapSize': 123,
                        'memory': 123,
                        'image': 'string',
                        'carrier': 'string',
                        'radio': 'string',
                        'remoteAccessEnabled': True|False,
                        'remoteDebugEnabled': True|False,
                        'fleetType': 'string',
                        'fleetName': 'string',
                        'instances': [
                            {
                                'arn': 'string',
                                'deviceArn': 'string',
                                'labels': [
                                    'string',
                                ],
                                'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                                'udid': 'string',
                                'instanceProfile': {
                                    'arn': 'string',
                                    'packageCleanup': True|False,
                                    'excludeAppPackagesFromCleanup': [
                                        'string',
                                    ],
                                    'rebootAfterUse': True|False,
                                    'name': 'string',
                                    'description': 'string'
                                }
                            },
                        ],
                        'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
                    },
                    'instanceArn': 'string',
                    'deviceMinutes': {
                        'total': 123.0,
                        'metered': 123.0,
                        'unmetered': 123.0
                    },
                    'videoEndpoint': 'string',
                    'videoCapture': True|False
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of a get job request.
            - **job** *(dict) --* 
              An object containing information about the requested job.
              - **arn** *(string) --* 
                The job's ARN.
              - **name** *(string) --* 
                The job's name.
              - **type** *(string) --* 
                The job's type.
                Allowed values include the following:
                * BUILTIN_FUZZ: The built-in fuzz type. 
                * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
                * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
                * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
                * APPIUM_PYTHON: The Appium Python type. 
                * APPIUM_NODE: The Appium Node.js type. 
                * APPIUM_RUBY: The Appium Ruby type. 
                * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for web apps. 
                * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for web apps. 
                * APPIUM_WEB_PYTHON: The Appium Python type for web apps. 
                * APPIUM_WEB_NODE: The Appium Node.js type for web apps. 
                * APPIUM_WEB_RUBY: The Appium Ruby test type for web apps. 
                * CALABASH: The Calabash type. 
                * INSTRUMENTATION: The Instrumentation type. 
                * UIAUTOMATION: The uiautomation type. 
                * UIAUTOMATOR: The uiautomator type. 
                * XCTEST: The XCode test type. 
                * XCTEST_UI: The XCode UI test type. 
              - **created** *(datetime) --* 
                When the job was created.
              - **status** *(string) --* 
                The job's status.
                Allowed values include:
                * PENDING: A pending status. 
                * PENDING_CONCURRENCY: A pending concurrency status. 
                * PENDING_DEVICE: A pending device status. 
                * PROCESSING: A processing status. 
                * SCHEDULING: A scheduling status. 
                * PREPARING: A preparing status. 
                * RUNNING: A running status. 
                * COMPLETED: A completed status. 
                * STOPPING: A stopping status. 
              - **result** *(string) --* 
                The job's result.
                Allowed values include:
                * PENDING: A pending condition. 
                * PASSED: A passing condition. 
                * WARNED: A warning condition. 
                * FAILED: A failed condition. 
                * SKIPPED: A skipped condition. 
                * ERRORED: An error condition. 
                * STOPPED: A stopped condition. 
              - **started** *(datetime) --* 
                The job's start time.
              - **stopped** *(datetime) --* 
                The job's stop time.
              - **counters** *(dict) --* 
                The job's result counters.
                - **total** *(integer) --* 
                  The total number of entities.
                - **passed** *(integer) --* 
                  The number of passed entities.
                - **failed** *(integer) --* 
                  The number of failed entities.
                - **warned** *(integer) --* 
                  The number of warned entities.
                - **errored** *(integer) --* 
                  The number of errored entities.
                - **stopped** *(integer) --* 
                  The number of stopped entities.
                - **skipped** *(integer) --* 
                  The number of skipped entities.
              - **message** *(string) --* 
                A message about the job's result.
              - **device** *(dict) --* 
                The device (phone or tablet).
                - **arn** *(string) --* 
                  The device's ARN.
                - **name** *(string) --* 
                  The device's display name.
                - **manufacturer** *(string) --* 
                  The device's manufacturer name.
                - **model** *(string) --* 
                  The device's model name.
                - **modelId** *(string) --* 
                  The device's model ID.
                - **formFactor** *(string) --* 
                  The device's form factor.
                  Allowed values include:
                  * PHONE: The phone form factor. 
                  * TABLET: The tablet form factor. 
                - **platform** *(string) --* 
                  The device's platform.
                  Allowed values include:
                  * ANDROID: The Android platform. 
                  * IOS: The iOS platform. 
                - **os** *(string) --* 
                  The device's operating system type.
                - **cpu** *(dict) --* 
                  Information about the device's CPU.
                  - **frequency** *(string) --* 
                    The CPU's frequency.
                  - **architecture** *(string) --* 
                    The CPU's architecture, for example x86 or ARM.
                  - **clock** *(float) --* 
                    The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.
                - **resolution** *(dict) --* 
                  The resolution of the device.
                  - **width** *(integer) --* 
                    The screen resolution's width, expressed in pixels.
                  - **height** *(integer) --* 
                    The screen resolution's height, expressed in pixels.
                - **heapSize** *(integer) --* 
                  The device's heap size, expressed in bytes.
                - **memory** *(integer) --* 
                  The device's total memory size, expressed in bytes.
                - **image** *(string) --* 
                  The device's image name.
                - **carrier** *(string) --* 
                  The device's carrier.
                - **radio** *(string) --* 
                  The device's radio.
                - **remoteAccessEnabled** *(boolean) --* 
                  Specifies whether remote access has been enabled for the specified device.
                - **remoteDebugEnabled** *(boolean) --* 
                  This flag is set to ``true`` if remote debugging is enabled for the device.
                - **fleetType** *(string) --* 
                  The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.
                - **fleetName** *(string) --* 
                  The name of the fleet to which this device belongs.
                - **instances** *(list) --* 
                  The instances belonging to this device.
                  - *(dict) --* 
                    Represents the device instance.
                    - **arn** *(string) --* 
                      The Amazon Resource Name (ARN) of the device instance.
                    - **deviceArn** *(string) --* 
                      The Amazon Resource Name (ARN) of the device.
                    - **labels** *(list) --* 
                      An array of strings describing the device instance.
                      - *(string) --* 
                    - **status** *(string) --* 
                      The status of the device instance. Valid values are listed below.
                    - **udid** *(string) --* 
                      Unique device identifier for the device instance.
                    - **instanceProfile** *(dict) --* 
                      A object containing information about the instance profile.
                      - **arn** *(string) --* 
                        The Amazon Resource Name (ARN) of the instance profile.
                      - **packageCleanup** *(boolean) --* 
                        When set to ``true`` , Device Farm will remove app packages after a test run. The default value is ``false`` for private devices.
                      - **excludeAppPackagesFromCleanup** *(list) --* 
                        An array of strings specifying the list of app packages that should not be cleaned up from the device after a test run is over.
                        The list of packages is only considered if you set ``packageCleanup`` to ``true`` .
                        - *(string) --* 
                      - **rebootAfterUse** *(boolean) --* 
                        When set to ``true`` , Device Farm will reboot the instance after a test run. The default value is ``true`` .
                      - **name** *(string) --* 
                        The name of the instance profile.
                      - **description** *(string) --* 
                        The description of the instance profile.
                - **availability** *(string) --* 
                  Reflects how likely a device will be available for a test run. It is currently available in the ListDevices and GetDevice API methods.
              - **instanceArn** *(string) --* 
                The Amazon Resource Name (ARN) of the instance.
              - **deviceMinutes** *(dict) --* 
                Represents the total (metered or unmetered) minutes used by the job.
                - **total** *(float) --* 
                  When specified, represents the total minutes used by the resource to run tests.
                - **metered** *(float) --* 
                  When specified, represents only the sum of metered minutes used by the resource to run tests.
                - **unmetered** *(float) --* 
                  When specified, represents only the sum of unmetered minutes used by the resource to run tests.
              - **videoEndpoint** *(string) --* 
                The endpoint for streaming device video.
              - **videoCapture** *(boolean) --* 
                This value is set to true if video capture is enabled; otherwise, it is set to false.
        :type arn: string
        :param arn: **[REQUIRED]**
          The job\'s ARN.
        :rtype: dict
        :returns:
        """
        pass

    def get_network_profile(self, arn: str) -> Dict:
        """
        Returns information about a network profile.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetNetworkProfile>`_
        
        **Request Syntax**
        ::
          response = client.get_network_profile(
              arn='string'
          )
        
        **Response Syntax**
        ::
            {
                'networkProfile': {
                    'arn': 'string',
                    'name': 'string',
                    'description': 'string',
                    'type': 'CURATED'|'PRIVATE',
                    'uplinkBandwidthBits': 123,
                    'downlinkBandwidthBits': 123,
                    'uplinkDelayMs': 123,
                    'downlinkDelayMs': 123,
                    'uplinkJitterMs': 123,
                    'downlinkJitterMs': 123,
                    'uplinkLossPercent': 123,
                    'downlinkLossPercent': 123
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **networkProfile** *(dict) --* 
              The network profile.
              - **arn** *(string) --* 
                The Amazon Resource Name (ARN) of the network profile.
              - **name** *(string) --* 
                The name of the network profile.
              - **description** *(string) --* 
                The description of the network profile.
              - **type** *(string) --* 
                The type of network profile. Valid values are listed below.
              - **uplinkBandwidthBits** *(integer) --* 
                The data throughput rate in bits per second, as an integer from 0 to 104857600.
              - **downlinkBandwidthBits** *(integer) --* 
                The data throughput rate in bits per second, as an integer from 0 to 104857600.
              - **uplinkDelayMs** *(integer) --* 
                Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
              - **downlinkDelayMs** *(integer) --* 
                Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
              - **uplinkJitterMs** *(integer) --* 
                Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
              - **downlinkJitterMs** *(integer) --* 
                Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
              - **uplinkLossPercent** *(integer) --* 
                Proportion of transmitted packets that fail to arrive from 0 to 100 percent.
              - **downlinkLossPercent** *(integer) --* 
                Proportion of received packets that fail to arrive from 0 to 100 percent.
        :type arn: string
        :param arn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the network profile you want to return information about.
        :rtype: dict
        :returns:
        """
        pass

    def get_offering_status(self, nextToken: str = None) -> Dict:
        """
        Gets the current status and future status of all offerings purchased by an AWS account. The response indicates how many offerings are currently available and the offerings that will be available in the next period. The API returns a ``NotEligible`` error if the user is not permitted to invoke the operation. Please contact `aws-devicefarm-support@amazon.com <mailto:aws-devicefarm-support@amazon.com>`__ if you believe that you should be able to invoke this operation.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetOfferingStatus>`_
        
        **Request Syntax**
        ::
          response = client.get_offering_status(
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'current': {
                    'string': {
                        'type': 'PURCHASE'|'RENEW'|'SYSTEM',
                        'offering': {
                            'id': 'string',
                            'description': 'string',
                            'type': 'RECURRING',
                            'platform': 'ANDROID'|'IOS',
                            'recurringCharges': [
                                {
                                    'cost': {
                                        'amount': 123.0,
                                        'currencyCode': 'USD'
                                    },
                                    'frequency': 'MONTHLY'
                                },
                            ]
                        },
                        'quantity': 123,
                        'effectiveOn': datetime(2015, 1, 1)
                    }
                },
                'nextPeriod': {
                    'string': {
                        'type': 'PURCHASE'|'RENEW'|'SYSTEM',
                        'offering': {
                            'id': 'string',
                            'description': 'string',
                            'type': 'RECURRING',
                            'platform': 'ANDROID'|'IOS',
                            'recurringCharges': [
                                {
                                    'cost': {
                                        'amount': 123.0,
                                        'currencyCode': 'USD'
                                    },
                                    'frequency': 'MONTHLY'
                                },
                            ]
                        },
                        'quantity': 123,
                        'effectiveOn': datetime(2015, 1, 1)
                    }
                },
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Returns the status result for a device offering.
            - **current** *(dict) --* 
              When specified, gets the offering status for the current period.
              - *(string) --* 
                - *(dict) --* 
                  The status of the offering.
                  - **type** *(string) --* 
                    The type specified for the offering status.
                  - **offering** *(dict) --* 
                    Represents the metadata of an offering status.
                    - **id** *(string) --* 
                      The ID that corresponds to a device offering.
                    - **description** *(string) --* 
                      A string describing the offering.
                    - **type** *(string) --* 
                      The type of offering (e.g., "RECURRING") for a device.
                    - **platform** *(string) --* 
                      The platform of the device (e.g., ANDROID or IOS).
                    - **recurringCharges** *(list) --* 
                      Specifies whether there are recurring charges for the offering.
                      - *(dict) --* 
                        Specifies whether charges for devices will be recurring.
                        - **cost** *(dict) --* 
                          The cost of the recurring charge.
                          - **amount** *(float) --* 
                            The numerical amount of an offering or transaction.
                          - **currencyCode** *(string) --* 
                            The currency code of a monetary amount. For example, ``USD`` means "U.S. dollars."
                        - **frequency** *(string) --* 
                          The frequency in which charges will recur.
                  - **quantity** *(integer) --* 
                    The number of available devices in the offering.
                  - **effectiveOn** *(datetime) --* 
                    The date on which the offering is effective.
            - **nextPeriod** *(dict) --* 
              When specified, gets the offering status for the next period.
              - *(string) --* 
                - *(dict) --* 
                  The status of the offering.
                  - **type** *(string) --* 
                    The type specified for the offering status.
                  - **offering** *(dict) --* 
                    Represents the metadata of an offering status.
                    - **id** *(string) --* 
                      The ID that corresponds to a device offering.
                    - **description** *(string) --* 
                      A string describing the offering.
                    - **type** *(string) --* 
                      The type of offering (e.g., "RECURRING") for a device.
                    - **platform** *(string) --* 
                      The platform of the device (e.g., ANDROID or IOS).
                    - **recurringCharges** *(list) --* 
                      Specifies whether there are recurring charges for the offering.
                      - *(dict) --* 
                        Specifies whether charges for devices will be recurring.
                        - **cost** *(dict) --* 
                          The cost of the recurring charge.
                          - **amount** *(float) --* 
                            The numerical amount of an offering or transaction.
                          - **currencyCode** *(string) --* 
                            The currency code of a monetary amount. For example, ``USD`` means "U.S. dollars."
                        - **frequency** *(string) --* 
                          The frequency in which charges will recur.
                  - **quantity** *(integer) --* 
                    The number of available devices in the offering.
                  - **effectiveOn** *(datetime) --* 
                    The date on which the offering is effective.
            - **nextToken** *(string) --* 
              An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type nextToken: string
        :param nextToken:
          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :rtype: dict
        :returns:
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

    def get_project(self, arn: str) -> Dict:
        """
        Gets information about a project.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetProject>`_
        
        **Request Syntax**
        ::
          response = client.get_project(
              arn='string'
          )
        
        **Response Syntax**
        ::
            {
                'project': {
                    'arn': 'string',
                    'name': 'string',
                    'defaultJobTimeoutMinutes': 123,
                    'created': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of a get project request.
            - **project** *(dict) --* 
              The project you wish to get information about.
              - **arn** *(string) --* 
                The project's ARN.
              - **name** *(string) --* 
                The project's name.
              - **defaultJobTimeoutMinutes** *(integer) --* 
                The default number of minutes (at the project level) a test run will execute before it times out. Default value is 60 minutes.
              - **created** *(datetime) --* 
                When the project was created.
        :type arn: string
        :param arn: **[REQUIRED]**
          The project\'s ARN.
        :rtype: dict
        :returns:
        """
        pass

    def get_remote_access_session(self, arn: str) -> Dict:
        """
        Returns a link to a currently running remote access session.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetRemoteAccessSession>`_
        
        **Request Syntax**
        ::
          response = client.get_remote_access_session(
              arn='string'
          )
        
        **Response Syntax**
        ::
            {
                'remoteAccessSession': {
                    'arn': 'string',
                    'name': 'string',
                    'created': datetime(2015, 1, 1),
                    'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                    'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                    'message': 'string',
                    'started': datetime(2015, 1, 1),
                    'stopped': datetime(2015, 1, 1),
                    'device': {
                        'arn': 'string',
                        'name': 'string',
                        'manufacturer': 'string',
                        'model': 'string',
                        'modelId': 'string',
                        'formFactor': 'PHONE'|'TABLET',
                        'platform': 'ANDROID'|'IOS',
                        'os': 'string',
                        'cpu': {
                            'frequency': 'string',
                            'architecture': 'string',
                            'clock': 123.0
                        },
                        'resolution': {
                            'width': 123,
                            'height': 123
                        },
                        'heapSize': 123,
                        'memory': 123,
                        'image': 'string',
                        'carrier': 'string',
                        'radio': 'string',
                        'remoteAccessEnabled': True|False,
                        'remoteDebugEnabled': True|False,
                        'fleetType': 'string',
                        'fleetName': 'string',
                        'instances': [
                            {
                                'arn': 'string',
                                'deviceArn': 'string',
                                'labels': [
                                    'string',
                                ],
                                'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                                'udid': 'string',
                                'instanceProfile': {
                                    'arn': 'string',
                                    'packageCleanup': True|False,
                                    'excludeAppPackagesFromCleanup': [
                                        'string',
                                    ],
                                    'rebootAfterUse': True|False,
                                    'name': 'string',
                                    'description': 'string'
                                }
                            },
                        ],
                        'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
                    },
                    'instanceArn': 'string',
                    'remoteDebugEnabled': True|False,
                    'remoteRecordEnabled': True|False,
                    'remoteRecordAppArn': 'string',
                    'hostAddress': 'string',
                    'clientId': 'string',
                    'billingMethod': 'METERED'|'UNMETERED',
                    'deviceMinutes': {
                        'total': 123.0,
                        'metered': 123.0,
                        'unmetered': 123.0
                    },
                    'endpoint': 'string',
                    'deviceUdid': 'string',
                    'interactionMode': 'INTERACTIVE'|'NO_VIDEO'|'VIDEO_ONLY',
                    'skipAppResign': True|False
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the response from the server that lists detailed information about the remote access session.
            - **remoteAccessSession** *(dict) --* 
              A container that lists detailed information about the remote access session.
              - **arn** *(string) --* 
                The Amazon Resource Name (ARN) of the remote access session.
              - **name** *(string) --* 
                The name of the remote access session.
              - **created** *(datetime) --* 
                The date and time the remote access session was created.
              - **status** *(string) --* 
                The status of the remote access session. Can be any of the following:
                * PENDING: A pending status. 
                * PENDING_CONCURRENCY: A pending concurrency status. 
                * PENDING_DEVICE: A pending device status. 
                * PROCESSING: A processing status. 
                * SCHEDULING: A scheduling status. 
                * PREPARING: A preparing status. 
                * RUNNING: A running status. 
                * COMPLETED: A completed status. 
                * STOPPING: A stopping status. 
              - **result** *(string) --* 
                The result of the remote access session. Can be any of the following:
                * PENDING: A pending condition. 
                * PASSED: A passing condition. 
                * WARNED: A warning condition. 
                * FAILED: A failed condition. 
                * SKIPPED: A skipped condition. 
                * ERRORED: An error condition. 
                * STOPPED: A stopped condition. 
              - **message** *(string) --* 
                A message about the remote access session.
              - **started** *(datetime) --* 
                The date and time the remote access session was started.
              - **stopped** *(datetime) --* 
                The date and time the remote access session was stopped.
              - **device** *(dict) --* 
                The device (phone or tablet) used in the remote access session.
                - **arn** *(string) --* 
                  The device's ARN.
                - **name** *(string) --* 
                  The device's display name.
                - **manufacturer** *(string) --* 
                  The device's manufacturer name.
                - **model** *(string) --* 
                  The device's model name.
                - **modelId** *(string) --* 
                  The device's model ID.
                - **formFactor** *(string) --* 
                  The device's form factor.
                  Allowed values include:
                  * PHONE: The phone form factor. 
                  * TABLET: The tablet form factor. 
                - **platform** *(string) --* 
                  The device's platform.
                  Allowed values include:
                  * ANDROID: The Android platform. 
                  * IOS: The iOS platform. 
                - **os** *(string) --* 
                  The device's operating system type.
                - **cpu** *(dict) --* 
                  Information about the device's CPU.
                  - **frequency** *(string) --* 
                    The CPU's frequency.
                  - **architecture** *(string) --* 
                    The CPU's architecture, for example x86 or ARM.
                  - **clock** *(float) --* 
                    The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.
                - **resolution** *(dict) --* 
                  The resolution of the device.
                  - **width** *(integer) --* 
                    The screen resolution's width, expressed in pixels.
                  - **height** *(integer) --* 
                    The screen resolution's height, expressed in pixels.
                - **heapSize** *(integer) --* 
                  The device's heap size, expressed in bytes.
                - **memory** *(integer) --* 
                  The device's total memory size, expressed in bytes.
                - **image** *(string) --* 
                  The device's image name.
                - **carrier** *(string) --* 
                  The device's carrier.
                - **radio** *(string) --* 
                  The device's radio.
                - **remoteAccessEnabled** *(boolean) --* 
                  Specifies whether remote access has been enabled for the specified device.
                - **remoteDebugEnabled** *(boolean) --* 
                  This flag is set to ``true`` if remote debugging is enabled for the device.
                - **fleetType** *(string) --* 
                  The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.
                - **fleetName** *(string) --* 
                  The name of the fleet to which this device belongs.
                - **instances** *(list) --* 
                  The instances belonging to this device.
                  - *(dict) --* 
                    Represents the device instance.
                    - **arn** *(string) --* 
                      The Amazon Resource Name (ARN) of the device instance.
                    - **deviceArn** *(string) --* 
                      The Amazon Resource Name (ARN) of the device.
                    - **labels** *(list) --* 
                      An array of strings describing the device instance.
                      - *(string) --* 
                    - **status** *(string) --* 
                      The status of the device instance. Valid values are listed below.
                    - **udid** *(string) --* 
                      Unique device identifier for the device instance.
                    - **instanceProfile** *(dict) --* 
                      A object containing information about the instance profile.
                      - **arn** *(string) --* 
                        The Amazon Resource Name (ARN) of the instance profile.
                      - **packageCleanup** *(boolean) --* 
                        When set to ``true`` , Device Farm will remove app packages after a test run. The default value is ``false`` for private devices.
                      - **excludeAppPackagesFromCleanup** *(list) --* 
                        An array of strings specifying the list of app packages that should not be cleaned up from the device after a test run is over.
                        The list of packages is only considered if you set ``packageCleanup`` to ``true`` .
                        - *(string) --* 
                      - **rebootAfterUse** *(boolean) --* 
                        When set to ``true`` , Device Farm will reboot the instance after a test run. The default value is ``true`` .
                      - **name** *(string) --* 
                        The name of the instance profile.
                      - **description** *(string) --* 
                        The description of the instance profile.
                - **availability** *(string) --* 
                  Reflects how likely a device will be available for a test run. It is currently available in the ListDevices and GetDevice API methods.
              - **instanceArn** *(string) --* 
                The Amazon Resource Name (ARN) of the instance.
              - **remoteDebugEnabled** *(boolean) --* 
                This flag is set to ``true`` if remote debugging is enabled for the remote access session.
              - **remoteRecordEnabled** *(boolean) --* 
                This flag is set to ``true`` if remote recording is enabled for the remote access session.
              - **remoteRecordAppArn** *(string) --* 
                The Amazon Resource Name (ARN) for the app to be recorded in the remote access session.
              - **hostAddress** *(string) --* 
                IP address of the EC2 host where you need to connect to remotely debug devices. Only returned if remote debugging is enabled for the remote access session.
              - **clientId** *(string) --* 
                Unique identifier of your client for the remote access session. Only returned if remote debugging is enabled for the remote access session.
              - **billingMethod** *(string) --* 
                The billing method of the remote access session. Possible values include ``METERED`` or ``UNMETERED`` . For more information about metered devices, see `AWS Device Farm terminology <https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html#welcome-terminology>`__ ."
              - **deviceMinutes** *(dict) --* 
                The number of minutes a device is used in a remote access sesssion (including setup and teardown minutes).
                - **total** *(float) --* 
                  When specified, represents the total minutes used by the resource to run tests.
                - **metered** *(float) --* 
                  When specified, represents only the sum of metered minutes used by the resource to run tests.
                - **unmetered** *(float) --* 
                  When specified, represents only the sum of unmetered minutes used by the resource to run tests.
              - **endpoint** *(string) --* 
                The endpoint for the remote access sesssion.
              - **deviceUdid** *(string) --* 
                Unique device identifier for the remote device. Only returned if remote debugging is enabled for the remote access session.
              - **interactionMode** *(string) --* 
                The interaction mode of the remote access session. Valid values are:
                * INTERACTIVE: You can interact with the iOS device by viewing, touching, and rotating the screen. You **cannot** run XCUITest framework-based tests in this mode. 
                * NO_VIDEO: You are connected to the device but cannot interact with it or view the screen. This mode has the fastest test execution speed. You **can** run XCUITest framework-based tests in this mode. 
                * VIDEO_ONLY: You can view the screen but cannot touch or rotate it. You **can** run XCUITest framework-based tests and watch the screen in this mode. 
              - **skipAppResign** *(boolean) --* 
                When set to ``true`` , for private devices, Device Farm will not sign your app again. For public devices, Device Farm always signs your apps again and this parameter has no effect.
                For more information about how Device Farm re-signs your app(s), see `Do you modify my app? <https://aws.amazon.com/device-farm/faq/>`__ in the *AWS Device Farm FAQs* .
        :type arn: string
        :param arn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the remote access session about which you want to get session information.
        :rtype: dict
        :returns:
        """
        pass

    def get_run(self, arn: str) -> Dict:
        """
        Gets information about a run.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetRun>`_
        
        **Request Syntax**
        ::
          response = client.get_run(
              arn='string'
          )
        
        **Response Syntax**
        ::
            {
                'run': {
                    'arn': 'string',
                    'name': 'string',
                    'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
                    'platform': 'ANDROID'|'IOS',
                    'created': datetime(2015, 1, 1),
                    'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                    'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                    'started': datetime(2015, 1, 1),
                    'stopped': datetime(2015, 1, 1),
                    'counters': {
                        'total': 123,
                        'passed': 123,
                        'failed': 123,
                        'warned': 123,
                        'errored': 123,
                        'stopped': 123,
                        'skipped': 123
                    },
                    'message': 'string',
                    'totalJobs': 123,
                    'completedJobs': 123,
                    'billingMethod': 'METERED'|'UNMETERED',
                    'deviceMinutes': {
                        'total': 123.0,
                        'metered': 123.0,
                        'unmetered': 123.0
                    },
                    'networkProfile': {
                        'arn': 'string',
                        'name': 'string',
                        'description': 'string',
                        'type': 'CURATED'|'PRIVATE',
                        'uplinkBandwidthBits': 123,
                        'downlinkBandwidthBits': 123,
                        'uplinkDelayMs': 123,
                        'downlinkDelayMs': 123,
                        'uplinkJitterMs': 123,
                        'downlinkJitterMs': 123,
                        'uplinkLossPercent': 123,
                        'downlinkLossPercent': 123
                    },
                    'parsingResultUrl': 'string',
                    'resultCode': 'PARSING_FAILED'|'VPC_ENDPOINT_SETUP_FAILED',
                    'seed': 123,
                    'appUpload': 'string',
                    'eventCount': 123,
                    'jobTimeoutMinutes': 123,
                    'devicePoolArn': 'string',
                    'locale': 'string',
                    'radios': {
                        'wifi': True|False,
                        'bluetooth': True|False,
                        'nfc': True|False,
                        'gps': True|False
                    },
                    'location': {
                        'latitude': 123.0,
                        'longitude': 123.0
                    },
                    'customerArtifactPaths': {
                        'iosPaths': [
                            'string',
                        ],
                        'androidPaths': [
                            'string',
                        ],
                        'deviceHostPaths': [
                            'string',
                        ]
                    },
                    'webUrl': 'string',
                    'skipAppResign': True|False,
                    'testSpecArn': 'string',
                    'deviceSelectionResult': {
                        'filters': [
                            {
                                'attribute': 'ARN'|'PLATFORM'|'OS_VERSION'|'MODEL'|'AVAILABILITY'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                                'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                                'values': [
                                    'string',
                                ]
                            },
                        ],
                        'matchedDevicesCount': 123,
                        'maxDevices': 123
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of a get run request.
            - **run** *(dict) --* 
              The run you wish to get results from.
              - **arn** *(string) --* 
                The run's ARN.
              - **name** *(string) --* 
                The run's name.
              - **type** *(string) --* 
                The run's type.
                Must be one of the following values:
                * BUILTIN_FUZZ: The built-in fuzz type. 
                * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
                * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
                * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
                * APPIUM_PYTHON: The Appium Python type. 
                * APPIUM_NODE: The Appium Node.js type. 
                * APPIUM_RUBY: The Appium Ruby type. 
                * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for web apps. 
                * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for web apps. 
                * APPIUM_WEB_PYTHON: The Appium Python type for web apps. 
                * APPIUM_WEB_NODE: The Appium Node.js type for web apps. 
                * APPIUM_WEB_RUBY: The Appium Ruby type for web apps. 
                * CALABASH: The Calabash type. 
                * INSTRUMENTATION: The Instrumentation type. 
                * UIAUTOMATION: The uiautomation type. 
                * UIAUTOMATOR: The uiautomator type. 
                * XCTEST: The XCode test type. 
                * XCTEST_UI: The XCode UI test type. 
              - **platform** *(string) --* 
                The run's platform.
                Allowed values include:
                * ANDROID: The Android platform. 
                * IOS: The iOS platform. 
              - **created** *(datetime) --* 
                When the run was created.
              - **status** *(string) --* 
                The run's status.
                Allowed values include:
                * PENDING: A pending status. 
                * PENDING_CONCURRENCY: A pending concurrency status. 
                * PENDING_DEVICE: A pending device status. 
                * PROCESSING: A processing status. 
                * SCHEDULING: A scheduling status. 
                * PREPARING: A preparing status. 
                * RUNNING: A running status. 
                * COMPLETED: A completed status. 
                * STOPPING: A stopping status. 
              - **result** *(string) --* 
                The run's result.
                Allowed values include:
                * PENDING: A pending condition. 
                * PASSED: A passing condition. 
                * WARNED: A warning condition. 
                * FAILED: A failed condition. 
                * SKIPPED: A skipped condition. 
                * ERRORED: An error condition. 
                * STOPPED: A stopped condition. 
              - **started** *(datetime) --* 
                The run's start time.
              - **stopped** *(datetime) --* 
                The run's stop time.
              - **counters** *(dict) --* 
                The run's result counters.
                - **total** *(integer) --* 
                  The total number of entities.
                - **passed** *(integer) --* 
                  The number of passed entities.
                - **failed** *(integer) --* 
                  The number of failed entities.
                - **warned** *(integer) --* 
                  The number of warned entities.
                - **errored** *(integer) --* 
                  The number of errored entities.
                - **stopped** *(integer) --* 
                  The number of stopped entities.
                - **skipped** *(integer) --* 
                  The number of skipped entities.
              - **message** *(string) --* 
                A message about the run's result.
              - **totalJobs** *(integer) --* 
                The total number of jobs for the run.
              - **completedJobs** *(integer) --* 
                The total number of completed jobs.
              - **billingMethod** *(string) --* 
                Specifies the billing method for a test run: ``metered`` or ``unmetered`` . If the parameter is not specified, the default value is ``metered`` .
              - **deviceMinutes** *(dict) --* 
                Represents the total (metered or unmetered) minutes used by the test run.
                - **total** *(float) --* 
                  When specified, represents the total minutes used by the resource to run tests.
                - **metered** *(float) --* 
                  When specified, represents only the sum of metered minutes used by the resource to run tests.
                - **unmetered** *(float) --* 
                  When specified, represents only the sum of unmetered minutes used by the resource to run tests.
              - **networkProfile** *(dict) --* 
                The network profile being used for a test run.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the network profile.
                - **name** *(string) --* 
                  The name of the network profile.
                - **description** *(string) --* 
                  The description of the network profile.
                - **type** *(string) --* 
                  The type of network profile. Valid values are listed below.
                - **uplinkBandwidthBits** *(integer) --* 
                  The data throughput rate in bits per second, as an integer from 0 to 104857600.
                - **downlinkBandwidthBits** *(integer) --* 
                  The data throughput rate in bits per second, as an integer from 0 to 104857600.
                - **uplinkDelayMs** *(integer) --* 
                  Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
                - **downlinkDelayMs** *(integer) --* 
                  Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
                - **uplinkJitterMs** *(integer) --* 
                  Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
                - **downlinkJitterMs** *(integer) --* 
                  Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
                - **uplinkLossPercent** *(integer) --* 
                  Proportion of transmitted packets that fail to arrive from 0 to 100 percent.
                - **downlinkLossPercent** *(integer) --* 
                  Proportion of received packets that fail to arrive from 0 to 100 percent.
              - **parsingResultUrl** *(string) --* 
                Read-only URL for an object in S3 bucket where you can get the parsing results of the test package. If the test package doesn't parse, the reason why it doesn't parse appears in the file that this URL points to.
              - **resultCode** *(string) --* 
                Supporting field for the result field. Set only if ``result`` is ``SKIPPED`` . ``PARSING_FAILED`` if the result is skipped because of test package parsing failure.
              - **seed** *(integer) --* 
                For fuzz tests, this is a seed to use for randomizing the UI fuzz test. Using the same seed value between tests ensures identical event sequences.
              - **appUpload** *(string) --* 
                An app to upload or that has been uploaded.
              - **eventCount** *(integer) --* 
                For fuzz tests, this is the number of events, between 1 and 10000, that the UI fuzz test should perform.
              - **jobTimeoutMinutes** *(integer) --* 
                The number of minutes the job will execute before it times out.
              - **devicePoolArn** *(string) --* 
                The ARN of the device pool for the run.
              - **locale** *(string) --* 
                Information about the locale that is used for the run.
              - **radios** *(dict) --* 
                Information about the radio states for the run.
                - **wifi** *(boolean) --* 
                  True if Wi-Fi is enabled at the beginning of the test; otherwise, false.
                - **bluetooth** *(boolean) --* 
                  True if Bluetooth is enabled at the beginning of the test; otherwise, false.
                - **nfc** *(boolean) --* 
                  True if NFC is enabled at the beginning of the test; otherwise, false.
                - **gps** *(boolean) --* 
                  True if GPS is enabled at the beginning of the test; otherwise, false.
              - **location** *(dict) --* 
                Information about the location that is used for the run.
                - **latitude** *(float) --* 
                  The latitude.
                - **longitude** *(float) --* 
                  The longitude.
              - **customerArtifactPaths** *(dict) --* 
                Output ``CustomerArtifactPaths`` object for the test run.
                - **iosPaths** *(list) --* 
                  Comma-separated list of paths on the iOS device where the artifacts generated by the customer's tests will be pulled from.
                  - *(string) --* 
                - **androidPaths** *(list) --* 
                  Comma-separated list of paths on the Android device where the artifacts generated by the customer's tests will be pulled from.
                  - *(string) --* 
                - **deviceHostPaths** *(list) --* 
                  Comma-separated list of paths in the test execution environment where the artifacts generated by the customer's tests will be pulled from.
                  - *(string) --* 
              - **webUrl** *(string) --* 
                The Device Farm console URL for the recording of the run.
              - **skipAppResign** *(boolean) --* 
                When set to ``true`` , for private devices, Device Farm will not sign your app again. For public devices, Device Farm always signs your apps again and this parameter has no effect.
                For more information about how Device Farm re-signs your app(s), see `Do you modify my app? <https://aws.amazon.com/device-farm/faq/>`__ in the *AWS Device Farm FAQs* .
              - **testSpecArn** *(string) --* 
                The ARN of the YAML-formatted test specification for the run.
              - **deviceSelectionResult** *(dict) --* 
                The results of a device filter used to select the devices for a test run.
                - **filters** *(list) --* 
                  The filters in a device selection result.
                  - *(dict) --* 
                    Represents a device filter used to select a set of devices to be included in a test run. This data structure is passed in as the ``deviceSelectionConfiguration`` parameter to ScheduleRun. For an example of the JSON request syntax, see  ScheduleRun .
                    It is also passed in as the ``filters`` parameter to ListDevices. For an example of the JSON request syntax, see  ListDevices .
                    - **attribute** *(string) --* 
                      The aspect of a device such as platform or model used as the selection criteria in a device filter.
                      The supported operators for each attribute are provided in the following list.
                        ARN  
                      The Amazon Resource Name (ARN) of the device. For example, "arn:aws:devicefarm:us-west-2::device:12345Example".
                       *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                        PLATFORM  
                      The device platform. Valid values are "ANDROID" or "IOS".
                       *Supported operators* : ``EQUALS``  
                        OS_VERSION  
                      The operating system version. For example, "10.3.2".
                       *Supported operators* : ``EQUALS`` , ``GREATER_THAN`` , ``GREATER_THAN_OR_EQUALS`` , ``IN`` , ``LESS_THAN`` , ``LESS_THAN_OR_EQUALS`` , ``NOT_IN``  
                        MODEL  
                      The device model. For example, "iPad 5th Gen".
                       *Supported operators* : ``CONTAINS`` , ``EQUALS`` , ``IN`` , ``NOT_IN``  
                        AVAILABILITY  
                      The current availability of the device. Valid values are "AVAILABLE", "HIGHLY_AVAILABLE", "BUSY", or "TEMPORARY_NOT_AVAILABLE".
                       *Supported operators* : ``EQUALS``  
                        FORM_FACTOR  
                      The device form factor. Valid values are "PHONE" or "TABLET".
                       *Supported operators* : ``EQUALS``  
                        MANUFACTURER  
                      The device manufacturer. For example, "Apple".
                       *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                        REMOTE_ACCESS_ENABLED  
                      Whether the device is enabled for remote access. Valid values are "TRUE" or "FALSE".
                       *Supported operators* : ``EQUALS``  
                        REMOTE_DEBUG_ENABLED  
                      Whether the device is enabled for remote debugging. Valid values are "TRUE" or "FALSE".
                       *Supported operators* : ``EQUALS``  
                        INSTANCE_ARN  
                      The Amazon Resource Name (ARN) of the device instance.
                       *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                        INSTANCE_LABELS  
                      The label of the device instance.
                       *Supported operators* : ``CONTAINS``  
                        FLEET_TYPE  
                      The fleet type. Valid values are "PUBLIC" or "PRIVATE".
                       *Supported operators* : ``EQUALS``  
                    - **operator** *(string) --* 
                      Specifies how Device Farm compares the filter's attribute to the value. For the operators that are supported by each attribute, see the attribute descriptions.
                    - **values** *(list) --* 
                      An array of one or more filter values used in a device filter.
        
        **Operator Values**
                      * The IN and NOT_IN operators can take a values array that has more than one element. 
                      * The other operators require an array with a single element. 
        
        **Attribute Values**
                      * The PLATFORM attribute can be set to "ANDROID" or "IOS". 
                      * The AVAILABILITY attribute can be set to "AVAILABLE", "HIGHLY_AVAILABLE", "BUSY", or "TEMPORARY_NOT_AVAILABLE". 
                      * The FORM_FACTOR attribute can be set to "PHONE" or "TABLET". 
                      * The FLEET_TYPE attribute can be set to "PUBLIC" or "PRIVATE". 
                      - *(string) --* 
                - **matchedDevicesCount** *(integer) --* 
                  The number of devices that matched the device filter selection criteria.
                - **maxDevices** *(integer) --* 
                  The maximum number of devices to be selected by a device filter and included in a test run.
        :type arn: string
        :param arn: **[REQUIRED]**
          The run\'s ARN.
        :rtype: dict
        :returns:
        """
        pass

    def get_suite(self, arn: str) -> Dict:
        """
        Gets information about a suite.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetSuite>`_
        
        **Request Syntax**
        ::
          response = client.get_suite(
              arn='string'
          )
        
        **Response Syntax**
        ::
            {
                'suite': {
                    'arn': 'string',
                    'name': 'string',
                    'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
                    'created': datetime(2015, 1, 1),
                    'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                    'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                    'started': datetime(2015, 1, 1),
                    'stopped': datetime(2015, 1, 1),
                    'counters': {
                        'total': 123,
                        'passed': 123,
                        'failed': 123,
                        'warned': 123,
                        'errored': 123,
                        'stopped': 123,
                        'skipped': 123
                    },
                    'message': 'string',
                    'deviceMinutes': {
                        'total': 123.0,
                        'metered': 123.0,
                        'unmetered': 123.0
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of a get suite request.
            - **suite** *(dict) --* 
              A collection of one or more tests.
              - **arn** *(string) --* 
                The suite's ARN.
              - **name** *(string) --* 
                The suite's name.
              - **type** *(string) --* 
                The suite's type.
                Must be one of the following values:
                * BUILTIN_FUZZ: The built-in fuzz type. 
                * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
                * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
                * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
                * APPIUM_PYTHON: The Appium Python type. 
                * APPIUM_NODE: The Appium Node.js type. 
                * APPIUM_RUBY: The Appium Ruby type. 
                * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for web apps. 
                * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for web apps. 
                * APPIUM_WEB_PYTHON: The Appium Python type for web apps. 
                * APPIUM_WEB_NODE: The Appium Node.js type for web apps. 
                * APPIUM_WEB_RUBY: The Appium Ruby type for web apps. 
                * CALABASH: The Calabash type. 
                * INSTRUMENTATION: The Instrumentation type. 
                * UIAUTOMATION: The uiautomation type. 
                * UIAUTOMATOR: The uiautomator type. 
                * XCTEST: The XCode test type. 
                * XCTEST_UI: The XCode UI test type. 
              - **created** *(datetime) --* 
                When the suite was created.
              - **status** *(string) --* 
                The suite's status.
                Allowed values include:
                * PENDING: A pending status. 
                * PENDING_CONCURRENCY: A pending concurrency status. 
                * PENDING_DEVICE: A pending device status. 
                * PROCESSING: A processing status. 
                * SCHEDULING: A scheduling status. 
                * PREPARING: A preparing status. 
                * RUNNING: A running status. 
                * COMPLETED: A completed status. 
                * STOPPING: A stopping status. 
              - **result** *(string) --* 
                The suite's result.
                Allowed values include:
                * PENDING: A pending condition. 
                * PASSED: A passing condition. 
                * WARNED: A warning condition. 
                * FAILED: A failed condition. 
                * SKIPPED: A skipped condition. 
                * ERRORED: An error condition. 
                * STOPPED: A stopped condition. 
              - **started** *(datetime) --* 
                The suite's start time.
              - **stopped** *(datetime) --* 
                The suite's stop time.
              - **counters** *(dict) --* 
                The suite's result counters.
                - **total** *(integer) --* 
                  The total number of entities.
                - **passed** *(integer) --* 
                  The number of passed entities.
                - **failed** *(integer) --* 
                  The number of failed entities.
                - **warned** *(integer) --* 
                  The number of warned entities.
                - **errored** *(integer) --* 
                  The number of errored entities.
                - **stopped** *(integer) --* 
                  The number of stopped entities.
                - **skipped** *(integer) --* 
                  The number of skipped entities.
              - **message** *(string) --* 
                A message about the suite's result.
              - **deviceMinutes** *(dict) --* 
                Represents the total (metered or unmetered) minutes used by the test suite.
                - **total** *(float) --* 
                  When specified, represents the total minutes used by the resource to run tests.
                - **metered** *(float) --* 
                  When specified, represents only the sum of metered minutes used by the resource to run tests.
                - **unmetered** *(float) --* 
                  When specified, represents only the sum of unmetered minutes used by the resource to run tests.
        :type arn: string
        :param arn: **[REQUIRED]**
          The suite\'s ARN.
        :rtype: dict
        :returns:
        """
        pass

    def get_test(self, arn: str) -> Dict:
        """
        Gets information about a test.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetTest>`_
        
        **Request Syntax**
        ::
          response = client.get_test(
              arn='string'
          )
        
        **Response Syntax**
        ::
            {
                'test': {
                    'arn': 'string',
                    'name': 'string',
                    'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
                    'created': datetime(2015, 1, 1),
                    'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                    'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                    'started': datetime(2015, 1, 1),
                    'stopped': datetime(2015, 1, 1),
                    'counters': {
                        'total': 123,
                        'passed': 123,
                        'failed': 123,
                        'warned': 123,
                        'errored': 123,
                        'stopped': 123,
                        'skipped': 123
                    },
                    'message': 'string',
                    'deviceMinutes': {
                        'total': 123.0,
                        'metered': 123.0,
                        'unmetered': 123.0
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of a get test request.
            - **test** *(dict) --* 
              A test condition that is evaluated.
              - **arn** *(string) --* 
                The test's ARN.
              - **name** *(string) --* 
                The test's name.
              - **type** *(string) --* 
                The test's type.
                Must be one of the following values:
                * BUILTIN_FUZZ: The built-in fuzz type. 
                * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
                * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
                * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
                * APPIUM_PYTHON: The Appium Python type. 
                * APPIUM_NODE: The Appium Node.js type. 
                * APPIUM_RUBY: The Appium Ruby type. 
                * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for web apps. 
                * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for web apps. 
                * APPIUM_WEB_PYTHON: The Appium Python type for web apps. 
                * APPIUM_WEB_NODE: The Appium Node.js type for web apps. 
                * APPIUM_WEB_RUBY: The Appium Ruby type for web apps. 
                * CALABASH: The Calabash type. 
                * INSTRUMENTATION: The Instrumentation type. 
                * UIAUTOMATION: The uiautomation type. 
                * UIAUTOMATOR: The uiautomator type. 
                * XCTEST: The XCode test type. 
                * XCTEST_UI: The XCode UI test type. 
              - **created** *(datetime) --* 
                When the test was created.
              - **status** *(string) --* 
                The test's status.
                Allowed values include:
                * PENDING: A pending status. 
                * PENDING_CONCURRENCY: A pending concurrency status. 
                * PENDING_DEVICE: A pending device status. 
                * PROCESSING: A processing status. 
                * SCHEDULING: A scheduling status. 
                * PREPARING: A preparing status. 
                * RUNNING: A running status. 
                * COMPLETED: A completed status. 
                * STOPPING: A stopping status. 
              - **result** *(string) --* 
                The test's result.
                Allowed values include:
                * PENDING: A pending condition. 
                * PASSED: A passing condition. 
                * WARNED: A warning condition. 
                * FAILED: A failed condition. 
                * SKIPPED: A skipped condition. 
                * ERRORED: An error condition. 
                * STOPPED: A stopped condition. 
              - **started** *(datetime) --* 
                The test's start time.
              - **stopped** *(datetime) --* 
                The test's stop time.
              - **counters** *(dict) --* 
                The test's result counters.
                - **total** *(integer) --* 
                  The total number of entities.
                - **passed** *(integer) --* 
                  The number of passed entities.
                - **failed** *(integer) --* 
                  The number of failed entities.
                - **warned** *(integer) --* 
                  The number of warned entities.
                - **errored** *(integer) --* 
                  The number of errored entities.
                - **stopped** *(integer) --* 
                  The number of stopped entities.
                - **skipped** *(integer) --* 
                  The number of skipped entities.
              - **message** *(string) --* 
                A message about the test's result.
              - **deviceMinutes** *(dict) --* 
                Represents the total (metered or unmetered) minutes used by the test.
                - **total** *(float) --* 
                  When specified, represents the total minutes used by the resource to run tests.
                - **metered** *(float) --* 
                  When specified, represents only the sum of metered minutes used by the resource to run tests.
                - **unmetered** *(float) --* 
                  When specified, represents only the sum of unmetered minutes used by the resource to run tests.
        :type arn: string
        :param arn: **[REQUIRED]**
          The test\'s ARN.
        :rtype: dict
        :returns:
        """
        pass

    def get_upload(self, arn: str) -> Dict:
        """
        Gets information about an upload.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetUpload>`_
        
        **Request Syntax**
        ::
          response = client.get_upload(
              arn='string'
          )
        
        **Response Syntax**
        ::
            {
                'upload': {
                    'arn': 'string',
                    'name': 'string',
                    'created': datetime(2015, 1, 1),
                    'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_NODE_TEST_PACKAGE'|'APPIUM_RUBY_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_NODE_TEST_PACKAGE'|'APPIUM_WEB_RUBY_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE'|'APPIUM_JAVA_JUNIT_TEST_SPEC'|'APPIUM_JAVA_TESTNG_TEST_SPEC'|'APPIUM_PYTHON_TEST_SPEC'|'APPIUM_NODE_TEST_SPEC'|'APPIUM_RUBY_TEST_SPEC'|'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC'|'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC'|'APPIUM_WEB_PYTHON_TEST_SPEC'|'APPIUM_WEB_NODE_TEST_SPEC'|'APPIUM_WEB_RUBY_TEST_SPEC'|'INSTRUMENTATION_TEST_SPEC'|'XCTEST_UI_TEST_SPEC',
                    'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
                    'url': 'string',
                    'metadata': 'string',
                    'contentType': 'string',
                    'message': 'string',
                    'category': 'CURATED'|'PRIVATE'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of a get upload request.
            - **upload** *(dict) --* 
              An app or a set of one or more tests to upload or that have been uploaded.
              - **arn** *(string) --* 
                The upload's ARN.
              - **name** *(string) --* 
                The upload's file name.
              - **created** *(datetime) --* 
                When the upload was created.
              - **type** *(string) --* 
                The upload's type.
                Must be one of the following values:
                * ANDROID_APP: An Android upload. 
                * IOS_APP: An iOS upload. 
                * WEB_APP: A web appliction upload. 
                * EXTERNAL_DATA: An external data upload. 
                * APPIUM_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload. 
                * APPIUM_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload. 
                * APPIUM_PYTHON_TEST_PACKAGE: An Appium Python test package upload. 
                * APPIUM_NODE_TEST_PACKAGE: An Appium Node.js test package upload. 
                * APPIUM_RUBY_TEST_PACKAGE: An Appium Ruby test package upload. 
                * APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload for web apps. 
                * APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload for web apps. 
                * APPIUM_WEB_PYTHON_TEST_PACKAGE: An Appium Python test package upload for web apps. 
                * APPIUM_WEB_NODE_TEST_PACKAGE: An Appium Node.js test package upload for web apps. 
                * APPIUM_WEB_RUBY_TEST_PACKAGE: An Appium Ruby test package upload for web apps. 
                * CALABASH_TEST_PACKAGE: A Calabash test package upload. 
                * INSTRUMENTATION_TEST_PACKAGE: An instrumentation upload. 
                * UIAUTOMATION_TEST_PACKAGE: A uiautomation test package upload. 
                * UIAUTOMATOR_TEST_PACKAGE: A uiautomator test package upload. 
                * XCTEST_TEST_PACKAGE: An XCode test package upload. 
                * XCTEST_UI_TEST_PACKAGE: An XCode UI test package upload. 
                * APPIUM_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload. 
                * APPIUM_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload. 
                * APPIUM_PYTHON_TEST_SPEC: An Appium Python test spec upload. 
                * APPIUM_NODE_TEST_SPEC: An Appium Node.js test spec upload. 
                * APPIUM_RUBY_TEST_SPEC: An Appium Ruby test spec upload. 
                * APPIUM_WEB_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload for a web app. 
                * APPIUM_WEB_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload for a web app. 
                * APPIUM_WEB_PYTHON_TEST_SPEC: An Appium Python test spec upload for a web app. 
                * APPIUM_WEB_NODE_TEST_SPEC: An Appium Node.js test spec upload for a web app. 
                * APPIUM_WEB_RUBY_TEST_SPEC: An Appium Ruby test spec upload for a web app. 
                * INSTRUMENTATION_TEST_SPEC: An instrumentation test spec upload. 
                * XCTEST_UI_TEST_SPEC: An XCode UI test spec upload. 
              - **status** *(string) --* 
                The upload's status.
                Must be one of the following values:
                * FAILED: A failed status. 
                * INITIALIZED: An initialized status. 
                * PROCESSING: A processing status. 
                * SUCCEEDED: A succeeded status. 
              - **url** *(string) --* 
                The pre-signed Amazon S3 URL that was used to store a file through a corresponding PUT request.
              - **metadata** *(string) --* 
                The upload's metadata. For example, for Android, this contains information that is parsed from the manifest and is displayed in the AWS Device Farm console after the associated app is uploaded.
              - **contentType** *(string) --* 
                The upload's content type (for example, "application/octet-stream").
              - **message** *(string) --* 
                A message about the upload's result.
              - **category** *(string) --* 
                The upload's category. Allowed values include:
                * CURATED: An upload managed by AWS Device Farm. 
                * PRIVATE: An upload managed by the AWS Device Farm customer. 
        :type arn: string
        :param arn: **[REQUIRED]**
          The upload\'s ARN.
        :rtype: dict
        :returns:
        """
        pass

    def get_vpce_configuration(self, arn: str) -> Dict:
        """
        Returns information about the configuration settings for your Amazon Virtual Private Cloud (VPC) endpoint.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetVPCEConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.get_vpce_configuration(
              arn='string'
          )
        
        **Response Syntax**
        ::
            {
                'vpceConfiguration': {
                    'arn': 'string',
                    'vpceConfigurationName': 'string',
                    'vpceServiceName': 'string',
                    'serviceDnsName': 'string',
                    'vpceConfigurationDescription': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **vpceConfiguration** *(dict) --* 
              An object containing information about your VPC endpoint configuration.
              - **arn** *(string) --* 
                The Amazon Resource Name (ARN) of the VPC endpoint configuration.
              - **vpceConfigurationName** *(string) --* 
                The friendly name you give to your VPC endpoint configuration, to manage your configurations more easily.
              - **vpceServiceName** *(string) --* 
                The name of the VPC endpoint service running inside your AWS account that you want Device Farm to test.
              - **serviceDnsName** *(string) --* 
                The DNS name that maps to the private IP address of the service you want to access.
              - **vpceConfigurationDescription** *(string) --* 
                An optional description, providing more details about your VPC endpoint configuration.
        :type arn: string
        :param arn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the VPC endpoint configuration you want to describe.
        :rtype: dict
        :returns:
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

    def install_to_remote_access_session(self, remoteAccessSessionArn: str, appArn: str) -> Dict:
        """
        Installs an application to the device in a remote access session. For Android applications, the file must be in .apk format. For iOS applications, the file must be in .ipa format.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/InstallToRemoteAccessSession>`_
        
        **Request Syntax**
        ::
          response = client.install_to_remote_access_session(
              remoteAccessSessionArn='string',
              appArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'appUpload': {
                    'arn': 'string',
                    'name': 'string',
                    'created': datetime(2015, 1, 1),
                    'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_NODE_TEST_PACKAGE'|'APPIUM_RUBY_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_NODE_TEST_PACKAGE'|'APPIUM_WEB_RUBY_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE'|'APPIUM_JAVA_JUNIT_TEST_SPEC'|'APPIUM_JAVA_TESTNG_TEST_SPEC'|'APPIUM_PYTHON_TEST_SPEC'|'APPIUM_NODE_TEST_SPEC'|'APPIUM_RUBY_TEST_SPEC'|'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC'|'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC'|'APPIUM_WEB_PYTHON_TEST_SPEC'|'APPIUM_WEB_NODE_TEST_SPEC'|'APPIUM_WEB_RUBY_TEST_SPEC'|'INSTRUMENTATION_TEST_SPEC'|'XCTEST_UI_TEST_SPEC',
                    'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
                    'url': 'string',
                    'metadata': 'string',
                    'contentType': 'string',
                    'message': 'string',
                    'category': 'CURATED'|'PRIVATE'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the response from the server after AWS Device Farm makes a request to install to a remote access session.
            - **appUpload** *(dict) --* 
              An app to upload or that has been uploaded.
              - **arn** *(string) --* 
                The upload's ARN.
              - **name** *(string) --* 
                The upload's file name.
              - **created** *(datetime) --* 
                When the upload was created.
              - **type** *(string) --* 
                The upload's type.
                Must be one of the following values:
                * ANDROID_APP: An Android upload. 
                * IOS_APP: An iOS upload. 
                * WEB_APP: A web appliction upload. 
                * EXTERNAL_DATA: An external data upload. 
                * APPIUM_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload. 
                * APPIUM_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload. 
                * APPIUM_PYTHON_TEST_PACKAGE: An Appium Python test package upload. 
                * APPIUM_NODE_TEST_PACKAGE: An Appium Node.js test package upload. 
                * APPIUM_RUBY_TEST_PACKAGE: An Appium Ruby test package upload. 
                * APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload for web apps. 
                * APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload for web apps. 
                * APPIUM_WEB_PYTHON_TEST_PACKAGE: An Appium Python test package upload for web apps. 
                * APPIUM_WEB_NODE_TEST_PACKAGE: An Appium Node.js test package upload for web apps. 
                * APPIUM_WEB_RUBY_TEST_PACKAGE: An Appium Ruby test package upload for web apps. 
                * CALABASH_TEST_PACKAGE: A Calabash test package upload. 
                * INSTRUMENTATION_TEST_PACKAGE: An instrumentation upload. 
                * UIAUTOMATION_TEST_PACKAGE: A uiautomation test package upload. 
                * UIAUTOMATOR_TEST_PACKAGE: A uiautomator test package upload. 
                * XCTEST_TEST_PACKAGE: An XCode test package upload. 
                * XCTEST_UI_TEST_PACKAGE: An XCode UI test package upload. 
                * APPIUM_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload. 
                * APPIUM_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload. 
                * APPIUM_PYTHON_TEST_SPEC: An Appium Python test spec upload. 
                * APPIUM_NODE_TEST_SPEC: An Appium Node.js test spec upload. 
                * APPIUM_RUBY_TEST_SPEC: An Appium Ruby test spec upload. 
                * APPIUM_WEB_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload for a web app. 
                * APPIUM_WEB_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload for a web app. 
                * APPIUM_WEB_PYTHON_TEST_SPEC: An Appium Python test spec upload for a web app. 
                * APPIUM_WEB_NODE_TEST_SPEC: An Appium Node.js test spec upload for a web app. 
                * APPIUM_WEB_RUBY_TEST_SPEC: An Appium Ruby test spec upload for a web app. 
                * INSTRUMENTATION_TEST_SPEC: An instrumentation test spec upload. 
                * XCTEST_UI_TEST_SPEC: An XCode UI test spec upload. 
              - **status** *(string) --* 
                The upload's status.
                Must be one of the following values:
                * FAILED: A failed status. 
                * INITIALIZED: An initialized status. 
                * PROCESSING: A processing status. 
                * SUCCEEDED: A succeeded status. 
              - **url** *(string) --* 
                The pre-signed Amazon S3 URL that was used to store a file through a corresponding PUT request.
              - **metadata** *(string) --* 
                The upload's metadata. For example, for Android, this contains information that is parsed from the manifest and is displayed in the AWS Device Farm console after the associated app is uploaded.
              - **contentType** *(string) --* 
                The upload's content type (for example, "application/octet-stream").
              - **message** *(string) --* 
                A message about the upload's result.
              - **category** *(string) --* 
                The upload's category. Allowed values include:
                * CURATED: An upload managed by AWS Device Farm. 
                * PRIVATE: An upload managed by the AWS Device Farm customer. 
        :type remoteAccessSessionArn: string
        :param remoteAccessSessionArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the remote access session about which you are requesting information.
        :type appArn: string
        :param appArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the app about which you are requesting information.
        :rtype: dict
        :returns:
        """
        pass

    def list_artifacts(self, arn: str, type: str, nextToken: str = None) -> Dict:
        """
        Gets information about artifacts.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListArtifacts>`_
        
        **Request Syntax**
        ::
          response = client.list_artifacts(
              arn='string',
              type='SCREENSHOT'|'FILE'|'LOG',
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'artifacts': [
                    {
                        'arn': 'string',
                        'name': 'string',
                        'type': 'UNKNOWN'|'SCREENSHOT'|'DEVICE_LOG'|'MESSAGE_LOG'|'VIDEO_LOG'|'RESULT_LOG'|'SERVICE_LOG'|'WEBKIT_LOG'|'INSTRUMENTATION_OUTPUT'|'EXERCISER_MONKEY_OUTPUT'|'CALABASH_JSON_OUTPUT'|'CALABASH_PRETTY_OUTPUT'|'CALABASH_STANDARD_OUTPUT'|'CALABASH_JAVA_XML_OUTPUT'|'AUTOMATION_OUTPUT'|'APPIUM_SERVER_OUTPUT'|'APPIUM_JAVA_OUTPUT'|'APPIUM_JAVA_XML_OUTPUT'|'APPIUM_PYTHON_OUTPUT'|'APPIUM_PYTHON_XML_OUTPUT'|'EXPLORER_EVENT_LOG'|'EXPLORER_SUMMARY_LOG'|'APPLICATION_CRASH_REPORT'|'XCTEST_LOG'|'VIDEO'|'CUSTOMER_ARTIFACT'|'CUSTOMER_ARTIFACT_LOG'|'TESTSPEC_OUTPUT',
                        'extension': 'string',
                        'url': 'string'
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of a list artifacts operation.
            - **artifacts** *(list) --* 
              Information about the artifacts.
              - *(dict) --* 
                Represents the output of a test. Examples of artifacts include logs and screenshots.
                - **arn** *(string) --* 
                  The artifact's ARN.
                - **name** *(string) --* 
                  The artifact's name.
                - **type** *(string) --* 
                  The artifact's type.
                  Allowed values include the following:
                  * UNKNOWN: An unknown type. 
                  * SCREENSHOT: The screenshot type. 
                  * DEVICE_LOG: The device log type. 
                  * MESSAGE_LOG: The message log type. 
                  * VIDEO_LOG: The video log type. 
                  * RESULT_LOG: The result log type. 
                  * SERVICE_LOG: The service log type. 
                  * WEBKIT_LOG: The web kit log type. 
                  * INSTRUMENTATION_OUTPUT: The instrumentation type. 
                  * EXERCISER_MONKEY_OUTPUT: For Android, the artifact (log) generated by an Android fuzz test. 
                  * CALABASH_JSON_OUTPUT: The Calabash JSON output type. 
                  * CALABASH_PRETTY_OUTPUT: The Calabash pretty output type. 
                  * CALABASH_STANDARD_OUTPUT: The Calabash standard output type. 
                  * CALABASH_JAVA_XML_OUTPUT: The Calabash Java XML output type. 
                  * AUTOMATION_OUTPUT: The automation output type. 
                  * APPIUM_SERVER_OUTPUT: The Appium server output type. 
                  * APPIUM_JAVA_OUTPUT: The Appium Java output type. 
                  * APPIUM_JAVA_XML_OUTPUT: The Appium Java XML output type. 
                  * APPIUM_PYTHON_OUTPUT: The Appium Python output type. 
                  * APPIUM_PYTHON_XML_OUTPUT: The Appium Python XML output type. 
                  * EXPLORER_EVENT_LOG: The Explorer event log output type. 
                  * EXPLORER_SUMMARY_LOG: The Explorer summary log output type. 
                  * APPLICATION_CRASH_REPORT: The application crash report output type. 
                  * XCTEST_LOG: The XCode test output type. 
                  * VIDEO: The Video output type. 
                  * CUSTOMER_ARTIFACT:The Customer Artifact output type. 
                  * CUSTOMER_ARTIFACT_LOG: The Customer Artifact Log output type. 
                  * TESTSPEC_OUTPUT: The Test Spec Output type. 
                - **extension** *(string) --* 
                  The artifact's file extension.
                - **url** *(string) --* 
                  The pre-signed Amazon S3 URL that can be used with a corresponding GET request to download the artifact's file.
            - **nextToken** *(string) --* 
              If the number of items that are returned is significantly large, this is an identifier that is also returned, which can be used in a subsequent call to this operation to return the next set of items in the list.
        :type arn: string
        :param arn: **[REQUIRED]**
          The Run, Job, Suite, or Test ARN.
        :type type: string
        :param type: **[REQUIRED]**
          The artifacts\' type.
          Allowed values include:
          * FILE: The artifacts are files.
          * LOG: The artifacts are logs.
          * SCREENSHOT: The artifacts are screenshots.
        :type nextToken: string
        :param nextToken:
          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :rtype: dict
        :returns:
        """
        pass

    def list_device_instances(self, maxResults: int = None, nextToken: str = None) -> Dict:
        """
        Returns information about the private device instances associated with one or more AWS accounts.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListDeviceInstances>`_
        
        **Request Syntax**
        ::
          response = client.list_device_instances(
              maxResults=123,
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'deviceInstances': [
                    {
                        'arn': 'string',
                        'deviceArn': 'string',
                        'labels': [
                            'string',
                        ],
                        'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                        'udid': 'string',
                        'instanceProfile': {
                            'arn': 'string',
                            'packageCleanup': True|False,
                            'excludeAppPackagesFromCleanup': [
                                'string',
                            ],
                            'rebootAfterUse': True|False,
                            'name': 'string',
                            'description': 'string'
                        }
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **deviceInstances** *(list) --* 
              An object containing information about your device instances.
              - *(dict) --* 
                Represents the device instance.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the device instance.
                - **deviceArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the device.
                - **labels** *(list) --* 
                  An array of strings describing the device instance.
                  - *(string) --* 
                - **status** *(string) --* 
                  The status of the device instance. Valid values are listed below.
                - **udid** *(string) --* 
                  Unique device identifier for the device instance.
                - **instanceProfile** *(dict) --* 
                  A object containing information about the instance profile.
                  - **arn** *(string) --* 
                    The Amazon Resource Name (ARN) of the instance profile.
                  - **packageCleanup** *(boolean) --* 
                    When set to ``true`` , Device Farm will remove app packages after a test run. The default value is ``false`` for private devices.
                  - **excludeAppPackagesFromCleanup** *(list) --* 
                    An array of strings specifying the list of app packages that should not be cleaned up from the device after a test run is over.
                    The list of packages is only considered if you set ``packageCleanup`` to ``true`` .
                    - *(string) --* 
                  - **rebootAfterUse** *(boolean) --* 
                    When set to ``true`` , Device Farm will reboot the instance after a test run. The default value is ``true`` .
                  - **name** *(string) --* 
                    The name of the instance profile.
                  - **description** *(string) --* 
                    The description of the instance profile.
            - **nextToken** *(string) --* 
              An identifier that can be used in the next call to this operation to return the next set of items in the list.
        :type maxResults: integer
        :param maxResults:
          An integer specifying the maximum number of items you want to return in the API response.
        :type nextToken: string
        :param nextToken:
          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :rtype: dict
        :returns:
        """
        pass

    def list_device_pools(self, arn: str, type: str = None, nextToken: str = None) -> Dict:
        """
        Gets information about device pools.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListDevicePools>`_
        
        **Request Syntax**
        ::
          response = client.list_device_pools(
              arn='string',
              type='CURATED'|'PRIVATE',
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'devicePools': [
                    {
                        'arn': 'string',
                        'name': 'string',
                        'description': 'string',
                        'type': 'CURATED'|'PRIVATE',
                        'rules': [
                            {
                                'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE'|'OS_VERSION'|'MODEL'|'AVAILABILITY',
                                'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                                'value': 'string'
                            },
                        ],
                        'maxDevices': 123
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of a list device pools request.
            - **devicePools** *(list) --* 
              Information about the device pools.
              - *(dict) --* 
                Represents a collection of device types.
                - **arn** *(string) --* 
                  The device pool's ARN.
                - **name** *(string) --* 
                  The device pool's name.
                - **description** *(string) --* 
                  The device pool's description.
                - **type** *(string) --* 
                  The device pool's type.
                  Allowed values include:
                  * CURATED: A device pool that is created and managed by AWS Device Farm. 
                  * PRIVATE: A device pool that is created and managed by the device pool developer. 
                - **rules** *(list) --* 
                  Information about the device pool's rules.
                  - *(dict) --* 
                    Represents a condition for a device pool.
                    - **attribute** *(string) --* 
                      The rule's stringified attribute. For example, specify the value as ``"\"abc\""`` .
                      The supported operators for each attribute are provided in the following list.
                        APPIUM_VERSION  
                      The Appium version for the test.
                       *Supported operators* : ``CONTAINS``  
                        ARN  
                      The Amazon Resource Name (ARN) of the device. For example, "arn:aws:devicefarm:us-west-2::device:12345Example".
                       *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                        AVAILABILITY  
                      The current availability of the device. Valid values are "AVAILABLE", "HIGHLY_AVAILABLE", "BUSY", or "TEMPORARY_NOT_AVAILABLE".
                       *Supported operators* : ``EQUALS``  
                        FLEET_TYPE  
                      The fleet type. Valid values are "PUBLIC" or "PRIVATE".
                       *Supported operators* : ``EQUALS``  
                        FORM_FACTOR  
                      The device form factor. Valid values are "PHONE" or "TABLET".
                       *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                        INSTANCE_ARN  
                      The Amazon Resource Name (ARN) of the device instance.
                       *Supported operators* : ``IN`` , ``NOT_IN``  
                        INSTANCE_LABELS  
                      The label of the device instance.
                       *Supported operators* : ``CONTAINS``  
                        MANUFACTURER  
                      The device manufacturer. For example, "Apple".
                       *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                        MODEL  
                      The device model, such as "Apple iPad Air 2" or "Google Pixel".
                       *Supported operators* : ``CONTAINS`` , ``EQUALS`` , ``IN`` , ``NOT_IN``  
                        OS_VERSION  
                      The operating system version. For example, "10.3.2".
                       *Supported operators* : ``EQUALS`` , ``GREATER_THAN`` , ``GREATER_THAN_OR_EQUALS`` , ``IN`` , ``LESS_THAN`` , ``LESS_THAN_OR_EQUALS`` , ``NOT_IN``  
                        PLATFORM  
                      The device platform. Valid values are "ANDROID" or "IOS".
                       *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                        REMOTE_ACCESS_ENABLED  
                      Whether the device is enabled for remote access. Valid values are "TRUE" or "FALSE".
                       *Supported operators* : ``EQUALS``  
                        REMOTE_DEBUG_ENABLED  
                      Whether the device is enabled for remote debugging. Valid values are "TRUE" or "FALSE".
                       *Supported operators* : ``EQUALS``  
                    - **operator** *(string) --* 
                      Specifies how Device Farm compares the rule's attribute to the value. For the operators that are supported by each attribute, see the attribute descriptions.
                    - **value** *(string) --* 
                      The rule's value.
                - **maxDevices** *(integer) --* 
                  The number of devices that Device Farm can add to your device pool. Device Farm adds devices that are available and that meet the criteria that you assign for the ``rules`` parameter. Depending on how many devices meet these constraints, your device pool might contain fewer devices than the value for this parameter.
                  By specifying the maximum number of devices, you can control the costs that you incur by running tests.
            - **nextToken** *(string) --* 
              If the number of items that are returned is significantly large, this is an identifier that is also returned, which can be used in a subsequent call to this operation to return the next set of items in the list.
        :type arn: string
        :param arn: **[REQUIRED]**
          The project ARN.
        :type type: string
        :param type:
          The device pools\' type.
          Allowed values include:
          * CURATED: A device pool that is created and managed by AWS Device Farm.
          * PRIVATE: A device pool that is created and managed by the device pool developer.
        :type nextToken: string
        :param nextToken:
          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :rtype: dict
        :returns:
        """
        pass

    def list_devices(self, arn: str = None, nextToken: str = None, filters: List = None) -> Dict:
        """
        Gets information about unique device types.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListDevices>`_
        
        **Request Syntax**
        ::
          response = client.list_devices(
              arn='string',
              nextToken='string',
              filters=[
                  {
                      'attribute': 'ARN'|'PLATFORM'|'OS_VERSION'|'MODEL'|'AVAILABILITY'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                      'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                      'values': [
                          'string',
                      ]
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'devices': [
                    {
                        'arn': 'string',
                        'name': 'string',
                        'manufacturer': 'string',
                        'model': 'string',
                        'modelId': 'string',
                        'formFactor': 'PHONE'|'TABLET',
                        'platform': 'ANDROID'|'IOS',
                        'os': 'string',
                        'cpu': {
                            'frequency': 'string',
                            'architecture': 'string',
                            'clock': 123.0
                        },
                        'resolution': {
                            'width': 123,
                            'height': 123
                        },
                        'heapSize': 123,
                        'memory': 123,
                        'image': 'string',
                        'carrier': 'string',
                        'radio': 'string',
                        'remoteAccessEnabled': True|False,
                        'remoteDebugEnabled': True|False,
                        'fleetType': 'string',
                        'fleetName': 'string',
                        'instances': [
                            {
                                'arn': 'string',
                                'deviceArn': 'string',
                                'labels': [
                                    'string',
                                ],
                                'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                                'udid': 'string',
                                'instanceProfile': {
                                    'arn': 'string',
                                    'packageCleanup': True|False,
                                    'excludeAppPackagesFromCleanup': [
                                        'string',
                                    ],
                                    'rebootAfterUse': True|False,
                                    'name': 'string',
                                    'description': 'string'
                                }
                            },
                        ],
                        'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of a list devices operation.
            - **devices** *(list) --* 
              Information about the devices.
              - *(dict) --* 
                Represents a device type that an app is tested against.
                - **arn** *(string) --* 
                  The device's ARN.
                - **name** *(string) --* 
                  The device's display name.
                - **manufacturer** *(string) --* 
                  The device's manufacturer name.
                - **model** *(string) --* 
                  The device's model name.
                - **modelId** *(string) --* 
                  The device's model ID.
                - **formFactor** *(string) --* 
                  The device's form factor.
                  Allowed values include:
                  * PHONE: The phone form factor. 
                  * TABLET: The tablet form factor. 
                - **platform** *(string) --* 
                  The device's platform.
                  Allowed values include:
                  * ANDROID: The Android platform. 
                  * IOS: The iOS platform. 
                - **os** *(string) --* 
                  The device's operating system type.
                - **cpu** *(dict) --* 
                  Information about the device's CPU.
                  - **frequency** *(string) --* 
                    The CPU's frequency.
                  - **architecture** *(string) --* 
                    The CPU's architecture, for example x86 or ARM.
                  - **clock** *(float) --* 
                    The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.
                - **resolution** *(dict) --* 
                  The resolution of the device.
                  - **width** *(integer) --* 
                    The screen resolution's width, expressed in pixels.
                  - **height** *(integer) --* 
                    The screen resolution's height, expressed in pixels.
                - **heapSize** *(integer) --* 
                  The device's heap size, expressed in bytes.
                - **memory** *(integer) --* 
                  The device's total memory size, expressed in bytes.
                - **image** *(string) --* 
                  The device's image name.
                - **carrier** *(string) --* 
                  The device's carrier.
                - **radio** *(string) --* 
                  The device's radio.
                - **remoteAccessEnabled** *(boolean) --* 
                  Specifies whether remote access has been enabled for the specified device.
                - **remoteDebugEnabled** *(boolean) --* 
                  This flag is set to ``true`` if remote debugging is enabled for the device.
                - **fleetType** *(string) --* 
                  The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.
                - **fleetName** *(string) --* 
                  The name of the fleet to which this device belongs.
                - **instances** *(list) --* 
                  The instances belonging to this device.
                  - *(dict) --* 
                    Represents the device instance.
                    - **arn** *(string) --* 
                      The Amazon Resource Name (ARN) of the device instance.
                    - **deviceArn** *(string) --* 
                      The Amazon Resource Name (ARN) of the device.
                    - **labels** *(list) --* 
                      An array of strings describing the device instance.
                      - *(string) --* 
                    - **status** *(string) --* 
                      The status of the device instance. Valid values are listed below.
                    - **udid** *(string) --* 
                      Unique device identifier for the device instance.
                    - **instanceProfile** *(dict) --* 
                      A object containing information about the instance profile.
                      - **arn** *(string) --* 
                        The Amazon Resource Name (ARN) of the instance profile.
                      - **packageCleanup** *(boolean) --* 
                        When set to ``true`` , Device Farm will remove app packages after a test run. The default value is ``false`` for private devices.
                      - **excludeAppPackagesFromCleanup** *(list) --* 
                        An array of strings specifying the list of app packages that should not be cleaned up from the device after a test run is over.
                        The list of packages is only considered if you set ``packageCleanup`` to ``true`` .
                        - *(string) --* 
                      - **rebootAfterUse** *(boolean) --* 
                        When set to ``true`` , Device Farm will reboot the instance after a test run. The default value is ``true`` .
                      - **name** *(string) --* 
                        The name of the instance profile.
                      - **description** *(string) --* 
                        The description of the instance profile.
                - **availability** *(string) --* 
                  Reflects how likely a device will be available for a test run. It is currently available in the ListDevices and GetDevice API methods.
            - **nextToken** *(string) --* 
              If the number of items that are returned is significantly large, this is an identifier that is also returned, which can be used in a subsequent call to this operation to return the next set of items in the list.
        :type arn: string
        :param arn:
          The Amazon Resource Name (ARN) of the project.
        :type nextToken: string
        :param nextToken:
          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type filters: list
        :param filters:
          Used to select a set of devices. A filter is made up of an attribute, an operator, and one or more values.
          * Attribute: The aspect of a device such as platform or model used as the selction criteria in a device filter. Allowed values include:
            * ARN: The Amazon Resource Name (ARN) of the device. For example, \"arn:aws:devicefarm:us-west-2::device:12345Example\".
            * PLATFORM: The device platform. Valid values are \"ANDROID\" or \"IOS\".
            * OS_VERSION: The operating system version. For example, \"10.3.2\".
            * MODEL: The device model. For example, \"iPad 5th Gen\".
            * AVAILABILITY: The current availability of the device. Valid values are \"AVAILABLE\", \"HIGHLY_AVAILABLE\", \"BUSY\", or \"TEMPORARY_NOT_AVAILABLE\".
            * FORM_FACTOR: The device form factor. Valid values are \"PHONE\" or \"TABLET\".
            * MANUFACTURER: The device manufacturer. For example, \"Apple\".
            * REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. Valid values are \"TRUE\" or \"FALSE\".
            * REMOTE_DEBUG_ENABLED: Whether the device is enabled for remote debugging. Valid values are \"TRUE\" or \"FALSE\".
            * INSTANCE_ARN: The Amazon Resource Name (ARN) of the device instance.
            * INSTANCE_LABELS: The label of the device instance.
            * FLEET_TYPE: The fleet type. Valid values are \"PUBLIC\" or \"PRIVATE\".
          * Operator: The filter operator.
            * The EQUALS operator is available for every attribute except INSTANCE_LABELS.
            * The CONTAINS operator is available for the INSTANCE_LABELS and MODEL attributes.
            * The IN and NOT_IN operators are available for the ARN, OS_VERSION, MODEL, MANUFACTURER, and INSTANCE_ARN attributes.
            * The LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUALS, and GREATER_THAN_OR_EQUALS operators are also available for the OS_VERSION attribute.
          * Values: An array of one or more filter values.
            * The IN and NOT_IN operators take a values array that has one or more elements.
            * The other operators require an array with a single element.
            * In a request, the AVAILABILITY attribute takes \"AVAILABLE\", \"HIGHLY_AVAILABLE\", \"BUSY\", or \"TEMPORARY_NOT_AVAILABLE\" as values.
          - *(dict) --*
            Represents a device filter used to select a set of devices to be included in a test run. This data structure is passed in as the ``deviceSelectionConfiguration`` parameter to ScheduleRun. For an example of the JSON request syntax, see  ScheduleRun .
            It is also passed in as the ``filters`` parameter to ListDevices. For an example of the JSON request syntax, see  ListDevices .
            - **attribute** *(string) --*
              The aspect of a device such as platform or model used as the selection criteria in a device filter.
              The supported operators for each attribute are provided in the following list.
                ARN
              The Amazon Resource Name (ARN) of the device. For example, \"arn:aws:devicefarm:us-west-2::device:12345Example\".
               *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``
                PLATFORM
              The device platform. Valid values are \"ANDROID\" or \"IOS\".
               *Supported operators* : ``EQUALS``
                OS_VERSION
              The operating system version. For example, \"10.3.2\".
               *Supported operators* : ``EQUALS`` , ``GREATER_THAN`` , ``GREATER_THAN_OR_EQUALS`` , ``IN`` , ``LESS_THAN`` , ``LESS_THAN_OR_EQUALS`` , ``NOT_IN``
                MODEL
              The device model. For example, \"iPad 5th Gen\".
               *Supported operators* : ``CONTAINS`` , ``EQUALS`` , ``IN`` , ``NOT_IN``
                AVAILABILITY
              The current availability of the device. Valid values are \"AVAILABLE\", \"HIGHLY_AVAILABLE\", \"BUSY\", or \"TEMPORARY_NOT_AVAILABLE\".
               *Supported operators* : ``EQUALS``
                FORM_FACTOR
              The device form factor. Valid values are \"PHONE\" or \"TABLET\".
               *Supported operators* : ``EQUALS``
                MANUFACTURER
              The device manufacturer. For example, \"Apple\".
               *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``
                REMOTE_ACCESS_ENABLED
              Whether the device is enabled for remote access. Valid values are \"TRUE\" or \"FALSE\".
               *Supported operators* : ``EQUALS``
                REMOTE_DEBUG_ENABLED
              Whether the device is enabled for remote debugging. Valid values are \"TRUE\" or \"FALSE\".
               *Supported operators* : ``EQUALS``
                INSTANCE_ARN
              The Amazon Resource Name (ARN) of the device instance.
               *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``
                INSTANCE_LABELS
              The label of the device instance.
               *Supported operators* : ``CONTAINS``
                FLEET_TYPE
              The fleet type. Valid values are \"PUBLIC\" or \"PRIVATE\".
               *Supported operators* : ``EQUALS``
            - **operator** *(string) --*
              Specifies how Device Farm compares the filter\'s attribute to the value. For the operators that are supported by each attribute, see the attribute descriptions.
            - **values** *(list) --*
              An array of one or more filter values used in a device filter.
               **Operator Values**
              * The IN and NOT_IN operators can take a values array that has more than one element.
              * The other operators require an array with a single element.
               **Attribute Values**
              * The PLATFORM attribute can be set to \"ANDROID\" or \"IOS\".
              * The AVAILABILITY attribute can be set to \"AVAILABLE\", \"HIGHLY_AVAILABLE\", \"BUSY\", or \"TEMPORARY_NOT_AVAILABLE\".
              * The FORM_FACTOR attribute can be set to \"PHONE\" or \"TABLET\".
              * The FLEET_TYPE attribute can be set to \"PUBLIC\" or \"PRIVATE\".
              - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def list_instance_profiles(self, maxResults: int = None, nextToken: str = None) -> Dict:
        """
        Returns information about all the instance profiles in an AWS account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListInstanceProfiles>`_
        
        **Request Syntax**
        ::
          response = client.list_instance_profiles(
              maxResults=123,
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'instanceProfiles': [
                    {
                        'arn': 'string',
                        'packageCleanup': True|False,
                        'excludeAppPackagesFromCleanup': [
                            'string',
                        ],
                        'rebootAfterUse': True|False,
                        'name': 'string',
                        'description': 'string'
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **instanceProfiles** *(list) --* 
              An object containing information about your instance profiles.
              - *(dict) --* 
                Represents the instance profile.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the instance profile.
                - **packageCleanup** *(boolean) --* 
                  When set to ``true`` , Device Farm will remove app packages after a test run. The default value is ``false`` for private devices.
                - **excludeAppPackagesFromCleanup** *(list) --* 
                  An array of strings specifying the list of app packages that should not be cleaned up from the device after a test run is over.
                  The list of packages is only considered if you set ``packageCleanup`` to ``true`` .
                  - *(string) --* 
                - **rebootAfterUse** *(boolean) --* 
                  When set to ``true`` , Device Farm will reboot the instance after a test run. The default value is ``true`` .
                - **name** *(string) --* 
                  The name of the instance profile.
                - **description** *(string) --* 
                  The description of the instance profile.
            - **nextToken** *(string) --* 
              An identifier that can be used in the next call to this operation to return the next set of items in the list.
        :type maxResults: integer
        :param maxResults:
          An integer specifying the maximum number of items you want to return in the API response.
        :type nextToken: string
        :param nextToken:
          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :rtype: dict
        :returns:
        """
        pass

    def list_jobs(self, arn: str, nextToken: str = None) -> Dict:
        """
        Gets information about jobs for a given test run.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListJobs>`_
        
        **Request Syntax**
        ::
          response = client.list_jobs(
              arn='string',
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'jobs': [
                    {
                        'arn': 'string',
                        'name': 'string',
                        'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
                        'created': datetime(2015, 1, 1),
                        'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                        'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                        'started': datetime(2015, 1, 1),
                        'stopped': datetime(2015, 1, 1),
                        'counters': {
                            'total': 123,
                            'passed': 123,
                            'failed': 123,
                            'warned': 123,
                            'errored': 123,
                            'stopped': 123,
                            'skipped': 123
                        },
                        'message': 'string',
                        'device': {
                            'arn': 'string',
                            'name': 'string',
                            'manufacturer': 'string',
                            'model': 'string',
                            'modelId': 'string',
                            'formFactor': 'PHONE'|'TABLET',
                            'platform': 'ANDROID'|'IOS',
                            'os': 'string',
                            'cpu': {
                                'frequency': 'string',
                                'architecture': 'string',
                                'clock': 123.0
                            },
                            'resolution': {
                                'width': 123,
                                'height': 123
                            },
                            'heapSize': 123,
                            'memory': 123,
                            'image': 'string',
                            'carrier': 'string',
                            'radio': 'string',
                            'remoteAccessEnabled': True|False,
                            'remoteDebugEnabled': True|False,
                            'fleetType': 'string',
                            'fleetName': 'string',
                            'instances': [
                                {
                                    'arn': 'string',
                                    'deviceArn': 'string',
                                    'labels': [
                                        'string',
                                    ],
                                    'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                                    'udid': 'string',
                                    'instanceProfile': {
                                        'arn': 'string',
                                        'packageCleanup': True|False,
                                        'excludeAppPackagesFromCleanup': [
                                            'string',
                                        ],
                                        'rebootAfterUse': True|False,
                                        'name': 'string',
                                        'description': 'string'
                                    }
                                },
                            ],
                            'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
                        },
                        'instanceArn': 'string',
                        'deviceMinutes': {
                            'total': 123.0,
                            'metered': 123.0,
                            'unmetered': 123.0
                        },
                        'videoEndpoint': 'string',
                        'videoCapture': True|False
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of a list jobs request.
            - **jobs** *(list) --* 
              Information about the jobs.
              - *(dict) --* 
                Represents a device.
                - **arn** *(string) --* 
                  The job's ARN.
                - **name** *(string) --* 
                  The job's name.
                - **type** *(string) --* 
                  The job's type.
                  Allowed values include the following:
                  * BUILTIN_FUZZ: The built-in fuzz type. 
                  * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
                  * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
                  * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
                  * APPIUM_PYTHON: The Appium Python type. 
                  * APPIUM_NODE: The Appium Node.js type. 
                  * APPIUM_RUBY: The Appium Ruby type. 
                  * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for web apps. 
                  * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for web apps. 
                  * APPIUM_WEB_PYTHON: The Appium Python type for web apps. 
                  * APPIUM_WEB_NODE: The Appium Node.js type for web apps. 
                  * APPIUM_WEB_RUBY: The Appium Ruby test type for web apps. 
                  * CALABASH: The Calabash type. 
                  * INSTRUMENTATION: The Instrumentation type. 
                  * UIAUTOMATION: The uiautomation type. 
                  * UIAUTOMATOR: The uiautomator type. 
                  * XCTEST: The XCode test type. 
                  * XCTEST_UI: The XCode UI test type. 
                - **created** *(datetime) --* 
                  When the job was created.
                - **status** *(string) --* 
                  The job's status.
                  Allowed values include:
                  * PENDING: A pending status. 
                  * PENDING_CONCURRENCY: A pending concurrency status. 
                  * PENDING_DEVICE: A pending device status. 
                  * PROCESSING: A processing status. 
                  * SCHEDULING: A scheduling status. 
                  * PREPARING: A preparing status. 
                  * RUNNING: A running status. 
                  * COMPLETED: A completed status. 
                  * STOPPING: A stopping status. 
                - **result** *(string) --* 
                  The job's result.
                  Allowed values include:
                  * PENDING: A pending condition. 
                  * PASSED: A passing condition. 
                  * WARNED: A warning condition. 
                  * FAILED: A failed condition. 
                  * SKIPPED: A skipped condition. 
                  * ERRORED: An error condition. 
                  * STOPPED: A stopped condition. 
                - **started** *(datetime) --* 
                  The job's start time.
                - **stopped** *(datetime) --* 
                  The job's stop time.
                - **counters** *(dict) --* 
                  The job's result counters.
                  - **total** *(integer) --* 
                    The total number of entities.
                  - **passed** *(integer) --* 
                    The number of passed entities.
                  - **failed** *(integer) --* 
                    The number of failed entities.
                  - **warned** *(integer) --* 
                    The number of warned entities.
                  - **errored** *(integer) --* 
                    The number of errored entities.
                  - **stopped** *(integer) --* 
                    The number of stopped entities.
                  - **skipped** *(integer) --* 
                    The number of skipped entities.
                - **message** *(string) --* 
                  A message about the job's result.
                - **device** *(dict) --* 
                  The device (phone or tablet).
                  - **arn** *(string) --* 
                    The device's ARN.
                  - **name** *(string) --* 
                    The device's display name.
                  - **manufacturer** *(string) --* 
                    The device's manufacturer name.
                  - **model** *(string) --* 
                    The device's model name.
                  - **modelId** *(string) --* 
                    The device's model ID.
                  - **formFactor** *(string) --* 
                    The device's form factor.
                    Allowed values include:
                    * PHONE: The phone form factor. 
                    * TABLET: The tablet form factor. 
                  - **platform** *(string) --* 
                    The device's platform.
                    Allowed values include:
                    * ANDROID: The Android platform. 
                    * IOS: The iOS platform. 
                  - **os** *(string) --* 
                    The device's operating system type.
                  - **cpu** *(dict) --* 
                    Information about the device's CPU.
                    - **frequency** *(string) --* 
                      The CPU's frequency.
                    - **architecture** *(string) --* 
                      The CPU's architecture, for example x86 or ARM.
                    - **clock** *(float) --* 
                      The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.
                  - **resolution** *(dict) --* 
                    The resolution of the device.
                    - **width** *(integer) --* 
                      The screen resolution's width, expressed in pixels.
                    - **height** *(integer) --* 
                      The screen resolution's height, expressed in pixels.
                  - **heapSize** *(integer) --* 
                    The device's heap size, expressed in bytes.
                  - **memory** *(integer) --* 
                    The device's total memory size, expressed in bytes.
                  - **image** *(string) --* 
                    The device's image name.
                  - **carrier** *(string) --* 
                    The device's carrier.
                  - **radio** *(string) --* 
                    The device's radio.
                  - **remoteAccessEnabled** *(boolean) --* 
                    Specifies whether remote access has been enabled for the specified device.
                  - **remoteDebugEnabled** *(boolean) --* 
                    This flag is set to ``true`` if remote debugging is enabled for the device.
                  - **fleetType** *(string) --* 
                    The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.
                  - **fleetName** *(string) --* 
                    The name of the fleet to which this device belongs.
                  - **instances** *(list) --* 
                    The instances belonging to this device.
                    - *(dict) --* 
                      Represents the device instance.
                      - **arn** *(string) --* 
                        The Amazon Resource Name (ARN) of the device instance.
                      - **deviceArn** *(string) --* 
                        The Amazon Resource Name (ARN) of the device.
                      - **labels** *(list) --* 
                        An array of strings describing the device instance.
                        - *(string) --* 
                      - **status** *(string) --* 
                        The status of the device instance. Valid values are listed below.
                      - **udid** *(string) --* 
                        Unique device identifier for the device instance.
                      - **instanceProfile** *(dict) --* 
                        A object containing information about the instance profile.
                        - **arn** *(string) --* 
                          The Amazon Resource Name (ARN) of the instance profile.
                        - **packageCleanup** *(boolean) --* 
                          When set to ``true`` , Device Farm will remove app packages after a test run. The default value is ``false`` for private devices.
                        - **excludeAppPackagesFromCleanup** *(list) --* 
                          An array of strings specifying the list of app packages that should not be cleaned up from the device after a test run is over.
                          The list of packages is only considered if you set ``packageCleanup`` to ``true`` .
                          - *(string) --* 
                        - **rebootAfterUse** *(boolean) --* 
                          When set to ``true`` , Device Farm will reboot the instance after a test run. The default value is ``true`` .
                        - **name** *(string) --* 
                          The name of the instance profile.
                        - **description** *(string) --* 
                          The description of the instance profile.
                  - **availability** *(string) --* 
                    Reflects how likely a device will be available for a test run. It is currently available in the ListDevices and GetDevice API methods.
                - **instanceArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the instance.
                - **deviceMinutes** *(dict) --* 
                  Represents the total (metered or unmetered) minutes used by the job.
                  - **total** *(float) --* 
                    When specified, represents the total minutes used by the resource to run tests.
                  - **metered** *(float) --* 
                    When specified, represents only the sum of metered minutes used by the resource to run tests.
                  - **unmetered** *(float) --* 
                    When specified, represents only the sum of unmetered minutes used by the resource to run tests.
                - **videoEndpoint** *(string) --* 
                  The endpoint for streaming device video.
                - **videoCapture** *(boolean) --* 
                  This value is set to true if video capture is enabled; otherwise, it is set to false.
            - **nextToken** *(string) --* 
              If the number of items that are returned is significantly large, this is an identifier that is also returned, which can be used in a subsequent call to this operation to return the next set of items in the list.
        :type arn: string
        :param arn: **[REQUIRED]**
          The run\'s Amazon Resource Name (ARN).
        :type nextToken: string
        :param nextToken:
          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :rtype: dict
        :returns:
        """
        pass

    def list_network_profiles(self, arn: str, type: str = None, nextToken: str = None) -> Dict:
        """
        Returns the list of available network profiles.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListNetworkProfiles>`_
        
        **Request Syntax**
        ::
          response = client.list_network_profiles(
              arn='string',
              type='CURATED'|'PRIVATE',
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'networkProfiles': [
                    {
                        'arn': 'string',
                        'name': 'string',
                        'description': 'string',
                        'type': 'CURATED'|'PRIVATE',
                        'uplinkBandwidthBits': 123,
                        'downlinkBandwidthBits': 123,
                        'uplinkDelayMs': 123,
                        'downlinkDelayMs': 123,
                        'uplinkJitterMs': 123,
                        'downlinkJitterMs': 123,
                        'uplinkLossPercent': 123,
                        'downlinkLossPercent': 123
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **networkProfiles** *(list) --* 
              A list of the available network profiles.
              - *(dict) --* 
                An array of settings that describes characteristics of a network profile.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the network profile.
                - **name** *(string) --* 
                  The name of the network profile.
                - **description** *(string) --* 
                  The description of the network profile.
                - **type** *(string) --* 
                  The type of network profile. Valid values are listed below.
                - **uplinkBandwidthBits** *(integer) --* 
                  The data throughput rate in bits per second, as an integer from 0 to 104857600.
                - **downlinkBandwidthBits** *(integer) --* 
                  The data throughput rate in bits per second, as an integer from 0 to 104857600.
                - **uplinkDelayMs** *(integer) --* 
                  Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
                - **downlinkDelayMs** *(integer) --* 
                  Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
                - **uplinkJitterMs** *(integer) --* 
                  Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
                - **downlinkJitterMs** *(integer) --* 
                  Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
                - **uplinkLossPercent** *(integer) --* 
                  Proportion of transmitted packets that fail to arrive from 0 to 100 percent.
                - **downlinkLossPercent** *(integer) --* 
                  Proportion of received packets that fail to arrive from 0 to 100 percent.
            - **nextToken** *(string) --* 
              An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type arn: string
        :param arn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the project for which you want to list network profiles.
        :type type: string
        :param type:
          The type of network profile you wish to return information about. Valid values are listed below.
        :type nextToken: string
        :param nextToken:
          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :rtype: dict
        :returns:
        """
        pass

    def list_offering_promotions(self, nextToken: str = None) -> Dict:
        """
        Returns a list of offering promotions. Each offering promotion record contains the ID and description of the promotion. The API returns a ``NotEligible`` error if the caller is not permitted to invoke the operation. Contact `aws-devicefarm-support@amazon.com <mailto:aws-devicefarm-support@amazon.com>`__ if you believe that you should be able to invoke this operation.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListOfferingPromotions>`_
        
        **Request Syntax**
        ::
          response = client.list_offering_promotions(
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'offeringPromotions': [
                    {
                        'id': 'string',
                        'description': 'string'
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **offeringPromotions** *(list) --* 
              Information about the offering promotions.
              - *(dict) --* 
                Represents information about an offering promotion.
                - **id** *(string) --* 
                  The ID of the offering promotion.
                - **description** *(string) --* 
                  A string describing the offering promotion.
            - **nextToken** *(string) --* 
              An identifier to be used in the next call to this operation, to return the next set of items in the list.
        :type nextToken: string
        :param nextToken:
          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :rtype: dict
        :returns:
        """
        pass

    def list_offering_transactions(self, nextToken: str = None) -> Dict:
        """
        Returns a list of all historical purchases, renewals, and system renewal transactions for an AWS account. The list is paginated and ordered by a descending timestamp (most recent transactions are first). The API returns a ``NotEligible`` error if the user is not permitted to invoke the operation. Please contact `aws-devicefarm-support@amazon.com <mailto:aws-devicefarm-support@amazon.com>`__ if you believe that you should be able to invoke this operation.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListOfferingTransactions>`_
        
        **Request Syntax**
        ::
          response = client.list_offering_transactions(
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'offeringTransactions': [
                    {
                        'offeringStatus': {
                            'type': 'PURCHASE'|'RENEW'|'SYSTEM',
                            'offering': {
                                'id': 'string',
                                'description': 'string',
                                'type': 'RECURRING',
                                'platform': 'ANDROID'|'IOS',
                                'recurringCharges': [
                                    {
                                        'cost': {
                                            'amount': 123.0,
                                            'currencyCode': 'USD'
                                        },
                                        'frequency': 'MONTHLY'
                                    },
                                ]
                            },
                            'quantity': 123,
                            'effectiveOn': datetime(2015, 1, 1)
                        },
                        'transactionId': 'string',
                        'offeringPromotionId': 'string',
                        'createdOn': datetime(2015, 1, 1),
                        'cost': {
                            'amount': 123.0,
                            'currencyCode': 'USD'
                        }
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Returns the transaction log of the specified offerings.
            - **offeringTransactions** *(list) --* 
              The audit log of subscriptions you have purchased and modified through AWS Device Farm.
              - *(dict) --* 
                Represents the metadata of an offering transaction.
                - **offeringStatus** *(dict) --* 
                  The status of an offering transaction.
                  - **type** *(string) --* 
                    The type specified for the offering status.
                  - **offering** *(dict) --* 
                    Represents the metadata of an offering status.
                    - **id** *(string) --* 
                      The ID that corresponds to a device offering.
                    - **description** *(string) --* 
                      A string describing the offering.
                    - **type** *(string) --* 
                      The type of offering (e.g., "RECURRING") for a device.
                    - **platform** *(string) --* 
                      The platform of the device (e.g., ANDROID or IOS).
                    - **recurringCharges** *(list) --* 
                      Specifies whether there are recurring charges for the offering.
                      - *(dict) --* 
                        Specifies whether charges for devices will be recurring.
                        - **cost** *(dict) --* 
                          The cost of the recurring charge.
                          - **amount** *(float) --* 
                            The numerical amount of an offering or transaction.
                          - **currencyCode** *(string) --* 
                            The currency code of a monetary amount. For example, ``USD`` means "U.S. dollars."
                        - **frequency** *(string) --* 
                          The frequency in which charges will recur.
                  - **quantity** *(integer) --* 
                    The number of available devices in the offering.
                  - **effectiveOn** *(datetime) --* 
                    The date on which the offering is effective.
                - **transactionId** *(string) --* 
                  The transaction ID of the offering transaction.
                - **offeringPromotionId** *(string) --* 
                  The ID that corresponds to a device offering promotion.
                - **createdOn** *(datetime) --* 
                  The date on which an offering transaction was created.
                - **cost** *(dict) --* 
                  The cost of an offering transaction.
                  - **amount** *(float) --* 
                    The numerical amount of an offering or transaction.
                  - **currencyCode** *(string) --* 
                    The currency code of a monetary amount. For example, ``USD`` means "U.S. dollars."
            - **nextToken** *(string) --* 
              An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type nextToken: string
        :param nextToken:
          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :rtype: dict
        :returns:
        """
        pass

    def list_offerings(self, nextToken: str = None) -> Dict:
        """
        Returns a list of products or offerings that the user can manage through the API. Each offering record indicates the recurring price per unit and the frequency for that offering. The API returns a ``NotEligible`` error if the user is not permitted to invoke the operation. Please contact `aws-devicefarm-support@amazon.com <mailto:aws-devicefarm-support@amazon.com>`__ if you believe that you should be able to invoke this operation.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListOfferings>`_
        
        **Request Syntax**
        ::
          response = client.list_offerings(
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'offerings': [
                    {
                        'id': 'string',
                        'description': 'string',
                        'type': 'RECURRING',
                        'platform': 'ANDROID'|'IOS',
                        'recurringCharges': [
                            {
                                'cost': {
                                    'amount': 123.0,
                                    'currencyCode': 'USD'
                                },
                                'frequency': 'MONTHLY'
                            },
                        ]
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the return values of the list of offerings.
            - **offerings** *(list) --* 
              A value representing the list offering results.
              - *(dict) --* 
                Represents the metadata of a device offering.
                - **id** *(string) --* 
                  The ID that corresponds to a device offering.
                - **description** *(string) --* 
                  A string describing the offering.
                - **type** *(string) --* 
                  The type of offering (e.g., "RECURRING") for a device.
                - **platform** *(string) --* 
                  The platform of the device (e.g., ANDROID or IOS).
                - **recurringCharges** *(list) --* 
                  Specifies whether there are recurring charges for the offering.
                  - *(dict) --* 
                    Specifies whether charges for devices will be recurring.
                    - **cost** *(dict) --* 
                      The cost of the recurring charge.
                      - **amount** *(float) --* 
                        The numerical amount of an offering or transaction.
                      - **currencyCode** *(string) --* 
                        The currency code of a monetary amount. For example, ``USD`` means "U.S. dollars."
                    - **frequency** *(string) --* 
                      The frequency in which charges will recur.
            - **nextToken** *(string) --* 
              An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type nextToken: string
        :param nextToken:
          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :rtype: dict
        :returns:
        """
        pass

    def list_projects(self, arn: str = None, nextToken: str = None) -> Dict:
        """
        Gets information about projects.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListProjects>`_
        
        **Request Syntax**
        ::
          response = client.list_projects(
              arn='string',
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'projects': [
                    {
                        'arn': 'string',
                        'name': 'string',
                        'defaultJobTimeoutMinutes': 123,
                        'created': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of a list projects request.
            - **projects** *(list) --* 
              Information about the projects.
              - *(dict) --* 
                Represents an operating-system neutral workspace for running and managing tests.
                - **arn** *(string) --* 
                  The project's ARN.
                - **name** *(string) --* 
                  The project's name.
                - **defaultJobTimeoutMinutes** *(integer) --* 
                  The default number of minutes (at the project level) a test run will execute before it times out. Default value is 60 minutes.
                - **created** *(datetime) --* 
                  When the project was created.
            - **nextToken** *(string) --* 
              If the number of items that are returned is significantly large, this is an identifier that is also returned, which can be used in a subsequent call to this operation to return the next set of items in the list.
        :type arn: string
        :param arn:
          Optional. If no Amazon Resource Name (ARN) is specified, then AWS Device Farm returns a list of all projects for the AWS account. You can also specify a project ARN.
        :type nextToken: string
        :param nextToken:
          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :rtype: dict
        :returns:
        """
        pass

    def list_remote_access_sessions(self, arn: str, nextToken: str = None) -> Dict:
        """
        Returns a list of all currently running remote access sessions.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListRemoteAccessSessions>`_
        
        **Request Syntax**
        ::
          response = client.list_remote_access_sessions(
              arn='string',
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'remoteAccessSessions': [
                    {
                        'arn': 'string',
                        'name': 'string',
                        'created': datetime(2015, 1, 1),
                        'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                        'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                        'message': 'string',
                        'started': datetime(2015, 1, 1),
                        'stopped': datetime(2015, 1, 1),
                        'device': {
                            'arn': 'string',
                            'name': 'string',
                            'manufacturer': 'string',
                            'model': 'string',
                            'modelId': 'string',
                            'formFactor': 'PHONE'|'TABLET',
                            'platform': 'ANDROID'|'IOS',
                            'os': 'string',
                            'cpu': {
                                'frequency': 'string',
                                'architecture': 'string',
                                'clock': 123.0
                            },
                            'resolution': {
                                'width': 123,
                                'height': 123
                            },
                            'heapSize': 123,
                            'memory': 123,
                            'image': 'string',
                            'carrier': 'string',
                            'radio': 'string',
                            'remoteAccessEnabled': True|False,
                            'remoteDebugEnabled': True|False,
                            'fleetType': 'string',
                            'fleetName': 'string',
                            'instances': [
                                {
                                    'arn': 'string',
                                    'deviceArn': 'string',
                                    'labels': [
                                        'string',
                                    ],
                                    'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                                    'udid': 'string',
                                    'instanceProfile': {
                                        'arn': 'string',
                                        'packageCleanup': True|False,
                                        'excludeAppPackagesFromCleanup': [
                                            'string',
                                        ],
                                        'rebootAfterUse': True|False,
                                        'name': 'string',
                                        'description': 'string'
                                    }
                                },
                            ],
                            'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
                        },
                        'instanceArn': 'string',
                        'remoteDebugEnabled': True|False,
                        'remoteRecordEnabled': True|False,
                        'remoteRecordAppArn': 'string',
                        'hostAddress': 'string',
                        'clientId': 'string',
                        'billingMethod': 'METERED'|'UNMETERED',
                        'deviceMinutes': {
                            'total': 123.0,
                            'metered': 123.0,
                            'unmetered': 123.0
                        },
                        'endpoint': 'string',
                        'deviceUdid': 'string',
                        'interactionMode': 'INTERACTIVE'|'NO_VIDEO'|'VIDEO_ONLY',
                        'skipAppResign': True|False
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the response from the server after AWS Device Farm makes a request to return information about the remote access session.
            - **remoteAccessSessions** *(list) --* 
              A container representing the metadata from the service about each remote access session you are requesting.
              - *(dict) --* 
                Represents information about the remote access session.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the remote access session.
                - **name** *(string) --* 
                  The name of the remote access session.
                - **created** *(datetime) --* 
                  The date and time the remote access session was created.
                - **status** *(string) --* 
                  The status of the remote access session. Can be any of the following:
                  * PENDING: A pending status. 
                  * PENDING_CONCURRENCY: A pending concurrency status. 
                  * PENDING_DEVICE: A pending device status. 
                  * PROCESSING: A processing status. 
                  * SCHEDULING: A scheduling status. 
                  * PREPARING: A preparing status. 
                  * RUNNING: A running status. 
                  * COMPLETED: A completed status. 
                  * STOPPING: A stopping status. 
                - **result** *(string) --* 
                  The result of the remote access session. Can be any of the following:
                  * PENDING: A pending condition. 
                  * PASSED: A passing condition. 
                  * WARNED: A warning condition. 
                  * FAILED: A failed condition. 
                  * SKIPPED: A skipped condition. 
                  * ERRORED: An error condition. 
                  * STOPPED: A stopped condition. 
                - **message** *(string) --* 
                  A message about the remote access session.
                - **started** *(datetime) --* 
                  The date and time the remote access session was started.
                - **stopped** *(datetime) --* 
                  The date and time the remote access session was stopped.
                - **device** *(dict) --* 
                  The device (phone or tablet) used in the remote access session.
                  - **arn** *(string) --* 
                    The device's ARN.
                  - **name** *(string) --* 
                    The device's display name.
                  - **manufacturer** *(string) --* 
                    The device's manufacturer name.
                  - **model** *(string) --* 
                    The device's model name.
                  - **modelId** *(string) --* 
                    The device's model ID.
                  - **formFactor** *(string) --* 
                    The device's form factor.
                    Allowed values include:
                    * PHONE: The phone form factor. 
                    * TABLET: The tablet form factor. 
                  - **platform** *(string) --* 
                    The device's platform.
                    Allowed values include:
                    * ANDROID: The Android platform. 
                    * IOS: The iOS platform. 
                  - **os** *(string) --* 
                    The device's operating system type.
                  - **cpu** *(dict) --* 
                    Information about the device's CPU.
                    - **frequency** *(string) --* 
                      The CPU's frequency.
                    - **architecture** *(string) --* 
                      The CPU's architecture, for example x86 or ARM.
                    - **clock** *(float) --* 
                      The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.
                  - **resolution** *(dict) --* 
                    The resolution of the device.
                    - **width** *(integer) --* 
                      The screen resolution's width, expressed in pixels.
                    - **height** *(integer) --* 
                      The screen resolution's height, expressed in pixels.
                  - **heapSize** *(integer) --* 
                    The device's heap size, expressed in bytes.
                  - **memory** *(integer) --* 
                    The device's total memory size, expressed in bytes.
                  - **image** *(string) --* 
                    The device's image name.
                  - **carrier** *(string) --* 
                    The device's carrier.
                  - **radio** *(string) --* 
                    The device's radio.
                  - **remoteAccessEnabled** *(boolean) --* 
                    Specifies whether remote access has been enabled for the specified device.
                  - **remoteDebugEnabled** *(boolean) --* 
                    This flag is set to ``true`` if remote debugging is enabled for the device.
                  - **fleetType** *(string) --* 
                    The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.
                  - **fleetName** *(string) --* 
                    The name of the fleet to which this device belongs.
                  - **instances** *(list) --* 
                    The instances belonging to this device.
                    - *(dict) --* 
                      Represents the device instance.
                      - **arn** *(string) --* 
                        The Amazon Resource Name (ARN) of the device instance.
                      - **deviceArn** *(string) --* 
                        The Amazon Resource Name (ARN) of the device.
                      - **labels** *(list) --* 
                        An array of strings describing the device instance.
                        - *(string) --* 
                      - **status** *(string) --* 
                        The status of the device instance. Valid values are listed below.
                      - **udid** *(string) --* 
                        Unique device identifier for the device instance.
                      - **instanceProfile** *(dict) --* 
                        A object containing information about the instance profile.
                        - **arn** *(string) --* 
                          The Amazon Resource Name (ARN) of the instance profile.
                        - **packageCleanup** *(boolean) --* 
                          When set to ``true`` , Device Farm will remove app packages after a test run. The default value is ``false`` for private devices.
                        - **excludeAppPackagesFromCleanup** *(list) --* 
                          An array of strings specifying the list of app packages that should not be cleaned up from the device after a test run is over.
                          The list of packages is only considered if you set ``packageCleanup`` to ``true`` .
                          - *(string) --* 
                        - **rebootAfterUse** *(boolean) --* 
                          When set to ``true`` , Device Farm will reboot the instance after a test run. The default value is ``true`` .
                        - **name** *(string) --* 
                          The name of the instance profile.
                        - **description** *(string) --* 
                          The description of the instance profile.
                  - **availability** *(string) --* 
                    Reflects how likely a device will be available for a test run. It is currently available in the ListDevices and GetDevice API methods.
                - **instanceArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the instance.
                - **remoteDebugEnabled** *(boolean) --* 
                  This flag is set to ``true`` if remote debugging is enabled for the remote access session.
                - **remoteRecordEnabled** *(boolean) --* 
                  This flag is set to ``true`` if remote recording is enabled for the remote access session.
                - **remoteRecordAppArn** *(string) --* 
                  The Amazon Resource Name (ARN) for the app to be recorded in the remote access session.
                - **hostAddress** *(string) --* 
                  IP address of the EC2 host where you need to connect to remotely debug devices. Only returned if remote debugging is enabled for the remote access session.
                - **clientId** *(string) --* 
                  Unique identifier of your client for the remote access session. Only returned if remote debugging is enabled for the remote access session.
                - **billingMethod** *(string) --* 
                  The billing method of the remote access session. Possible values include ``METERED`` or ``UNMETERED`` . For more information about metered devices, see `AWS Device Farm terminology <https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html#welcome-terminology>`__ ."
                - **deviceMinutes** *(dict) --* 
                  The number of minutes a device is used in a remote access sesssion (including setup and teardown minutes).
                  - **total** *(float) --* 
                    When specified, represents the total minutes used by the resource to run tests.
                  - **metered** *(float) --* 
                    When specified, represents only the sum of metered minutes used by the resource to run tests.
                  - **unmetered** *(float) --* 
                    When specified, represents only the sum of unmetered minutes used by the resource to run tests.
                - **endpoint** *(string) --* 
                  The endpoint for the remote access sesssion.
                - **deviceUdid** *(string) --* 
                  Unique device identifier for the remote device. Only returned if remote debugging is enabled for the remote access session.
                - **interactionMode** *(string) --* 
                  The interaction mode of the remote access session. Valid values are:
                  * INTERACTIVE: You can interact with the iOS device by viewing, touching, and rotating the screen. You **cannot** run XCUITest framework-based tests in this mode. 
                  * NO_VIDEO: You are connected to the device but cannot interact with it or view the screen. This mode has the fastest test execution speed. You **can** run XCUITest framework-based tests in this mode. 
                  * VIDEO_ONLY: You can view the screen but cannot touch or rotate it. You **can** run XCUITest framework-based tests and watch the screen in this mode. 
                - **skipAppResign** *(boolean) --* 
                  When set to ``true`` , for private devices, Device Farm will not sign your app again. For public devices, Device Farm always signs your apps again and this parameter has no effect.
                  For more information about how Device Farm re-signs your app(s), see `Do you modify my app? <https://aws.amazon.com/device-farm/faq/>`__ in the *AWS Device Farm FAQs* .
            - **nextToken** *(string) --* 
              An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type arn: string
        :param arn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the remote access session about which you are requesting information.
        :type nextToken: string
        :param nextToken:
          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :rtype: dict
        :returns:
        """
        pass

    def list_runs(self, arn: str, nextToken: str = None) -> Dict:
        """
        Gets information about runs, given an AWS Device Farm project ARN.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListRuns>`_
        
        **Request Syntax**
        ::
          response = client.list_runs(
              arn='string',
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'runs': [
                    {
                        'arn': 'string',
                        'name': 'string',
                        'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
                        'platform': 'ANDROID'|'IOS',
                        'created': datetime(2015, 1, 1),
                        'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                        'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                        'started': datetime(2015, 1, 1),
                        'stopped': datetime(2015, 1, 1),
                        'counters': {
                            'total': 123,
                            'passed': 123,
                            'failed': 123,
                            'warned': 123,
                            'errored': 123,
                            'stopped': 123,
                            'skipped': 123
                        },
                        'message': 'string',
                        'totalJobs': 123,
                        'completedJobs': 123,
                        'billingMethod': 'METERED'|'UNMETERED',
                        'deviceMinutes': {
                            'total': 123.0,
                            'metered': 123.0,
                            'unmetered': 123.0
                        },
                        'networkProfile': {
                            'arn': 'string',
                            'name': 'string',
                            'description': 'string',
                            'type': 'CURATED'|'PRIVATE',
                            'uplinkBandwidthBits': 123,
                            'downlinkBandwidthBits': 123,
                            'uplinkDelayMs': 123,
                            'downlinkDelayMs': 123,
                            'uplinkJitterMs': 123,
                            'downlinkJitterMs': 123,
                            'uplinkLossPercent': 123,
                            'downlinkLossPercent': 123
                        },
                        'parsingResultUrl': 'string',
                        'resultCode': 'PARSING_FAILED'|'VPC_ENDPOINT_SETUP_FAILED',
                        'seed': 123,
                        'appUpload': 'string',
                        'eventCount': 123,
                        'jobTimeoutMinutes': 123,
                        'devicePoolArn': 'string',
                        'locale': 'string',
                        'radios': {
                            'wifi': True|False,
                            'bluetooth': True|False,
                            'nfc': True|False,
                            'gps': True|False
                        },
                        'location': {
                            'latitude': 123.0,
                            'longitude': 123.0
                        },
                        'customerArtifactPaths': {
                            'iosPaths': [
                                'string',
                            ],
                            'androidPaths': [
                                'string',
                            ],
                            'deviceHostPaths': [
                                'string',
                            ]
                        },
                        'webUrl': 'string',
                        'skipAppResign': True|False,
                        'testSpecArn': 'string',
                        'deviceSelectionResult': {
                            'filters': [
                                {
                                    'attribute': 'ARN'|'PLATFORM'|'OS_VERSION'|'MODEL'|'AVAILABILITY'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                                    'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                                    'values': [
                                        'string',
                                    ]
                                },
                            ],
                            'matchedDevicesCount': 123,
                            'maxDevices': 123
                        }
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of a list runs request.
            - **runs** *(list) --* 
              Information about the runs.
              - *(dict) --* 
                Represents a test run on a set of devices with a given app package, test parameters, etc.
                - **arn** *(string) --* 
                  The run's ARN.
                - **name** *(string) --* 
                  The run's name.
                - **type** *(string) --* 
                  The run's type.
                  Must be one of the following values:
                  * BUILTIN_FUZZ: The built-in fuzz type. 
                  * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
                  * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
                  * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
                  * APPIUM_PYTHON: The Appium Python type. 
                  * APPIUM_NODE: The Appium Node.js type. 
                  * APPIUM_RUBY: The Appium Ruby type. 
                  * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for web apps. 
                  * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for web apps. 
                  * APPIUM_WEB_PYTHON: The Appium Python type for web apps. 
                  * APPIUM_WEB_NODE: The Appium Node.js type for web apps. 
                  * APPIUM_WEB_RUBY: The Appium Ruby type for web apps. 
                  * CALABASH: The Calabash type. 
                  * INSTRUMENTATION: The Instrumentation type. 
                  * UIAUTOMATION: The uiautomation type. 
                  * UIAUTOMATOR: The uiautomator type. 
                  * XCTEST: The XCode test type. 
                  * XCTEST_UI: The XCode UI test type. 
                - **platform** *(string) --* 
                  The run's platform.
                  Allowed values include:
                  * ANDROID: The Android platform. 
                  * IOS: The iOS platform. 
                - **created** *(datetime) --* 
                  When the run was created.
                - **status** *(string) --* 
                  The run's status.
                  Allowed values include:
                  * PENDING: A pending status. 
                  * PENDING_CONCURRENCY: A pending concurrency status. 
                  * PENDING_DEVICE: A pending device status. 
                  * PROCESSING: A processing status. 
                  * SCHEDULING: A scheduling status. 
                  * PREPARING: A preparing status. 
                  * RUNNING: A running status. 
                  * COMPLETED: A completed status. 
                  * STOPPING: A stopping status. 
                - **result** *(string) --* 
                  The run's result.
                  Allowed values include:
                  * PENDING: A pending condition. 
                  * PASSED: A passing condition. 
                  * WARNED: A warning condition. 
                  * FAILED: A failed condition. 
                  * SKIPPED: A skipped condition. 
                  * ERRORED: An error condition. 
                  * STOPPED: A stopped condition. 
                - **started** *(datetime) --* 
                  The run's start time.
                - **stopped** *(datetime) --* 
                  The run's stop time.
                - **counters** *(dict) --* 
                  The run's result counters.
                  - **total** *(integer) --* 
                    The total number of entities.
                  - **passed** *(integer) --* 
                    The number of passed entities.
                  - **failed** *(integer) --* 
                    The number of failed entities.
                  - **warned** *(integer) --* 
                    The number of warned entities.
                  - **errored** *(integer) --* 
                    The number of errored entities.
                  - **stopped** *(integer) --* 
                    The number of stopped entities.
                  - **skipped** *(integer) --* 
                    The number of skipped entities.
                - **message** *(string) --* 
                  A message about the run's result.
                - **totalJobs** *(integer) --* 
                  The total number of jobs for the run.
                - **completedJobs** *(integer) --* 
                  The total number of completed jobs.
                - **billingMethod** *(string) --* 
                  Specifies the billing method for a test run: ``metered`` or ``unmetered`` . If the parameter is not specified, the default value is ``metered`` .
                - **deviceMinutes** *(dict) --* 
                  Represents the total (metered or unmetered) minutes used by the test run.
                  - **total** *(float) --* 
                    When specified, represents the total minutes used by the resource to run tests.
                  - **metered** *(float) --* 
                    When specified, represents only the sum of metered minutes used by the resource to run tests.
                  - **unmetered** *(float) --* 
                    When specified, represents only the sum of unmetered minutes used by the resource to run tests.
                - **networkProfile** *(dict) --* 
                  The network profile being used for a test run.
                  - **arn** *(string) --* 
                    The Amazon Resource Name (ARN) of the network profile.
                  - **name** *(string) --* 
                    The name of the network profile.
                  - **description** *(string) --* 
                    The description of the network profile.
                  - **type** *(string) --* 
                    The type of network profile. Valid values are listed below.
                  - **uplinkBandwidthBits** *(integer) --* 
                    The data throughput rate in bits per second, as an integer from 0 to 104857600.
                  - **downlinkBandwidthBits** *(integer) --* 
                    The data throughput rate in bits per second, as an integer from 0 to 104857600.
                  - **uplinkDelayMs** *(integer) --* 
                    Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
                  - **downlinkDelayMs** *(integer) --* 
                    Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
                  - **uplinkJitterMs** *(integer) --* 
                    Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
                  - **downlinkJitterMs** *(integer) --* 
                    Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
                  - **uplinkLossPercent** *(integer) --* 
                    Proportion of transmitted packets that fail to arrive from 0 to 100 percent.
                  - **downlinkLossPercent** *(integer) --* 
                    Proportion of received packets that fail to arrive from 0 to 100 percent.
                - **parsingResultUrl** *(string) --* 
                  Read-only URL for an object in S3 bucket where you can get the parsing results of the test package. If the test package doesn't parse, the reason why it doesn't parse appears in the file that this URL points to.
                - **resultCode** *(string) --* 
                  Supporting field for the result field. Set only if ``result`` is ``SKIPPED`` . ``PARSING_FAILED`` if the result is skipped because of test package parsing failure.
                - **seed** *(integer) --* 
                  For fuzz tests, this is a seed to use for randomizing the UI fuzz test. Using the same seed value between tests ensures identical event sequences.
                - **appUpload** *(string) --* 
                  An app to upload or that has been uploaded.
                - **eventCount** *(integer) --* 
                  For fuzz tests, this is the number of events, between 1 and 10000, that the UI fuzz test should perform.
                - **jobTimeoutMinutes** *(integer) --* 
                  The number of minutes the job will execute before it times out.
                - **devicePoolArn** *(string) --* 
                  The ARN of the device pool for the run.
                - **locale** *(string) --* 
                  Information about the locale that is used for the run.
                - **radios** *(dict) --* 
                  Information about the radio states for the run.
                  - **wifi** *(boolean) --* 
                    True if Wi-Fi is enabled at the beginning of the test; otherwise, false.
                  - **bluetooth** *(boolean) --* 
                    True if Bluetooth is enabled at the beginning of the test; otherwise, false.
                  - **nfc** *(boolean) --* 
                    True if NFC is enabled at the beginning of the test; otherwise, false.
                  - **gps** *(boolean) --* 
                    True if GPS is enabled at the beginning of the test; otherwise, false.
                - **location** *(dict) --* 
                  Information about the location that is used for the run.
                  - **latitude** *(float) --* 
                    The latitude.
                  - **longitude** *(float) --* 
                    The longitude.
                - **customerArtifactPaths** *(dict) --* 
                  Output ``CustomerArtifactPaths`` object for the test run.
                  - **iosPaths** *(list) --* 
                    Comma-separated list of paths on the iOS device where the artifacts generated by the customer's tests will be pulled from.
                    - *(string) --* 
                  - **androidPaths** *(list) --* 
                    Comma-separated list of paths on the Android device where the artifacts generated by the customer's tests will be pulled from.
                    - *(string) --* 
                  - **deviceHostPaths** *(list) --* 
                    Comma-separated list of paths in the test execution environment where the artifacts generated by the customer's tests will be pulled from.
                    - *(string) --* 
                - **webUrl** *(string) --* 
                  The Device Farm console URL for the recording of the run.
                - **skipAppResign** *(boolean) --* 
                  When set to ``true`` , for private devices, Device Farm will not sign your app again. For public devices, Device Farm always signs your apps again and this parameter has no effect.
                  For more information about how Device Farm re-signs your app(s), see `Do you modify my app? <https://aws.amazon.com/device-farm/faq/>`__ in the *AWS Device Farm FAQs* .
                - **testSpecArn** *(string) --* 
                  The ARN of the YAML-formatted test specification for the run.
                - **deviceSelectionResult** *(dict) --* 
                  The results of a device filter used to select the devices for a test run.
                  - **filters** *(list) --* 
                    The filters in a device selection result.
                    - *(dict) --* 
                      Represents a device filter used to select a set of devices to be included in a test run. This data structure is passed in as the ``deviceSelectionConfiguration`` parameter to ScheduleRun. For an example of the JSON request syntax, see  ScheduleRun .
                      It is also passed in as the ``filters`` parameter to ListDevices. For an example of the JSON request syntax, see  ListDevices .
                      - **attribute** *(string) --* 
                        The aspect of a device such as platform or model used as the selection criteria in a device filter.
                        The supported operators for each attribute are provided in the following list.
                          ARN  
                        The Amazon Resource Name (ARN) of the device. For example, "arn:aws:devicefarm:us-west-2::device:12345Example".
                         *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                          PLATFORM  
                        The device platform. Valid values are "ANDROID" or "IOS".
                         *Supported operators* : ``EQUALS``  
                          OS_VERSION  
                        The operating system version. For example, "10.3.2".
                         *Supported operators* : ``EQUALS`` , ``GREATER_THAN`` , ``GREATER_THAN_OR_EQUALS`` , ``IN`` , ``LESS_THAN`` , ``LESS_THAN_OR_EQUALS`` , ``NOT_IN``  
                          MODEL  
                        The device model. For example, "iPad 5th Gen".
                         *Supported operators* : ``CONTAINS`` , ``EQUALS`` , ``IN`` , ``NOT_IN``  
                          AVAILABILITY  
                        The current availability of the device. Valid values are "AVAILABLE", "HIGHLY_AVAILABLE", "BUSY", or "TEMPORARY_NOT_AVAILABLE".
                         *Supported operators* : ``EQUALS``  
                          FORM_FACTOR  
                        The device form factor. Valid values are "PHONE" or "TABLET".
                         *Supported operators* : ``EQUALS``  
                          MANUFACTURER  
                        The device manufacturer. For example, "Apple".
                         *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                          REMOTE_ACCESS_ENABLED  
                        Whether the device is enabled for remote access. Valid values are "TRUE" or "FALSE".
                         *Supported operators* : ``EQUALS``  
                          REMOTE_DEBUG_ENABLED  
                        Whether the device is enabled for remote debugging. Valid values are "TRUE" or "FALSE".
                         *Supported operators* : ``EQUALS``  
                          INSTANCE_ARN  
                        The Amazon Resource Name (ARN) of the device instance.
                         *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                          INSTANCE_LABELS  
                        The label of the device instance.
                         *Supported operators* : ``CONTAINS``  
                          FLEET_TYPE  
                        The fleet type. Valid values are "PUBLIC" or "PRIVATE".
                         *Supported operators* : ``EQUALS``  
                      - **operator** *(string) --* 
                        Specifies how Device Farm compares the filter's attribute to the value. For the operators that are supported by each attribute, see the attribute descriptions.
                      - **values** *(list) --* 
                        An array of one or more filter values used in a device filter.
        
        **Operator Values**
                        * The IN and NOT_IN operators can take a values array that has more than one element. 
                        * The other operators require an array with a single element. 
        
        **Attribute Values**
                        * The PLATFORM attribute can be set to "ANDROID" or "IOS". 
                        * The AVAILABILITY attribute can be set to "AVAILABLE", "HIGHLY_AVAILABLE", "BUSY", or "TEMPORARY_NOT_AVAILABLE". 
                        * The FORM_FACTOR attribute can be set to "PHONE" or "TABLET". 
                        * The FLEET_TYPE attribute can be set to "PUBLIC" or "PRIVATE". 
                        - *(string) --* 
                  - **matchedDevicesCount** *(integer) --* 
                    The number of devices that matched the device filter selection criteria.
                  - **maxDevices** *(integer) --* 
                    The maximum number of devices to be selected by a device filter and included in a test run.
            - **nextToken** *(string) --* 
              If the number of items that are returned is significantly large, this is an identifier that is also returned, which can be used in a subsequent call to this operation to return the next set of items in the list.
        :type arn: string
        :param arn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the project for which you want to list runs.
        :type nextToken: string
        :param nextToken:
          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :rtype: dict
        :returns:
        """
        pass

    def list_samples(self, arn: str, nextToken: str = None) -> Dict:
        """
        Gets information about samples, given an AWS Device Farm job ARN.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListSamples>`_
        
        **Request Syntax**
        ::
          response = client.list_samples(
              arn='string',
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'samples': [
                    {
                        'arn': 'string',
                        'type': 'CPU'|'MEMORY'|'THREADS'|'RX_RATE'|'TX_RATE'|'RX'|'TX'|'NATIVE_FRAMES'|'NATIVE_FPS'|'NATIVE_MIN_DRAWTIME'|'NATIVE_AVG_DRAWTIME'|'NATIVE_MAX_DRAWTIME'|'OPENGL_FRAMES'|'OPENGL_FPS'|'OPENGL_MIN_DRAWTIME'|'OPENGL_AVG_DRAWTIME'|'OPENGL_MAX_DRAWTIME',
                        'url': 'string'
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of a list samples request.
            - **samples** *(list) --* 
              Information about the samples.
              - *(dict) --* 
                Represents a sample of performance data.
                - **arn** *(string) --* 
                  The sample's ARN.
                - **type** *(string) --* 
                  The sample's type.
                  Must be one of the following values:
                  * CPU: A CPU sample type. This is expressed as the app processing CPU time (including child processes) as reported by process, as a percentage. 
                  * MEMORY: A memory usage sample type. This is expressed as the total proportional set size of an app process, in kilobytes. 
                  * NATIVE_AVG_DRAWTIME 
                  * NATIVE_FPS 
                  * NATIVE_FRAMES 
                  * NATIVE_MAX_DRAWTIME 
                  * NATIVE_MIN_DRAWTIME 
                  * OPENGL_AVG_DRAWTIME 
                  * OPENGL_FPS 
                  * OPENGL_FRAMES 
                  * OPENGL_MAX_DRAWTIME 
                  * OPENGL_MIN_DRAWTIME 
                  * RX 
                  * RX_RATE: The total number of bytes per second (TCP and UDP) that are sent, by app process. 
                  * THREADS: A threads sample type. This is expressed as the total number of threads per app process. 
                  * TX 
                  * TX_RATE: The total number of bytes per second (TCP and UDP) that are received, by app process. 
                - **url** *(string) --* 
                  The pre-signed Amazon S3 URL that can be used with a corresponding GET request to download the sample's file.
            - **nextToken** *(string) --* 
              If the number of items that are returned is significantly large, this is an identifier that is also returned, which can be used in a subsequent call to this operation to return the next set of items in the list.
        :type arn: string
        :param arn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the job used to list samples.
        :type nextToken: string
        :param nextToken:
          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :rtype: dict
        :returns:
        """
        pass

    def list_suites(self, arn: str, nextToken: str = None) -> Dict:
        """
        Gets information about test suites for a given job.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListSuites>`_
        
        **Request Syntax**
        ::
          response = client.list_suites(
              arn='string',
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'suites': [
                    {
                        'arn': 'string',
                        'name': 'string',
                        'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
                        'created': datetime(2015, 1, 1),
                        'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                        'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                        'started': datetime(2015, 1, 1),
                        'stopped': datetime(2015, 1, 1),
                        'counters': {
                            'total': 123,
                            'passed': 123,
                            'failed': 123,
                            'warned': 123,
                            'errored': 123,
                            'stopped': 123,
                            'skipped': 123
                        },
                        'message': 'string',
                        'deviceMinutes': {
                            'total': 123.0,
                            'metered': 123.0,
                            'unmetered': 123.0
                        }
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of a list suites request.
            - **suites** *(list) --* 
              Information about the suites.
              - *(dict) --* 
                Represents a collection of one or more tests.
                - **arn** *(string) --* 
                  The suite's ARN.
                - **name** *(string) --* 
                  The suite's name.
                - **type** *(string) --* 
                  The suite's type.
                  Must be one of the following values:
                  * BUILTIN_FUZZ: The built-in fuzz type. 
                  * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
                  * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
                  * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
                  * APPIUM_PYTHON: The Appium Python type. 
                  * APPIUM_NODE: The Appium Node.js type. 
                  * APPIUM_RUBY: The Appium Ruby type. 
                  * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for web apps. 
                  * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for web apps. 
                  * APPIUM_WEB_PYTHON: The Appium Python type for web apps. 
                  * APPIUM_WEB_NODE: The Appium Node.js type for web apps. 
                  * APPIUM_WEB_RUBY: The Appium Ruby type for web apps. 
                  * CALABASH: The Calabash type. 
                  * INSTRUMENTATION: The Instrumentation type. 
                  * UIAUTOMATION: The uiautomation type. 
                  * UIAUTOMATOR: The uiautomator type. 
                  * XCTEST: The XCode test type. 
                  * XCTEST_UI: The XCode UI test type. 
                - **created** *(datetime) --* 
                  When the suite was created.
                - **status** *(string) --* 
                  The suite's status.
                  Allowed values include:
                  * PENDING: A pending status. 
                  * PENDING_CONCURRENCY: A pending concurrency status. 
                  * PENDING_DEVICE: A pending device status. 
                  * PROCESSING: A processing status. 
                  * SCHEDULING: A scheduling status. 
                  * PREPARING: A preparing status. 
                  * RUNNING: A running status. 
                  * COMPLETED: A completed status. 
                  * STOPPING: A stopping status. 
                - **result** *(string) --* 
                  The suite's result.
                  Allowed values include:
                  * PENDING: A pending condition. 
                  * PASSED: A passing condition. 
                  * WARNED: A warning condition. 
                  * FAILED: A failed condition. 
                  * SKIPPED: A skipped condition. 
                  * ERRORED: An error condition. 
                  * STOPPED: A stopped condition. 
                - **started** *(datetime) --* 
                  The suite's start time.
                - **stopped** *(datetime) --* 
                  The suite's stop time.
                - **counters** *(dict) --* 
                  The suite's result counters.
                  - **total** *(integer) --* 
                    The total number of entities.
                  - **passed** *(integer) --* 
                    The number of passed entities.
                  - **failed** *(integer) --* 
                    The number of failed entities.
                  - **warned** *(integer) --* 
                    The number of warned entities.
                  - **errored** *(integer) --* 
                    The number of errored entities.
                  - **stopped** *(integer) --* 
                    The number of stopped entities.
                  - **skipped** *(integer) --* 
                    The number of skipped entities.
                - **message** *(string) --* 
                  A message about the suite's result.
                - **deviceMinutes** *(dict) --* 
                  Represents the total (metered or unmetered) minutes used by the test suite.
                  - **total** *(float) --* 
                    When specified, represents the total minutes used by the resource to run tests.
                  - **metered** *(float) --* 
                    When specified, represents only the sum of metered minutes used by the resource to run tests.
                  - **unmetered** *(float) --* 
                    When specified, represents only the sum of unmetered minutes used by the resource to run tests.
            - **nextToken** *(string) --* 
              If the number of items that are returned is significantly large, this is an identifier that is also returned, which can be used in a subsequent call to this operation to return the next set of items in the list.
        :type arn: string
        :param arn: **[REQUIRED]**
          The job\'s Amazon Resource Name (ARN).
        :type nextToken: string
        :param nextToken:
          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :rtype: dict
        :returns:
        """
        pass

    def list_tests(self, arn: str, nextToken: str = None) -> Dict:
        """
        Gets information about tests in a given test suite.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListTests>`_
        
        **Request Syntax**
        ::
          response = client.list_tests(
              arn='string',
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'tests': [
                    {
                        'arn': 'string',
                        'name': 'string',
                        'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
                        'created': datetime(2015, 1, 1),
                        'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                        'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                        'started': datetime(2015, 1, 1),
                        'stopped': datetime(2015, 1, 1),
                        'counters': {
                            'total': 123,
                            'passed': 123,
                            'failed': 123,
                            'warned': 123,
                            'errored': 123,
                            'stopped': 123,
                            'skipped': 123
                        },
                        'message': 'string',
                        'deviceMinutes': {
                            'total': 123.0,
                            'metered': 123.0,
                            'unmetered': 123.0
                        }
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of a list tests request.
            - **tests** *(list) --* 
              Information about the tests.
              - *(dict) --* 
                Represents a condition that is evaluated.
                - **arn** *(string) --* 
                  The test's ARN.
                - **name** *(string) --* 
                  The test's name.
                - **type** *(string) --* 
                  The test's type.
                  Must be one of the following values:
                  * BUILTIN_FUZZ: The built-in fuzz type. 
                  * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
                  * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
                  * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
                  * APPIUM_PYTHON: The Appium Python type. 
                  * APPIUM_NODE: The Appium Node.js type. 
                  * APPIUM_RUBY: The Appium Ruby type. 
                  * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for web apps. 
                  * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for web apps. 
                  * APPIUM_WEB_PYTHON: The Appium Python type for web apps. 
                  * APPIUM_WEB_NODE: The Appium Node.js type for web apps. 
                  * APPIUM_WEB_RUBY: The Appium Ruby type for web apps. 
                  * CALABASH: The Calabash type. 
                  * INSTRUMENTATION: The Instrumentation type. 
                  * UIAUTOMATION: The uiautomation type. 
                  * UIAUTOMATOR: The uiautomator type. 
                  * XCTEST: The XCode test type. 
                  * XCTEST_UI: The XCode UI test type. 
                - **created** *(datetime) --* 
                  When the test was created.
                - **status** *(string) --* 
                  The test's status.
                  Allowed values include:
                  * PENDING: A pending status. 
                  * PENDING_CONCURRENCY: A pending concurrency status. 
                  * PENDING_DEVICE: A pending device status. 
                  * PROCESSING: A processing status. 
                  * SCHEDULING: A scheduling status. 
                  * PREPARING: A preparing status. 
                  * RUNNING: A running status. 
                  * COMPLETED: A completed status. 
                  * STOPPING: A stopping status. 
                - **result** *(string) --* 
                  The test's result.
                  Allowed values include:
                  * PENDING: A pending condition. 
                  * PASSED: A passing condition. 
                  * WARNED: A warning condition. 
                  * FAILED: A failed condition. 
                  * SKIPPED: A skipped condition. 
                  * ERRORED: An error condition. 
                  * STOPPED: A stopped condition. 
                - **started** *(datetime) --* 
                  The test's start time.
                - **stopped** *(datetime) --* 
                  The test's stop time.
                - **counters** *(dict) --* 
                  The test's result counters.
                  - **total** *(integer) --* 
                    The total number of entities.
                  - **passed** *(integer) --* 
                    The number of passed entities.
                  - **failed** *(integer) --* 
                    The number of failed entities.
                  - **warned** *(integer) --* 
                    The number of warned entities.
                  - **errored** *(integer) --* 
                    The number of errored entities.
                  - **stopped** *(integer) --* 
                    The number of stopped entities.
                  - **skipped** *(integer) --* 
                    The number of skipped entities.
                - **message** *(string) --* 
                  A message about the test's result.
                - **deviceMinutes** *(dict) --* 
                  Represents the total (metered or unmetered) minutes used by the test.
                  - **total** *(float) --* 
                    When specified, represents the total minutes used by the resource to run tests.
                  - **metered** *(float) --* 
                    When specified, represents only the sum of metered minutes used by the resource to run tests.
                  - **unmetered** *(float) --* 
                    When specified, represents only the sum of unmetered minutes used by the resource to run tests.
            - **nextToken** *(string) --* 
              If the number of items that are returned is significantly large, this is an identifier that is also returned, which can be used in a subsequent call to this operation to return the next set of items in the list.
        :type arn: string
        :param arn: **[REQUIRED]**
          The test suite\'s Amazon Resource Name (ARN).
        :type nextToken: string
        :param nextToken:
          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :rtype: dict
        :returns:
        """
        pass

    def list_unique_problems(self, arn: str, nextToken: str = None) -> Dict:
        """
        Gets information about unique problems.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListUniqueProblems>`_
        
        **Request Syntax**
        ::
          response = client.list_unique_problems(
              arn='string',
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'uniqueProblems': {
                    'string': [
                        {
                            'message': 'string',
                            'problems': [
                                {
                                    'run': {
                                        'arn': 'string',
                                        'name': 'string'
                                    },
                                    'job': {
                                        'arn': 'string',
                                        'name': 'string'
                                    },
                                    'suite': {
                                        'arn': 'string',
                                        'name': 'string'
                                    },
                                    'test': {
                                        'arn': 'string',
                                        'name': 'string'
                                    },
                                    'device': {
                                        'arn': 'string',
                                        'name': 'string',
                                        'manufacturer': 'string',
                                        'model': 'string',
                                        'modelId': 'string',
                                        'formFactor': 'PHONE'|'TABLET',
                                        'platform': 'ANDROID'|'IOS',
                                        'os': 'string',
                                        'cpu': {
                                            'frequency': 'string',
                                            'architecture': 'string',
                                            'clock': 123.0
                                        },
                                        'resolution': {
                                            'width': 123,
                                            'height': 123
                                        },
                                        'heapSize': 123,
                                        'memory': 123,
                                        'image': 'string',
                                        'carrier': 'string',
                                        'radio': 'string',
                                        'remoteAccessEnabled': True|False,
                                        'remoteDebugEnabled': True|False,
                                        'fleetType': 'string',
                                        'fleetName': 'string',
                                        'instances': [
                                            {
                                                'arn': 'string',
                                                'deviceArn': 'string',
                                                'labels': [
                                                    'string',
                                                ],
                                                'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                                                'udid': 'string',
                                                'instanceProfile': {
                                                    'arn': 'string',
                                                    'packageCleanup': True|False,
                                                    'excludeAppPackagesFromCleanup': [
                                                        'string',
                                                    ],
                                                    'rebootAfterUse': True|False,
                                                    'name': 'string',
                                                    'description': 'string'
                                                }
                                            },
                                        ],
                                        'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
                                    },
                                    'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                                    'message': 'string'
                                },
                            ]
                        },
                    ]
                },
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of a list unique problems request.
            - **uniqueProblems** *(dict) --* 
              Information about the unique problems.
              Allowed values include:
              * PENDING: A pending condition. 
              * PASSED: A passing condition. 
              * WARNED: A warning condition. 
              * FAILED: A failed condition. 
              * SKIPPED: A skipped condition. 
              * ERRORED: An error condition. 
              * STOPPED: A stopped condition. 
              - *(string) --* 
                - *(list) --* 
                  - *(dict) --* 
                    A collection of one or more problems, grouped by their result.
                    - **message** *(string) --* 
                      A message about the unique problems' result.
                    - **problems** *(list) --* 
                      Information about the problems.
                      - *(dict) --* 
                        Represents a specific warning or failure.
                        - **run** *(dict) --* 
                          Information about the associated run.
                          - **arn** *(string) --* 
                            The problem detail's ARN.
                          - **name** *(string) --* 
                            The problem detail's name.
                        - **job** *(dict) --* 
                          Information about the associated job.
                          - **arn** *(string) --* 
                            The problem detail's ARN.
                          - **name** *(string) --* 
                            The problem detail's name.
                        - **suite** *(dict) --* 
                          Information about the associated suite.
                          - **arn** *(string) --* 
                            The problem detail's ARN.
                          - **name** *(string) --* 
                            The problem detail's name.
                        - **test** *(dict) --* 
                          Information about the associated test.
                          - **arn** *(string) --* 
                            The problem detail's ARN.
                          - **name** *(string) --* 
                            The problem detail's name.
                        - **device** *(dict) --* 
                          Information about the associated device.
                          - **arn** *(string) --* 
                            The device's ARN.
                          - **name** *(string) --* 
                            The device's display name.
                          - **manufacturer** *(string) --* 
                            The device's manufacturer name.
                          - **model** *(string) --* 
                            The device's model name.
                          - **modelId** *(string) --* 
                            The device's model ID.
                          - **formFactor** *(string) --* 
                            The device's form factor.
                            Allowed values include:
                            * PHONE: The phone form factor. 
                            * TABLET: The tablet form factor. 
                          - **platform** *(string) --* 
                            The device's platform.
                            Allowed values include:
                            * ANDROID: The Android platform. 
                            * IOS: The iOS platform. 
                          - **os** *(string) --* 
                            The device's operating system type.
                          - **cpu** *(dict) --* 
                            Information about the device's CPU.
                            - **frequency** *(string) --* 
                              The CPU's frequency.
                            - **architecture** *(string) --* 
                              The CPU's architecture, for example x86 or ARM.
                            - **clock** *(float) --* 
                              The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.
                          - **resolution** *(dict) --* 
                            The resolution of the device.
                            - **width** *(integer) --* 
                              The screen resolution's width, expressed in pixels.
                            - **height** *(integer) --* 
                              The screen resolution's height, expressed in pixels.
                          - **heapSize** *(integer) --* 
                            The device's heap size, expressed in bytes.
                          - **memory** *(integer) --* 
                            The device's total memory size, expressed in bytes.
                          - **image** *(string) --* 
                            The device's image name.
                          - **carrier** *(string) --* 
                            The device's carrier.
                          - **radio** *(string) --* 
                            The device's radio.
                          - **remoteAccessEnabled** *(boolean) --* 
                            Specifies whether remote access has been enabled for the specified device.
                          - **remoteDebugEnabled** *(boolean) --* 
                            This flag is set to ``true`` if remote debugging is enabled for the device.
                          - **fleetType** *(string) --* 
                            The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.
                          - **fleetName** *(string) --* 
                            The name of the fleet to which this device belongs.
                          - **instances** *(list) --* 
                            The instances belonging to this device.
                            - *(dict) --* 
                              Represents the device instance.
                              - **arn** *(string) --* 
                                The Amazon Resource Name (ARN) of the device instance.
                              - **deviceArn** *(string) --* 
                                The Amazon Resource Name (ARN) of the device.
                              - **labels** *(list) --* 
                                An array of strings describing the device instance.
                                - *(string) --* 
                              - **status** *(string) --* 
                                The status of the device instance. Valid values are listed below.
                              - **udid** *(string) --* 
                                Unique device identifier for the device instance.
                              - **instanceProfile** *(dict) --* 
                                A object containing information about the instance profile.
                                - **arn** *(string) --* 
                                  The Amazon Resource Name (ARN) of the instance profile.
                                - **packageCleanup** *(boolean) --* 
                                  When set to ``true`` , Device Farm will remove app packages after a test run. The default value is ``false`` for private devices.
                                - **excludeAppPackagesFromCleanup** *(list) --* 
                                  An array of strings specifying the list of app packages that should not be cleaned up from the device after a test run is over.
                                  The list of packages is only considered if you set ``packageCleanup`` to ``true`` .
                                  - *(string) --* 
                                - **rebootAfterUse** *(boolean) --* 
                                  When set to ``true`` , Device Farm will reboot the instance after a test run. The default value is ``true`` .
                                - **name** *(string) --* 
                                  The name of the instance profile.
                                - **description** *(string) --* 
                                  The description of the instance profile.
                          - **availability** *(string) --* 
                            Reflects how likely a device will be available for a test run. It is currently available in the ListDevices and GetDevice API methods.
                        - **result** *(string) --* 
                          The problem's result.
                          Allowed values include:
                          * PENDING: A pending condition. 
                          * PASSED: A passing condition. 
                          * WARNED: A warning condition. 
                          * FAILED: A failed condition. 
                          * SKIPPED: A skipped condition. 
                          * ERRORED: An error condition. 
                          * STOPPED: A stopped condition. 
                        - **message** *(string) --* 
                          A message about the problem's result.
            - **nextToken** *(string) --* 
              If the number of items that are returned is significantly large, this is an identifier that is also returned, which can be used in a subsequent call to this operation to return the next set of items in the list.
        :type arn: string
        :param arn: **[REQUIRED]**
          The unique problems\' ARNs.
        :type nextToken: string
        :param nextToken:
          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :rtype: dict
        :returns:
        """
        pass

    def list_uploads(self, arn: str, type: str = None, nextToken: str = None) -> Dict:
        """
        Gets information about uploads, given an AWS Device Farm project ARN.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListUploads>`_
        
        **Request Syntax**
        ::
          response = client.list_uploads(
              arn='string',
              type='ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_NODE_TEST_PACKAGE'|'APPIUM_RUBY_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_NODE_TEST_PACKAGE'|'APPIUM_WEB_RUBY_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE'|'APPIUM_JAVA_JUNIT_TEST_SPEC'|'APPIUM_JAVA_TESTNG_TEST_SPEC'|'APPIUM_PYTHON_TEST_SPEC'|'APPIUM_NODE_TEST_SPEC'|'APPIUM_RUBY_TEST_SPEC'|'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC'|'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC'|'APPIUM_WEB_PYTHON_TEST_SPEC'|'APPIUM_WEB_NODE_TEST_SPEC'|'APPIUM_WEB_RUBY_TEST_SPEC'|'INSTRUMENTATION_TEST_SPEC'|'XCTEST_UI_TEST_SPEC',
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'uploads': [
                    {
                        'arn': 'string',
                        'name': 'string',
                        'created': datetime(2015, 1, 1),
                        'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_NODE_TEST_PACKAGE'|'APPIUM_RUBY_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_NODE_TEST_PACKAGE'|'APPIUM_WEB_RUBY_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE'|'APPIUM_JAVA_JUNIT_TEST_SPEC'|'APPIUM_JAVA_TESTNG_TEST_SPEC'|'APPIUM_PYTHON_TEST_SPEC'|'APPIUM_NODE_TEST_SPEC'|'APPIUM_RUBY_TEST_SPEC'|'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC'|'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC'|'APPIUM_WEB_PYTHON_TEST_SPEC'|'APPIUM_WEB_NODE_TEST_SPEC'|'APPIUM_WEB_RUBY_TEST_SPEC'|'INSTRUMENTATION_TEST_SPEC'|'XCTEST_UI_TEST_SPEC',
                        'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
                        'url': 'string',
                        'metadata': 'string',
                        'contentType': 'string',
                        'message': 'string',
                        'category': 'CURATED'|'PRIVATE'
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of a list uploads request.
            - **uploads** *(list) --* 
              Information about the uploads.
              - *(dict) --* 
                An app or a set of one or more tests to upload or that have been uploaded.
                - **arn** *(string) --* 
                  The upload's ARN.
                - **name** *(string) --* 
                  The upload's file name.
                - **created** *(datetime) --* 
                  When the upload was created.
                - **type** *(string) --* 
                  The upload's type.
                  Must be one of the following values:
                  * ANDROID_APP: An Android upload. 
                  * IOS_APP: An iOS upload. 
                  * WEB_APP: A web appliction upload. 
                  * EXTERNAL_DATA: An external data upload. 
                  * APPIUM_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload. 
                  * APPIUM_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload. 
                  * APPIUM_PYTHON_TEST_PACKAGE: An Appium Python test package upload. 
                  * APPIUM_NODE_TEST_PACKAGE: An Appium Node.js test package upload. 
                  * APPIUM_RUBY_TEST_PACKAGE: An Appium Ruby test package upload. 
                  * APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload for web apps. 
                  * APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload for web apps. 
                  * APPIUM_WEB_PYTHON_TEST_PACKAGE: An Appium Python test package upload for web apps. 
                  * APPIUM_WEB_NODE_TEST_PACKAGE: An Appium Node.js test package upload for web apps. 
                  * APPIUM_WEB_RUBY_TEST_PACKAGE: An Appium Ruby test package upload for web apps. 
                  * CALABASH_TEST_PACKAGE: A Calabash test package upload. 
                  * INSTRUMENTATION_TEST_PACKAGE: An instrumentation upload. 
                  * UIAUTOMATION_TEST_PACKAGE: A uiautomation test package upload. 
                  * UIAUTOMATOR_TEST_PACKAGE: A uiautomator test package upload. 
                  * XCTEST_TEST_PACKAGE: An XCode test package upload. 
                  * XCTEST_UI_TEST_PACKAGE: An XCode UI test package upload. 
                  * APPIUM_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload. 
                  * APPIUM_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload. 
                  * APPIUM_PYTHON_TEST_SPEC: An Appium Python test spec upload. 
                  * APPIUM_NODE_TEST_SPEC: An Appium Node.js test spec upload. 
                  * APPIUM_RUBY_TEST_SPEC: An Appium Ruby test spec upload. 
                  * APPIUM_WEB_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload for a web app. 
                  * APPIUM_WEB_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload for a web app. 
                  * APPIUM_WEB_PYTHON_TEST_SPEC: An Appium Python test spec upload for a web app. 
                  * APPIUM_WEB_NODE_TEST_SPEC: An Appium Node.js test spec upload for a web app. 
                  * APPIUM_WEB_RUBY_TEST_SPEC: An Appium Ruby test spec upload for a web app. 
                  * INSTRUMENTATION_TEST_SPEC: An instrumentation test spec upload. 
                  * XCTEST_UI_TEST_SPEC: An XCode UI test spec upload. 
                - **status** *(string) --* 
                  The upload's status.
                  Must be one of the following values:
                  * FAILED: A failed status. 
                  * INITIALIZED: An initialized status. 
                  * PROCESSING: A processing status. 
                  * SUCCEEDED: A succeeded status. 
                - **url** *(string) --* 
                  The pre-signed Amazon S3 URL that was used to store a file through a corresponding PUT request.
                - **metadata** *(string) --* 
                  The upload's metadata. For example, for Android, this contains information that is parsed from the manifest and is displayed in the AWS Device Farm console after the associated app is uploaded.
                - **contentType** *(string) --* 
                  The upload's content type (for example, "application/octet-stream").
                - **message** *(string) --* 
                  A message about the upload's result.
                - **category** *(string) --* 
                  The upload's category. Allowed values include:
                  * CURATED: An upload managed by AWS Device Farm. 
                  * PRIVATE: An upload managed by the AWS Device Farm customer. 
            - **nextToken** *(string) --* 
              If the number of items that are returned is significantly large, this is an identifier that is also returned, which can be used in a subsequent call to this operation to return the next set of items in the list.
        :type arn: string
        :param arn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the project for which you want to list uploads.
        :type type: string
        :param type:
          The type of upload.
          Must be one of the following values:
          * ANDROID_APP: An Android upload.
          * IOS_APP: An iOS upload.
          * WEB_APP: A web appliction upload.
          * EXTERNAL_DATA: An external data upload.
          * APPIUM_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload.
          * APPIUM_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload.
          * APPIUM_PYTHON_TEST_PACKAGE: An Appium Python test package upload.
          * APPIUM_NODE_TEST_PACKAGE: An Appium Node.js test package upload.
          * APPIUM_RUBY_TEST_PACKAGE: An Appium Ruby test package upload.
          * APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload for a web app.
          * APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload for a web app.
          * APPIUM_WEB_PYTHON_TEST_PACKAGE: An Appium Python test package upload for a web app.
          * APPIUM_WEB_NODE_TEST_PACKAGE: An Appium Node.js test package upload for a web app.
          * APPIUM_WEB_RUBY_TEST_PACKAGE: An Appium Ruby test package upload for a web app.
          * CALABASH_TEST_PACKAGE: A Calabash test package upload.
          * INSTRUMENTATION_TEST_PACKAGE: An instrumentation upload.
          * UIAUTOMATION_TEST_PACKAGE: A uiautomation test package upload.
          * UIAUTOMATOR_TEST_PACKAGE: A uiautomator test package upload.
          * XCTEST_TEST_PACKAGE: An XCode test package upload.
          * XCTEST_UI_TEST_PACKAGE: An XCode UI test package upload.
          * APPIUM_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload.
          * APPIUM_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload.
          * APPIUM_PYTHON_TEST_SPEC: An Appium Python test spec upload.
          * APPIUM_NODE_TEST_SPEC: An Appium Node.js test spec upload.
          * APPIUM_RUBY_TEST_SPEC: An Appium Ruby test spec upload.
          * APPIUM_WEB_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload for a web app.
          * APPIUM_WEB_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload for a web app.
          * APPIUM_WEB_PYTHON_TEST_SPEC: An Appium Python test spec upload for a web app.
          * APPIUM_WEB_NODE_TEST_SPEC: An Appium Node.js test spec upload for a web app.
          * APPIUM_WEB_RUBY_TEST_SPEC: An Appium Ruby test spec upload for a web app.
          * INSTRUMENTATION_TEST_SPEC: An instrumentation test spec upload.
          * XCTEST_UI_TEST_SPEC: An XCode UI test spec upload.
        :type nextToken: string
        :param nextToken:
          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :rtype: dict
        :returns:
        """
        pass

    def list_vpce_configurations(self, maxResults: int = None, nextToken: str = None) -> Dict:
        """
        Returns information about all Amazon Virtual Private Cloud (VPC) endpoint configurations in the AWS account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListVPCEConfigurations>`_
        
        **Request Syntax**
        ::
          response = client.list_vpce_configurations(
              maxResults=123,
              nextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'vpceConfigurations': [
                    {
                        'arn': 'string',
                        'vpceConfigurationName': 'string',
                        'vpceServiceName': 'string',
                        'serviceDnsName': 'string',
                        'vpceConfigurationDescription': 'string'
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **vpceConfigurations** *(list) --* 
              An array of ``VPCEConfiguration`` objects containing information about your VPC endpoint configuration.
              - *(dict) --* 
                Represents an Amazon Virtual Private Cloud (VPC) endpoint configuration.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the VPC endpoint configuration.
                - **vpceConfigurationName** *(string) --* 
                  The friendly name you give to your VPC endpoint configuration, to manage your configurations more easily.
                - **vpceServiceName** *(string) --* 
                  The name of the VPC endpoint service running inside your AWS account that you want Device Farm to test.
                - **serviceDnsName** *(string) --* 
                  The DNS name that maps to the private IP address of the service you want to access.
                - **vpceConfigurationDescription** *(string) --* 
                  An optional description, providing more details about your VPC endpoint configuration.
            - **nextToken** *(string) --* 
              An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :type maxResults: integer
        :param maxResults:
          An integer specifying the maximum number of items you want to return in the API response.
        :type nextToken: string
        :param nextToken:
          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
        :rtype: dict
        :returns:
        """
        pass

    def purchase_offering(self, offeringId: str = None, quantity: int = None, offeringPromotionId: str = None) -> Dict:
        """
        Immediately purchases offerings for an AWS account. Offerings renew with the latest total purchased quantity for an offering, unless the renewal was overridden. The API returns a ``NotEligible`` error if the user is not permitted to invoke the operation. Please contact `aws-devicefarm-support@amazon.com <mailto:aws-devicefarm-support@amazon.com>`__ if you believe that you should be able to invoke this operation.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/PurchaseOffering>`_
        
        **Request Syntax**
        ::
          response = client.purchase_offering(
              offeringId='string',
              quantity=123,
              offeringPromotionId='string'
          )
        
        **Response Syntax**
        ::
            {
                'offeringTransaction': {
                    'offeringStatus': {
                        'type': 'PURCHASE'|'RENEW'|'SYSTEM',
                        'offering': {
                            'id': 'string',
                            'description': 'string',
                            'type': 'RECURRING',
                            'platform': 'ANDROID'|'IOS',
                            'recurringCharges': [
                                {
                                    'cost': {
                                        'amount': 123.0,
                                        'currencyCode': 'USD'
                                    },
                                    'frequency': 'MONTHLY'
                                },
                            ]
                        },
                        'quantity': 123,
                        'effectiveOn': datetime(2015, 1, 1)
                    },
                    'transactionId': 'string',
                    'offeringPromotionId': 'string',
                    'createdOn': datetime(2015, 1, 1),
                    'cost': {
                        'amount': 123.0,
                        'currencyCode': 'USD'
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            The result of the purchase offering (e.g., success or failure).
            - **offeringTransaction** *(dict) --* 
              Represents the offering transaction for the purchase result.
              - **offeringStatus** *(dict) --* 
                The status of an offering transaction.
                - **type** *(string) --* 
                  The type specified for the offering status.
                - **offering** *(dict) --* 
                  Represents the metadata of an offering status.
                  - **id** *(string) --* 
                    The ID that corresponds to a device offering.
                  - **description** *(string) --* 
                    A string describing the offering.
                  - **type** *(string) --* 
                    The type of offering (e.g., "RECURRING") for a device.
                  - **platform** *(string) --* 
                    The platform of the device (e.g., ANDROID or IOS).
                  - **recurringCharges** *(list) --* 
                    Specifies whether there are recurring charges for the offering.
                    - *(dict) --* 
                      Specifies whether charges for devices will be recurring.
                      - **cost** *(dict) --* 
                        The cost of the recurring charge.
                        - **amount** *(float) --* 
                          The numerical amount of an offering or transaction.
                        - **currencyCode** *(string) --* 
                          The currency code of a monetary amount. For example, ``USD`` means "U.S. dollars."
                      - **frequency** *(string) --* 
                        The frequency in which charges will recur.
                - **quantity** *(integer) --* 
                  The number of available devices in the offering.
                - **effectiveOn** *(datetime) --* 
                  The date on which the offering is effective.
              - **transactionId** *(string) --* 
                The transaction ID of the offering transaction.
              - **offeringPromotionId** *(string) --* 
                The ID that corresponds to a device offering promotion.
              - **createdOn** *(datetime) --* 
                The date on which an offering transaction was created.
              - **cost** *(dict) --* 
                The cost of an offering transaction.
                - **amount** *(float) --* 
                  The numerical amount of an offering or transaction.
                - **currencyCode** *(string) --* 
                  The currency code of a monetary amount. For example, ``USD`` means "U.S. dollars."
        :type offeringId: string
        :param offeringId:
          The ID of the offering.
        :type quantity: integer
        :param quantity:
          The number of device slots you wish to purchase in an offering request.
        :type offeringPromotionId: string
        :param offeringPromotionId:
          The ID of the offering promotion to be applied to the purchase.
        :rtype: dict
        :returns:
        """
        pass

    def renew_offering(self, offeringId: str = None, quantity: int = None) -> Dict:
        """
        Explicitly sets the quantity of devices to renew for an offering, starting from the ``effectiveDate`` of the next period. The API returns a ``NotEligible`` error if the user is not permitted to invoke the operation. Please contact `aws-devicefarm-support@amazon.com <mailto:aws-devicefarm-support@amazon.com>`__ if you believe that you should be able to invoke this operation.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/RenewOffering>`_
        
        **Request Syntax**
        ::
          response = client.renew_offering(
              offeringId='string',
              quantity=123
          )
        
        **Response Syntax**
        ::
            {
                'offeringTransaction': {
                    'offeringStatus': {
                        'type': 'PURCHASE'|'RENEW'|'SYSTEM',
                        'offering': {
                            'id': 'string',
                            'description': 'string',
                            'type': 'RECURRING',
                            'platform': 'ANDROID'|'IOS',
                            'recurringCharges': [
                                {
                                    'cost': {
                                        'amount': 123.0,
                                        'currencyCode': 'USD'
                                    },
                                    'frequency': 'MONTHLY'
                                },
                            ]
                        },
                        'quantity': 123,
                        'effectiveOn': datetime(2015, 1, 1)
                    },
                    'transactionId': 'string',
                    'offeringPromotionId': 'string',
                    'createdOn': datetime(2015, 1, 1),
                    'cost': {
                        'amount': 123.0,
                        'currencyCode': 'USD'
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            The result of a renewal offering.
            - **offeringTransaction** *(dict) --* 
              Represents the status of the offering transaction for the renewal.
              - **offeringStatus** *(dict) --* 
                The status of an offering transaction.
                - **type** *(string) --* 
                  The type specified for the offering status.
                - **offering** *(dict) --* 
                  Represents the metadata of an offering status.
                  - **id** *(string) --* 
                    The ID that corresponds to a device offering.
                  - **description** *(string) --* 
                    A string describing the offering.
                  - **type** *(string) --* 
                    The type of offering (e.g., "RECURRING") for a device.
                  - **platform** *(string) --* 
                    The platform of the device (e.g., ANDROID or IOS).
                  - **recurringCharges** *(list) --* 
                    Specifies whether there are recurring charges for the offering.
                    - *(dict) --* 
                      Specifies whether charges for devices will be recurring.
                      - **cost** *(dict) --* 
                        The cost of the recurring charge.
                        - **amount** *(float) --* 
                          The numerical amount of an offering or transaction.
                        - **currencyCode** *(string) --* 
                          The currency code of a monetary amount. For example, ``USD`` means "U.S. dollars."
                      - **frequency** *(string) --* 
                        The frequency in which charges will recur.
                - **quantity** *(integer) --* 
                  The number of available devices in the offering.
                - **effectiveOn** *(datetime) --* 
                  The date on which the offering is effective.
              - **transactionId** *(string) --* 
                The transaction ID of the offering transaction.
              - **offeringPromotionId** *(string) --* 
                The ID that corresponds to a device offering promotion.
              - **createdOn** *(datetime) --* 
                The date on which an offering transaction was created.
              - **cost** *(dict) --* 
                The cost of an offering transaction.
                - **amount** *(float) --* 
                  The numerical amount of an offering or transaction.
                - **currencyCode** *(string) --* 
                  The currency code of a monetary amount. For example, ``USD`` means "U.S. dollars."
        :type offeringId: string
        :param offeringId:
          The ID of a request to renew an offering.
        :type quantity: integer
        :param quantity:
          The quantity requested in an offering renewal.
        :rtype: dict
        :returns:
        """
        pass

    def schedule_run(self, projectArn: str, test: Dict, appArn: str = None, devicePoolArn: str = None, deviceSelectionConfiguration: Dict = None, name: str = None, configuration: Dict = None, executionConfiguration: Dict = None) -> Dict:
        """
        Schedules a run.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ScheduleRun>`_
        
        **Request Syntax**
        ::
          response = client.schedule_run(
              projectArn='string',
              appArn='string',
              devicePoolArn='string',
              deviceSelectionConfiguration={
                  'filters': [
                      {
                          'attribute': 'ARN'|'PLATFORM'|'OS_VERSION'|'MODEL'|'AVAILABILITY'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                          'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                          'values': [
                              'string',
                          ]
                      },
                  ],
                  'maxDevices': 123
              },
              name='string',
              test={
                  'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
                  'testPackageArn': 'string',
                  'testSpecArn': 'string',
                  'filter': 'string',
                  'parameters': {
                      'string': 'string'
                  }
              },
              configuration={
                  'extraDataPackageArn': 'string',
                  'networkProfileArn': 'string',
                  'locale': 'string',
                  'location': {
                      'latitude': 123.0,
                      'longitude': 123.0
                  },
                  'vpceConfigurationArns': [
                      'string',
                  ],
                  'customerArtifactPaths': {
                      'iosPaths': [
                          'string',
                      ],
                      'androidPaths': [
                          'string',
                      ],
                      'deviceHostPaths': [
                          'string',
                      ]
                  },
                  'radios': {
                      'wifi': True|False,
                      'bluetooth': True|False,
                      'nfc': True|False,
                      'gps': True|False
                  },
                  'auxiliaryApps': [
                      'string',
                  ],
                  'billingMethod': 'METERED'|'UNMETERED'
              },
              executionConfiguration={
                  'jobTimeoutMinutes': 123,
                  'accountsCleanup': True|False,
                  'appPackagesCleanup': True|False,
                  'videoCapture': True|False,
                  'skipAppResign': True|False
              }
          )
        
        **Response Syntax**
        ::
            {
                'run': {
                    'arn': 'string',
                    'name': 'string',
                    'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
                    'platform': 'ANDROID'|'IOS',
                    'created': datetime(2015, 1, 1),
                    'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                    'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                    'started': datetime(2015, 1, 1),
                    'stopped': datetime(2015, 1, 1),
                    'counters': {
                        'total': 123,
                        'passed': 123,
                        'failed': 123,
                        'warned': 123,
                        'errored': 123,
                        'stopped': 123,
                        'skipped': 123
                    },
                    'message': 'string',
                    'totalJobs': 123,
                    'completedJobs': 123,
                    'billingMethod': 'METERED'|'UNMETERED',
                    'deviceMinutes': {
                        'total': 123.0,
                        'metered': 123.0,
                        'unmetered': 123.0
                    },
                    'networkProfile': {
                        'arn': 'string',
                        'name': 'string',
                        'description': 'string',
                        'type': 'CURATED'|'PRIVATE',
                        'uplinkBandwidthBits': 123,
                        'downlinkBandwidthBits': 123,
                        'uplinkDelayMs': 123,
                        'downlinkDelayMs': 123,
                        'uplinkJitterMs': 123,
                        'downlinkJitterMs': 123,
                        'uplinkLossPercent': 123,
                        'downlinkLossPercent': 123
                    },
                    'parsingResultUrl': 'string',
                    'resultCode': 'PARSING_FAILED'|'VPC_ENDPOINT_SETUP_FAILED',
                    'seed': 123,
                    'appUpload': 'string',
                    'eventCount': 123,
                    'jobTimeoutMinutes': 123,
                    'devicePoolArn': 'string',
                    'locale': 'string',
                    'radios': {
                        'wifi': True|False,
                        'bluetooth': True|False,
                        'nfc': True|False,
                        'gps': True|False
                    },
                    'location': {
                        'latitude': 123.0,
                        'longitude': 123.0
                    },
                    'customerArtifactPaths': {
                        'iosPaths': [
                            'string',
                        ],
                        'androidPaths': [
                            'string',
                        ],
                        'deviceHostPaths': [
                            'string',
                        ]
                    },
                    'webUrl': 'string',
                    'skipAppResign': True|False,
                    'testSpecArn': 'string',
                    'deviceSelectionResult': {
                        'filters': [
                            {
                                'attribute': 'ARN'|'PLATFORM'|'OS_VERSION'|'MODEL'|'AVAILABILITY'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                                'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                                'values': [
                                    'string',
                                ]
                            },
                        ],
                        'matchedDevicesCount': 123,
                        'maxDevices': 123
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of a schedule run request.
            - **run** *(dict) --* 
              Information about the scheduled run.
              - **arn** *(string) --* 
                The run's ARN.
              - **name** *(string) --* 
                The run's name.
              - **type** *(string) --* 
                The run's type.
                Must be one of the following values:
                * BUILTIN_FUZZ: The built-in fuzz type. 
                * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
                * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
                * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
                * APPIUM_PYTHON: The Appium Python type. 
                * APPIUM_NODE: The Appium Node.js type. 
                * APPIUM_RUBY: The Appium Ruby type. 
                * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for web apps. 
                * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for web apps. 
                * APPIUM_WEB_PYTHON: The Appium Python type for web apps. 
                * APPIUM_WEB_NODE: The Appium Node.js type for web apps. 
                * APPIUM_WEB_RUBY: The Appium Ruby type for web apps. 
                * CALABASH: The Calabash type. 
                * INSTRUMENTATION: The Instrumentation type. 
                * UIAUTOMATION: The uiautomation type. 
                * UIAUTOMATOR: The uiautomator type. 
                * XCTEST: The XCode test type. 
                * XCTEST_UI: The XCode UI test type. 
              - **platform** *(string) --* 
                The run's platform.
                Allowed values include:
                * ANDROID: The Android platform. 
                * IOS: The iOS platform. 
              - **created** *(datetime) --* 
                When the run was created.
              - **status** *(string) --* 
                The run's status.
                Allowed values include:
                * PENDING: A pending status. 
                * PENDING_CONCURRENCY: A pending concurrency status. 
                * PENDING_DEVICE: A pending device status. 
                * PROCESSING: A processing status. 
                * SCHEDULING: A scheduling status. 
                * PREPARING: A preparing status. 
                * RUNNING: A running status. 
                * COMPLETED: A completed status. 
                * STOPPING: A stopping status. 
              - **result** *(string) --* 
                The run's result.
                Allowed values include:
                * PENDING: A pending condition. 
                * PASSED: A passing condition. 
                * WARNED: A warning condition. 
                * FAILED: A failed condition. 
                * SKIPPED: A skipped condition. 
                * ERRORED: An error condition. 
                * STOPPED: A stopped condition. 
              - **started** *(datetime) --* 
                The run's start time.
              - **stopped** *(datetime) --* 
                The run's stop time.
              - **counters** *(dict) --* 
                The run's result counters.
                - **total** *(integer) --* 
                  The total number of entities.
                - **passed** *(integer) --* 
                  The number of passed entities.
                - **failed** *(integer) --* 
                  The number of failed entities.
                - **warned** *(integer) --* 
                  The number of warned entities.
                - **errored** *(integer) --* 
                  The number of errored entities.
                - **stopped** *(integer) --* 
                  The number of stopped entities.
                - **skipped** *(integer) --* 
                  The number of skipped entities.
              - **message** *(string) --* 
                A message about the run's result.
              - **totalJobs** *(integer) --* 
                The total number of jobs for the run.
              - **completedJobs** *(integer) --* 
                The total number of completed jobs.
              - **billingMethod** *(string) --* 
                Specifies the billing method for a test run: ``metered`` or ``unmetered`` . If the parameter is not specified, the default value is ``metered`` .
              - **deviceMinutes** *(dict) --* 
                Represents the total (metered or unmetered) minutes used by the test run.
                - **total** *(float) --* 
                  When specified, represents the total minutes used by the resource to run tests.
                - **metered** *(float) --* 
                  When specified, represents only the sum of metered minutes used by the resource to run tests.
                - **unmetered** *(float) --* 
                  When specified, represents only the sum of unmetered minutes used by the resource to run tests.
              - **networkProfile** *(dict) --* 
                The network profile being used for a test run.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the network profile.
                - **name** *(string) --* 
                  The name of the network profile.
                - **description** *(string) --* 
                  The description of the network profile.
                - **type** *(string) --* 
                  The type of network profile. Valid values are listed below.
                - **uplinkBandwidthBits** *(integer) --* 
                  The data throughput rate in bits per second, as an integer from 0 to 104857600.
                - **downlinkBandwidthBits** *(integer) --* 
                  The data throughput rate in bits per second, as an integer from 0 to 104857600.
                - **uplinkDelayMs** *(integer) --* 
                  Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
                - **downlinkDelayMs** *(integer) --* 
                  Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
                - **uplinkJitterMs** *(integer) --* 
                  Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
                - **downlinkJitterMs** *(integer) --* 
                  Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
                - **uplinkLossPercent** *(integer) --* 
                  Proportion of transmitted packets that fail to arrive from 0 to 100 percent.
                - **downlinkLossPercent** *(integer) --* 
                  Proportion of received packets that fail to arrive from 0 to 100 percent.
              - **parsingResultUrl** *(string) --* 
                Read-only URL for an object in S3 bucket where you can get the parsing results of the test package. If the test package doesn't parse, the reason why it doesn't parse appears in the file that this URL points to.
              - **resultCode** *(string) --* 
                Supporting field for the result field. Set only if ``result`` is ``SKIPPED`` . ``PARSING_FAILED`` if the result is skipped because of test package parsing failure.
              - **seed** *(integer) --* 
                For fuzz tests, this is a seed to use for randomizing the UI fuzz test. Using the same seed value between tests ensures identical event sequences.
              - **appUpload** *(string) --* 
                An app to upload or that has been uploaded.
              - **eventCount** *(integer) --* 
                For fuzz tests, this is the number of events, between 1 and 10000, that the UI fuzz test should perform.
              - **jobTimeoutMinutes** *(integer) --* 
                The number of minutes the job will execute before it times out.
              - **devicePoolArn** *(string) --* 
                The ARN of the device pool for the run.
              - **locale** *(string) --* 
                Information about the locale that is used for the run.
              - **radios** *(dict) --* 
                Information about the radio states for the run.
                - **wifi** *(boolean) --* 
                  True if Wi-Fi is enabled at the beginning of the test; otherwise, false.
                - **bluetooth** *(boolean) --* 
                  True if Bluetooth is enabled at the beginning of the test; otherwise, false.
                - **nfc** *(boolean) --* 
                  True if NFC is enabled at the beginning of the test; otherwise, false.
                - **gps** *(boolean) --* 
                  True if GPS is enabled at the beginning of the test; otherwise, false.
              - **location** *(dict) --* 
                Information about the location that is used for the run.
                - **latitude** *(float) --* 
                  The latitude.
                - **longitude** *(float) --* 
                  The longitude.
              - **customerArtifactPaths** *(dict) --* 
                Output ``CustomerArtifactPaths`` object for the test run.
                - **iosPaths** *(list) --* 
                  Comma-separated list of paths on the iOS device where the artifacts generated by the customer's tests will be pulled from.
                  - *(string) --* 
                - **androidPaths** *(list) --* 
                  Comma-separated list of paths on the Android device where the artifacts generated by the customer's tests will be pulled from.
                  - *(string) --* 
                - **deviceHostPaths** *(list) --* 
                  Comma-separated list of paths in the test execution environment where the artifacts generated by the customer's tests will be pulled from.
                  - *(string) --* 
              - **webUrl** *(string) --* 
                The Device Farm console URL for the recording of the run.
              - **skipAppResign** *(boolean) --* 
                When set to ``true`` , for private devices, Device Farm will not sign your app again. For public devices, Device Farm always signs your apps again and this parameter has no effect.
                For more information about how Device Farm re-signs your app(s), see `Do you modify my app? <https://aws.amazon.com/device-farm/faq/>`__ in the *AWS Device Farm FAQs* .
              - **testSpecArn** *(string) --* 
                The ARN of the YAML-formatted test specification for the run.
              - **deviceSelectionResult** *(dict) --* 
                The results of a device filter used to select the devices for a test run.
                - **filters** *(list) --* 
                  The filters in a device selection result.
                  - *(dict) --* 
                    Represents a device filter used to select a set of devices to be included in a test run. This data structure is passed in as the ``deviceSelectionConfiguration`` parameter to ScheduleRun. For an example of the JSON request syntax, see  ScheduleRun .
                    It is also passed in as the ``filters`` parameter to ListDevices. For an example of the JSON request syntax, see  ListDevices .
                    - **attribute** *(string) --* 
                      The aspect of a device such as platform or model used as the selection criteria in a device filter.
                      The supported operators for each attribute are provided in the following list.
                        ARN  
                      The Amazon Resource Name (ARN) of the device. For example, "arn:aws:devicefarm:us-west-2::device:12345Example".
                       *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                        PLATFORM  
                      The device platform. Valid values are "ANDROID" or "IOS".
                       *Supported operators* : ``EQUALS``  
                        OS_VERSION  
                      The operating system version. For example, "10.3.2".
                       *Supported operators* : ``EQUALS`` , ``GREATER_THAN`` , ``GREATER_THAN_OR_EQUALS`` , ``IN`` , ``LESS_THAN`` , ``LESS_THAN_OR_EQUALS`` , ``NOT_IN``  
                        MODEL  
                      The device model. For example, "iPad 5th Gen".
                       *Supported operators* : ``CONTAINS`` , ``EQUALS`` , ``IN`` , ``NOT_IN``  
                        AVAILABILITY  
                      The current availability of the device. Valid values are "AVAILABLE", "HIGHLY_AVAILABLE", "BUSY", or "TEMPORARY_NOT_AVAILABLE".
                       *Supported operators* : ``EQUALS``  
                        FORM_FACTOR  
                      The device form factor. Valid values are "PHONE" or "TABLET".
                       *Supported operators* : ``EQUALS``  
                        MANUFACTURER  
                      The device manufacturer. For example, "Apple".
                       *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                        REMOTE_ACCESS_ENABLED  
                      Whether the device is enabled for remote access. Valid values are "TRUE" or "FALSE".
                       *Supported operators* : ``EQUALS``  
                        REMOTE_DEBUG_ENABLED  
                      Whether the device is enabled for remote debugging. Valid values are "TRUE" or "FALSE".
                       *Supported operators* : ``EQUALS``  
                        INSTANCE_ARN  
                      The Amazon Resource Name (ARN) of the device instance.
                       *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                        INSTANCE_LABELS  
                      The label of the device instance.
                       *Supported operators* : ``CONTAINS``  
                        FLEET_TYPE  
                      The fleet type. Valid values are "PUBLIC" or "PRIVATE".
                       *Supported operators* : ``EQUALS``  
                    - **operator** *(string) --* 
                      Specifies how Device Farm compares the filter's attribute to the value. For the operators that are supported by each attribute, see the attribute descriptions.
                    - **values** *(list) --* 
                      An array of one or more filter values used in a device filter.
        
        **Operator Values**
                      * The IN and NOT_IN operators can take a values array that has more than one element. 
                      * The other operators require an array with a single element. 
        
        **Attribute Values**
                      * The PLATFORM attribute can be set to "ANDROID" or "IOS". 
                      * The AVAILABILITY attribute can be set to "AVAILABLE", "HIGHLY_AVAILABLE", "BUSY", or "TEMPORARY_NOT_AVAILABLE". 
                      * The FORM_FACTOR attribute can be set to "PHONE" or "TABLET". 
                      * The FLEET_TYPE attribute can be set to "PUBLIC" or "PRIVATE". 
                      - *(string) --* 
                - **matchedDevicesCount** *(integer) --* 
                  The number of devices that matched the device filter selection criteria.
                - **maxDevices** *(integer) --* 
                  The maximum number of devices to be selected by a device filter and included in a test run.
        :type projectArn: string
        :param projectArn: **[REQUIRED]**
          The ARN of the project for the run to be scheduled.
        :type appArn: string
        :param appArn:
          The ARN of the app to schedule a run.
        :type devicePoolArn: string
        :param devicePoolArn:
          The ARN of the device pool for the run to be scheduled.
        :type deviceSelectionConfiguration: dict
        :param deviceSelectionConfiguration:
          The filter criteria used to dynamically select a set of devices for a test run, as well as the maximum number of devices to be included in the run.
          Either ** ``devicePoolArn`` ** or ** ``deviceSelectionConfiguration`` ** is required in a request.
          - **filters** *(list) --* **[REQUIRED]**
            Used to dynamically select a set of devices for a test run. A filter is made up of an attribute, an operator, and one or more values.
            * **Attribute**   The aspect of a device such as platform or model used as the selection criteria in a device filter. Allowed values include:
              * ARN: The Amazon Resource Name (ARN) of the device. For example, \"arn:aws:devicefarm:us-west-2::device:12345Example\".
              * PLATFORM: The device platform. Valid values are \"ANDROID\" or \"IOS\".
              * OS_VERSION: The operating system version. For example, \"10.3.2\".
              * MODEL: The device model. For example, \"iPad 5th Gen\".
              * AVAILABILITY: The current availability of the device. Valid values are \"AVAILABLE\", \"HIGHLY_AVAILABLE\", \"BUSY\", or \"TEMPORARY_NOT_AVAILABLE\".
              * FORM_FACTOR: The device form factor. Valid values are \"PHONE\" or \"TABLET\".
              * MANUFACTURER: The device manufacturer. For example, \"Apple\".
              * REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. Valid values are \"TRUE\" or \"FALSE\".
              * REMOTE_DEBUG_ENABLED: Whether the device is enabled for remote debugging. Valid values are \"TRUE\" or \"FALSE\".
              * INSTANCE_ARN: The Amazon Resource Name (ARN) of the device instance.
              * INSTANCE_LABELS: The label of the device instance.
              * FLEET_TYPE: The fleet type. Valid values are \"PUBLIC\" or \"PRIVATE\".
            * **Operator**   The filter operator.
              * The EQUALS operator is available for every attribute except INSTANCE_LABELS.
              * The CONTAINS operator is available for the INSTANCE_LABELS and MODEL attributes.
              * The IN and NOT_IN operators are available for the ARN, OS_VERSION, MODEL, MANUFACTURER, and INSTANCE_ARN attributes.
              * The LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUALS, and GREATER_THAN_OR_EQUALS operators are also available for the OS_VERSION attribute.
            * **Values**   An array of one or more filter values.  **Operator Values**
              * The IN and NOT_IN operators can take a values array that has more than one element.
              * The other operators require an array with a single element.
             **Attribute Values**
              * The PLATFORM attribute can be set to \"ANDROID\" or \"IOS\".
              * The AVAILABILITY attribute can be set to \"AVAILABLE\", \"HIGHLY_AVAILABLE\", \"BUSY\", or \"TEMPORARY_NOT_AVAILABLE\".
              * The FORM_FACTOR attribute can be set to \"PHONE\" or \"TABLET\".
              * The FLEET_TYPE attribute can be set to \"PUBLIC\" or \"PRIVATE\".
            - *(dict) --*
              Represents a device filter used to select a set of devices to be included in a test run. This data structure is passed in as the ``deviceSelectionConfiguration`` parameter to ScheduleRun. For an example of the JSON request syntax, see  ScheduleRun .
              It is also passed in as the ``filters`` parameter to ListDevices. For an example of the JSON request syntax, see  ListDevices .
              - **attribute** *(string) --*
                The aspect of a device such as platform or model used as the selection criteria in a device filter.
                The supported operators for each attribute are provided in the following list.
                  ARN
                The Amazon Resource Name (ARN) of the device. For example, \"arn:aws:devicefarm:us-west-2::device:12345Example\".
                 *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``
                  PLATFORM
                The device platform. Valid values are \"ANDROID\" or \"IOS\".
                 *Supported operators* : ``EQUALS``
                  OS_VERSION
                The operating system version. For example, \"10.3.2\".
                 *Supported operators* : ``EQUALS`` , ``GREATER_THAN`` , ``GREATER_THAN_OR_EQUALS`` , ``IN`` , ``LESS_THAN`` , ``LESS_THAN_OR_EQUALS`` , ``NOT_IN``
                  MODEL
                The device model. For example, \"iPad 5th Gen\".
                 *Supported operators* : ``CONTAINS`` , ``EQUALS`` , ``IN`` , ``NOT_IN``
                  AVAILABILITY
                The current availability of the device. Valid values are \"AVAILABLE\", \"HIGHLY_AVAILABLE\", \"BUSY\", or \"TEMPORARY_NOT_AVAILABLE\".
                 *Supported operators* : ``EQUALS``
                  FORM_FACTOR
                The device form factor. Valid values are \"PHONE\" or \"TABLET\".
                 *Supported operators* : ``EQUALS``
                  MANUFACTURER
                The device manufacturer. For example, \"Apple\".
                 *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``
                  REMOTE_ACCESS_ENABLED
                Whether the device is enabled for remote access. Valid values are \"TRUE\" or \"FALSE\".
                 *Supported operators* : ``EQUALS``
                  REMOTE_DEBUG_ENABLED
                Whether the device is enabled for remote debugging. Valid values are \"TRUE\" or \"FALSE\".
                 *Supported operators* : ``EQUALS``
                  INSTANCE_ARN
                The Amazon Resource Name (ARN) of the device instance.
                 *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``
                  INSTANCE_LABELS
                The label of the device instance.
                 *Supported operators* : ``CONTAINS``
                  FLEET_TYPE
                The fleet type. Valid values are \"PUBLIC\" or \"PRIVATE\".
                 *Supported operators* : ``EQUALS``
              - **operator** *(string) --*
                Specifies how Device Farm compares the filter\'s attribute to the value. For the operators that are supported by each attribute, see the attribute descriptions.
              - **values** *(list) --*
                An array of one or more filter values used in a device filter.
                 **Operator Values**
                * The IN and NOT_IN operators can take a values array that has more than one element.
                * The other operators require an array with a single element.
                 **Attribute Values**
                * The PLATFORM attribute can be set to \"ANDROID\" or \"IOS\".
                * The AVAILABILITY attribute can be set to \"AVAILABLE\", \"HIGHLY_AVAILABLE\", \"BUSY\", or \"TEMPORARY_NOT_AVAILABLE\".
                * The FORM_FACTOR attribute can be set to \"PHONE\" or \"TABLET\".
                * The FLEET_TYPE attribute can be set to \"PUBLIC\" or \"PRIVATE\".
                - *(string) --*
          - **maxDevices** *(integer) --* **[REQUIRED]**
            The maximum number of devices to be included in a test run.
        :type name: string
        :param name:
          The name for the run to be scheduled.
        :type test: dict
        :param test: **[REQUIRED]**
          Information about the test for the run to be scheduled.
          - **type** *(string) --* **[REQUIRED]**
            The test\'s type.
            Must be one of the following values:
            * BUILTIN_FUZZ: The built-in fuzz type.
            * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time.
            * APPIUM_JAVA_JUNIT: The Appium Java JUnit type.
            * APPIUM_JAVA_TESTNG: The Appium Java TestNG type.
            * APPIUM_PYTHON: The Appium Python type.
            * APPIUM_NODE: The Appium Node.js type.
            * APPIUM_RUBY: The Appium Ruby type.
            * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for web apps.
            * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for web apps.
            * APPIUM_WEB_PYTHON: The Appium Python type for web apps.
            * APPIUM_WEB_NODE: The Appium Node.js type for web apps.
            * APPIUM_WEB_RUBY: The Appium Ruby type for web apps.
            * CALABASH: The Calabash type.
            * INSTRUMENTATION: The Instrumentation type.
            * UIAUTOMATION: The uiautomation type.
            * UIAUTOMATOR: The uiautomator type.
            * XCTEST: The XCode test type.
            * XCTEST_UI: The XCode UI test type.
          - **testPackageArn** *(string) --*
            The ARN of the uploaded test that will be run.
          - **testSpecArn** *(string) --*
            The ARN of the YAML-formatted test specification.
          - **filter** *(string) --*
            The test\'s filter.
          - **parameters** *(dict) --*
            The test\'s parameters, such as test framework parameters and fixture settings. Parameters are represented by name-value pairs of strings.
            For all tests:
            * app_performance_monitoring: Performance monitoring is enabled by default. Set this parameter to \"false\" to disable it.
            For Calabash tests:
            * profile: A cucumber profile, for example, \"my_profile_name\".
            * tags: You can limit execution to features or scenarios that have (or don\'t have) certain tags, for example, \"@smoke\" or \"@smoke,~@wip\".
            For Appium tests (all types):
            * appium_version: The Appium version. Currently supported values are \"1.6.5\" (and higher), \"latest\", and \"default\".
              * “latest” will run the latest Appium version supported by Device Farm (1.9.1).
              * For “default”, Device Farm will choose a compatible version of Appium for the device. The current behavior is to run 1.7.2 on Android devices and iOS 9 and earlier, 1.7.2 for iOS 10 and later.
              * This behavior is subject to change.
            For Fuzz tests (Android only):
            * event_count: The number of events, between 1 and 10000, that the UI fuzz test should perform.
            * throttle: The time, in ms, between 0 and 1000, that the UI fuzz test should wait between events.
            * seed: A seed to use for randomizing the UI fuzz test. Using the same seed value between tests ensures identical event sequences.
            For Explorer tests:
            * username: A username to use if the Explorer encounters a login form. If not supplied, no username will be inserted.
            * password: A password to use if the Explorer encounters a login form. If not supplied, no password will be inserted.
            For Instrumentation:
            * filter: A test filter string. Examples:
              * Running a single test case: \"com.android.abc.Test1\"
              * Running a single test: \"com.android.abc.Test1#smoke\"
              * Running multiple tests: \"com.android.abc.Test1,com.android.abc.Test2\"
            For XCTest and XCTestUI:
            * filter: A test filter string. Examples:
              * Running a single test class: \"LoginTests\"
              * Running a multiple test classes: \"LoginTests,SmokeTests\"
              * Running a single test: \"LoginTests/testValid\"
              * Running multiple tests: \"LoginTests/testValid,LoginTests/testInvalid\"
            For UIAutomator:
            * filter: A test filter string. Examples:
              * Running a single test case: \"com.android.abc.Test1\"
              * Running a single test: \"com.android.abc.Test1#smoke\"
              * Running multiple tests: \"com.android.abc.Test1,com.android.abc.Test2\"
            - *(string) --*
              - *(string) --*
        :type configuration: dict
        :param configuration:
          Information about the settings for the run to be scheduled.
          - **extraDataPackageArn** *(string) --*
            The ARN of the extra data for the run. The extra data is a .zip file that AWS Device Farm will extract to external data for Android or the app\'s sandbox for iOS.
          - **networkProfileArn** *(string) --*
            Reserved for internal use.
          - **locale** *(string) --*
            Information about the locale that is used for the run.
          - **location** *(dict) --*
            Information about the location that is used for the run.
            - **latitude** *(float) --* **[REQUIRED]**
              The latitude.
            - **longitude** *(float) --* **[REQUIRED]**
              The longitude.
          - **vpceConfigurationArns** *(list) --*
            An array of Amazon Resource Names (ARNs) for your VPC endpoint configurations.
            - *(string) --*
          - **customerArtifactPaths** *(dict) --*
            Input ``CustomerArtifactPaths`` object for the scheduled run configuration.
            - **iosPaths** *(list) --*
              Comma-separated list of paths on the iOS device where the artifacts generated by the customer\'s tests will be pulled from.
              - *(string) --*
            - **androidPaths** *(list) --*
              Comma-separated list of paths on the Android device where the artifacts generated by the customer\'s tests will be pulled from.
              - *(string) --*
            - **deviceHostPaths** *(list) --*
              Comma-separated list of paths in the test execution environment where the artifacts generated by the customer\'s tests will be pulled from.
              - *(string) --*
          - **radios** *(dict) --*
            Information about the radio states for the run.
            - **wifi** *(boolean) --*
              True if Wi-Fi is enabled at the beginning of the test; otherwise, false.
            - **bluetooth** *(boolean) --*
              True if Bluetooth is enabled at the beginning of the test; otherwise, false.
            - **nfc** *(boolean) --*
              True if NFC is enabled at the beginning of the test; otherwise, false.
            - **gps** *(boolean) --*
              True if GPS is enabled at the beginning of the test; otherwise, false.
          - **auxiliaryApps** *(list) --*
            A list of auxiliary apps for the run.
            - *(string) --*
          - **billingMethod** *(string) --*
            Specifies the billing method for a test run: ``metered`` or ``unmetered`` . If the parameter is not specified, the default value is ``metered`` .
        :type executionConfiguration: dict
        :param executionConfiguration:
          Specifies configuration information about a test run, such as the execution timeout (in minutes).
          - **jobTimeoutMinutes** *(integer) --*
            The number of minutes a test run will execute before it times out.
          - **accountsCleanup** *(boolean) --*
            True if account cleanup is enabled at the beginning of the test; otherwise, false.
          - **appPackagesCleanup** *(boolean) --*
            True if app package cleanup is enabled at the beginning of the test; otherwise, false.
          - **videoCapture** *(boolean) --*
            Set to true to enable video capture; otherwise, set to false. The default is true.
          - **skipAppResign** *(boolean) --*
            When set to ``true`` , for private devices, Device Farm will not sign your app again. For public devices, Device Farm always signs your apps again and this parameter has no effect.
            For more information about how Device Farm re-signs your app(s), see `Do you modify my app? <https://aws.amazon.com/device-farm/faq/>`__ in the *AWS Device Farm FAQs* .
        :rtype: dict
        :returns:
        """
        pass

    def stop_job(self, arn: str) -> Dict:
        """
        Initiates a stop request for the current job. AWS Device Farm will immediately stop the job on the device where tests have not started executing, and you will not be billed for this device. On the device where tests have started executing, Setup Suite and Teardown Suite tests will run to completion before stopping execution on the device. You will be billed for Setup, Teardown, and any tests that were in progress or already completed.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/StopJob>`_
        
        **Request Syntax**
        ::
          response = client.stop_job(
              arn='string'
          )
        
        **Response Syntax**
        ::
            {
                'job': {
                    'arn': 'string',
                    'name': 'string',
                    'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
                    'created': datetime(2015, 1, 1),
                    'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                    'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                    'started': datetime(2015, 1, 1),
                    'stopped': datetime(2015, 1, 1),
                    'counters': {
                        'total': 123,
                        'passed': 123,
                        'failed': 123,
                        'warned': 123,
                        'errored': 123,
                        'stopped': 123,
                        'skipped': 123
                    },
                    'message': 'string',
                    'device': {
                        'arn': 'string',
                        'name': 'string',
                        'manufacturer': 'string',
                        'model': 'string',
                        'modelId': 'string',
                        'formFactor': 'PHONE'|'TABLET',
                        'platform': 'ANDROID'|'IOS',
                        'os': 'string',
                        'cpu': {
                            'frequency': 'string',
                            'architecture': 'string',
                            'clock': 123.0
                        },
                        'resolution': {
                            'width': 123,
                            'height': 123
                        },
                        'heapSize': 123,
                        'memory': 123,
                        'image': 'string',
                        'carrier': 'string',
                        'radio': 'string',
                        'remoteAccessEnabled': True|False,
                        'remoteDebugEnabled': True|False,
                        'fleetType': 'string',
                        'fleetName': 'string',
                        'instances': [
                            {
                                'arn': 'string',
                                'deviceArn': 'string',
                                'labels': [
                                    'string',
                                ],
                                'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                                'udid': 'string',
                                'instanceProfile': {
                                    'arn': 'string',
                                    'packageCleanup': True|False,
                                    'excludeAppPackagesFromCleanup': [
                                        'string',
                                    ],
                                    'rebootAfterUse': True|False,
                                    'name': 'string',
                                    'description': 'string'
                                }
                            },
                        ],
                        'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
                    },
                    'instanceArn': 'string',
                    'deviceMinutes': {
                        'total': 123.0,
                        'metered': 123.0,
                        'unmetered': 123.0
                    },
                    'videoEndpoint': 'string',
                    'videoCapture': True|False
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **job** *(dict) --* 
              The job that was stopped.
              - **arn** *(string) --* 
                The job's ARN.
              - **name** *(string) --* 
                The job's name.
              - **type** *(string) --* 
                The job's type.
                Allowed values include the following:
                * BUILTIN_FUZZ: The built-in fuzz type. 
                * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
                * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
                * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
                * APPIUM_PYTHON: The Appium Python type. 
                * APPIUM_NODE: The Appium Node.js type. 
                * APPIUM_RUBY: The Appium Ruby type. 
                * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for web apps. 
                * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for web apps. 
                * APPIUM_WEB_PYTHON: The Appium Python type for web apps. 
                * APPIUM_WEB_NODE: The Appium Node.js type for web apps. 
                * APPIUM_WEB_RUBY: The Appium Ruby test type for web apps. 
                * CALABASH: The Calabash type. 
                * INSTRUMENTATION: The Instrumentation type. 
                * UIAUTOMATION: The uiautomation type. 
                * UIAUTOMATOR: The uiautomator type. 
                * XCTEST: The XCode test type. 
                * XCTEST_UI: The XCode UI test type. 
              - **created** *(datetime) --* 
                When the job was created.
              - **status** *(string) --* 
                The job's status.
                Allowed values include:
                * PENDING: A pending status. 
                * PENDING_CONCURRENCY: A pending concurrency status. 
                * PENDING_DEVICE: A pending device status. 
                * PROCESSING: A processing status. 
                * SCHEDULING: A scheduling status. 
                * PREPARING: A preparing status. 
                * RUNNING: A running status. 
                * COMPLETED: A completed status. 
                * STOPPING: A stopping status. 
              - **result** *(string) --* 
                The job's result.
                Allowed values include:
                * PENDING: A pending condition. 
                * PASSED: A passing condition. 
                * WARNED: A warning condition. 
                * FAILED: A failed condition. 
                * SKIPPED: A skipped condition. 
                * ERRORED: An error condition. 
                * STOPPED: A stopped condition. 
              - **started** *(datetime) --* 
                The job's start time.
              - **stopped** *(datetime) --* 
                The job's stop time.
              - **counters** *(dict) --* 
                The job's result counters.
                - **total** *(integer) --* 
                  The total number of entities.
                - **passed** *(integer) --* 
                  The number of passed entities.
                - **failed** *(integer) --* 
                  The number of failed entities.
                - **warned** *(integer) --* 
                  The number of warned entities.
                - **errored** *(integer) --* 
                  The number of errored entities.
                - **stopped** *(integer) --* 
                  The number of stopped entities.
                - **skipped** *(integer) --* 
                  The number of skipped entities.
              - **message** *(string) --* 
                A message about the job's result.
              - **device** *(dict) --* 
                The device (phone or tablet).
                - **arn** *(string) --* 
                  The device's ARN.
                - **name** *(string) --* 
                  The device's display name.
                - **manufacturer** *(string) --* 
                  The device's manufacturer name.
                - **model** *(string) --* 
                  The device's model name.
                - **modelId** *(string) --* 
                  The device's model ID.
                - **formFactor** *(string) --* 
                  The device's form factor.
                  Allowed values include:
                  * PHONE: The phone form factor. 
                  * TABLET: The tablet form factor. 
                - **platform** *(string) --* 
                  The device's platform.
                  Allowed values include:
                  * ANDROID: The Android platform. 
                  * IOS: The iOS platform. 
                - **os** *(string) --* 
                  The device's operating system type.
                - **cpu** *(dict) --* 
                  Information about the device's CPU.
                  - **frequency** *(string) --* 
                    The CPU's frequency.
                  - **architecture** *(string) --* 
                    The CPU's architecture, for example x86 or ARM.
                  - **clock** *(float) --* 
                    The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.
                - **resolution** *(dict) --* 
                  The resolution of the device.
                  - **width** *(integer) --* 
                    The screen resolution's width, expressed in pixels.
                  - **height** *(integer) --* 
                    The screen resolution's height, expressed in pixels.
                - **heapSize** *(integer) --* 
                  The device's heap size, expressed in bytes.
                - **memory** *(integer) --* 
                  The device's total memory size, expressed in bytes.
                - **image** *(string) --* 
                  The device's image name.
                - **carrier** *(string) --* 
                  The device's carrier.
                - **radio** *(string) --* 
                  The device's radio.
                - **remoteAccessEnabled** *(boolean) --* 
                  Specifies whether remote access has been enabled for the specified device.
                - **remoteDebugEnabled** *(boolean) --* 
                  This flag is set to ``true`` if remote debugging is enabled for the device.
                - **fleetType** *(string) --* 
                  The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.
                - **fleetName** *(string) --* 
                  The name of the fleet to which this device belongs.
                - **instances** *(list) --* 
                  The instances belonging to this device.
                  - *(dict) --* 
                    Represents the device instance.
                    - **arn** *(string) --* 
                      The Amazon Resource Name (ARN) of the device instance.
                    - **deviceArn** *(string) --* 
                      The Amazon Resource Name (ARN) of the device.
                    - **labels** *(list) --* 
                      An array of strings describing the device instance.
                      - *(string) --* 
                    - **status** *(string) --* 
                      The status of the device instance. Valid values are listed below.
                    - **udid** *(string) --* 
                      Unique device identifier for the device instance.
                    - **instanceProfile** *(dict) --* 
                      A object containing information about the instance profile.
                      - **arn** *(string) --* 
                        The Amazon Resource Name (ARN) of the instance profile.
                      - **packageCleanup** *(boolean) --* 
                        When set to ``true`` , Device Farm will remove app packages after a test run. The default value is ``false`` for private devices.
                      - **excludeAppPackagesFromCleanup** *(list) --* 
                        An array of strings specifying the list of app packages that should not be cleaned up from the device after a test run is over.
                        The list of packages is only considered if you set ``packageCleanup`` to ``true`` .
                        - *(string) --* 
                      - **rebootAfterUse** *(boolean) --* 
                        When set to ``true`` , Device Farm will reboot the instance after a test run. The default value is ``true`` .
                      - **name** *(string) --* 
                        The name of the instance profile.
                      - **description** *(string) --* 
                        The description of the instance profile.
                - **availability** *(string) --* 
                  Reflects how likely a device will be available for a test run. It is currently available in the ListDevices and GetDevice API methods.
              - **instanceArn** *(string) --* 
                The Amazon Resource Name (ARN) of the instance.
              - **deviceMinutes** *(dict) --* 
                Represents the total (metered or unmetered) minutes used by the job.
                - **total** *(float) --* 
                  When specified, represents the total minutes used by the resource to run tests.
                - **metered** *(float) --* 
                  When specified, represents only the sum of metered minutes used by the resource to run tests.
                - **unmetered** *(float) --* 
                  When specified, represents only the sum of unmetered minutes used by the resource to run tests.
              - **videoEndpoint** *(string) --* 
                The endpoint for streaming device video.
              - **videoCapture** *(boolean) --* 
                This value is set to true if video capture is enabled; otherwise, it is set to false.
        :type arn: string
        :param arn: **[REQUIRED]**
          Represents the Amazon Resource Name (ARN) of the Device Farm job you wish to stop.
        :rtype: dict
        :returns:
        """
        pass

    def stop_remote_access_session(self, arn: str) -> Dict:
        """
        Ends a specified remote access session.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/StopRemoteAccessSession>`_
        
        **Request Syntax**
        ::
          response = client.stop_remote_access_session(
              arn='string'
          )
        
        **Response Syntax**
        ::
            {
                'remoteAccessSession': {
                    'arn': 'string',
                    'name': 'string',
                    'created': datetime(2015, 1, 1),
                    'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                    'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                    'message': 'string',
                    'started': datetime(2015, 1, 1),
                    'stopped': datetime(2015, 1, 1),
                    'device': {
                        'arn': 'string',
                        'name': 'string',
                        'manufacturer': 'string',
                        'model': 'string',
                        'modelId': 'string',
                        'formFactor': 'PHONE'|'TABLET',
                        'platform': 'ANDROID'|'IOS',
                        'os': 'string',
                        'cpu': {
                            'frequency': 'string',
                            'architecture': 'string',
                            'clock': 123.0
                        },
                        'resolution': {
                            'width': 123,
                            'height': 123
                        },
                        'heapSize': 123,
                        'memory': 123,
                        'image': 'string',
                        'carrier': 'string',
                        'radio': 'string',
                        'remoteAccessEnabled': True|False,
                        'remoteDebugEnabled': True|False,
                        'fleetType': 'string',
                        'fleetName': 'string',
                        'instances': [
                            {
                                'arn': 'string',
                                'deviceArn': 'string',
                                'labels': [
                                    'string',
                                ],
                                'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                                'udid': 'string',
                                'instanceProfile': {
                                    'arn': 'string',
                                    'packageCleanup': True|False,
                                    'excludeAppPackagesFromCleanup': [
                                        'string',
                                    ],
                                    'rebootAfterUse': True|False,
                                    'name': 'string',
                                    'description': 'string'
                                }
                            },
                        ],
                        'availability': 'TEMPORARY_NOT_AVAILABLE'|'BUSY'|'AVAILABLE'|'HIGHLY_AVAILABLE'
                    },
                    'instanceArn': 'string',
                    'remoteDebugEnabled': True|False,
                    'remoteRecordEnabled': True|False,
                    'remoteRecordAppArn': 'string',
                    'hostAddress': 'string',
                    'clientId': 'string',
                    'billingMethod': 'METERED'|'UNMETERED',
                    'deviceMinutes': {
                        'total': 123.0,
                        'metered': 123.0,
                        'unmetered': 123.0
                    },
                    'endpoint': 'string',
                    'deviceUdid': 'string',
                    'interactionMode': 'INTERACTIVE'|'NO_VIDEO'|'VIDEO_ONLY',
                    'skipAppResign': True|False
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the response from the server that describes the remote access session when AWS Device Farm stops the session.
            - **remoteAccessSession** *(dict) --* 
              A container representing the metadata from the service about the remote access session you are stopping.
              - **arn** *(string) --* 
                The Amazon Resource Name (ARN) of the remote access session.
              - **name** *(string) --* 
                The name of the remote access session.
              - **created** *(datetime) --* 
                The date and time the remote access session was created.
              - **status** *(string) --* 
                The status of the remote access session. Can be any of the following:
                * PENDING: A pending status. 
                * PENDING_CONCURRENCY: A pending concurrency status. 
                * PENDING_DEVICE: A pending device status. 
                * PROCESSING: A processing status. 
                * SCHEDULING: A scheduling status. 
                * PREPARING: A preparing status. 
                * RUNNING: A running status. 
                * COMPLETED: A completed status. 
                * STOPPING: A stopping status. 
              - **result** *(string) --* 
                The result of the remote access session. Can be any of the following:
                * PENDING: A pending condition. 
                * PASSED: A passing condition. 
                * WARNED: A warning condition. 
                * FAILED: A failed condition. 
                * SKIPPED: A skipped condition. 
                * ERRORED: An error condition. 
                * STOPPED: A stopped condition. 
              - **message** *(string) --* 
                A message about the remote access session.
              - **started** *(datetime) --* 
                The date and time the remote access session was started.
              - **stopped** *(datetime) --* 
                The date and time the remote access session was stopped.
              - **device** *(dict) --* 
                The device (phone or tablet) used in the remote access session.
                - **arn** *(string) --* 
                  The device's ARN.
                - **name** *(string) --* 
                  The device's display name.
                - **manufacturer** *(string) --* 
                  The device's manufacturer name.
                - **model** *(string) --* 
                  The device's model name.
                - **modelId** *(string) --* 
                  The device's model ID.
                - **formFactor** *(string) --* 
                  The device's form factor.
                  Allowed values include:
                  * PHONE: The phone form factor. 
                  * TABLET: The tablet form factor. 
                - **platform** *(string) --* 
                  The device's platform.
                  Allowed values include:
                  * ANDROID: The Android platform. 
                  * IOS: The iOS platform. 
                - **os** *(string) --* 
                  The device's operating system type.
                - **cpu** *(dict) --* 
                  Information about the device's CPU.
                  - **frequency** *(string) --* 
                    The CPU's frequency.
                  - **architecture** *(string) --* 
                    The CPU's architecture, for example x86 or ARM.
                  - **clock** *(float) --* 
                    The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.
                - **resolution** *(dict) --* 
                  The resolution of the device.
                  - **width** *(integer) --* 
                    The screen resolution's width, expressed in pixels.
                  - **height** *(integer) --* 
                    The screen resolution's height, expressed in pixels.
                - **heapSize** *(integer) --* 
                  The device's heap size, expressed in bytes.
                - **memory** *(integer) --* 
                  The device's total memory size, expressed in bytes.
                - **image** *(string) --* 
                  The device's image name.
                - **carrier** *(string) --* 
                  The device's carrier.
                - **radio** *(string) --* 
                  The device's radio.
                - **remoteAccessEnabled** *(boolean) --* 
                  Specifies whether remote access has been enabled for the specified device.
                - **remoteDebugEnabled** *(boolean) --* 
                  This flag is set to ``true`` if remote debugging is enabled for the device.
                - **fleetType** *(string) --* 
                  The type of fleet to which this device belongs. Possible values for fleet type are PRIVATE and PUBLIC.
                - **fleetName** *(string) --* 
                  The name of the fleet to which this device belongs.
                - **instances** *(list) --* 
                  The instances belonging to this device.
                  - *(dict) --* 
                    Represents the device instance.
                    - **arn** *(string) --* 
                      The Amazon Resource Name (ARN) of the device instance.
                    - **deviceArn** *(string) --* 
                      The Amazon Resource Name (ARN) of the device.
                    - **labels** *(list) --* 
                      An array of strings describing the device instance.
                      - *(string) --* 
                    - **status** *(string) --* 
                      The status of the device instance. Valid values are listed below.
                    - **udid** *(string) --* 
                      Unique device identifier for the device instance.
                    - **instanceProfile** *(dict) --* 
                      A object containing information about the instance profile.
                      - **arn** *(string) --* 
                        The Amazon Resource Name (ARN) of the instance profile.
                      - **packageCleanup** *(boolean) --* 
                        When set to ``true`` , Device Farm will remove app packages after a test run. The default value is ``false`` for private devices.
                      - **excludeAppPackagesFromCleanup** *(list) --* 
                        An array of strings specifying the list of app packages that should not be cleaned up from the device after a test run is over.
                        The list of packages is only considered if you set ``packageCleanup`` to ``true`` .
                        - *(string) --* 
                      - **rebootAfterUse** *(boolean) --* 
                        When set to ``true`` , Device Farm will reboot the instance after a test run. The default value is ``true`` .
                      - **name** *(string) --* 
                        The name of the instance profile.
                      - **description** *(string) --* 
                        The description of the instance profile.
                - **availability** *(string) --* 
                  Reflects how likely a device will be available for a test run. It is currently available in the ListDevices and GetDevice API methods.
              - **instanceArn** *(string) --* 
                The Amazon Resource Name (ARN) of the instance.
              - **remoteDebugEnabled** *(boolean) --* 
                This flag is set to ``true`` if remote debugging is enabled for the remote access session.
              - **remoteRecordEnabled** *(boolean) --* 
                This flag is set to ``true`` if remote recording is enabled for the remote access session.
              - **remoteRecordAppArn** *(string) --* 
                The Amazon Resource Name (ARN) for the app to be recorded in the remote access session.
              - **hostAddress** *(string) --* 
                IP address of the EC2 host where you need to connect to remotely debug devices. Only returned if remote debugging is enabled for the remote access session.
              - **clientId** *(string) --* 
                Unique identifier of your client for the remote access session. Only returned if remote debugging is enabled for the remote access session.
              - **billingMethod** *(string) --* 
                The billing method of the remote access session. Possible values include ``METERED`` or ``UNMETERED`` . For more information about metered devices, see `AWS Device Farm terminology <https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html#welcome-terminology>`__ ."
              - **deviceMinutes** *(dict) --* 
                The number of minutes a device is used in a remote access sesssion (including setup and teardown minutes).
                - **total** *(float) --* 
                  When specified, represents the total minutes used by the resource to run tests.
                - **metered** *(float) --* 
                  When specified, represents only the sum of metered minutes used by the resource to run tests.
                - **unmetered** *(float) --* 
                  When specified, represents only the sum of unmetered minutes used by the resource to run tests.
              - **endpoint** *(string) --* 
                The endpoint for the remote access sesssion.
              - **deviceUdid** *(string) --* 
                Unique device identifier for the remote device. Only returned if remote debugging is enabled for the remote access session.
              - **interactionMode** *(string) --* 
                The interaction mode of the remote access session. Valid values are:
                * INTERACTIVE: You can interact with the iOS device by viewing, touching, and rotating the screen. You **cannot** run XCUITest framework-based tests in this mode. 
                * NO_VIDEO: You are connected to the device but cannot interact with it or view the screen. This mode has the fastest test execution speed. You **can** run XCUITest framework-based tests in this mode. 
                * VIDEO_ONLY: You can view the screen but cannot touch or rotate it. You **can** run XCUITest framework-based tests and watch the screen in this mode. 
              - **skipAppResign** *(boolean) --* 
                When set to ``true`` , for private devices, Device Farm will not sign your app again. For public devices, Device Farm always signs your apps again and this parameter has no effect.
                For more information about how Device Farm re-signs your app(s), see `Do you modify my app? <https://aws.amazon.com/device-farm/faq/>`__ in the *AWS Device Farm FAQs* .
        :type arn: string
        :param arn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the remote access session you wish to stop.
        :rtype: dict
        :returns:
        """
        pass

    def stop_run(self, arn: str) -> Dict:
        """
        Initiates a stop request for the current test run. AWS Device Farm will immediately stop the run on devices where tests have not started executing, and you will not be billed for these devices. On devices where tests have started executing, Setup Suite and Teardown Suite tests will run to completion before stopping execution on those devices. You will be billed for Setup, Teardown, and any tests that were in progress or already completed.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/StopRun>`_
        
        **Request Syntax**
        ::
          response = client.stop_run(
              arn='string'
          )
        
        **Response Syntax**
        ::
            {
                'run': {
                    'arn': 'string',
                    'name': 'string',
                    'type': 'BUILTIN_FUZZ'|'BUILTIN_EXPLORER'|'WEB_PERFORMANCE_PROFILE'|'APPIUM_JAVA_JUNIT'|'APPIUM_JAVA_TESTNG'|'APPIUM_PYTHON'|'APPIUM_NODE'|'APPIUM_RUBY'|'APPIUM_WEB_JAVA_JUNIT'|'APPIUM_WEB_JAVA_TESTNG'|'APPIUM_WEB_PYTHON'|'APPIUM_WEB_NODE'|'APPIUM_WEB_RUBY'|'CALABASH'|'INSTRUMENTATION'|'UIAUTOMATION'|'UIAUTOMATOR'|'XCTEST'|'XCTEST_UI'|'REMOTE_ACCESS_RECORD'|'REMOTE_ACCESS_REPLAY',
                    'platform': 'ANDROID'|'IOS',
                    'created': datetime(2015, 1, 1),
                    'status': 'PENDING'|'PENDING_CONCURRENCY'|'PENDING_DEVICE'|'PROCESSING'|'SCHEDULING'|'PREPARING'|'RUNNING'|'COMPLETED'|'STOPPING',
                    'result': 'PENDING'|'PASSED'|'WARNED'|'FAILED'|'SKIPPED'|'ERRORED'|'STOPPED',
                    'started': datetime(2015, 1, 1),
                    'stopped': datetime(2015, 1, 1),
                    'counters': {
                        'total': 123,
                        'passed': 123,
                        'failed': 123,
                        'warned': 123,
                        'errored': 123,
                        'stopped': 123,
                        'skipped': 123
                    },
                    'message': 'string',
                    'totalJobs': 123,
                    'completedJobs': 123,
                    'billingMethod': 'METERED'|'UNMETERED',
                    'deviceMinutes': {
                        'total': 123.0,
                        'metered': 123.0,
                        'unmetered': 123.0
                    },
                    'networkProfile': {
                        'arn': 'string',
                        'name': 'string',
                        'description': 'string',
                        'type': 'CURATED'|'PRIVATE',
                        'uplinkBandwidthBits': 123,
                        'downlinkBandwidthBits': 123,
                        'uplinkDelayMs': 123,
                        'downlinkDelayMs': 123,
                        'uplinkJitterMs': 123,
                        'downlinkJitterMs': 123,
                        'uplinkLossPercent': 123,
                        'downlinkLossPercent': 123
                    },
                    'parsingResultUrl': 'string',
                    'resultCode': 'PARSING_FAILED'|'VPC_ENDPOINT_SETUP_FAILED',
                    'seed': 123,
                    'appUpload': 'string',
                    'eventCount': 123,
                    'jobTimeoutMinutes': 123,
                    'devicePoolArn': 'string',
                    'locale': 'string',
                    'radios': {
                        'wifi': True|False,
                        'bluetooth': True|False,
                        'nfc': True|False,
                        'gps': True|False
                    },
                    'location': {
                        'latitude': 123.0,
                        'longitude': 123.0
                    },
                    'customerArtifactPaths': {
                        'iosPaths': [
                            'string',
                        ],
                        'androidPaths': [
                            'string',
                        ],
                        'deviceHostPaths': [
                            'string',
                        ]
                    },
                    'webUrl': 'string',
                    'skipAppResign': True|False,
                    'testSpecArn': 'string',
                    'deviceSelectionResult': {
                        'filters': [
                            {
                                'attribute': 'ARN'|'PLATFORM'|'OS_VERSION'|'MODEL'|'AVAILABILITY'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                                'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                                'values': [
                                    'string',
                                ]
                            },
                        ],
                        'matchedDevicesCount': 123,
                        'maxDevices': 123
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the results of your stop run attempt.
            - **run** *(dict) --* 
              The run that was stopped.
              - **arn** *(string) --* 
                The run's ARN.
              - **name** *(string) --* 
                The run's name.
              - **type** *(string) --* 
                The run's type.
                Must be one of the following values:
                * BUILTIN_FUZZ: The built-in fuzz type. 
                * BUILTIN_EXPLORER: For Android, an app explorer that will traverse an Android app, interacting with it and capturing screenshots at the same time. 
                * APPIUM_JAVA_JUNIT: The Appium Java JUnit type. 
                * APPIUM_JAVA_TESTNG: The Appium Java TestNG type. 
                * APPIUM_PYTHON: The Appium Python type. 
                * APPIUM_NODE: The Appium Node.js type. 
                * APPIUM_RUBY: The Appium Ruby type. 
                * APPIUM_WEB_JAVA_JUNIT: The Appium Java JUnit type for web apps. 
                * APPIUM_WEB_JAVA_TESTNG: The Appium Java TestNG type for web apps. 
                * APPIUM_WEB_PYTHON: The Appium Python type for web apps. 
                * APPIUM_WEB_NODE: The Appium Node.js type for web apps. 
                * APPIUM_WEB_RUBY: The Appium Ruby type for web apps. 
                * CALABASH: The Calabash type. 
                * INSTRUMENTATION: The Instrumentation type. 
                * UIAUTOMATION: The uiautomation type. 
                * UIAUTOMATOR: The uiautomator type. 
                * XCTEST: The XCode test type. 
                * XCTEST_UI: The XCode UI test type. 
              - **platform** *(string) --* 
                The run's platform.
                Allowed values include:
                * ANDROID: The Android platform. 
                * IOS: The iOS platform. 
              - **created** *(datetime) --* 
                When the run was created.
              - **status** *(string) --* 
                The run's status.
                Allowed values include:
                * PENDING: A pending status. 
                * PENDING_CONCURRENCY: A pending concurrency status. 
                * PENDING_DEVICE: A pending device status. 
                * PROCESSING: A processing status. 
                * SCHEDULING: A scheduling status. 
                * PREPARING: A preparing status. 
                * RUNNING: A running status. 
                * COMPLETED: A completed status. 
                * STOPPING: A stopping status. 
              - **result** *(string) --* 
                The run's result.
                Allowed values include:
                * PENDING: A pending condition. 
                * PASSED: A passing condition. 
                * WARNED: A warning condition. 
                * FAILED: A failed condition. 
                * SKIPPED: A skipped condition. 
                * ERRORED: An error condition. 
                * STOPPED: A stopped condition. 
              - **started** *(datetime) --* 
                The run's start time.
              - **stopped** *(datetime) --* 
                The run's stop time.
              - **counters** *(dict) --* 
                The run's result counters.
                - **total** *(integer) --* 
                  The total number of entities.
                - **passed** *(integer) --* 
                  The number of passed entities.
                - **failed** *(integer) --* 
                  The number of failed entities.
                - **warned** *(integer) --* 
                  The number of warned entities.
                - **errored** *(integer) --* 
                  The number of errored entities.
                - **stopped** *(integer) --* 
                  The number of stopped entities.
                - **skipped** *(integer) --* 
                  The number of skipped entities.
              - **message** *(string) --* 
                A message about the run's result.
              - **totalJobs** *(integer) --* 
                The total number of jobs for the run.
              - **completedJobs** *(integer) --* 
                The total number of completed jobs.
              - **billingMethod** *(string) --* 
                Specifies the billing method for a test run: ``metered`` or ``unmetered`` . If the parameter is not specified, the default value is ``metered`` .
              - **deviceMinutes** *(dict) --* 
                Represents the total (metered or unmetered) minutes used by the test run.
                - **total** *(float) --* 
                  When specified, represents the total minutes used by the resource to run tests.
                - **metered** *(float) --* 
                  When specified, represents only the sum of metered minutes used by the resource to run tests.
                - **unmetered** *(float) --* 
                  When specified, represents only the sum of unmetered minutes used by the resource to run tests.
              - **networkProfile** *(dict) --* 
                The network profile being used for a test run.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the network profile.
                - **name** *(string) --* 
                  The name of the network profile.
                - **description** *(string) --* 
                  The description of the network profile.
                - **type** *(string) --* 
                  The type of network profile. Valid values are listed below.
                - **uplinkBandwidthBits** *(integer) --* 
                  The data throughput rate in bits per second, as an integer from 0 to 104857600.
                - **downlinkBandwidthBits** *(integer) --* 
                  The data throughput rate in bits per second, as an integer from 0 to 104857600.
                - **uplinkDelayMs** *(integer) --* 
                  Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
                - **downlinkDelayMs** *(integer) --* 
                  Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
                - **uplinkJitterMs** *(integer) --* 
                  Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
                - **downlinkJitterMs** *(integer) --* 
                  Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
                - **uplinkLossPercent** *(integer) --* 
                  Proportion of transmitted packets that fail to arrive from 0 to 100 percent.
                - **downlinkLossPercent** *(integer) --* 
                  Proportion of received packets that fail to arrive from 0 to 100 percent.
              - **parsingResultUrl** *(string) --* 
                Read-only URL for an object in S3 bucket where you can get the parsing results of the test package. If the test package doesn't parse, the reason why it doesn't parse appears in the file that this URL points to.
              - **resultCode** *(string) --* 
                Supporting field for the result field. Set only if ``result`` is ``SKIPPED`` . ``PARSING_FAILED`` if the result is skipped because of test package parsing failure.
              - **seed** *(integer) --* 
                For fuzz tests, this is a seed to use for randomizing the UI fuzz test. Using the same seed value between tests ensures identical event sequences.
              - **appUpload** *(string) --* 
                An app to upload or that has been uploaded.
              - **eventCount** *(integer) --* 
                For fuzz tests, this is the number of events, between 1 and 10000, that the UI fuzz test should perform.
              - **jobTimeoutMinutes** *(integer) --* 
                The number of minutes the job will execute before it times out.
              - **devicePoolArn** *(string) --* 
                The ARN of the device pool for the run.
              - **locale** *(string) --* 
                Information about the locale that is used for the run.
              - **radios** *(dict) --* 
                Information about the radio states for the run.
                - **wifi** *(boolean) --* 
                  True if Wi-Fi is enabled at the beginning of the test; otherwise, false.
                - **bluetooth** *(boolean) --* 
                  True if Bluetooth is enabled at the beginning of the test; otherwise, false.
                - **nfc** *(boolean) --* 
                  True if NFC is enabled at the beginning of the test; otherwise, false.
                - **gps** *(boolean) --* 
                  True if GPS is enabled at the beginning of the test; otherwise, false.
              - **location** *(dict) --* 
                Information about the location that is used for the run.
                - **latitude** *(float) --* 
                  The latitude.
                - **longitude** *(float) --* 
                  The longitude.
              - **customerArtifactPaths** *(dict) --* 
                Output ``CustomerArtifactPaths`` object for the test run.
                - **iosPaths** *(list) --* 
                  Comma-separated list of paths on the iOS device where the artifacts generated by the customer's tests will be pulled from.
                  - *(string) --* 
                - **androidPaths** *(list) --* 
                  Comma-separated list of paths on the Android device where the artifacts generated by the customer's tests will be pulled from.
                  - *(string) --* 
                - **deviceHostPaths** *(list) --* 
                  Comma-separated list of paths in the test execution environment where the artifacts generated by the customer's tests will be pulled from.
                  - *(string) --* 
              - **webUrl** *(string) --* 
                The Device Farm console URL for the recording of the run.
              - **skipAppResign** *(boolean) --* 
                When set to ``true`` , for private devices, Device Farm will not sign your app again. For public devices, Device Farm always signs your apps again and this parameter has no effect.
                For more information about how Device Farm re-signs your app(s), see `Do you modify my app? <https://aws.amazon.com/device-farm/faq/>`__ in the *AWS Device Farm FAQs* .
              - **testSpecArn** *(string) --* 
                The ARN of the YAML-formatted test specification for the run.
              - **deviceSelectionResult** *(dict) --* 
                The results of a device filter used to select the devices for a test run.
                - **filters** *(list) --* 
                  The filters in a device selection result.
                  - *(dict) --* 
                    Represents a device filter used to select a set of devices to be included in a test run. This data structure is passed in as the ``deviceSelectionConfiguration`` parameter to ScheduleRun. For an example of the JSON request syntax, see  ScheduleRun .
                    It is also passed in as the ``filters`` parameter to ListDevices. For an example of the JSON request syntax, see  ListDevices .
                    - **attribute** *(string) --* 
                      The aspect of a device such as platform or model used as the selection criteria in a device filter.
                      The supported operators for each attribute are provided in the following list.
                        ARN  
                      The Amazon Resource Name (ARN) of the device. For example, "arn:aws:devicefarm:us-west-2::device:12345Example".
                       *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                        PLATFORM  
                      The device platform. Valid values are "ANDROID" or "IOS".
                       *Supported operators* : ``EQUALS``  
                        OS_VERSION  
                      The operating system version. For example, "10.3.2".
                       *Supported operators* : ``EQUALS`` , ``GREATER_THAN`` , ``GREATER_THAN_OR_EQUALS`` , ``IN`` , ``LESS_THAN`` , ``LESS_THAN_OR_EQUALS`` , ``NOT_IN``  
                        MODEL  
                      The device model. For example, "iPad 5th Gen".
                       *Supported operators* : ``CONTAINS`` , ``EQUALS`` , ``IN`` , ``NOT_IN``  
                        AVAILABILITY  
                      The current availability of the device. Valid values are "AVAILABLE", "HIGHLY_AVAILABLE", "BUSY", or "TEMPORARY_NOT_AVAILABLE".
                       *Supported operators* : ``EQUALS``  
                        FORM_FACTOR  
                      The device form factor. Valid values are "PHONE" or "TABLET".
                       *Supported operators* : ``EQUALS``  
                        MANUFACTURER  
                      The device manufacturer. For example, "Apple".
                       *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                        REMOTE_ACCESS_ENABLED  
                      Whether the device is enabled for remote access. Valid values are "TRUE" or "FALSE".
                       *Supported operators* : ``EQUALS``  
                        REMOTE_DEBUG_ENABLED  
                      Whether the device is enabled for remote debugging. Valid values are "TRUE" or "FALSE".
                       *Supported operators* : ``EQUALS``  
                        INSTANCE_ARN  
                      The Amazon Resource Name (ARN) of the device instance.
                       *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                        INSTANCE_LABELS  
                      The label of the device instance.
                       *Supported operators* : ``CONTAINS``  
                        FLEET_TYPE  
                      The fleet type. Valid values are "PUBLIC" or "PRIVATE".
                       *Supported operators* : ``EQUALS``  
                    - **operator** *(string) --* 
                      Specifies how Device Farm compares the filter's attribute to the value. For the operators that are supported by each attribute, see the attribute descriptions.
                    - **values** *(list) --* 
                      An array of one or more filter values used in a device filter.
        
        **Operator Values**
                      * The IN and NOT_IN operators can take a values array that has more than one element. 
                      * The other operators require an array with a single element. 
        
        **Attribute Values**
                      * The PLATFORM attribute can be set to "ANDROID" or "IOS". 
                      * The AVAILABILITY attribute can be set to "AVAILABLE", "HIGHLY_AVAILABLE", "BUSY", or "TEMPORARY_NOT_AVAILABLE". 
                      * The FORM_FACTOR attribute can be set to "PHONE" or "TABLET". 
                      * The FLEET_TYPE attribute can be set to "PUBLIC" or "PRIVATE". 
                      - *(string) --* 
                - **matchedDevicesCount** *(integer) --* 
                  The number of devices that matched the device filter selection criteria.
                - **maxDevices** *(integer) --* 
                  The maximum number of devices to be selected by a device filter and included in a test run.
        :type arn: string
        :param arn: **[REQUIRED]**
          Represents the Amazon Resource Name (ARN) of the Device Farm run you wish to stop.
        :rtype: dict
        :returns:
        """
        pass

    def update_device_instance(self, arn: str, profileArn: str = None, labels: List = None) -> Dict:
        """
        Updates information about an existing private device instance.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/UpdateDeviceInstance>`_
        
        **Request Syntax**
        ::
          response = client.update_device_instance(
              arn='string',
              profileArn='string',
              labels=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'deviceInstance': {
                    'arn': 'string',
                    'deviceArn': 'string',
                    'labels': [
                        'string',
                    ],
                    'status': 'IN_USE'|'PREPARING'|'AVAILABLE'|'NOT_AVAILABLE',
                    'udid': 'string',
                    'instanceProfile': {
                        'arn': 'string',
                        'packageCleanup': True|False,
                        'excludeAppPackagesFromCleanup': [
                            'string',
                        ],
                        'rebootAfterUse': True|False,
                        'name': 'string',
                        'description': 'string'
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **deviceInstance** *(dict) --* 
              An object containing information about your device instance.
              - **arn** *(string) --* 
                The Amazon Resource Name (ARN) of the device instance.
              - **deviceArn** *(string) --* 
                The Amazon Resource Name (ARN) of the device.
              - **labels** *(list) --* 
                An array of strings describing the device instance.
                - *(string) --* 
              - **status** *(string) --* 
                The status of the device instance. Valid values are listed below.
              - **udid** *(string) --* 
                Unique device identifier for the device instance.
              - **instanceProfile** *(dict) --* 
                A object containing information about the instance profile.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the instance profile.
                - **packageCleanup** *(boolean) --* 
                  When set to ``true`` , Device Farm will remove app packages after a test run. The default value is ``false`` for private devices.
                - **excludeAppPackagesFromCleanup** *(list) --* 
                  An array of strings specifying the list of app packages that should not be cleaned up from the device after a test run is over.
                  The list of packages is only considered if you set ``packageCleanup`` to ``true`` .
                  - *(string) --* 
                - **rebootAfterUse** *(boolean) --* 
                  When set to ``true`` , Device Farm will reboot the instance after a test run. The default value is ``true`` .
                - **name** *(string) --* 
                  The name of the instance profile.
                - **description** *(string) --* 
                  The description of the instance profile.
        :type arn: string
        :param arn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the device instance.
        :type profileArn: string
        :param profileArn:
          The Amazon Resource Name (ARN) of the profile that you want to associate with the device instance.
        :type labels: list
        :param labels:
          An array of strings that you want to associate with the device instance.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def update_device_pool(self, arn: str, name: str = None, description: str = None, rules: List = None, maxDevices: int = None, clearMaxDevices: bool = None) -> Dict:
        """
        Modifies the name, description, and rules in a device pool given the attributes and the pool ARN. Rule updates are all-or-nothing, meaning they can only be updated as a whole (or not at all).
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/UpdateDevicePool>`_
        
        **Request Syntax**
        ::
          response = client.update_device_pool(
              arn='string',
              name='string',
              description='string',
              rules=[
                  {
                      'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE'|'OS_VERSION'|'MODEL'|'AVAILABILITY',
                      'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                      'value': 'string'
                  },
              ],
              maxDevices=123,
              clearMaxDevices=True|False
          )
        
        **Response Syntax**
        ::
            {
                'devicePool': {
                    'arn': 'string',
                    'name': 'string',
                    'description': 'string',
                    'type': 'CURATED'|'PRIVATE',
                    'rules': [
                        {
                            'attribute': 'ARN'|'PLATFORM'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'APPIUM_VERSION'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE'|'OS_VERSION'|'MODEL'|'AVAILABILITY',
                            'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                            'value': 'string'
                        },
                    ],
                    'maxDevices': 123
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of an update device pool request.
            - **devicePool** *(dict) --* 
              The device pool you just updated.
              - **arn** *(string) --* 
                The device pool's ARN.
              - **name** *(string) --* 
                The device pool's name.
              - **description** *(string) --* 
                The device pool's description.
              - **type** *(string) --* 
                The device pool's type.
                Allowed values include:
                * CURATED: A device pool that is created and managed by AWS Device Farm. 
                * PRIVATE: A device pool that is created and managed by the device pool developer. 
              - **rules** *(list) --* 
                Information about the device pool's rules.
                - *(dict) --* 
                  Represents a condition for a device pool.
                  - **attribute** *(string) --* 
                    The rule's stringified attribute. For example, specify the value as ``"\"abc\""`` .
                    The supported operators for each attribute are provided in the following list.
                      APPIUM_VERSION  
                    The Appium version for the test.
                     *Supported operators* : ``CONTAINS``  
                      ARN  
                    The Amazon Resource Name (ARN) of the device. For example, "arn:aws:devicefarm:us-west-2::device:12345Example".
                     *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                      AVAILABILITY  
                    The current availability of the device. Valid values are "AVAILABLE", "HIGHLY_AVAILABLE", "BUSY", or "TEMPORARY_NOT_AVAILABLE".
                     *Supported operators* : ``EQUALS``  
                      FLEET_TYPE  
                    The fleet type. Valid values are "PUBLIC" or "PRIVATE".
                     *Supported operators* : ``EQUALS``  
                      FORM_FACTOR  
                    The device form factor. Valid values are "PHONE" or "TABLET".
                     *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                      INSTANCE_ARN  
                    The Amazon Resource Name (ARN) of the device instance.
                     *Supported operators* : ``IN`` , ``NOT_IN``  
                      INSTANCE_LABELS  
                    The label of the device instance.
                     *Supported operators* : ``CONTAINS``  
                      MANUFACTURER  
                    The device manufacturer. For example, "Apple".
                     *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                      MODEL  
                    The device model, such as "Apple iPad Air 2" or "Google Pixel".
                     *Supported operators* : ``CONTAINS`` , ``EQUALS`` , ``IN`` , ``NOT_IN``  
                      OS_VERSION  
                    The operating system version. For example, "10.3.2".
                     *Supported operators* : ``EQUALS`` , ``GREATER_THAN`` , ``GREATER_THAN_OR_EQUALS`` , ``IN`` , ``LESS_THAN`` , ``LESS_THAN_OR_EQUALS`` , ``NOT_IN``  
                      PLATFORM  
                    The device platform. Valid values are "ANDROID" or "IOS".
                     *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``  
                      REMOTE_ACCESS_ENABLED  
                    Whether the device is enabled for remote access. Valid values are "TRUE" or "FALSE".
                     *Supported operators* : ``EQUALS``  
                      REMOTE_DEBUG_ENABLED  
                    Whether the device is enabled for remote debugging. Valid values are "TRUE" or "FALSE".
                     *Supported operators* : ``EQUALS``  
                  - **operator** *(string) --* 
                    Specifies how Device Farm compares the rule's attribute to the value. For the operators that are supported by each attribute, see the attribute descriptions.
                  - **value** *(string) --* 
                    The rule's value.
              - **maxDevices** *(integer) --* 
                The number of devices that Device Farm can add to your device pool. Device Farm adds devices that are available and that meet the criteria that you assign for the ``rules`` parameter. Depending on how many devices meet these constraints, your device pool might contain fewer devices than the value for this parameter.
                By specifying the maximum number of devices, you can control the costs that you incur by running tests.
        :type arn: string
        :param arn: **[REQUIRED]**
          The Amazon Resourc Name (ARN) of the Device Farm device pool you wish to update.
        :type name: string
        :param name:
          A string representing the name of the device pool you wish to update.
        :type description: string
        :param description:
          A description of the device pool you wish to update.
        :type rules: list
        :param rules:
          Represents the rules you wish to modify for the device pool. Updating rules is optional; however, if you choose to update rules for your request, the update will replace the existing rules.
          - *(dict) --*
            Represents a condition for a device pool.
            - **attribute** *(string) --*
              The rule\'s stringified attribute. For example, specify the value as ``\"\\"abc\\"\"`` .
              The supported operators for each attribute are provided in the following list.
                APPIUM_VERSION
              The Appium version for the test.
               *Supported operators* : ``CONTAINS``
                ARN
              The Amazon Resource Name (ARN) of the device. For example, \"arn:aws:devicefarm:us-west-2::device:12345Example\".
               *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``
                AVAILABILITY
              The current availability of the device. Valid values are \"AVAILABLE\", \"HIGHLY_AVAILABLE\", \"BUSY\", or \"TEMPORARY_NOT_AVAILABLE\".
               *Supported operators* : ``EQUALS``
                FLEET_TYPE
              The fleet type. Valid values are \"PUBLIC\" or \"PRIVATE\".
               *Supported operators* : ``EQUALS``
                FORM_FACTOR
              The device form factor. Valid values are \"PHONE\" or \"TABLET\".
               *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``
                INSTANCE_ARN
              The Amazon Resource Name (ARN) of the device instance.
               *Supported operators* : ``IN`` , ``NOT_IN``
                INSTANCE_LABELS
              The label of the device instance.
               *Supported operators* : ``CONTAINS``
                MANUFACTURER
              The device manufacturer. For example, \"Apple\".
               *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``
                MODEL
              The device model, such as \"Apple iPad Air 2\" or \"Google Pixel\".
               *Supported operators* : ``CONTAINS`` , ``EQUALS`` , ``IN`` , ``NOT_IN``
                OS_VERSION
              The operating system version. For example, \"10.3.2\".
               *Supported operators* : ``EQUALS`` , ``GREATER_THAN`` , ``GREATER_THAN_OR_EQUALS`` , ``IN`` , ``LESS_THAN`` , ``LESS_THAN_OR_EQUALS`` , ``NOT_IN``
                PLATFORM
              The device platform. Valid values are \"ANDROID\" or \"IOS\".
               *Supported operators* : ``EQUALS`` , ``IN`` , ``NOT_IN``
                REMOTE_ACCESS_ENABLED
              Whether the device is enabled for remote access. Valid values are \"TRUE\" or \"FALSE\".
               *Supported operators* : ``EQUALS``
                REMOTE_DEBUG_ENABLED
              Whether the device is enabled for remote debugging. Valid values are \"TRUE\" or \"FALSE\".
               *Supported operators* : ``EQUALS``
            - **operator** *(string) --*
              Specifies how Device Farm compares the rule\'s attribute to the value. For the operators that are supported by each attribute, see the attribute descriptions.
            - **value** *(string) --*
              The rule\'s value.
        :type maxDevices: integer
        :param maxDevices:
          The number of devices that Device Farm can add to your device pool. Device Farm adds devices that are available and that meet the criteria that you assign for the ``rules`` parameter. Depending on how many devices meet these constraints, your device pool might contain fewer devices than the value for this parameter.
          By specifying the maximum number of devices, you can control the costs that you incur by running tests.
          If you use this parameter in your request, you cannot use the ``clearMaxDevices`` parameter in the same request.
        :type clearMaxDevices: boolean
        :param clearMaxDevices:
          Sets whether the ``maxDevices`` parameter applies to your device pool. If you set this parameter to ``true`` , the ``maxDevices`` parameter does not apply, and Device Farm does not limit the number of devices that it adds to your device pool. In this case, Device Farm adds all available devices that meet the criteria that are specified for the ``rules`` parameter.
          If you use this parameter in your request, you cannot use the ``maxDevices`` parameter in the same request.
        :rtype: dict
        :returns:
        """
        pass

    def update_instance_profile(self, arn: str, name: str = None, description: str = None, packageCleanup: bool = None, excludeAppPackagesFromCleanup: List = None, rebootAfterUse: bool = None) -> Dict:
        """
        Updates information about an existing private device instance profile.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/UpdateInstanceProfile>`_
        
        **Request Syntax**
        ::
          response = client.update_instance_profile(
              arn='string',
              name='string',
              description='string',
              packageCleanup=True|False,
              excludeAppPackagesFromCleanup=[
                  'string',
              ],
              rebootAfterUse=True|False
          )
        
        **Response Syntax**
        ::
            {
                'instanceProfile': {
                    'arn': 'string',
                    'packageCleanup': True|False,
                    'excludeAppPackagesFromCleanup': [
                        'string',
                    ],
                    'rebootAfterUse': True|False,
                    'name': 'string',
                    'description': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **instanceProfile** *(dict) --* 
              An object containing information about your instance profile.
              - **arn** *(string) --* 
                The Amazon Resource Name (ARN) of the instance profile.
              - **packageCleanup** *(boolean) --* 
                When set to ``true`` , Device Farm will remove app packages after a test run. The default value is ``false`` for private devices.
              - **excludeAppPackagesFromCleanup** *(list) --* 
                An array of strings specifying the list of app packages that should not be cleaned up from the device after a test run is over.
                The list of packages is only considered if you set ``packageCleanup`` to ``true`` .
                - *(string) --* 
              - **rebootAfterUse** *(boolean) --* 
                When set to ``true`` , Device Farm will reboot the instance after a test run. The default value is ``true`` .
              - **name** *(string) --* 
                The name of the instance profile.
              - **description** *(string) --* 
                The description of the instance profile.
        :type arn: string
        :param arn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the instance profile.
        :type name: string
        :param name:
          The updated name for your instance profile.
        :type description: string
        :param description:
          The updated description for your instance profile.
        :type packageCleanup: boolean
        :param packageCleanup:
          The updated choice for whether you want to specify package cleanup. The default value is ``false`` for private devices.
        :type excludeAppPackagesFromCleanup: list
        :param excludeAppPackagesFromCleanup:
          An array of strings specifying the list of app packages that should not be cleaned up from the device after a test run is over.
          The list of packages is only considered if you set ``packageCleanup`` to ``true`` .
          - *(string) --*
        :type rebootAfterUse: boolean
        :param rebootAfterUse:
          The updated choice for whether you want to reboot the device after use. The default value is ``true`` .
        :rtype: dict
        :returns:
        """
        pass

    def update_network_profile(self, arn: str, name: str = None, description: str = None, type: str = None, uplinkBandwidthBits: int = None, downlinkBandwidthBits: int = None, uplinkDelayMs: int = None, downlinkDelayMs: int = None, uplinkJitterMs: int = None, downlinkJitterMs: int = None, uplinkLossPercent: int = None, downlinkLossPercent: int = None) -> Dict:
        """
        Updates the network profile with specific settings.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/UpdateNetworkProfile>`_
        
        **Request Syntax**
        ::
          response = client.update_network_profile(
              arn='string',
              name='string',
              description='string',
              type='CURATED'|'PRIVATE',
              uplinkBandwidthBits=123,
              downlinkBandwidthBits=123,
              uplinkDelayMs=123,
              downlinkDelayMs=123,
              uplinkJitterMs=123,
              downlinkJitterMs=123,
              uplinkLossPercent=123,
              downlinkLossPercent=123
          )
        
        **Response Syntax**
        ::
            {
                'networkProfile': {
                    'arn': 'string',
                    'name': 'string',
                    'description': 'string',
                    'type': 'CURATED'|'PRIVATE',
                    'uplinkBandwidthBits': 123,
                    'downlinkBandwidthBits': 123,
                    'uplinkDelayMs': 123,
                    'downlinkDelayMs': 123,
                    'uplinkJitterMs': 123,
                    'downlinkJitterMs': 123,
                    'uplinkLossPercent': 123,
                    'downlinkLossPercent': 123
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **networkProfile** *(dict) --* 
              A list of the available network profiles.
              - **arn** *(string) --* 
                The Amazon Resource Name (ARN) of the network profile.
              - **name** *(string) --* 
                The name of the network profile.
              - **description** *(string) --* 
                The description of the network profile.
              - **type** *(string) --* 
                The type of network profile. Valid values are listed below.
              - **uplinkBandwidthBits** *(integer) --* 
                The data throughput rate in bits per second, as an integer from 0 to 104857600.
              - **downlinkBandwidthBits** *(integer) --* 
                The data throughput rate in bits per second, as an integer from 0 to 104857600.
              - **uplinkDelayMs** *(integer) --* 
                Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
              - **downlinkDelayMs** *(integer) --* 
                Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
              - **uplinkJitterMs** *(integer) --* 
                Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
              - **downlinkJitterMs** *(integer) --* 
                Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
              - **uplinkLossPercent** *(integer) --* 
                Proportion of transmitted packets that fail to arrive from 0 to 100 percent.
              - **downlinkLossPercent** *(integer) --* 
                Proportion of received packets that fail to arrive from 0 to 100 percent.
        :type arn: string
        :param arn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the project for which you want to update network profile settings.
        :type name: string
        :param name:
          The name of the network profile about which you are returning information.
        :type description: string
        :param description:
          The descriptoin of the network profile about which you are returning information.
        :type type: string
        :param type:
          The type of network profile you wish to return information about. Valid values are listed below.
        :type uplinkBandwidthBits: integer
        :param uplinkBandwidthBits:
          The data throughput rate in bits per second, as an integer from 0 to 104857600.
        :type downlinkBandwidthBits: integer
        :param downlinkBandwidthBits:
          The data throughput rate in bits per second, as an integer from 0 to 104857600.
        :type uplinkDelayMs: integer
        :param uplinkDelayMs:
          Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
        :type downlinkDelayMs: integer
        :param downlinkDelayMs:
          Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
        :type uplinkJitterMs: integer
        :param uplinkJitterMs:
          Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
        :type downlinkJitterMs: integer
        :param downlinkJitterMs:
          Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
        :type uplinkLossPercent: integer
        :param uplinkLossPercent:
          Proportion of transmitted packets that fail to arrive from 0 to 100 percent.
        :type downlinkLossPercent: integer
        :param downlinkLossPercent:
          Proportion of received packets that fail to arrive from 0 to 100 percent.
        :rtype: dict
        :returns:
        """
        pass

    def update_project(self, arn: str, name: str = None, defaultJobTimeoutMinutes: int = None) -> Dict:
        """
        Modifies the specified project name, given the project ARN and a new name.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/UpdateProject>`_
        
        **Request Syntax**
        ::
          response = client.update_project(
              arn='string',
              name='string',
              defaultJobTimeoutMinutes=123
          )
        
        **Response Syntax**
        ::
            {
                'project': {
                    'arn': 'string',
                    'name': 'string',
                    'defaultJobTimeoutMinutes': 123,
                    'created': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            Represents the result of an update project request.
            - **project** *(dict) --* 
              The project you wish to update.
              - **arn** *(string) --* 
                The project's ARN.
              - **name** *(string) --* 
                The project's name.
              - **defaultJobTimeoutMinutes** *(integer) --* 
                The default number of minutes (at the project level) a test run will execute before it times out. Default value is 60 minutes.
              - **created** *(datetime) --* 
                When the project was created.
        :type arn: string
        :param arn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the project whose name you wish to update.
        :type name: string
        :param name:
          A string representing the new name of the project that you are updating.
        :type defaultJobTimeoutMinutes: integer
        :param defaultJobTimeoutMinutes:
          The number of minutes a test run in the project will execute before it times out.
        :rtype: dict
        :returns:
        """
        pass

    def update_upload(self, arn: str, name: str = None, contentType: str = None, editContent: bool = None) -> Dict:
        """
        Update an uploaded test specification (test spec).
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/UpdateUpload>`_
        
        **Request Syntax**
        ::
          response = client.update_upload(
              arn='string',
              name='string',
              contentType='string',
              editContent=True|False
          )
        
        **Response Syntax**
        ::
            {
                'upload': {
                    'arn': 'string',
                    'name': 'string',
                    'created': datetime(2015, 1, 1),
                    'type': 'ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_NODE_TEST_PACKAGE'|'APPIUM_RUBY_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_NODE_TEST_PACKAGE'|'APPIUM_WEB_RUBY_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE'|'APPIUM_JAVA_JUNIT_TEST_SPEC'|'APPIUM_JAVA_TESTNG_TEST_SPEC'|'APPIUM_PYTHON_TEST_SPEC'|'APPIUM_NODE_TEST_SPEC'|'APPIUM_RUBY_TEST_SPEC'|'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC'|'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC'|'APPIUM_WEB_PYTHON_TEST_SPEC'|'APPIUM_WEB_NODE_TEST_SPEC'|'APPIUM_WEB_RUBY_TEST_SPEC'|'INSTRUMENTATION_TEST_SPEC'|'XCTEST_UI_TEST_SPEC',
                    'status': 'INITIALIZED'|'PROCESSING'|'SUCCEEDED'|'FAILED',
                    'url': 'string',
                    'metadata': 'string',
                    'contentType': 'string',
                    'message': 'string',
                    'category': 'CURATED'|'PRIVATE'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **upload** *(dict) --* 
              A test spec uploaded to Device Farm.
              - **arn** *(string) --* 
                The upload's ARN.
              - **name** *(string) --* 
                The upload's file name.
              - **created** *(datetime) --* 
                When the upload was created.
              - **type** *(string) --* 
                The upload's type.
                Must be one of the following values:
                * ANDROID_APP: An Android upload. 
                * IOS_APP: An iOS upload. 
                * WEB_APP: A web appliction upload. 
                * EXTERNAL_DATA: An external data upload. 
                * APPIUM_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload. 
                * APPIUM_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload. 
                * APPIUM_PYTHON_TEST_PACKAGE: An Appium Python test package upload. 
                * APPIUM_NODE_TEST_PACKAGE: An Appium Node.js test package upload. 
                * APPIUM_RUBY_TEST_PACKAGE: An Appium Ruby test package upload. 
                * APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE: An Appium Java JUnit test package upload for web apps. 
                * APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE: An Appium Java TestNG test package upload for web apps. 
                * APPIUM_WEB_PYTHON_TEST_PACKAGE: An Appium Python test package upload for web apps. 
                * APPIUM_WEB_NODE_TEST_PACKAGE: An Appium Node.js test package upload for web apps. 
                * APPIUM_WEB_RUBY_TEST_PACKAGE: An Appium Ruby test package upload for web apps. 
                * CALABASH_TEST_PACKAGE: A Calabash test package upload. 
                * INSTRUMENTATION_TEST_PACKAGE: An instrumentation upload. 
                * UIAUTOMATION_TEST_PACKAGE: A uiautomation test package upload. 
                * UIAUTOMATOR_TEST_PACKAGE: A uiautomator test package upload. 
                * XCTEST_TEST_PACKAGE: An XCode test package upload. 
                * XCTEST_UI_TEST_PACKAGE: An XCode UI test package upload. 
                * APPIUM_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload. 
                * APPIUM_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload. 
                * APPIUM_PYTHON_TEST_SPEC: An Appium Python test spec upload. 
                * APPIUM_NODE_TEST_SPEC: An Appium Node.js test spec upload. 
                * APPIUM_RUBY_TEST_SPEC: An Appium Ruby test spec upload. 
                * APPIUM_WEB_JAVA_JUNIT_TEST_SPEC: An Appium Java JUnit test spec upload for a web app. 
                * APPIUM_WEB_JAVA_TESTNG_TEST_SPEC: An Appium Java TestNG test spec upload for a web app. 
                * APPIUM_WEB_PYTHON_TEST_SPEC: An Appium Python test spec upload for a web app. 
                * APPIUM_WEB_NODE_TEST_SPEC: An Appium Node.js test spec upload for a web app. 
                * APPIUM_WEB_RUBY_TEST_SPEC: An Appium Ruby test spec upload for a web app. 
                * INSTRUMENTATION_TEST_SPEC: An instrumentation test spec upload. 
                * XCTEST_UI_TEST_SPEC: An XCode UI test spec upload. 
              - **status** *(string) --* 
                The upload's status.
                Must be one of the following values:
                * FAILED: A failed status. 
                * INITIALIZED: An initialized status. 
                * PROCESSING: A processing status. 
                * SUCCEEDED: A succeeded status. 
              - **url** *(string) --* 
                The pre-signed Amazon S3 URL that was used to store a file through a corresponding PUT request.
              - **metadata** *(string) --* 
                The upload's metadata. For example, for Android, this contains information that is parsed from the manifest and is displayed in the AWS Device Farm console after the associated app is uploaded.
              - **contentType** *(string) --* 
                The upload's content type (for example, "application/octet-stream").
              - **message** *(string) --* 
                A message about the upload's result.
              - **category** *(string) --* 
                The upload's category. Allowed values include:
                * CURATED: An upload managed by AWS Device Farm. 
                * PRIVATE: An upload managed by the AWS Device Farm customer. 
        :type arn: string
        :param arn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the uploaded test spec.
        :type name: string
        :param name:
          The upload\'s test spec file name. The name should not contain the \'/\' character. The test spec file name must end with the ``.yaml`` or ``.yml`` file extension.
        :type contentType: string
        :param contentType:
          The upload\'s content type (for example, \"application/x-yaml\").
        :type editContent: boolean
        :param editContent:
          Set to true if the YAML file has changed and needs to be updated; otherwise, set to false.
        :rtype: dict
        :returns:
        """
        pass

    def update_vpce_configuration(self, arn: str, vpceConfigurationName: str = None, vpceServiceName: str = None, serviceDnsName: str = None, vpceConfigurationDescription: str = None) -> Dict:
        """
        Updates information about an existing Amazon Virtual Private Cloud (VPC) endpoint configuration.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/UpdateVPCEConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.update_vpce_configuration(
              arn='string',
              vpceConfigurationName='string',
              vpceServiceName='string',
              serviceDnsName='string',
              vpceConfigurationDescription='string'
          )
        
        **Response Syntax**
        ::
            {
                'vpceConfiguration': {
                    'arn': 'string',
                    'vpceConfigurationName': 'string',
                    'vpceServiceName': 'string',
                    'serviceDnsName': 'string',
                    'vpceConfigurationDescription': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **vpceConfiguration** *(dict) --* 
              An object containing information about your VPC endpoint configuration.
              - **arn** *(string) --* 
                The Amazon Resource Name (ARN) of the VPC endpoint configuration.
              - **vpceConfigurationName** *(string) --* 
                The friendly name you give to your VPC endpoint configuration, to manage your configurations more easily.
              - **vpceServiceName** *(string) --* 
                The name of the VPC endpoint service running inside your AWS account that you want Device Farm to test.
              - **serviceDnsName** *(string) --* 
                The DNS name that maps to the private IP address of the service you want to access.
              - **vpceConfigurationDescription** *(string) --* 
                An optional description, providing more details about your VPC endpoint configuration.
        :type arn: string
        :param arn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the VPC endpoint configuration you want to update.
        :type vpceConfigurationName: string
        :param vpceConfigurationName:
          The friendly name you give to your VPC endpoint configuration, to manage your configurations more easily.
        :type vpceServiceName: string
        :param vpceServiceName:
          The name of the VPC endpoint service running inside your AWS account that you want Device Farm to test.
        :type serviceDnsName: string
        :param serviceDnsName:
          The DNS (domain) name used to connect to your private service in your Amazon VPC. The DNS name must not already be in use on the Internet.
        :type vpceConfigurationDescription: string
        :param vpceConfigurationDescription:
          An optional description, providing more details about your VPC endpoint configuration.
        :rtype: dict
        :returns:
        """
        pass
