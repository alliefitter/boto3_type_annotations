from typing import NoReturn
from typing import List
from typing import Dict
from botocore.waiter import Waiter


class BundleTaskComplete(Waiter):
    def wait(self, BundleIds: List = None, Filters: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeBundleTasks>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              BundleIds=[
                  \'string\',
              ],
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              DryRun=True|False,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type BundleIds: list
        :param BundleIds: 
        
          One or more bundle task IDs.
        
          Default: Describes all your bundle tasks.
        
          - *(string) --* 
        
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``bundle-id`` - The ID of the bundle task. 
           
          * ``error-code`` - If the task failed, the error code returned. 
           
          * ``error-message`` - If the task failed, the error message returned. 
           
          * ``instance-id`` - The ID of the instance. 
           
          * ``progress`` - The level of task completion, as a percentage (for example, 20%). 
           
          * ``s3-bucket`` - The Amazon S3 bucket to store the AMI. 
           
          * ``s3-prefix`` - The beginning of the AMI name. 
           
          * ``start-time`` - The time the task started (for example, 2013-09-15T17:15:20.000Z). 
           
          * ``state`` - The state of the task (``pending`` | ``waiting-for-shutdown`` | ``bundling`` | ``storing`` | ``cancelling`` | ``complete`` | ``failed`` ). 
           
          * ``update-time`` - The time of the most recent update for the task. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class ConversionTaskCancelled(Waiter):
    def wait(self, ConversionTaskIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeConversionTasks>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              ConversionTaskIds=[
                  \'string\',
              ],
              DryRun=True|False,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type ConversionTaskIds: list
        :param ConversionTaskIds: 
        
          One or more conversion task IDs.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class ConversionTaskCompleted(Waiter):
    def wait(self, ConversionTaskIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeConversionTasks>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              ConversionTaskIds=[
                  \'string\',
              ],
              DryRun=True|False,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type ConversionTaskIds: list
        :param ConversionTaskIds: 
        
          One or more conversion task IDs.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class ConversionTaskDeleted(Waiter):
    def wait(self, ConversionTaskIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeConversionTasks>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              ConversionTaskIds=[
                  \'string\',
              ],
              DryRun=True|False,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type ConversionTaskIds: list
        :param ConversionTaskIds: 
        
          One or more conversion task IDs.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class CustomerGatewayAvailable(Waiter):
    def wait(self, CustomerGatewayIds: List = None, Filters: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeCustomerGateways>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              CustomerGatewayIds=[
                  \'string\',
              ],
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              DryRun=True|False,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type CustomerGatewayIds: list
        :param CustomerGatewayIds: 
        
          One or more customer gateway IDs.
        
          Default: Describes all your customer gateways.
        
          - *(string) --* 
        
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``bgp-asn`` - The customer gateway\'s Border Gateway Protocol (BGP) Autonomous System Number (ASN). 
           
          * ``customer-gateway-id`` - The ID of the customer gateway. 
           
          * ``ip-address`` - The IP address of the customer gateway\'s Internet-routable external interface. 
           
          * ``state`` - The state of the customer gateway (``pending`` | ``available`` | ``deleting`` | ``deleted`` ). 
           
          * ``type`` - The type of customer gateway. Currently, the only supported type is ``ipsec.1`` . 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class ExportTaskCancelled(Waiter):
    def wait(self, ExportTaskIds: List = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeExportTasks>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              ExportTaskIds=[
                  \'string\',
              ],
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type ExportTaskIds: list
        :param ExportTaskIds: 
        
          One or more export task IDs.
        
          - *(string) --* 
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class ExportTaskCompleted(Waiter):
    def wait(self, ExportTaskIds: List = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeExportTasks>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              ExportTaskIds=[
                  \'string\',
              ],
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type ExportTaskIds: list
        :param ExportTaskIds: 
        
          One or more export task IDs.
        
          - *(string) --* 
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class ImageAvailable(Waiter):
    def wait(self, ExecutableUsers: List = None, Filters: List = None, ImageIds: List = None, Owners: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeImages>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              ExecutableUsers=[
                  \'string\',
              ],
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              ImageIds=[
                  \'string\',
              ],
              Owners=[
                  \'string\',
              ],
              DryRun=True|False,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type ExecutableUsers: list
        :param ExecutableUsers: 
        
          Scopes the images by users with explicit launch permissions. Specify an AWS account ID, ``self`` (the sender of the request), or ``all`` (public AMIs).
        
          - *(string) --* 
        
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``architecture`` - The image architecture (``i386`` | ``x86_64`` ). 
           
          * ``block-device-mapping.delete-on-termination`` - A Boolean value that indicates whether the Amazon EBS volume is deleted on instance termination. 
           
          * ``block-device-mapping.device-name`` - The device name specified in the block device mapping (for example, ``/dev/sdh`` or ``xvdh`` ). 
           
          * ``block-device-mapping.snapshot-id`` - The ID of the snapshot used for the EBS volume. 
           
          * ``block-device-mapping.volume-size`` - The volume size of the EBS volume, in GiB. 
           
          * ``block-device-mapping.volume-type`` - The volume type of the EBS volume (``gp2`` | ``io1`` | ``st1`` | ``sc1`` | ``standard`` ). 
           
          * ``description`` - The description of the image (provided during image creation). 
           
          * ``ena-support`` - A Boolean that indicates whether enhanced networking with ENA is enabled. 
           
          * ``hypervisor`` - The hypervisor type (``ovm`` | ``xen`` ). 
           
          * ``image-id`` - The ID of the image. 
           
          * ``image-type`` - The image type (``machine`` | ``kernel`` | ``ramdisk`` ). 
           
          * ``is-public`` - A Boolean that indicates whether the image is public. 
           
          * ``kernel-id`` - The kernel ID. 
           
          * ``manifest-location`` - The location of the image manifest. 
           
          * ``name`` - The name of the AMI (provided during image creation). 
           
          * ``owner-alias`` - String value from an Amazon-maintained list (``amazon`` | ``aws-marketplace`` | ``microsoft`` ) of snapshot owners. Not to be confused with the user-configured AWS account alias, which is set from the IAM console. 
           
          * ``owner-id`` - The AWS account ID of the image owner. 
           
          * ``platform`` - The platform. To only list Windows-based AMIs, use ``windows`` . 
           
          * ``product-code`` - The product code. 
           
          * ``product-code.type`` - The type of the product code (``devpay`` | ``marketplace`` ). 
           
          * ``ramdisk-id`` - The RAM disk ID. 
           
          * ``root-device-name`` - The device name of the root device volume (for example, ``/dev/sda1`` ). 
           
          * ``root-device-type`` - The type of the root device volume (``ebs`` | ``instance-store`` ). 
           
          * ``state`` - The state of the image (``available`` | ``pending`` | ``failed`` ). 
           
          * ``state-reason-code`` - The reason code for the state change. 
           
          * ``state-reason-message`` - The message for the state change. 
           
          * ``sriov-net-support`` - A value of ``simple`` indicates that enhanced networking with the Intel 82599 VF interface is enabled. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``virtualization-type`` - The virtualization type (``paravirtual`` | ``hvm`` ). 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type ImageIds: list
        :param ImageIds: 
        
          One or more image IDs.
        
          Default: Describes all images available to you.
        
          - *(string) --* 
        
        :type Owners: list
        :param Owners: 
        
          Filters the images by the owner. Specify an AWS account ID, ``self`` (owner is the sender of the request), or an AWS owner alias (valid values are ``amazon`` | ``aws-marketplace`` | ``microsoft`` ). Omitting this option returns all images for which you have launch permissions, regardless of ownership.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class ImageExists(Waiter):
    def wait(self, ExecutableUsers: List = None, Filters: List = None, ImageIds: List = None, Owners: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeImages>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              ExecutableUsers=[
                  \'string\',
              ],
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              ImageIds=[
                  \'string\',
              ],
              Owners=[
                  \'string\',
              ],
              DryRun=True|False,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type ExecutableUsers: list
        :param ExecutableUsers: 
        
          Scopes the images by users with explicit launch permissions. Specify an AWS account ID, ``self`` (the sender of the request), or ``all`` (public AMIs).
        
          - *(string) --* 
        
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``architecture`` - The image architecture (``i386`` | ``x86_64`` ). 
           
          * ``block-device-mapping.delete-on-termination`` - A Boolean value that indicates whether the Amazon EBS volume is deleted on instance termination. 
           
          * ``block-device-mapping.device-name`` - The device name specified in the block device mapping (for example, ``/dev/sdh`` or ``xvdh`` ). 
           
          * ``block-device-mapping.snapshot-id`` - The ID of the snapshot used for the EBS volume. 
           
          * ``block-device-mapping.volume-size`` - The volume size of the EBS volume, in GiB. 
           
          * ``block-device-mapping.volume-type`` - The volume type of the EBS volume (``gp2`` | ``io1`` | ``st1`` | ``sc1`` | ``standard`` ). 
           
          * ``description`` - The description of the image (provided during image creation). 
           
          * ``ena-support`` - A Boolean that indicates whether enhanced networking with ENA is enabled. 
           
          * ``hypervisor`` - The hypervisor type (``ovm`` | ``xen`` ). 
           
          * ``image-id`` - The ID of the image. 
           
          * ``image-type`` - The image type (``machine`` | ``kernel`` | ``ramdisk`` ). 
           
          * ``is-public`` - A Boolean that indicates whether the image is public. 
           
          * ``kernel-id`` - The kernel ID. 
           
          * ``manifest-location`` - The location of the image manifest. 
           
          * ``name`` - The name of the AMI (provided during image creation). 
           
          * ``owner-alias`` - String value from an Amazon-maintained list (``amazon`` | ``aws-marketplace`` | ``microsoft`` ) of snapshot owners. Not to be confused with the user-configured AWS account alias, which is set from the IAM console. 
           
          * ``owner-id`` - The AWS account ID of the image owner. 
           
          * ``platform`` - The platform. To only list Windows-based AMIs, use ``windows`` . 
           
          * ``product-code`` - The product code. 
           
          * ``product-code.type`` - The type of the product code (``devpay`` | ``marketplace`` ). 
           
          * ``ramdisk-id`` - The RAM disk ID. 
           
          * ``root-device-name`` - The device name of the root device volume (for example, ``/dev/sda1`` ). 
           
          * ``root-device-type`` - The type of the root device volume (``ebs`` | ``instance-store`` ). 
           
          * ``state`` - The state of the image (``available`` | ``pending`` | ``failed`` ). 
           
          * ``state-reason-code`` - The reason code for the state change. 
           
          * ``state-reason-message`` - The message for the state change. 
           
          * ``sriov-net-support`` - A value of ``simple`` indicates that enhanced networking with the Intel 82599 VF interface is enabled. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``virtualization-type`` - The virtualization type (``paravirtual`` | ``hvm`` ). 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type ImageIds: list
        :param ImageIds: 
        
          One or more image IDs.
        
          Default: Describes all images available to you.
        
          - *(string) --* 
        
        :type Owners: list
        :param Owners: 
        
          Filters the images by the owner. Specify an AWS account ID, ``self`` (owner is the sender of the request), or an AWS owner alias (valid values are ``amazon`` | ``aws-marketplace`` | ``microsoft`` ). Omitting this option returns all images for which you have launch permissions, regardless of ownership.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class InstanceExists(Waiter):
    def wait(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInstances>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              InstanceIds=[
                  \'string\',
              ],
              DryRun=True|False,
              MaxResults=123,
              NextToken=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``affinity`` - The affinity setting for an instance running on a Dedicated Host (``default`` | ``host`` ). 
           
          * ``architecture`` - The instance architecture (``i386`` | ``x86_64`` ). 
           
          * ``availability-zone`` - The Availability Zone of the instance. 
           
          * ``block-device-mapping.attach-time`` - The attach time for an EBS volume mapped to the instance, for example, ``2010-09-15T17:15:20.000Z`` . 
           
          * ``block-device-mapping.delete-on-termination`` - A Boolean that indicates whether the EBS volume is deleted on instance termination. 
           
          * ``block-device-mapping.device-name`` - The device name specified in the block device mapping (for example, ``/dev/sdh`` or ``xvdh`` ). 
           
          * ``block-device-mapping.status`` - The status for the EBS volume (``attaching`` | ``attached`` | ``detaching`` | ``detached`` ). 
           
          * ``block-device-mapping.volume-id`` - The volume ID of the EBS volume. 
           
          * ``client-token`` - The idempotency token you provided when you launched the instance. 
           
          * ``dns-name`` - The public DNS name of the instance. 
           
          * ``group-id`` - The ID of the security group for the instance. EC2-Classic only. 
           
          * ``group-name`` - The name of the security group for the instance. EC2-Classic only. 
           
          * ``host-id`` - The ID of the Dedicated Host on which the instance is running, if applicable. 
           
          * ``hypervisor`` - The hypervisor type of the instance (``ovm`` | ``xen`` ). 
           
          * ``iam-instance-profile.arn`` - The instance profile associated with the instance. Specified as an ARN. 
           
          * ``image-id`` - The ID of the image used to launch the instance. 
           
          * ``instance-id`` - The ID of the instance. 
           
          * ``instance-lifecycle`` - Indicates whether this is a Spot Instance or a Scheduled Instance (``spot`` | ``scheduled`` ). 
           
          * ``instance-state-code`` - The state of the instance, as a 16-bit unsigned integer. The high byte is used for internal purposes and should be ignored. The low byte is set based on the state represented. The valid values are: 0 (pending), 16 (running), 32 (shutting-down), 48 (terminated), 64 (stopping), and 80 (stopped). 
           
          * ``instance-state-name`` - The state of the instance (``pending`` | ``running`` | ``shutting-down`` | ``terminated`` | ``stopping`` | ``stopped`` ). 
           
          * ``instance-type`` - The type of instance (for example, ``t2.micro`` ). 
           
          * ``instance.group-id`` - The ID of the security group for the instance.  
           
          * ``instance.group-name`` - The name of the security group for the instance.  
           
          * ``ip-address`` - The public IPv4 address of the instance. 
           
          * ``kernel-id`` - The kernel ID. 
           
          * ``key-name`` - The name of the key pair used when the instance was launched. 
           
          * ``launch-index`` - When launching multiple instances, this is the index for the instance in the launch group (for example, 0, 1, 2, and so on).  
           
          * ``launch-time`` - The time when the instance was launched. 
           
          * ``monitoring-state`` - Indicates whether detailed monitoring is enabled (``disabled`` | ``enabled`` ). 
           
          * ``network-interface.addresses.private-ip-address`` - The private IPv4 address associated with the network interface. 
           
          * ``network-interface.addresses.primary`` - Specifies whether the IPv4 address of the network interface is the primary private IPv4 address. 
           
          * ``network-interface.addresses.association.public-ip`` - The ID of the association of an Elastic IP address (IPv4) with a network interface. 
           
          * ``network-interface.addresses.association.ip-owner-id`` - The owner ID of the private IPv4 address associated with the network interface. 
           
          * ``network-interface.association.public-ip`` - The address of the Elastic IP address (IPv4) bound to the network interface. 
           
          * ``network-interface.association.ip-owner-id`` - The owner of the Elastic IP address (IPv4) associated with the network interface. 
           
          * ``network-interface.association.allocation-id`` - The allocation ID returned when you allocated the Elastic IP address (IPv4) for your network interface. 
           
          * ``network-interface.association.association-id`` - The association ID returned when the network interface was associated with an IPv4 address. 
           
          * ``network-interface.attachment.attachment-id`` - The ID of the interface attachment. 
           
          * ``network-interface.attachment.instance-id`` - The ID of the instance to which the network interface is attached. 
           
          * ``network-interface.attachment.instance-owner-id`` - The owner ID of the instance to which the network interface is attached. 
           
          * ``network-interface.attachment.device-index`` - The device index to which the network interface is attached. 
           
          * ``network-interface.attachment.status`` - The status of the attachment (``attaching`` | ``attached`` | ``detaching`` | ``detached`` ). 
           
          * ``network-interface.attachment.attach-time`` - The time that the network interface was attached to an instance. 
           
          * ``network-interface.attachment.delete-on-termination`` - Specifies whether the attachment is deleted when an instance is terminated. 
           
          * ``network-interface.availability-zone`` - The Availability Zone for the network interface. 
           
          * ``network-interface.description`` - The description of the network interface. 
           
          * ``network-interface.group-id`` - The ID of a security group associated with the network interface. 
           
          * ``network-interface.group-name`` - The name of a security group associated with the network interface. 
           
          * ``network-interface.ipv6-addresses.ipv6-address`` - The IPv6 address associated with the network interface. 
           
          * ``network-interface.mac-address`` - The MAC address of the network interface. 
           
          * ``network-interface.network-interface-id`` - The ID of the network interface. 
           
          * ``network-interface.owner-id`` - The ID of the owner of the network interface. 
           
          * ``network-interface.private-dns-name`` - The private DNS name of the network interface. 
           
          * ``network-interface.requester-id`` - The requester ID for the network interface. 
           
          * ``network-interface.requester-managed`` - Indicates whether the network interface is being managed by AWS. 
           
          * ``network-interface.status`` - The status of the network interface (``available`` ) | ``in-use`` ). 
           
          * ``network-interface.source-dest-check`` - Whether the network interface performs source/destination checking. A value of ``true`` means that checking is enabled, and ``false`` means that checking is disabled. The value must be ``false`` for the network interface to perform network address translation (NAT) in your VPC. 
           
          * ``network-interface.subnet-id`` - The ID of the subnet for the network interface. 
           
          * ``network-interface.vpc-id`` - The ID of the VPC for the network interface. 
           
          * ``owner-id`` - The AWS account ID of the instance owner. 
           
          * ``placement-group-name`` - The name of the placement group for the instance. 
           
          * ``platform`` - The platform. Use ``windows`` if you have Windows instances; otherwise, leave blank. 
           
          * ``private-dns-name`` - The private IPv4 DNS name of the instance. 
           
          * ``private-ip-address`` - The private IPv4 address of the instance. 
           
          * ``product-code`` - The product code associated with the AMI used to launch the instance. 
           
          * ``product-code.type`` - The type of product code (``devpay`` | ``marketplace`` ). 
           
          * ``ramdisk-id`` - The RAM disk ID. 
           
          * ``reason`` - The reason for the current state of the instance (for example, shows \"User Initiated [date]\" when you stop or terminate the instance). Similar to the state-reason-code filter. 
           
          * ``requester-id`` - The ID of the entity that launched the instance on your behalf (for example, AWS Management Console, Auto Scaling, and so on). 
           
          * ``reservation-id`` - The ID of the instance\'s reservation. A reservation ID is created any time you launch an instance. A reservation ID has a one-to-one relationship with an instance launch request, but can be associated with more than one instance if you launch multiple instances using the same launch request. For example, if you launch one instance, you get one reservation ID. If you launch ten instances using the same launch request, you also get one reservation ID. 
           
          * ``root-device-name`` - The device name of the root device volume (for example, ``/dev/sda1`` ). 
           
          * ``root-device-type`` - The type of the root device volume (``ebs`` | ``instance-store`` ). 
           
          * ``source-dest-check`` - Indicates whether the instance performs source/destination checking. A value of ``true`` means that checking is enabled, and ``false`` means that checking is disabled. The value must be ``false`` for the instance to perform network address translation (NAT) in your VPC.  
           
          * ``spot-instance-request-id`` - The ID of the Spot Instance request. 
           
          * ``state-reason-code`` - The reason code for the state change. 
           
          * ``state-reason-message`` - A message that describes the state change. 
           
          * ``subnet-id`` - The ID of the subnet for the instance. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources that have a tag with a specific key, regardless of the tag value. 
           
          * ``tenancy`` - The tenancy of an instance (``dedicated`` | ``default`` | ``host`` ). 
           
          * ``virtualization-type`` - The virtualization type of the instance (``paravirtual`` | ``hvm`` ). 
           
          * ``vpc-id`` - The ID of the VPC that the instance is running in. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type InstanceIds: list
        :param InstanceIds: 
        
          One or more instance IDs.
        
          Default: Describes all your instances.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned ``NextToken`` value. This value can be between 5 and 1000. You cannot specify this parameter and the instance IDs parameter in the same call.
        
        :type NextToken: string
        :param NextToken: 
        
          The token to request the next page of results.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 5
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class InstanceRunning(Waiter):
    def wait(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInstances>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              InstanceIds=[
                  \'string\',
              ],
              DryRun=True|False,
              MaxResults=123,
              NextToken=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``affinity`` - The affinity setting for an instance running on a Dedicated Host (``default`` | ``host`` ). 
           
          * ``architecture`` - The instance architecture (``i386`` | ``x86_64`` ). 
           
          * ``availability-zone`` - The Availability Zone of the instance. 
           
          * ``block-device-mapping.attach-time`` - The attach time for an EBS volume mapped to the instance, for example, ``2010-09-15T17:15:20.000Z`` . 
           
          * ``block-device-mapping.delete-on-termination`` - A Boolean that indicates whether the EBS volume is deleted on instance termination. 
           
          * ``block-device-mapping.device-name`` - The device name specified in the block device mapping (for example, ``/dev/sdh`` or ``xvdh`` ). 
           
          * ``block-device-mapping.status`` - The status for the EBS volume (``attaching`` | ``attached`` | ``detaching`` | ``detached`` ). 
           
          * ``block-device-mapping.volume-id`` - The volume ID of the EBS volume. 
           
          * ``client-token`` - The idempotency token you provided when you launched the instance. 
           
          * ``dns-name`` - The public DNS name of the instance. 
           
          * ``group-id`` - The ID of the security group for the instance. EC2-Classic only. 
           
          * ``group-name`` - The name of the security group for the instance. EC2-Classic only. 
           
          * ``host-id`` - The ID of the Dedicated Host on which the instance is running, if applicable. 
           
          * ``hypervisor`` - The hypervisor type of the instance (``ovm`` | ``xen`` ). 
           
          * ``iam-instance-profile.arn`` - The instance profile associated with the instance. Specified as an ARN. 
           
          * ``image-id`` - The ID of the image used to launch the instance. 
           
          * ``instance-id`` - The ID of the instance. 
           
          * ``instance-lifecycle`` - Indicates whether this is a Spot Instance or a Scheduled Instance (``spot`` | ``scheduled`` ). 
           
          * ``instance-state-code`` - The state of the instance, as a 16-bit unsigned integer. The high byte is used for internal purposes and should be ignored. The low byte is set based on the state represented. The valid values are: 0 (pending), 16 (running), 32 (shutting-down), 48 (terminated), 64 (stopping), and 80 (stopped). 
           
          * ``instance-state-name`` - The state of the instance (``pending`` | ``running`` | ``shutting-down`` | ``terminated`` | ``stopping`` | ``stopped`` ). 
           
          * ``instance-type`` - The type of instance (for example, ``t2.micro`` ). 
           
          * ``instance.group-id`` - The ID of the security group for the instance.  
           
          * ``instance.group-name`` - The name of the security group for the instance.  
           
          * ``ip-address`` - The public IPv4 address of the instance. 
           
          * ``kernel-id`` - The kernel ID. 
           
          * ``key-name`` - The name of the key pair used when the instance was launched. 
           
          * ``launch-index`` - When launching multiple instances, this is the index for the instance in the launch group (for example, 0, 1, 2, and so on).  
           
          * ``launch-time`` - The time when the instance was launched. 
           
          * ``monitoring-state`` - Indicates whether detailed monitoring is enabled (``disabled`` | ``enabled`` ). 
           
          * ``network-interface.addresses.private-ip-address`` - The private IPv4 address associated with the network interface. 
           
          * ``network-interface.addresses.primary`` - Specifies whether the IPv4 address of the network interface is the primary private IPv4 address. 
           
          * ``network-interface.addresses.association.public-ip`` - The ID of the association of an Elastic IP address (IPv4) with a network interface. 
           
          * ``network-interface.addresses.association.ip-owner-id`` - The owner ID of the private IPv4 address associated with the network interface. 
           
          * ``network-interface.association.public-ip`` - The address of the Elastic IP address (IPv4) bound to the network interface. 
           
          * ``network-interface.association.ip-owner-id`` - The owner of the Elastic IP address (IPv4) associated with the network interface. 
           
          * ``network-interface.association.allocation-id`` - The allocation ID returned when you allocated the Elastic IP address (IPv4) for your network interface. 
           
          * ``network-interface.association.association-id`` - The association ID returned when the network interface was associated with an IPv4 address. 
           
          * ``network-interface.attachment.attachment-id`` - The ID of the interface attachment. 
           
          * ``network-interface.attachment.instance-id`` - The ID of the instance to which the network interface is attached. 
           
          * ``network-interface.attachment.instance-owner-id`` - The owner ID of the instance to which the network interface is attached. 
           
          * ``network-interface.attachment.device-index`` - The device index to which the network interface is attached. 
           
          * ``network-interface.attachment.status`` - The status of the attachment (``attaching`` | ``attached`` | ``detaching`` | ``detached`` ). 
           
          * ``network-interface.attachment.attach-time`` - The time that the network interface was attached to an instance. 
           
          * ``network-interface.attachment.delete-on-termination`` - Specifies whether the attachment is deleted when an instance is terminated. 
           
          * ``network-interface.availability-zone`` - The Availability Zone for the network interface. 
           
          * ``network-interface.description`` - The description of the network interface. 
           
          * ``network-interface.group-id`` - The ID of a security group associated with the network interface. 
           
          * ``network-interface.group-name`` - The name of a security group associated with the network interface. 
           
          * ``network-interface.ipv6-addresses.ipv6-address`` - The IPv6 address associated with the network interface. 
           
          * ``network-interface.mac-address`` - The MAC address of the network interface. 
           
          * ``network-interface.network-interface-id`` - The ID of the network interface. 
           
          * ``network-interface.owner-id`` - The ID of the owner of the network interface. 
           
          * ``network-interface.private-dns-name`` - The private DNS name of the network interface. 
           
          * ``network-interface.requester-id`` - The requester ID for the network interface. 
           
          * ``network-interface.requester-managed`` - Indicates whether the network interface is being managed by AWS. 
           
          * ``network-interface.status`` - The status of the network interface (``available`` ) | ``in-use`` ). 
           
          * ``network-interface.source-dest-check`` - Whether the network interface performs source/destination checking. A value of ``true`` means that checking is enabled, and ``false`` means that checking is disabled. The value must be ``false`` for the network interface to perform network address translation (NAT) in your VPC. 
           
          * ``network-interface.subnet-id`` - The ID of the subnet for the network interface. 
           
          * ``network-interface.vpc-id`` - The ID of the VPC for the network interface. 
           
          * ``owner-id`` - The AWS account ID of the instance owner. 
           
          * ``placement-group-name`` - The name of the placement group for the instance. 
           
          * ``platform`` - The platform. Use ``windows`` if you have Windows instances; otherwise, leave blank. 
           
          * ``private-dns-name`` - The private IPv4 DNS name of the instance. 
           
          * ``private-ip-address`` - The private IPv4 address of the instance. 
           
          * ``product-code`` - The product code associated with the AMI used to launch the instance. 
           
          * ``product-code.type`` - The type of product code (``devpay`` | ``marketplace`` ). 
           
          * ``ramdisk-id`` - The RAM disk ID. 
           
          * ``reason`` - The reason for the current state of the instance (for example, shows \"User Initiated [date]\" when you stop or terminate the instance). Similar to the state-reason-code filter. 
           
          * ``requester-id`` - The ID of the entity that launched the instance on your behalf (for example, AWS Management Console, Auto Scaling, and so on). 
           
          * ``reservation-id`` - The ID of the instance\'s reservation. A reservation ID is created any time you launch an instance. A reservation ID has a one-to-one relationship with an instance launch request, but can be associated with more than one instance if you launch multiple instances using the same launch request. For example, if you launch one instance, you get one reservation ID. If you launch ten instances using the same launch request, you also get one reservation ID. 
           
          * ``root-device-name`` - The device name of the root device volume (for example, ``/dev/sda1`` ). 
           
          * ``root-device-type`` - The type of the root device volume (``ebs`` | ``instance-store`` ). 
           
          * ``source-dest-check`` - Indicates whether the instance performs source/destination checking. A value of ``true`` means that checking is enabled, and ``false`` means that checking is disabled. The value must be ``false`` for the instance to perform network address translation (NAT) in your VPC.  
           
          * ``spot-instance-request-id`` - The ID of the Spot Instance request. 
           
          * ``state-reason-code`` - The reason code for the state change. 
           
          * ``state-reason-message`` - A message that describes the state change. 
           
          * ``subnet-id`` - The ID of the subnet for the instance. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources that have a tag with a specific key, regardless of the tag value. 
           
          * ``tenancy`` - The tenancy of an instance (``dedicated`` | ``default`` | ``host`` ). 
           
          * ``virtualization-type`` - The virtualization type of the instance (``paravirtual`` | ``hvm`` ). 
           
          * ``vpc-id`` - The ID of the VPC that the instance is running in. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type InstanceIds: list
        :param InstanceIds: 
        
          One or more instance IDs.
        
          Default: Describes all your instances.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned ``NextToken`` value. This value can be between 5 and 1000. You cannot specify this parameter and the instance IDs parameter in the same call.
        
        :type NextToken: string
        :param NextToken: 
        
          The token to request the next page of results.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class InstanceStatusOk(Waiter):
    def wait(self, Filters: List = None, InstanceIds: List = None, MaxResults: int = None, NextToken: str = None, DryRun: bool = None, IncludeAllInstances: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInstanceStatus>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              InstanceIds=[
                  \'string\',
              ],
              MaxResults=123,
              NextToken=\'string\',
              DryRun=True|False,
              IncludeAllInstances=True|False,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``availability-zone`` - The Availability Zone of the instance. 
           
          * ``event.code`` - The code for the scheduled event (``instance-reboot`` | ``system-reboot`` | ``system-maintenance`` | ``instance-retirement`` | ``instance-stop`` ). 
           
          * ``event.description`` - A description of the event. 
           
          * ``event.not-after`` - The latest end time for the scheduled event (for example, ``2014-09-15T17:15:20.000Z`` ). 
           
          * ``event.not-before`` - The earliest start time for the scheduled event (for example, ``2014-09-15T17:15:20.000Z`` ). 
           
          * ``instance-state-code`` - The code for the instance state, as a 16-bit unsigned integer. The high byte is used for internal purposes and should be ignored. The low byte is set based on the state represented. The valid values are 0 (pending), 16 (running), 32 (shutting-down), 48 (terminated), 64 (stopping), and 80 (stopped). 
           
          * ``instance-state-name`` - The state of the instance (``pending`` | ``running`` | ``shutting-down`` | ``terminated`` | ``stopping`` | ``stopped`` ). 
           
          * ``instance-status.reachability`` - Filters on instance status where the name is ``reachability`` (``passed`` | ``failed`` | ``initializing`` | ``insufficient-data`` ). 
           
          * ``instance-status.status`` - The status of the instance (``ok`` | ``impaired`` | ``initializing`` | ``insufficient-data`` | ``not-applicable`` ). 
           
          * ``system-status.reachability`` - Filters on system status where the name is ``reachability`` (``passed`` | ``failed`` | ``initializing`` | ``insufficient-data`` ). 
           
          * ``system-status.status`` - The system status of the instance (``ok`` | ``impaired`` | ``initializing`` | ``insufficient-data`` | ``not-applicable`` ). 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type InstanceIds: list
        :param InstanceIds: 
        
          One or more instance IDs.
        
          Default: Describes all your instances.
        
          Constraints: Maximum 100 explicitly specified instance IDs.
        
          - *(string) --* 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned ``NextToken`` value. This value can be between 5 and 1000. You cannot specify this parameter and the instance IDs parameter in the same call.
        
        :type NextToken: string
        :param NextToken: 
        
          The token to retrieve the next page of results.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type IncludeAllInstances: boolean
        :param IncludeAllInstances: 
        
          When ``true`` , includes the health status for all instances. When ``false`` , includes the health status for running instances only.
        
          Default: ``false``  
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class InstanceStopped(Waiter):
    def wait(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInstances>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              InstanceIds=[
                  \'string\',
              ],
              DryRun=True|False,
              MaxResults=123,
              NextToken=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``affinity`` - The affinity setting for an instance running on a Dedicated Host (``default`` | ``host`` ). 
           
          * ``architecture`` - The instance architecture (``i386`` | ``x86_64`` ). 
           
          * ``availability-zone`` - The Availability Zone of the instance. 
           
          * ``block-device-mapping.attach-time`` - The attach time for an EBS volume mapped to the instance, for example, ``2010-09-15T17:15:20.000Z`` . 
           
          * ``block-device-mapping.delete-on-termination`` - A Boolean that indicates whether the EBS volume is deleted on instance termination. 
           
          * ``block-device-mapping.device-name`` - The device name specified in the block device mapping (for example, ``/dev/sdh`` or ``xvdh`` ). 
           
          * ``block-device-mapping.status`` - The status for the EBS volume (``attaching`` | ``attached`` | ``detaching`` | ``detached`` ). 
           
          * ``block-device-mapping.volume-id`` - The volume ID of the EBS volume. 
           
          * ``client-token`` - The idempotency token you provided when you launched the instance. 
           
          * ``dns-name`` - The public DNS name of the instance. 
           
          * ``group-id`` - The ID of the security group for the instance. EC2-Classic only. 
           
          * ``group-name`` - The name of the security group for the instance. EC2-Classic only. 
           
          * ``host-id`` - The ID of the Dedicated Host on which the instance is running, if applicable. 
           
          * ``hypervisor`` - The hypervisor type of the instance (``ovm`` | ``xen`` ). 
           
          * ``iam-instance-profile.arn`` - The instance profile associated with the instance. Specified as an ARN. 
           
          * ``image-id`` - The ID of the image used to launch the instance. 
           
          * ``instance-id`` - The ID of the instance. 
           
          * ``instance-lifecycle`` - Indicates whether this is a Spot Instance or a Scheduled Instance (``spot`` | ``scheduled`` ). 
           
          * ``instance-state-code`` - The state of the instance, as a 16-bit unsigned integer. The high byte is used for internal purposes and should be ignored. The low byte is set based on the state represented. The valid values are: 0 (pending), 16 (running), 32 (shutting-down), 48 (terminated), 64 (stopping), and 80 (stopped). 
           
          * ``instance-state-name`` - The state of the instance (``pending`` | ``running`` | ``shutting-down`` | ``terminated`` | ``stopping`` | ``stopped`` ). 
           
          * ``instance-type`` - The type of instance (for example, ``t2.micro`` ). 
           
          * ``instance.group-id`` - The ID of the security group for the instance.  
           
          * ``instance.group-name`` - The name of the security group for the instance.  
           
          * ``ip-address`` - The public IPv4 address of the instance. 
           
          * ``kernel-id`` - The kernel ID. 
           
          * ``key-name`` - The name of the key pair used when the instance was launched. 
           
          * ``launch-index`` - When launching multiple instances, this is the index for the instance in the launch group (for example, 0, 1, 2, and so on).  
           
          * ``launch-time`` - The time when the instance was launched. 
           
          * ``monitoring-state`` - Indicates whether detailed monitoring is enabled (``disabled`` | ``enabled`` ). 
           
          * ``network-interface.addresses.private-ip-address`` - The private IPv4 address associated with the network interface. 
           
          * ``network-interface.addresses.primary`` - Specifies whether the IPv4 address of the network interface is the primary private IPv4 address. 
           
          * ``network-interface.addresses.association.public-ip`` - The ID of the association of an Elastic IP address (IPv4) with a network interface. 
           
          * ``network-interface.addresses.association.ip-owner-id`` - The owner ID of the private IPv4 address associated with the network interface. 
           
          * ``network-interface.association.public-ip`` - The address of the Elastic IP address (IPv4) bound to the network interface. 
           
          * ``network-interface.association.ip-owner-id`` - The owner of the Elastic IP address (IPv4) associated with the network interface. 
           
          * ``network-interface.association.allocation-id`` - The allocation ID returned when you allocated the Elastic IP address (IPv4) for your network interface. 
           
          * ``network-interface.association.association-id`` - The association ID returned when the network interface was associated with an IPv4 address. 
           
          * ``network-interface.attachment.attachment-id`` - The ID of the interface attachment. 
           
          * ``network-interface.attachment.instance-id`` - The ID of the instance to which the network interface is attached. 
           
          * ``network-interface.attachment.instance-owner-id`` - The owner ID of the instance to which the network interface is attached. 
           
          * ``network-interface.attachment.device-index`` - The device index to which the network interface is attached. 
           
          * ``network-interface.attachment.status`` - The status of the attachment (``attaching`` | ``attached`` | ``detaching`` | ``detached`` ). 
           
          * ``network-interface.attachment.attach-time`` - The time that the network interface was attached to an instance. 
           
          * ``network-interface.attachment.delete-on-termination`` - Specifies whether the attachment is deleted when an instance is terminated. 
           
          * ``network-interface.availability-zone`` - The Availability Zone for the network interface. 
           
          * ``network-interface.description`` - The description of the network interface. 
           
          * ``network-interface.group-id`` - The ID of a security group associated with the network interface. 
           
          * ``network-interface.group-name`` - The name of a security group associated with the network interface. 
           
          * ``network-interface.ipv6-addresses.ipv6-address`` - The IPv6 address associated with the network interface. 
           
          * ``network-interface.mac-address`` - The MAC address of the network interface. 
           
          * ``network-interface.network-interface-id`` - The ID of the network interface. 
           
          * ``network-interface.owner-id`` - The ID of the owner of the network interface. 
           
          * ``network-interface.private-dns-name`` - The private DNS name of the network interface. 
           
          * ``network-interface.requester-id`` - The requester ID for the network interface. 
           
          * ``network-interface.requester-managed`` - Indicates whether the network interface is being managed by AWS. 
           
          * ``network-interface.status`` - The status of the network interface (``available`` ) | ``in-use`` ). 
           
          * ``network-interface.source-dest-check`` - Whether the network interface performs source/destination checking. A value of ``true`` means that checking is enabled, and ``false`` means that checking is disabled. The value must be ``false`` for the network interface to perform network address translation (NAT) in your VPC. 
           
          * ``network-interface.subnet-id`` - The ID of the subnet for the network interface. 
           
          * ``network-interface.vpc-id`` - The ID of the VPC for the network interface. 
           
          * ``owner-id`` - The AWS account ID of the instance owner. 
           
          * ``placement-group-name`` - The name of the placement group for the instance. 
           
          * ``platform`` - The platform. Use ``windows`` if you have Windows instances; otherwise, leave blank. 
           
          * ``private-dns-name`` - The private IPv4 DNS name of the instance. 
           
          * ``private-ip-address`` - The private IPv4 address of the instance. 
           
          * ``product-code`` - The product code associated with the AMI used to launch the instance. 
           
          * ``product-code.type`` - The type of product code (``devpay`` | ``marketplace`` ). 
           
          * ``ramdisk-id`` - The RAM disk ID. 
           
          * ``reason`` - The reason for the current state of the instance (for example, shows \"User Initiated [date]\" when you stop or terminate the instance). Similar to the state-reason-code filter. 
           
          * ``requester-id`` - The ID of the entity that launched the instance on your behalf (for example, AWS Management Console, Auto Scaling, and so on). 
           
          * ``reservation-id`` - The ID of the instance\'s reservation. A reservation ID is created any time you launch an instance. A reservation ID has a one-to-one relationship with an instance launch request, but can be associated with more than one instance if you launch multiple instances using the same launch request. For example, if you launch one instance, you get one reservation ID. If you launch ten instances using the same launch request, you also get one reservation ID. 
           
          * ``root-device-name`` - The device name of the root device volume (for example, ``/dev/sda1`` ). 
           
          * ``root-device-type`` - The type of the root device volume (``ebs`` | ``instance-store`` ). 
           
          * ``source-dest-check`` - Indicates whether the instance performs source/destination checking. A value of ``true`` means that checking is enabled, and ``false`` means that checking is disabled. The value must be ``false`` for the instance to perform network address translation (NAT) in your VPC.  
           
          * ``spot-instance-request-id`` - The ID of the Spot Instance request. 
           
          * ``state-reason-code`` - The reason code for the state change. 
           
          * ``state-reason-message`` - A message that describes the state change. 
           
          * ``subnet-id`` - The ID of the subnet for the instance. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources that have a tag with a specific key, regardless of the tag value. 
           
          * ``tenancy`` - The tenancy of an instance (``dedicated`` | ``default`` | ``host`` ). 
           
          * ``virtualization-type`` - The virtualization type of the instance (``paravirtual`` | ``hvm`` ). 
           
          * ``vpc-id`` - The ID of the VPC that the instance is running in. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type InstanceIds: list
        :param InstanceIds: 
        
          One or more instance IDs.
        
          Default: Describes all your instances.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned ``NextToken`` value. This value can be between 5 and 1000. You cannot specify this parameter and the instance IDs parameter in the same call.
        
        :type NextToken: string
        :param NextToken: 
        
          The token to request the next page of results.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class InstanceTerminated(Waiter):
    def wait(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInstances>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              InstanceIds=[
                  \'string\',
              ],
              DryRun=True|False,
              MaxResults=123,
              NextToken=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``affinity`` - The affinity setting for an instance running on a Dedicated Host (``default`` | ``host`` ). 
           
          * ``architecture`` - The instance architecture (``i386`` | ``x86_64`` ). 
           
          * ``availability-zone`` - The Availability Zone of the instance. 
           
          * ``block-device-mapping.attach-time`` - The attach time for an EBS volume mapped to the instance, for example, ``2010-09-15T17:15:20.000Z`` . 
           
          * ``block-device-mapping.delete-on-termination`` - A Boolean that indicates whether the EBS volume is deleted on instance termination. 
           
          * ``block-device-mapping.device-name`` - The device name specified in the block device mapping (for example, ``/dev/sdh`` or ``xvdh`` ). 
           
          * ``block-device-mapping.status`` - The status for the EBS volume (``attaching`` | ``attached`` | ``detaching`` | ``detached`` ). 
           
          * ``block-device-mapping.volume-id`` - The volume ID of the EBS volume. 
           
          * ``client-token`` - The idempotency token you provided when you launched the instance. 
           
          * ``dns-name`` - The public DNS name of the instance. 
           
          * ``group-id`` - The ID of the security group for the instance. EC2-Classic only. 
           
          * ``group-name`` - The name of the security group for the instance. EC2-Classic only. 
           
          * ``host-id`` - The ID of the Dedicated Host on which the instance is running, if applicable. 
           
          * ``hypervisor`` - The hypervisor type of the instance (``ovm`` | ``xen`` ). 
           
          * ``iam-instance-profile.arn`` - The instance profile associated with the instance. Specified as an ARN. 
           
          * ``image-id`` - The ID of the image used to launch the instance. 
           
          * ``instance-id`` - The ID of the instance. 
           
          * ``instance-lifecycle`` - Indicates whether this is a Spot Instance or a Scheduled Instance (``spot`` | ``scheduled`` ). 
           
          * ``instance-state-code`` - The state of the instance, as a 16-bit unsigned integer. The high byte is used for internal purposes and should be ignored. The low byte is set based on the state represented. The valid values are: 0 (pending), 16 (running), 32 (shutting-down), 48 (terminated), 64 (stopping), and 80 (stopped). 
           
          * ``instance-state-name`` - The state of the instance (``pending`` | ``running`` | ``shutting-down`` | ``terminated`` | ``stopping`` | ``stopped`` ). 
           
          * ``instance-type`` - The type of instance (for example, ``t2.micro`` ). 
           
          * ``instance.group-id`` - The ID of the security group for the instance.  
           
          * ``instance.group-name`` - The name of the security group for the instance.  
           
          * ``ip-address`` - The public IPv4 address of the instance. 
           
          * ``kernel-id`` - The kernel ID. 
           
          * ``key-name`` - The name of the key pair used when the instance was launched. 
           
          * ``launch-index`` - When launching multiple instances, this is the index for the instance in the launch group (for example, 0, 1, 2, and so on).  
           
          * ``launch-time`` - The time when the instance was launched. 
           
          * ``monitoring-state`` - Indicates whether detailed monitoring is enabled (``disabled`` | ``enabled`` ). 
           
          * ``network-interface.addresses.private-ip-address`` - The private IPv4 address associated with the network interface. 
           
          * ``network-interface.addresses.primary`` - Specifies whether the IPv4 address of the network interface is the primary private IPv4 address. 
           
          * ``network-interface.addresses.association.public-ip`` - The ID of the association of an Elastic IP address (IPv4) with a network interface. 
           
          * ``network-interface.addresses.association.ip-owner-id`` - The owner ID of the private IPv4 address associated with the network interface. 
           
          * ``network-interface.association.public-ip`` - The address of the Elastic IP address (IPv4) bound to the network interface. 
           
          * ``network-interface.association.ip-owner-id`` - The owner of the Elastic IP address (IPv4) associated with the network interface. 
           
          * ``network-interface.association.allocation-id`` - The allocation ID returned when you allocated the Elastic IP address (IPv4) for your network interface. 
           
          * ``network-interface.association.association-id`` - The association ID returned when the network interface was associated with an IPv4 address. 
           
          * ``network-interface.attachment.attachment-id`` - The ID of the interface attachment. 
           
          * ``network-interface.attachment.instance-id`` - The ID of the instance to which the network interface is attached. 
           
          * ``network-interface.attachment.instance-owner-id`` - The owner ID of the instance to which the network interface is attached. 
           
          * ``network-interface.attachment.device-index`` - The device index to which the network interface is attached. 
           
          * ``network-interface.attachment.status`` - The status of the attachment (``attaching`` | ``attached`` | ``detaching`` | ``detached`` ). 
           
          * ``network-interface.attachment.attach-time`` - The time that the network interface was attached to an instance. 
           
          * ``network-interface.attachment.delete-on-termination`` - Specifies whether the attachment is deleted when an instance is terminated. 
           
          * ``network-interface.availability-zone`` - The Availability Zone for the network interface. 
           
          * ``network-interface.description`` - The description of the network interface. 
           
          * ``network-interface.group-id`` - The ID of a security group associated with the network interface. 
           
          * ``network-interface.group-name`` - The name of a security group associated with the network interface. 
           
          * ``network-interface.ipv6-addresses.ipv6-address`` - The IPv6 address associated with the network interface. 
           
          * ``network-interface.mac-address`` - The MAC address of the network interface. 
           
          * ``network-interface.network-interface-id`` - The ID of the network interface. 
           
          * ``network-interface.owner-id`` - The ID of the owner of the network interface. 
           
          * ``network-interface.private-dns-name`` - The private DNS name of the network interface. 
           
          * ``network-interface.requester-id`` - The requester ID for the network interface. 
           
          * ``network-interface.requester-managed`` - Indicates whether the network interface is being managed by AWS. 
           
          * ``network-interface.status`` - The status of the network interface (``available`` ) | ``in-use`` ). 
           
          * ``network-interface.source-dest-check`` - Whether the network interface performs source/destination checking. A value of ``true`` means that checking is enabled, and ``false`` means that checking is disabled. The value must be ``false`` for the network interface to perform network address translation (NAT) in your VPC. 
           
          * ``network-interface.subnet-id`` - The ID of the subnet for the network interface. 
           
          * ``network-interface.vpc-id`` - The ID of the VPC for the network interface. 
           
          * ``owner-id`` - The AWS account ID of the instance owner. 
           
          * ``placement-group-name`` - The name of the placement group for the instance. 
           
          * ``platform`` - The platform. Use ``windows`` if you have Windows instances; otherwise, leave blank. 
           
          * ``private-dns-name`` - The private IPv4 DNS name of the instance. 
           
          * ``private-ip-address`` - The private IPv4 address of the instance. 
           
          * ``product-code`` - The product code associated with the AMI used to launch the instance. 
           
          * ``product-code.type`` - The type of product code (``devpay`` | ``marketplace`` ). 
           
          * ``ramdisk-id`` - The RAM disk ID. 
           
          * ``reason`` - The reason for the current state of the instance (for example, shows \"User Initiated [date]\" when you stop or terminate the instance). Similar to the state-reason-code filter. 
           
          * ``requester-id`` - The ID of the entity that launched the instance on your behalf (for example, AWS Management Console, Auto Scaling, and so on). 
           
          * ``reservation-id`` - The ID of the instance\'s reservation. A reservation ID is created any time you launch an instance. A reservation ID has a one-to-one relationship with an instance launch request, but can be associated with more than one instance if you launch multiple instances using the same launch request. For example, if you launch one instance, you get one reservation ID. If you launch ten instances using the same launch request, you also get one reservation ID. 
           
          * ``root-device-name`` - The device name of the root device volume (for example, ``/dev/sda1`` ). 
           
          * ``root-device-type`` - The type of the root device volume (``ebs`` | ``instance-store`` ). 
           
          * ``source-dest-check`` - Indicates whether the instance performs source/destination checking. A value of ``true`` means that checking is enabled, and ``false`` means that checking is disabled. The value must be ``false`` for the instance to perform network address translation (NAT) in your VPC.  
           
          * ``spot-instance-request-id`` - The ID of the Spot Instance request. 
           
          * ``state-reason-code`` - The reason code for the state change. 
           
          * ``state-reason-message`` - A message that describes the state change. 
           
          * ``subnet-id`` - The ID of the subnet for the instance. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources that have a tag with a specific key, regardless of the tag value. 
           
          * ``tenancy`` - The tenancy of an instance (``dedicated`` | ``default`` | ``host`` ). 
           
          * ``virtualization-type`` - The virtualization type of the instance (``paravirtual`` | ``hvm`` ). 
           
          * ``vpc-id`` - The ID of the VPC that the instance is running in. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type InstanceIds: list
        :param InstanceIds: 
        
          One or more instance IDs.
        
          Default: Describes all your instances.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned ``NextToken`` value. This value can be between 5 and 1000. You cannot specify this parameter and the instance IDs parameter in the same call.
        
        :type NextToken: string
        :param NextToken: 
        
          The token to request the next page of results.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class KeyPairExists(Waiter):
    def wait(self, Filters: List = None, KeyNames: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeKeyPairs>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              KeyNames=[
                  \'string\',
              ],
              DryRun=True|False,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``fingerprint`` - The fingerprint of the key pair. 
           
          * ``key-name`` - The name of the key pair. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type KeyNames: list
        :param KeyNames: 
        
          One or more key pair names.
        
          Default: Describes all your key pairs.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 5
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 6
        
        :returns: None
        """
        pass


class NatGatewayAvailable(Waiter):
    def wait(self, Filters: List = None, MaxResults: int = None, NatGatewayIds: List = None, NextToken: str = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeNatGateways>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxResults=123,
              NatGatewayIds=[
                  \'string\',
              ],
              NextToken=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``nat-gateway-id`` - The ID of the NAT gateway. 
           
          * ``state`` - The state of the NAT gateway (``pending`` | ``failed`` | ``available`` | ``deleting`` | ``deleted`` ). 
           
          * ``subnet-id`` - The ID of the subnet in which the NAT gateway resides. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``vpc-id`` - The ID of the VPC in which the NAT gateway resides. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results.
        
          Constraint: If the value specified is greater than 1000, we return only 1000 items.
        
        :type NatGatewayIds: list
        :param NatGatewayIds: 
        
          One or more NAT gateway IDs.
        
          - *(string) --* 
        
        :type NextToken: string
        :param NextToken: 
        
          The token to retrieve the next page of results.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class NetworkInterfaceAvailable(Waiter):
    def wait(self, Filters: List = None, DryRun: bool = None, NetworkInterfaceIds: List = None, NextToken: str = None, MaxResults: int = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeNetworkInterfaces>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              DryRun=True|False,
              NetworkInterfaceIds=[
                  \'string\',
              ],
              NextToken=\'string\',
              MaxResults=123,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``addresses.private-ip-address`` - The private IPv4 addresses associated with the network interface. 
           
          * ``addresses.primary`` - Whether the private IPv4 address is the primary IP address associated with the network interface.  
           
          * ``addresses.association.public-ip`` - The association ID returned when the network interface was associated with the Elastic IP address (IPv4). 
           
          * ``addresses.association.owner-id`` - The owner ID of the addresses associated with the network interface. 
           
          * ``association.association-id`` - The association ID returned when the network interface was associated with an IPv4 address. 
           
          * ``association.allocation-id`` - The allocation ID returned when you allocated the Elastic IP address (IPv4) for your network interface. 
           
          * ``association.ip-owner-id`` - The owner of the Elastic IP address (IPv4) associated with the network interface. 
           
          * ``association.public-ip`` - The address of the Elastic IP address (IPv4) bound to the network interface. 
           
          * ``association.public-dns-name`` - The public DNS name for the network interface (IPv4). 
           
          * ``attachment.attachment-id`` - The ID of the interface attachment. 
           
          * ``attachment.attach.time`` - The time that the network interface was attached to an instance. 
           
          * ``attachment.delete-on-termination`` - Indicates whether the attachment is deleted when an instance is terminated. 
           
          * ``attachment.device-index`` - The device index to which the network interface is attached. 
           
          * ``attachment.instance-id`` - The ID of the instance to which the network interface is attached. 
           
          * ``attachment.instance-owner-id`` - The owner ID of the instance to which the network interface is attached. 
           
          * ``attachment.nat-gateway-id`` - The ID of the NAT gateway to which the network interface is attached. 
           
          * ``attachment.status`` - The status of the attachment (``attaching`` | ``attached`` | ``detaching`` | ``detached`` ). 
           
          * ``availability-zone`` - The Availability Zone of the network interface. 
           
          * ``description`` - The description of the network interface. 
           
          * ``group-id`` - The ID of a security group associated with the network interface. 
           
          * ``group-name`` - The name of a security group associated with the network interface. 
           
          * ``ipv6-addresses.ipv6-address`` - An IPv6 address associated with the network interface. 
           
          * ``mac-address`` - The MAC address of the network interface. 
           
          * ``network-interface-id`` - The ID of the network interface. 
           
          * ``owner-id`` - The AWS account ID of the network interface owner. 
           
          * ``private-ip-address`` - The private IPv4 address or addresses of the network interface. 
           
          * ``private-dns-name`` - The private DNS name of the network interface (IPv4). 
           
          * ``requester-id`` - The ID of the entity that launched the instance on your behalf (for example, AWS Management Console, Auto Scaling, and so on). 
           
          * ``requester-managed`` - Indicates whether the network interface is being managed by an AWS service (for example, AWS Management Console, Auto Scaling, and so on). 
           
          * ``source-desk-check`` - Indicates whether the network interface performs source/destination checking. A value of ``true`` means checking is enabled, and ``false`` means checking is disabled. The value must be ``false`` for the network interface to perform network address translation (NAT) in your VPC.  
           
          * ``status`` - The status of the network interface. If the network interface is not attached to an instance, the status is ``available`` ; if a network interface is attached to an instance the status is ``in-use`` . 
           
          * ``subnet-id`` - The ID of the subnet for the network interface. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``vpc-id`` - The ID of the VPC for the network interface. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type NetworkInterfaceIds: list
        :param NetworkInterfaceIds: 
        
          One or more network interface IDs.
        
          Default: Describes all your network interfaces.
        
          - *(string) --* 
        
        :type NextToken: string
        :param NextToken: 
        
          The token to retrieve the next page of results.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 20
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 10
        
        :returns: None
        """
        pass


class PasswordDataAvailable(Waiter):
    def wait(self, InstanceId: str, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/GetPasswordData>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              InstanceId=\'string\',
              DryRun=True|False,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]** 
        
          The ID of the Windows instance.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class SnapshotCompleted(Waiter):
    def wait(self, Filters: List = None, MaxResults: int = None, NextToken: str = None, OwnerIds: List = None, RestorableByUserIds: List = None, SnapshotIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSnapshots>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              MaxResults=123,
              NextToken=\'string\',
              OwnerIds=[
                  \'string\',
              ],
              RestorableByUserIds=[
                  \'string\',
              ],
              SnapshotIds=[
                  \'string\',
              ],
              DryRun=True|False,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``description`` - A description of the snapshot. 
           
          * ``owner-alias`` - Value from an Amazon-maintained list (``amazon`` | ``aws-marketplace`` | ``microsoft`` ) of snapshot owners. Not to be confused with the user-configured AWS account alias, which is set from the IAM console. 
           
          * ``owner-id`` - The ID of the AWS account that owns the snapshot. 
           
          * ``progress`` - The progress of the snapshot, as a percentage (for example, 80%). 
           
          * ``snapshot-id`` - The snapshot ID. 
           
          * ``start-time`` - The time stamp when the snapshot was initiated. 
           
          * ``status`` - The status of the snapshot (``pending`` | ``completed`` | ``error`` ). 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``volume-id`` - The ID of the volume the snapshot is for. 
           
          * ``volume-size`` - The size of the volume, in GiB. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of snapshot results returned by ``DescribeSnapshots`` in paginated output. When this parameter is used, ``DescribeSnapshots`` only returns ``MaxResults`` results in a single page along with a ``NextToken`` response element. The remaining results of the initial request can be seen by sending another ``DescribeSnapshots`` request with the returned ``NextToken`` value. This value can be between 5 and 1000; if ``MaxResults`` is given a value larger than 1000, only 1000 results are returned. If this parameter is not used, then ``DescribeSnapshots`` returns all results. You cannot specify this parameter and the snapshot IDs parameter in the same request.
        
        :type NextToken: string
        :param NextToken: 
        
          The ``NextToken`` value returned from a previous paginated ``DescribeSnapshots`` request where ``MaxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``NextToken`` value. This value is ``null`` when there are no more results to return.
        
        :type OwnerIds: list
        :param OwnerIds: 
        
          Returns the snapshots owned by the specified owner. Multiple owners can be specified.
        
          - *(string) --* 
        
        :type RestorableByUserIds: list
        :param RestorableByUserIds: 
        
          One or more AWS accounts IDs that can create volumes from the snapshot.
        
          - *(string) --* 
        
        :type SnapshotIds: list
        :param SnapshotIds: 
        
          One or more snapshot IDs.
        
          Default: Describes snapshots for which you have launch permissions.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class SpotInstanceRequestFulfilled(Waiter):
    def wait(self, Filters: List = None, DryRun: bool = None, SpotInstanceRequestIds: List = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSpotInstanceRequests>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              DryRun=True|False,
              SpotInstanceRequestIds=[
                  \'string\',
              ],
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``availability-zone-group`` - The Availability Zone group. 
           
          * ``create-time`` - The time stamp when the Spot Instance request was created. 
           
          * ``fault-code`` - The fault code related to the request. 
           
          * ``fault-message`` - The fault message related to the request. 
           
          * ``instance-id`` - The ID of the instance that fulfilled the request. 
           
          * ``launch-group`` - The Spot Instance launch group. 
           
          * ``launch.block-device-mapping.delete-on-termination`` - Indicates whether the EBS volume is deleted on instance termination. 
           
          * ``launch.block-device-mapping.device-name`` - The device name for the volume in the block device mapping (for example, ``/dev/sdh`` or ``xvdh`` ). 
           
          * ``launch.block-device-mapping.snapshot-id`` - The ID of the snapshot for the EBS volume. 
           
          * ``launch.block-device-mapping.volume-size`` - The size of the EBS volume, in GiB. 
           
          * ``launch.block-device-mapping.volume-type`` - The type of EBS volume: ``gp2`` for General Purpose SSD, ``io1`` for Provisioned IOPS SSD, ``st1`` for Throughput Optimized HDD, ``sc1`` for Cold HDD, or ``standard`` for Magnetic. 
           
          * ``launch.group-id`` - The ID of the security group for the instance. 
           
          * ``launch.group-name`` - The name of the security group for the instance. 
           
          * ``launch.image-id`` - The ID of the AMI. 
           
          * ``launch.instance-type`` - The type of instance (for example, ``m3.medium`` ). 
           
          * ``launch.kernel-id`` - The kernel ID. 
           
          * ``launch.key-name`` - The name of the key pair the instance launched with. 
           
          * ``launch.monitoring-enabled`` - Whether detailed monitoring is enabled for the Spot Instance. 
           
          * ``launch.ramdisk-id`` - The RAM disk ID. 
           
          * ``launched-availability-zone`` - The Availability Zone in which the request is launched. 
           
          * ``network-interface.addresses.primary`` - Indicates whether the IP address is the primary private IP address. 
           
          * ``network-interface.delete-on-termination`` - Indicates whether the network interface is deleted when the instance is terminated. 
           
          * ``network-interface.description`` - A description of the network interface. 
           
          * ``network-interface.device-index`` - The index of the device for the network interface attachment on the instance. 
           
          * ``network-interface.group-id`` - The ID of the security group associated with the network interface. 
           
          * ``network-interface.network-interface-id`` - The ID of the network interface. 
           
          * ``network-interface.private-ip-address`` - The primary private IP address of the network interface. 
           
          * ``network-interface.subnet-id`` - The ID of the subnet for the instance. 
           
          * ``product-description`` - The product description associated with the instance (``Linux/UNIX`` | ``Windows`` ). 
           
          * ``spot-instance-request-id`` - The Spot Instance request ID. 
           
          * ``spot-price`` - The maximum hourly price for any Spot Instance launched to fulfill the request. 
           
          * ``state`` - The state of the Spot Instance request (``open`` | ``active`` | ``closed`` | ``cancelled`` | ``failed`` ). Spot request status information can help you track your Amazon EC2 Spot Instance requests. For more information, see `Spot Request Status <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-bid-status.html>`__ in the *Amazon EC2 User Guide for Linux Instances* . 
           
          * ``status-code`` - The short code describing the most recent evaluation of your Spot Instance request. 
           
          * ``status-message`` - The message explaining the status of the Spot Instance request. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``type`` - The type of Spot Instance request (``one-time`` | ``persistent`` ). 
           
          * ``valid-from`` - The start date of the request. 
           
          * ``valid-until`` - The end date of the request. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type SpotInstanceRequestIds: list
        :param SpotInstanceRequestIds: 
        
          One or more Spot Instance request IDs.
        
          - *(string) --* 
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class SubnetAvailable(Waiter):
    def wait(self, Filters: List = None, SubnetIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeSubnets>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              SubnetIds=[
                  \'string\',
              ],
              DryRun=True|False,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``availabilityZone`` - The Availability Zone for the subnet. You can also use ``availability-zone`` as the filter name. 
           
          * ``available-ip-address-count`` - The number of IPv4 addresses in the subnet that are available. 
           
          * ``cidrBlock`` - The IPv4 CIDR block of the subnet. The CIDR block you specify must exactly match the subnet\'s CIDR block for information to be returned for the subnet. You can also use ``cidr`` or ``cidr-block`` as the filter names. 
           
          * ``defaultForAz`` - Indicates whether this is the default subnet for the Availability Zone. You can also use ``default-for-az`` as the filter name. 
           
          * ``ipv6-cidr-block-association.ipv6-cidr-block`` - An IPv6 CIDR block associated with the subnet. 
           
          * ``ipv6-cidr-block-association.association-id`` - An association ID for an IPv6 CIDR block associated with the subnet. 
           
          * ``ipv6-cidr-block-association.state`` - The state of an IPv6 CIDR block associated with the subnet. 
           
          * ``state`` - The state of the subnet (``pending`` | ``available`` ). 
           
          * ``subnet-id`` - The ID of the subnet. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``vpc-id`` - The ID of the VPC for the subnet. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type SubnetIds: list
        :param SubnetIds: 
        
          One or more subnet IDs.
        
          Default: Describes all your subnets.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class SystemStatusOk(Waiter):
    def wait(self, Filters: List = None, InstanceIds: List = None, MaxResults: int = None, NextToken: str = None, DryRun: bool = None, IncludeAllInstances: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeInstanceStatus>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              InstanceIds=[
                  \'string\',
              ],
              MaxResults=123,
              NextToken=\'string\',
              DryRun=True|False,
              IncludeAllInstances=True|False,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``availability-zone`` - The Availability Zone of the instance. 
           
          * ``event.code`` - The code for the scheduled event (``instance-reboot`` | ``system-reboot`` | ``system-maintenance`` | ``instance-retirement`` | ``instance-stop`` ). 
           
          * ``event.description`` - A description of the event. 
           
          * ``event.not-after`` - The latest end time for the scheduled event (for example, ``2014-09-15T17:15:20.000Z`` ). 
           
          * ``event.not-before`` - The earliest start time for the scheduled event (for example, ``2014-09-15T17:15:20.000Z`` ). 
           
          * ``instance-state-code`` - The code for the instance state, as a 16-bit unsigned integer. The high byte is used for internal purposes and should be ignored. The low byte is set based on the state represented. The valid values are 0 (pending), 16 (running), 32 (shutting-down), 48 (terminated), 64 (stopping), and 80 (stopped). 
           
          * ``instance-state-name`` - The state of the instance (``pending`` | ``running`` | ``shutting-down`` | ``terminated`` | ``stopping`` | ``stopped`` ). 
           
          * ``instance-status.reachability`` - Filters on instance status where the name is ``reachability`` (``passed`` | ``failed`` | ``initializing`` | ``insufficient-data`` ). 
           
          * ``instance-status.status`` - The status of the instance (``ok`` | ``impaired`` | ``initializing`` | ``insufficient-data`` | ``not-applicable`` ). 
           
          * ``system-status.reachability`` - Filters on system status where the name is ``reachability`` (``passed`` | ``failed`` | ``initializing`` | ``insufficient-data`` ). 
           
          * ``system-status.status`` - The system status of the instance (``ok`` | ``impaired`` | ``initializing`` | ``insufficient-data`` | ``not-applicable`` ). 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type InstanceIds: list
        :param InstanceIds: 
        
          One or more instance IDs.
        
          Default: Describes all your instances.
        
          Constraints: Maximum 100 explicitly specified instance IDs.
        
          - *(string) --* 
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned ``NextToken`` value. This value can be between 5 and 1000. You cannot specify this parameter and the instance IDs parameter in the same call.
        
        :type NextToken: string
        :param NextToken: 
        
          The token to retrieve the next page of results.
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type IncludeAllInstances: boolean
        :param IncludeAllInstances: 
        
          When ``true`` , includes the health status for all instances. When ``false`` , includes the health status for running instances only.
        
          Default: ``false``  
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class VolumeAvailable(Waiter):
    def wait(self, Filters: List = None, VolumeIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVolumes>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              VolumeIds=[
                  \'string\',
              ],
              DryRun=True|False,
              MaxResults=123,
              NextToken=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``attachment.attach-time`` - The time stamp when the attachment initiated. 
           
          * ``attachment.delete-on-termination`` - Whether the volume is deleted on instance termination. 
           
          * ``attachment.device`` - The device name specified in the block device mapping (for example, ``/dev/sda1`` ). 
           
          * ``attachment.instance-id`` - The ID of the instance the volume is attached to. 
           
          * ``attachment.status`` - The attachment state (``attaching`` | ``attached`` | ``detaching`` ). 
           
          * ``availability-zone`` - The Availability Zone in which the volume was created. 
           
          * ``create-time`` - The time stamp when the volume was created. 
           
          * ``encrypted`` - The encryption status of the volume. 
           
          * ``size`` - The size of the volume, in GiB. 
           
          * ``snapshot-id`` - The snapshot from which the volume was created. 
           
          * ``status`` - The status of the volume (``creating`` | ``available`` | ``in-use`` | ``deleting`` | ``deleted`` | ``error`` ). 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``volume-id`` - The volume ID. 
           
          * ``volume-type`` - The Amazon EBS volume type. This can be ``gp2`` for General Purpose SSD, ``io1`` for Provisioned IOPS SSD, ``st1`` for Throughput Optimized HDD, ``sc1`` for Cold HDD, or ``standard`` for Magnetic volumes. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type VolumeIds: list
        :param VolumeIds: 
        
          One or more volume IDs.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of volume results returned by ``DescribeVolumes`` in paginated output. When this parameter is used, ``DescribeVolumes`` only returns ``MaxResults`` results in a single page along with a ``NextToken`` response element. The remaining results of the initial request can be seen by sending another ``DescribeVolumes`` request with the returned ``NextToken`` value. This value can be between 5 and 500; if ``MaxResults`` is given a value larger than 500, only 500 results are returned. If this parameter is not used, then ``DescribeVolumes`` returns all results. You cannot specify this parameter and the volume IDs parameter in the same request.
        
        :type NextToken: string
        :param NextToken: 
        
          The ``NextToken`` value returned from a previous paginated ``DescribeVolumes`` request where ``MaxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``NextToken`` value. This value is ``null`` when there are no more results to return.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class VolumeDeleted(Waiter):
    def wait(self, Filters: List = None, VolumeIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVolumes>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              VolumeIds=[
                  \'string\',
              ],
              DryRun=True|False,
              MaxResults=123,
              NextToken=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``attachment.attach-time`` - The time stamp when the attachment initiated. 
           
          * ``attachment.delete-on-termination`` - Whether the volume is deleted on instance termination. 
           
          * ``attachment.device`` - The device name specified in the block device mapping (for example, ``/dev/sda1`` ). 
           
          * ``attachment.instance-id`` - The ID of the instance the volume is attached to. 
           
          * ``attachment.status`` - The attachment state (``attaching`` | ``attached`` | ``detaching`` ). 
           
          * ``availability-zone`` - The Availability Zone in which the volume was created. 
           
          * ``create-time`` - The time stamp when the volume was created. 
           
          * ``encrypted`` - The encryption status of the volume. 
           
          * ``size`` - The size of the volume, in GiB. 
           
          * ``snapshot-id`` - The snapshot from which the volume was created. 
           
          * ``status`` - The status of the volume (``creating`` | ``available`` | ``in-use`` | ``deleting`` | ``deleted`` | ``error`` ). 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``volume-id`` - The volume ID. 
           
          * ``volume-type`` - The Amazon EBS volume type. This can be ``gp2`` for General Purpose SSD, ``io1`` for Provisioned IOPS SSD, ``st1`` for Throughput Optimized HDD, ``sc1`` for Cold HDD, or ``standard`` for Magnetic volumes. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type VolumeIds: list
        :param VolumeIds: 
        
          One or more volume IDs.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of volume results returned by ``DescribeVolumes`` in paginated output. When this parameter is used, ``DescribeVolumes`` only returns ``MaxResults`` results in a single page along with a ``NextToken`` response element. The remaining results of the initial request can be seen by sending another ``DescribeVolumes`` request with the returned ``NextToken`` value. This value can be between 5 and 500; if ``MaxResults`` is given a value larger than 500, only 500 results are returned. If this parameter is not used, then ``DescribeVolumes`` returns all results. You cannot specify this parameter and the volume IDs parameter in the same request.
        
        :type NextToken: string
        :param NextToken: 
        
          The ``NextToken`` value returned from a previous paginated ``DescribeVolumes`` request where ``MaxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``NextToken`` value. This value is ``null`` when there are no more results to return.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class VolumeInUse(Waiter):
    def wait(self, Filters: List = None, VolumeIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVolumes>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              VolumeIds=[
                  \'string\',
              ],
              DryRun=True|False,
              MaxResults=123,
              NextToken=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``attachment.attach-time`` - The time stamp when the attachment initiated. 
           
          * ``attachment.delete-on-termination`` - Whether the volume is deleted on instance termination. 
           
          * ``attachment.device`` - The device name specified in the block device mapping (for example, ``/dev/sda1`` ). 
           
          * ``attachment.instance-id`` - The ID of the instance the volume is attached to. 
           
          * ``attachment.status`` - The attachment state (``attaching`` | ``attached`` | ``detaching`` ). 
           
          * ``availability-zone`` - The Availability Zone in which the volume was created. 
           
          * ``create-time`` - The time stamp when the volume was created. 
           
          * ``encrypted`` - The encryption status of the volume. 
           
          * ``size`` - The size of the volume, in GiB. 
           
          * ``snapshot-id`` - The snapshot from which the volume was created. 
           
          * ``status`` - The status of the volume (``creating`` | ``available`` | ``in-use`` | ``deleting`` | ``deleted`` | ``error`` ). 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``volume-id`` - The volume ID. 
           
          * ``volume-type`` - The Amazon EBS volume type. This can be ``gp2`` for General Purpose SSD, ``io1`` for Provisioned IOPS SSD, ``st1`` for Throughput Optimized HDD, ``sc1`` for Cold HDD, or ``standard`` for Magnetic volumes. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type VolumeIds: list
        :param VolumeIds: 
        
          One or more volume IDs.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type MaxResults: integer
        :param MaxResults: 
        
          The maximum number of volume results returned by ``DescribeVolumes`` in paginated output. When this parameter is used, ``DescribeVolumes`` only returns ``MaxResults`` results in a single page along with a ``NextToken`` response element. The remaining results of the initial request can be seen by sending another ``DescribeVolumes`` request with the returned ``NextToken`` value. This value can be between 5 and 500; if ``MaxResults`` is given a value larger than 500, only 500 results are returned. If this parameter is not used, then ``DescribeVolumes`` returns all results. You cannot specify this parameter and the volume IDs parameter in the same request.
        
        :type NextToken: string
        :param NextToken: 
        
          The ``NextToken`` value returned from a previous paginated ``DescribeVolumes`` request where ``MaxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``NextToken`` value. This value is ``null`` when there are no more results to return.
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class VpcAvailable(Waiter):
    def wait(self, Filters: List = None, VpcIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpcs>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              VpcIds=[
                  \'string\',
              ],
              DryRun=True|False,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``cidr`` - The primary IPv4 CIDR block of the VPC. The CIDR block you specify must exactly match the VPC\'s CIDR block for information to be returned for the VPC. Must contain the slash followed by one or two digits (for example, ``/28`` ). 
           
          * ``cidr-block-association.cidr-block`` - An IPv4 CIDR block associated with the VPC. 
           
          * ``cidr-block-association.association-id`` - The association ID for an IPv4 CIDR block associated with the VPC. 
           
          * ``cidr-block-association.state`` - The state of an IPv4 CIDR block associated with the VPC. 
           
          * ``dhcp-options-id`` - The ID of a set of DHCP options. 
           
          * ``ipv6-cidr-block-association.ipv6-cidr-block`` - An IPv6 CIDR block associated with the VPC. 
           
          * ``ipv6-cidr-block-association.association-id`` - The association ID for an IPv6 CIDR block associated with the VPC. 
           
          * ``ipv6-cidr-block-association.state`` - The state of an IPv6 CIDR block associated with the VPC. 
           
          * ``isDefault`` - Indicates whether the VPC is the default VPC. 
           
          * ``state`` - The state of the VPC (``pending`` | ``available`` ). 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``vpc-id`` - The ID of the VPC. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type VpcIds: list
        :param VpcIds: 
        
          One or more VPC IDs.
        
          Default: Describes all your VPCs.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class VpcExists(Waiter):
    def wait(self, Filters: List = None, VpcIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpcs>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              VpcIds=[
                  \'string\',
              ],
              DryRun=True|False,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``cidr`` - The primary IPv4 CIDR block of the VPC. The CIDR block you specify must exactly match the VPC\'s CIDR block for information to be returned for the VPC. Must contain the slash followed by one or two digits (for example, ``/28`` ). 
           
          * ``cidr-block-association.cidr-block`` - An IPv4 CIDR block associated with the VPC. 
           
          * ``cidr-block-association.association-id`` - The association ID for an IPv4 CIDR block associated with the VPC. 
           
          * ``cidr-block-association.state`` - The state of an IPv4 CIDR block associated with the VPC. 
           
          * ``dhcp-options-id`` - The ID of a set of DHCP options. 
           
          * ``ipv6-cidr-block-association.ipv6-cidr-block`` - An IPv6 CIDR block associated with the VPC. 
           
          * ``ipv6-cidr-block-association.association-id`` - The association ID for an IPv6 CIDR block associated with the VPC. 
           
          * ``ipv6-cidr-block-association.state`` - The state of an IPv6 CIDR block associated with the VPC. 
           
          * ``isDefault`` - Indicates whether the VPC is the default VPC. 
           
          * ``state`` - The state of the VPC (``pending`` | ``available`` ). 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``vpc-id`` - The ID of the VPC. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type VpcIds: list
        :param VpcIds: 
        
          One or more VPC IDs.
        
          Default: Describes all your VPCs.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 1
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 5
        
        :returns: None
        """
        pass


class VpcPeeringConnectionDeleted(Waiter):
    def wait(self, Filters: List = None, DryRun: bool = None, VpcPeeringConnectionIds: List = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpcPeeringConnections>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              DryRun=True|False,
              VpcPeeringConnectionIds=[
                  \'string\',
              ],
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``accepter-vpc-info.cidr-block`` - The IPv4 CIDR block of the accepter VPC. 
           
          * ``accepter-vpc-info.owner-id`` - The AWS account ID of the owner of the accepter VPC. 
           
          * ``accepter-vpc-info.vpc-id`` - The ID of the accepter VPC. 
           
          * ``expiration-time`` - The expiration date and time for the VPC peering connection. 
           
          * ``requester-vpc-info.cidr-block`` - The IPv4 CIDR block of the requester\'s VPC. 
           
          * ``requester-vpc-info.owner-id`` - The AWS account ID of the owner of the requester VPC. 
           
          * ``requester-vpc-info.vpc-id`` - The ID of the requester VPC. 
           
          * ``status-code`` - The status of the VPC peering connection (``pending-acceptance`` | ``failed`` | ``expired`` | ``provisioning`` | ``active`` | ``deleting`` | ``deleted`` | ``rejected`` ). 
           
          * ``status-message`` - A message that provides more information about the status of the VPC peering connection, if applicable. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``vpc-peering-connection-id`` - The ID of the VPC peering connection. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type VpcPeeringConnectionIds: list
        :param VpcPeeringConnectionIds: 
        
          One or more VPC peering connection IDs.
        
          Default: Describes all your VPC peering connections.
        
          - *(string) --* 
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class VpcPeeringConnectionExists(Waiter):
    def wait(self, Filters: List = None, DryRun: bool = None, VpcPeeringConnectionIds: List = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpcPeeringConnections>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              DryRun=True|False,
              VpcPeeringConnectionIds=[
                  \'string\',
              ],
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``accepter-vpc-info.cidr-block`` - The IPv4 CIDR block of the accepter VPC. 
           
          * ``accepter-vpc-info.owner-id`` - The AWS account ID of the owner of the accepter VPC. 
           
          * ``accepter-vpc-info.vpc-id`` - The ID of the accepter VPC. 
           
          * ``expiration-time`` - The expiration date and time for the VPC peering connection. 
           
          * ``requester-vpc-info.cidr-block`` - The IPv4 CIDR block of the requester\'s VPC. 
           
          * ``requester-vpc-info.owner-id`` - The AWS account ID of the owner of the requester VPC. 
           
          * ``requester-vpc-info.vpc-id`` - The ID of the requester VPC. 
           
          * ``status-code`` - The status of the VPC peering connection (``pending-acceptance`` | ``failed`` | ``expired`` | ``provisioning`` | ``active`` | ``deleting`` | ``deleted`` | ``rejected`` ). 
           
          * ``status-message`` - A message that provides more information about the status of the VPC peering connection, if applicable. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``vpc-peering-connection-id`` - The ID of the VPC peering connection. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type VpcPeeringConnectionIds: list
        :param VpcPeeringConnectionIds: 
        
          One or more VPC peering connection IDs.
        
          Default: Describes all your VPC peering connections.
        
          - *(string) --* 
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class VpnConnectionAvailable(Waiter):
    def wait(self, Filters: List = None, VpnConnectionIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpnConnections>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              VpnConnectionIds=[
                  \'string\',
              ],
              DryRun=True|False,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``customer-gateway-configuration`` - The configuration information for the customer gateway. 
           
          * ``customer-gateway-id`` - The ID of a customer gateway associated with the VPN connection. 
           
          * ``state`` - The state of the VPN connection (``pending`` | ``available`` | ``deleting`` | ``deleted`` ). 
           
          * ``option.static-routes-only`` - Indicates whether the connection has static routes only. Used for devices that do not support Border Gateway Protocol (BGP). 
           
          * ``route.destination-cidr-block`` - The destination CIDR block. This corresponds to the subnet used in a customer data center. 
           
          * ``bgp-asn`` - The BGP Autonomous System Number (ASN) associated with a BGP device. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``type`` - The type of VPN connection. Currently the only supported type is ``ipsec.1`` . 
           
          * ``vpn-connection-id`` - The ID of the VPN connection. 
           
          * ``vpn-gateway-id`` - The ID of a virtual private gateway associated with the VPN connection. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type VpnConnectionIds: list
        :param VpnConnectionIds: 
        
          One or more VPN connection IDs.
        
          Default: Describes your VPN connections.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass


class VpnConnectionDeleted(Waiter):
    def wait(self, Filters: List = None, VpnConnectionIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpnConnections>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              Filters=[
                  {
                      \'Name\': \'string\',
                      \'Values\': [
                          \'string\',
                      ]
                  },
              ],
              VpnConnectionIds=[
                  \'string\',
              ],
              DryRun=True|False,
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type Filters: list
        :param Filters: 
        
          One or more filters.
        
          * ``customer-gateway-configuration`` - The configuration information for the customer gateway. 
           
          * ``customer-gateway-id`` - The ID of a customer gateway associated with the VPN connection. 
           
          * ``state`` - The state of the VPN connection (``pending`` | ``available`` | ``deleting`` | ``deleted`` ). 
           
          * ``option.static-routes-only`` - Indicates whether the connection has static routes only. Used for devices that do not support Border Gateway Protocol (BGP). 
           
          * ``route.destination-cidr-block`` - The destination CIDR block. This corresponds to the subnet used in a customer data center. 
           
          * ``bgp-asn`` - The BGP Autonomous System Number (ASN) associated with a BGP device. 
           
          * ``tag`` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key ``Owner`` and the value ``TeamA`` , specify ``tag:Owner`` for the filter name and ``TeamA`` for the filter value. 
           
          * ``tag-key`` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value. 
           
          * ``type`` - The type of VPN connection. Currently the only supported type is ``ipsec.1`` . 
           
          * ``vpn-connection-id`` - The ID of the VPN connection. 
           
          * ``vpn-gateway-id`` - The ID of a virtual private gateway associated with the VPN connection. 
           
          - *(dict) --* 
        
            A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs. The filters supported by a describe operation are documented with the describe operation. For example:
        
            *  DescribeAvailabilityZones   
             
            *  DescribeImages   
             
            *  DescribeInstances   
             
            *  DescribeKeyPairs   
             
            *  DescribeSecurityGroups   
             
            *  DescribeSnapshots   
             
            *  DescribeSubnets   
             
            *  DescribeTags   
             
            *  DescribeVolumes   
             
            *  DescribeVpcs   
             
            - **Name** *(string) --* 
        
              The name of the filter. Filter names are case-sensitive.
        
            - **Values** *(list) --* 
        
              One or more filter values. Filter values are case-sensitive.
        
              - *(string) --* 
        
        :type VpnConnectionIds: list
        :param VpnConnectionIds: 
        
          One or more VPN connection IDs.
        
          Default: Describes your VPN connections.
        
          - *(string) --* 
        
        :type DryRun: boolean
        :param DryRun: 
        
          Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is ``DryRunOperation`` . Otherwise, it is ``UnauthorizedOperation`` .
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 15
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass
