from datetime import datetime
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

    def claim_devices_by_claim_code(self, ClaimCode: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devices-2018-05-14/ClaimDevicesByClaimCode>`_
        
        **Request Syntax** 
        ::
        
          response = client.claim_devices_by_claim_code(
              ClaimCode=\'string\'
          )
        :type ClaimCode: string
        :param ClaimCode: **[REQUIRED]** 
        
          The claim code, starting with \"C-\", as provided by the device manufacturer.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ClaimCode\': \'string\',
                \'Total\': 123
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            200 response
        
            - **ClaimCode** *(string) --* 
        
              The claim code provided by the device manufacturer.
        
            - **Total** *(integer) --* 
        
              The total number of devices associated with the claim code that has been processed in the claim request.
        
        """
        pass

    def describe_device(self, DeviceId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devices-2018-05-14/DescribeDevice>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_device(
              DeviceId=\'string\'
          )
        :type DeviceId: string
        :param DeviceId: **[REQUIRED]** 
        
          The unique identifier of the device.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DeviceDescription\': {
                    \'Attributes\': {
                        \'string\': \'string\'
                    },
                    \'DeviceId\': \'string\',
                    \'Enabled\': True|False,
                    \'RemainingLife\': 123.0,
                    \'Type\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            200 response
        
            - **DeviceDescription** *(dict) --* 
        
              Device details.
        
              - **Attributes** *(dict) --* 
        
                An array of zero or more elements of DeviceAttribute objects providing user specified device attributes.
        
                - *(string) --* 
                  
                  - *(string) --* 
            
              - **DeviceId** *(string) --* 
        
                The unique identifier of the device.
        
              - **Enabled** *(boolean) --* 
        
                A Boolean value indicating whether or not the device is enabled.
        
              - **RemainingLife** *(float) --* 
        
                A value between 0 and 1 inclusive, representing the fraction of life remaining for the device.
        
              - **Type** *(string) --* 
        
                The type of the device, such as \"button\".
        
        """
        pass

    def finalize_device_claim(self, DeviceId: str) -> Dict:
        """
        
        .. note::
        
          Claiming a device consists of initiating a claim, then publishing a device event, and finalizing the claim. For a device of type button, a device event can be published by simply clicking the device.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devices-2018-05-14/FinalizeDeviceClaim>`_
        
        **Request Syntax** 
        ::
        
          response = client.finalize_device_claim(
              DeviceId=\'string\'
          )
        :type DeviceId: string
        :param DeviceId: **[REQUIRED]** 
        
          The unique identifier of the device.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'State\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            200 response
        
            - **State** *(string) --* 
        
              The device\'s final claim state.
        
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

    def get_device_methods(self, DeviceId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devices-2018-05-14/GetDeviceMethods>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_device_methods(
              DeviceId=\'string\'
          )
        :type DeviceId: string
        :param DeviceId: **[REQUIRED]** 
        
          The unique identifier of the device.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DeviceMethods\': [
                    {
                        \'DeviceType\': \'string\',
                        \'MethodName\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            200 response
        
            - **DeviceMethods** *(list) --* 
        
              List of available device APIs.
        
              - *(dict) --* 
                
                - **DeviceType** *(string) --* 
        
                  The type of the device, such as \"button\".
        
                - **MethodName** *(string) --* 
        
                  The name of the method applicable to the deviceType.
        
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

    def initiate_device_claim(self, DeviceId: str) -> Dict:
        """
        
        .. note::
        
          Claiming a device consists of initiating a claim, then publishing a device event, and finalizing the claim. For a device of type button, a device event can be published by simply clicking the device.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devices-2018-05-14/InitiateDeviceClaim>`_
        
        **Request Syntax** 
        ::
        
          response = client.initiate_device_claim(
              DeviceId=\'string\'
          )
        :type DeviceId: string
        :param DeviceId: **[REQUIRED]** 
        
          The unique identifier of the device.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'State\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            200 response
        
            - **State** *(string) --* 
        
              The device\'s final claim state.
        
        """
        pass

    def invoke_device_method(self, DeviceId: str, DeviceMethod: Dict = None, DeviceMethodParameters: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devices-2018-05-14/InvokeDeviceMethod>`_
        
        **Request Syntax** 
        ::
        
          response = client.invoke_device_method(
              DeviceId=\'string\',
              DeviceMethod={
                  \'DeviceType\': \'string\',
                  \'MethodName\': \'string\'
              },
              DeviceMethodParameters=\'string\'
          )
        :type DeviceId: string
        :param DeviceId: **[REQUIRED]** 
        
          The unique identifier of the device.
        
        :type DeviceMethod: dict
        :param DeviceMethod: 
        
          The device method to invoke.
        
          - **DeviceType** *(string) --* 
        
            The type of the device, such as \"button\".
        
          - **MethodName** *(string) --* 
        
            The name of the method applicable to the deviceType.
        
        :type DeviceMethodParameters: string
        :param DeviceMethodParameters: 
        
          A JSON encoded string containing the device method request parameters.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DeviceMethodResponse\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            200 response
        
            - **DeviceMethodResponse** *(string) --* 
        
              A JSON encoded string containing the device method response.
        
        """
        pass

    def list_device_events(self, DeviceId: str, FromTimeStamp: datetime, ToTimeStamp: datetime, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devices-2018-05-14/ListDeviceEvents>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_device_events(
              DeviceId=\'string\',
              FromTimeStamp=datetime(2015, 1, 1),
              MaxResults=123,
              NextToken=\'string\',
              ToTimeStamp=datetime(2015, 1, 1)
          )
        :type DeviceId: string
        :param DeviceId: **[REQUIRED]** 
        
          The unique identifier of the device.
        
        :type FromTimeStamp: datetime
        :param FromTimeStamp: **[REQUIRED]** 
        
          The start date for the device event query, in ISO8061 format. For example, 2018-03-28T15:45:12.880Z 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return per request. If not set, a default value of 100 is used.
        
        :type NextToken: string
        :param NextToken: 
        
          The token to retrieve the next set of results.
        
        :type ToTimeStamp: datetime
        :param ToTimeStamp: **[REQUIRED]** 
        
          The end date for the device event query, in ISO8061 format. For example, 2018-03-28T15:45:12.880Z 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Events\': [
                    {
                        \'Device\': {
                            \'Attributes\': {},
                            \'DeviceId\': \'string\',
                            \'Type\': \'string\'
                        },
                        \'StdEvent\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            200 response
        
            - **Events** *(list) --* 
        
              An array of zero or more elements describing the event(s) associated with the device.
        
              - *(dict) --* 
                
                - **Device** *(dict) --* 
        
                  An object representing the device associated with the event.
        
                  - **Attributes** *(dict) --* 
        
                    The user specified attributes associated with the device for an event.
        
                  - **DeviceId** *(string) --* 
        
                    The unique identifier of the device.
        
                  - **Type** *(string) --* 
        
                    The device type, such as \"button\".
        
                - **StdEvent** *(string) --* 
        
                  A serialized JSON object representing the device-type specific event.
        
            - **NextToken** *(string) --* 
        
              The token to retrieve the next set of results.
        
        """
        pass

    def list_devices(self, DeviceType: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devices-2018-05-14/ListDevices>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_devices(
              DeviceType=\'string\',
              MaxResults=123,
              NextToken=\'string\'
          )
        :type DeviceType: string
        :param DeviceType: 
        
          The type of the device, such as \"button\".
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return per request. If not set, a default value of 100 is used.
        
        :type NextToken: string
        :param NextToken: 
        
          The token to retrieve the next set of results.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Devices\': [
                    {
                        \'Attributes\': {
                            \'string\': \'string\'
                        },
                        \'DeviceId\': \'string\',
                        \'Enabled\': True|False,
                        \'RemainingLife\': 123.0,
                        \'Type\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            200 response
        
            - **Devices** *(list) --* 
        
              A list of devices.
        
              - *(dict) --* 
                
                - **Attributes** *(dict) --* 
        
                  An array of zero or more elements of DeviceAttribute objects providing user specified device attributes.
        
                  - *(string) --* 
                    
                    - *(string) --* 
              
                - **DeviceId** *(string) --* 
        
                  The unique identifier of the device.
        
                - **Enabled** *(boolean) --* 
        
                  A Boolean value indicating whether or not the device is enabled.
        
                - **RemainingLife** *(float) --* 
        
                  A value between 0 and 1 inclusive, representing the fraction of life remaining for the device.
        
                - **Type** *(string) --* 
        
                  The type of the device, such as \"button\".
        
            - **NextToken** *(string) --* 
        
              The token to retrieve the next set of results.
        
        """
        pass

    def unclaim_device(self, DeviceId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devices-2018-05-14/UnclaimDevice>`_
        
        **Request Syntax** 
        ::
        
          response = client.unclaim_device(
              DeviceId=\'string\'
          )
        :type DeviceId: string
        :param DeviceId: **[REQUIRED]** 
        
          The unique identifier of the device.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'State\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            200 response
        
            - **State** *(string) --* 
        
              The device\'s final claim state.
        
        """
        pass

    def update_device_state(self, DeviceId: str, Enabled: bool = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devices-2018-05-14/UpdateDeviceState>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_device_state(
              DeviceId=\'string\',
              Enabled=True|False
          )
        :type DeviceId: string
        :param DeviceId: **[REQUIRED]** 
        
          The unique identifier of the device.
        
        :type Enabled: boolean
        :param Enabled: 
        
          If true, the device is enabled. If false, the device is disabled.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        
            200 response
        
        """
        pass
