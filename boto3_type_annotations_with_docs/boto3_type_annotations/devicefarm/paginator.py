from typing import List
from typing import Dict
from botocore.paginate import Paginator


class GetOfferingStatus(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.get_offering_status`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetOfferingStatus>`_
        
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class ListArtifacts(Paginator):
    def paginate(self, arn: str, type: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_artifacts`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListArtifacts>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              arn='string',
              type='SCREENSHOT'|'FILE'|'LOG',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class ListDeviceInstances(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_device_instances`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListDeviceInstances>`_
        
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class ListDevicePools(Paginator):
    def paginate(self, arn: str, type: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_device_pools`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListDevicePools>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              arn='string',
              type='CURATED'|'PRIVATE',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type arn: string
        :param arn: **[REQUIRED]**
          The project ARN.
        :type type: string
        :param type:
          The device pools\' type.
          Allowed values include:
          * CURATED: A device pool that is created and managed by AWS Device Farm.
          * PRIVATE: A device pool that is created and managed by the device pool developer.
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


class ListDevices(Paginator):
    def paginate(self, arn: str = None, filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_devices`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListDevices>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              arn='string',
              filters=[
                  {
                      'attribute': 'ARN'|'PLATFORM'|'OS_VERSION'|'MODEL'|'AVAILABILITY'|'FORM_FACTOR'|'MANUFACTURER'|'REMOTE_ACCESS_ENABLED'|'REMOTE_DEBUG_ENABLED'|'INSTANCE_ARN'|'INSTANCE_LABELS'|'FLEET_TYPE',
                      'operator': 'EQUALS'|'LESS_THAN'|'LESS_THAN_OR_EQUALS'|'GREATER_THAN'|'GREATER_THAN_OR_EQUALS'|'IN'|'NOT_IN'|'CONTAINS',
                      'values': [
                          'string',
                      ]
                  },
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type arn: string
        :param arn:
          The Amazon Resource Name (ARN) of the project.
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


class ListInstanceProfiles(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_instance_profiles`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListInstanceProfiles>`_
        
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
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
    def paginate(self, arn: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_jobs`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListJobs>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              arn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type arn: string
        :param arn: **[REQUIRED]**
          The run\'s Amazon Resource Name (ARN).
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


class ListNetworkProfiles(Paginator):
    def paginate(self, arn: str, type: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_network_profiles`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListNetworkProfiles>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              arn='string',
              type='CURATED'|'PRIVATE',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type arn: string
        :param arn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the project for which you want to list network profiles.
        :type type: string
        :param type:
          The type of network profile you wish to return information about. Valid values are listed below.
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


class ListOfferingPromotions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_offering_promotions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListOfferingPromotions>`_
        
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
                'offeringPromotions': [
                    {
                        'id': 'string',
                        'description': 'string'
                    },
                ],
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class ListOfferingTransactions(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_offering_transactions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListOfferingTransactions>`_
        
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class ListOfferings(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_offerings`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListOfferings>`_
        
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class ListProjects(Paginator):
    def paginate(self, arn: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_projects`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListProjects>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              arn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type arn: string
        :param arn:
          Optional. If no Amazon Resource Name (ARN) is specified, then AWS Device Farm returns a list of all projects for the AWS account. You can also specify a project ARN.
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


class ListRemoteAccessSessions(Paginator):
    def paginate(self, arn: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_remote_access_sessions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListRemoteAccessSessions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              arn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type arn: string
        :param arn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the remote access session about which you are requesting information.
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


class ListRuns(Paginator):
    def paginate(self, arn: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_runs`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListRuns>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              arn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type arn: string
        :param arn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the project for which you want to list runs.
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


class ListSamples(Paginator):
    def paginate(self, arn: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_samples`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListSamples>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              arn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type arn: string
        :param arn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the job used to list samples.
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


class ListSuites(Paginator):
    def paginate(self, arn: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_suites`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListSuites>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              arn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type arn: string
        :param arn: **[REQUIRED]**
          The job\'s Amazon Resource Name (ARN).
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


class ListTests(Paginator):
    def paginate(self, arn: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_tests`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListTests>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              arn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type arn: string
        :param arn: **[REQUIRED]**
          The test suite\'s Amazon Resource Name (ARN).
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


class ListUniqueProblems(Paginator):
    def paginate(self, arn: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_unique_problems`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListUniqueProblems>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              arn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type arn: string
        :param arn: **[REQUIRED]**
          The unique problems\' ARNs.
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


class ListUploads(Paginator):
    def paginate(self, arn: str, type: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_uploads`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListUploads>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              arn='string',
              type='ANDROID_APP'|'IOS_APP'|'WEB_APP'|'EXTERNAL_DATA'|'APPIUM_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_PYTHON_TEST_PACKAGE'|'APPIUM_NODE_TEST_PACKAGE'|'APPIUM_RUBY_TEST_PACKAGE'|'APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE'|'APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE'|'APPIUM_WEB_PYTHON_TEST_PACKAGE'|'APPIUM_WEB_NODE_TEST_PACKAGE'|'APPIUM_WEB_RUBY_TEST_PACKAGE'|'CALABASH_TEST_PACKAGE'|'INSTRUMENTATION_TEST_PACKAGE'|'UIAUTOMATION_TEST_PACKAGE'|'UIAUTOMATOR_TEST_PACKAGE'|'XCTEST_TEST_PACKAGE'|'XCTEST_UI_TEST_PACKAGE'|'APPIUM_JAVA_JUNIT_TEST_SPEC'|'APPIUM_JAVA_TESTNG_TEST_SPEC'|'APPIUM_PYTHON_TEST_SPEC'|'APPIUM_NODE_TEST_SPEC'|'APPIUM_RUBY_TEST_SPEC'|'APPIUM_WEB_JAVA_JUNIT_TEST_SPEC'|'APPIUM_WEB_JAVA_TESTNG_TEST_SPEC'|'APPIUM_WEB_PYTHON_TEST_SPEC'|'APPIUM_WEB_NODE_TEST_SPEC'|'APPIUM_WEB_RUBY_TEST_SPEC'|'INSTRUMENTATION_TEST_SPEC'|'XCTEST_UI_TEST_SPEC',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class ListVPCEConfigurations(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`DeviceFarm.Client.list_vpce_configurations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListVPCEConfigurations>`_
        
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
                'vpceConfigurations': [
                    {
                        'arn': 'string',
                        'vpceConfigurationName': 'string',
                        'vpceServiceName': 'string',
                        'serviceDnsName': 'string',
                        'vpceConfigurationDescription': 'string'
                    },
                ],
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A token to resume pagination.
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
