from typing import List
from typing import Dict
from botocore.paginate import Paginator


class DescribeTapeArchives(Paginator):
    def paginate(self, TapeARNs: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeTapeArchives>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              TapeARNs=[
                  \'string\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type TapeARNs: list
        :param TapeARNs: 
        
          Specifies one or more unique Amazon Resource Names (ARNs) that represent the virtual tapes you want to describe.
        
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'TapeArchives\': [
                    {
                        \'TapeARN\': \'string\',
                        \'TapeBarcode\': \'string\',
                        \'TapeCreatedDate\': datetime(2015, 1, 1),
                        \'TapeSizeInBytes\': 123,
                        \'CompletionTime\': datetime(2015, 1, 1),
                        \'RetrievedTo\': \'string\',
                        \'TapeStatus\': \'string\',
                        \'TapeUsedInBytes\': 123,
                        \'KMSKey\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            DescribeTapeArchivesOutput
        
            - **TapeArchives** *(list) --* 
        
              An array of virtual tape objects in the virtual tape shelf (VTS). The description includes of the Amazon Resource Name (ARN) of the virtual tapes. The information returned includes the Amazon Resource Names (ARNs) of the tapes, size of the tapes, status of the tapes, progress of the description and tape barcode.
        
              - *(dict) --* 
        
                Represents a virtual tape that is archived in the virtual tape shelf (VTS).
        
                - **TapeARN** *(string) --* 
        
                  The Amazon Resource Name (ARN) of an archived virtual tape.
        
                - **TapeBarcode** *(string) --* 
        
                  The barcode that identifies the archived virtual tape.
        
                - **TapeCreatedDate** *(datetime) --* 
        
                  The date the virtual tape was created.
        
                - **TapeSizeInBytes** *(integer) --* 
        
                  The size, in bytes, of the archived virtual tape.
        
                - **CompletionTime** *(datetime) --* 
        
                  The time that the archiving of the virtual tape was completed.
        
                  The default time stamp format is in the ISO8601 extended YYYY-MM-DD\'T\'HH:MM:SS\'Z\' format.
        
                - **RetrievedTo** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the tape gateway that the virtual tape is being retrieved to.
        
                  The virtual tape is retrieved from the virtual tape shelf (VTS).
        
                - **TapeStatus** *(string) --* 
        
                  The current state of the archived virtual tape.
        
                - **TapeUsedInBytes** *(integer) --* 
        
                  The size, in bytes, of data stored on the virtual tape.
        
                  .. note::
        
                    This value is not available for tapes created prior to May 13, 2015.
        
                - **KMSKey** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side encryption. This value can only be set when KMSEncrypted is true. Optional.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeTapeRecoveryPoints(Paginator):
    def paginate(self, GatewayARN: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeTapeRecoveryPoints>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              GatewayARN=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and region.
        
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'GatewayARN\': \'string\',
                \'TapeRecoveryPointInfos\': [
                    {
                        \'TapeARN\': \'string\',
                        \'TapeRecoveryPointTime\': datetime(2015, 1, 1),
                        \'TapeSizeInBytes\': 123,
                        \'TapeStatus\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            DescribeTapeRecoveryPointsOutput
        
            - **GatewayARN** *(string) --* 
        
              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and region.
        
            - **TapeRecoveryPointInfos** *(list) --* 
        
              An array of TapeRecoveryPointInfos that are available for the specified gateway.
        
              - *(dict) --* 
        
                Describes a recovery point.
        
                - **TapeARN** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the virtual tape.
        
                - **TapeRecoveryPointTime** *(datetime) --* 
        
                  The time when the point-in-time view of the virtual tape was replicated for later recovery.
        
                  The default time stamp format of the tape recovery point time is in the ISO8601 extended YYYY-MM-DD\'T\'HH:MM:SS\'Z\' format.
        
                - **TapeSizeInBytes** *(integer) --* 
        
                  The size, in bytes, of the virtual tapes to recover.
        
                - **TapeStatus** *(string) --* 
            
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeTapes(Paginator):
    def paginate(self, GatewayARN: str, TapeARNs: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeTapes>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              GatewayARN=\'string\',
              TapeARNs=[
                  \'string\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and region.
        
        :type TapeARNs: list
        :param TapeARNs: 
        
          Specifies one or more unique Amazon Resource Names (ARNs) that represent the virtual tapes you want to describe. If this parameter is not specified, Tape gateway returns a description of all virtual tapes associated with the specified gateway.
        
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Tapes\': [
                    {
                        \'TapeARN\': \'string\',
                        \'TapeBarcode\': \'string\',
                        \'TapeCreatedDate\': datetime(2015, 1, 1),
                        \'TapeSizeInBytes\': 123,
                        \'TapeStatus\': \'string\',
                        \'VTLDevice\': \'string\',
                        \'Progress\': 123.0,
                        \'TapeUsedInBytes\': 123,
                        \'KMSKey\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            DescribeTapesOutput
        
            - **Tapes** *(list) --* 
        
              An array of virtual tape descriptions.
        
              - *(dict) --* 
        
                Describes a virtual tape object.
        
                - **TapeARN** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the virtual tape.
        
                - **TapeBarcode** *(string) --* 
        
                  The barcode that identifies a specific virtual tape.
        
                - **TapeCreatedDate** *(datetime) --* 
        
                  The date the virtual tape was created.
        
                - **TapeSizeInBytes** *(integer) --* 
        
                  The size, in bytes, of the virtual tape capacity.
        
                - **TapeStatus** *(string) --* 
        
                  The current state of the virtual tape.
        
                - **VTLDevice** *(string) --* 
        
                  The virtual tape library (VTL) device that the virtual tape is associated with.
        
                - **Progress** *(float) --* 
        
                  For archiving virtual tapes, indicates how much data remains to be uploaded before archiving is complete.
        
                  Range: 0 (not started) to 100 (complete).
        
                - **TapeUsedInBytes** *(integer) --* 
        
                  The size, in bytes, of data stored on the virtual tape.
        
                  .. note::
        
                    This value is not available for tapes created prior to May 13, 2015.
        
                - **KMSKey** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side encryption. This value can only be set when KMSEncrypted is true. Optional.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class DescribeVTLDevices(Paginator):
    def paginate(self, GatewayARN: str, VTLDeviceARNs: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeVTLDevices>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              GatewayARN=\'string\',
              VTLDeviceARNs=[
                  \'string\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type GatewayARN: string
        :param GatewayARN: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and region.
        
        :type VTLDeviceARNs: list
        :param VTLDeviceARNs: 
        
          An array of strings, where each string represents the Amazon Resource Name (ARN) of a VTL device.
        
          .. note::
        
            All of the specified VTL devices must be from the same gateway. If no VTL devices are specified, the result will contain all devices on the specified gateway.
        
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'GatewayARN\': \'string\',
                \'VTLDevices\': [
                    {
                        \'VTLDeviceARN\': \'string\',
                        \'VTLDeviceType\': \'string\',
                        \'VTLDeviceVendor\': \'string\',
                        \'VTLDeviceProductIdentifier\': \'string\',
                        \'DeviceiSCSIAttributes\': {
                            \'TargetARN\': \'string\',
                            \'NetworkInterfaceId\': \'string\',
                            \'NetworkInterfacePort\': 123,
                            \'ChapEnabled\': True|False
                        }
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            DescribeVTLDevicesOutput
        
            - **GatewayARN** *(string) --* 
        
              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and region.
        
            - **VTLDevices** *(list) --* 
        
              An array of VTL device objects composed of the Amazon Resource Name(ARN) of the VTL devices.
        
              - *(dict) --* 
        
                Represents a device object associated with a tape gateway.
        
                - **VTLDeviceARN** *(string) --* 
        
                  Specifies the unique Amazon Resource Name (ARN) of the device (tape drive or media changer).
        
                - **VTLDeviceType** *(string) --* 
                
                - **VTLDeviceVendor** *(string) --* 
                
                - **VTLDeviceProductIdentifier** *(string) --* 
                
                - **DeviceiSCSIAttributes** *(dict) --* 
        
                  A list of iSCSI information about a VTL device.
        
                  - **TargetARN** *(string) --* 
        
                    Specifies the unique Amazon Resource Name (ARN) that encodes the iSCSI qualified name(iqn) of a tape drive or media changer target.
        
                  - **NetworkInterfaceId** *(string) --* 
        
                    The network interface identifier of the VTL device.
        
                  - **NetworkInterfacePort** *(integer) --* 
        
                    The port used to communicate with iSCSI VTL device targets.
        
                  - **ChapEnabled** *(boolean) --* 
        
                    Indicates whether mutual CHAP is enabled for the iSCSI target.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListGateways(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/ListGateways>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Gateways\': [
                    {
                        \'GatewayId\': \'string\',
                        \'GatewayARN\': \'string\',
                        \'GatewayType\': \'string\',
                        \'GatewayOperationalState\': \'string\',
                        \'GatewayName\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Gateways** *(list) --* 
              
              - *(dict) --* 
        
                Describes a gateway object.
        
                - **GatewayId** *(string) --* 
        
                  The unique identifier assigned to your gateway during activation. This ID becomes part of the gateway Amazon Resource Name (ARN), which you use as input for other operations.
        
                - **GatewayARN** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and region.
        
                - **GatewayType** *(string) --* 
        
                  The type of the gateway.
        
                - **GatewayOperationalState** *(string) --* 
        
                  The state of the gateway.
        
                  Valid Values: DISABLED or ACTIVE
        
                - **GatewayName** *(string) --* 
        
                  The name of the gateway.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListVolumes(Paginator):
    def paginate(self, GatewayARN: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/ListVolumes>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              GatewayARN=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type GatewayARN: string
        :param GatewayARN: 
        
          The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and region.
        
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'GatewayARN\': \'string\',
                \'VolumeInfos\': [
                    {
                        \'VolumeARN\': \'string\',
                        \'VolumeId\': \'string\',
                        \'GatewayARN\': \'string\',
                        \'GatewayId\': \'string\',
                        \'VolumeType\': \'string\',
                        \'VolumeSizeInBytes\': 123
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **GatewayARN** *(string) --* 
        
              The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and region.
        
            - **VolumeInfos** *(list) --* 
              
              - *(dict) --* 
        
                Describes a storage volume object.
        
                - **VolumeARN** *(string) --* 
        
                  The Amazon Resource Name (ARN) for the storage volume. For example, the following is a valid ARN:
        
                   ``arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB``  
        
                  Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).
        
                - **VolumeId** *(string) --* 
        
                  The unique identifier assigned to the volume. This ID becomes part of the volume Amazon Resource Name (ARN), which you use as input for other operations.
        
                  Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).
        
                - **GatewayARN** *(string) --* 
        
                  The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and region.
        
                - **GatewayId** *(string) --* 
        
                  The unique identifier assigned to your gateway during activation. This ID becomes part of the gateway Amazon Resource Name (ARN), which you use as input for other operations.
        
                  Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).
        
                - **VolumeType** *(string) --* 
                
                - **VolumeSizeInBytes** *(integer) --* 
        
                  The size of the volume in bytes.
        
                  Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
