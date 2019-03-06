from datetime import datetime
from typing import Dict
from botocore.paginate import Paginator


class ListDeviceEvents(Paginator):
    def paginate(self, DeviceId: str, FromTimeStamp: datetime, ToTimeStamp: datetime, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT1ClickDevicesService.Client.list_device_events`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devices-2018-05-14/ListDeviceEvents>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DeviceId='string',
              FromTimeStamp=datetime(2015, 1, 1),
              ToTimeStamp=datetime(2015, 1, 1),
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Events': [
                    {
                        'Device': {
                            'Attributes': {},
                            'DeviceId': 'string',
                            'Type': 'string'
                        },
                        'StdEvent': 'string'
                    },
                ],
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
                    The device type, such as "button".
                - **StdEvent** *(string) --* 
                  A serialized JSON object representing the device-type specific event.
        :type DeviceId: string
        :param DeviceId: **[REQUIRED]**
          The unique identifier of the device.
        :type FromTimeStamp: datetime
        :param FromTimeStamp: **[REQUIRED]**
          The start date for the device event query, in ISO8061 format. For example, 2018-03-28T15:45:12.880Z
        :type ToTimeStamp: datetime
        :param ToTimeStamp: **[REQUIRED]**
          The end date for the device event query, in ISO8061 format. For example, 2018-03-28T15:45:12.880Z
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
    def paginate(self, DeviceType: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`IoT1ClickDevicesService.Client.list_devices`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/devices-2018-05-14/ListDevices>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              DeviceType='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Devices': [
                    {
                        'Attributes': {
                            'string': 'string'
                        },
                        'DeviceId': 'string',
                        'Enabled': True|False,
                        'RemainingLife': 123.0,
                        'Type': 'string'
                    },
                ],
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
                  The type of the device, such as "button".
        :type DeviceType: string
        :param DeviceType:
          The type of the device, such as \"button\".
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
