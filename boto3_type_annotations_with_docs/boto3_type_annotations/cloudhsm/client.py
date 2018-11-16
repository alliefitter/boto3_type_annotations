from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def add_tags_to_resource(self, ResourceArn: str, TagList: List) -> Dict:
        """
        
         **For information about the current version of AWS CloudHSM** , see `AWS CloudHSM <http://aws.amazon.com/cloudhsm/>`__ , the `AWS CloudHSM User Guide <http://docs.aws.amazon.com/cloudhsm/latest/userguide/>`__ , and the `AWS CloudHSM API Reference <http://docs.aws.amazon.com/cloudhsm/latest/APIReference/>`__ .
        
        Adds or overwrites one or more tags for the specified AWS CloudHSM resource.
        
        Each tag consists of a key and a value. Tag keys must be unique to each resource.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsm-2014-05-30/AddTagsToResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.add_tags_to_resource(
              ResourceArn=\'string\',
              TagList=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the AWS CloudHSM resource to tag.
        
        :type TagList: list
        :param TagList: **[REQUIRED]** 
        
          One or more tags.
        
          - *(dict) --* 
        
            A key-value pair that identifies or specifies metadata about an AWS CloudHSM resource.
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              The key of the tag.
        
            - **Value** *(string) --* **[REQUIRED]** 
        
              The value of the tag.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Status\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Status** *(string) --* 
        
              The status of the operation.
        
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

    def create_hapg(self, Label: str) -> Dict:
        """
        
         **For information about the current version of AWS CloudHSM** , see `AWS CloudHSM <http://aws.amazon.com/cloudhsm/>`__ , the `AWS CloudHSM User Guide <http://docs.aws.amazon.com/cloudhsm/latest/userguide/>`__ , and the `AWS CloudHSM API Reference <http://docs.aws.amazon.com/cloudhsm/latest/APIReference/>`__ .
        
        Creates a high-availability partition group. A high-availability partition group is a group of partitions that spans multiple physical HSMs.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsm-2014-05-30/CreateHapg>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_hapg(
              Label=\'string\'
          )
        :type Label: string
        :param Label: **[REQUIRED]** 
        
          The label of the new high-availability partition group.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'HapgArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of the  CreateHAPartitionGroup action.
        
            - **HapgArn** *(string) --* 
        
              The ARN of the high-availability partition group.
        
        """
        pass

    def create_hsm(self, SubnetId: str, SshKey: str, IamRoleArn: str, SubscriptionType: str, EniIp: str = None, ExternalId: str = None, ClientToken: str = None, SyslogIp: str = None) -> Dict:
        """
        
         **For information about the current version of AWS CloudHSM** , see `AWS CloudHSM <http://aws.amazon.com/cloudhsm/>`__ , the `AWS CloudHSM User Guide <http://docs.aws.amazon.com/cloudhsm/latest/userguide/>`__ , and the `AWS CloudHSM API Reference <http://docs.aws.amazon.com/cloudhsm/latest/APIReference/>`__ .
        
        Creates an uninitialized HSM instance.
        
        There is an upfront fee charged for each HSM instance that you create with the ``CreateHsm`` operation. If you accidentally provision an HSM and want to request a refund, delete the instance using the  DeleteHsm operation, go to the `AWS Support Center <https://console.aws.amazon.com/support/home>`__ , create a new case, and select **Account and Billing Support** .
        
        .. warning::
        
          It can take up to 20 minutes to create and provision an HSM. You can monitor the status of the HSM with the  DescribeHsm operation. The HSM is ready to be initialized when the status changes to ``RUNNING`` .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsm-2014-05-30/CreateHsm>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_hsm(
              SubnetId=\'string\',
              SshKey=\'string\',
              EniIp=\'string\',
              IamRoleArn=\'string\',
              ExternalId=\'string\',
              SubscriptionType=\'PRODUCTION\',
              ClientToken=\'string\',
              SyslogIp=\'string\'
          )
        :type SubnetId: string
        :param SubnetId: **[REQUIRED]** 
        
          The identifier of the subnet in your VPC in which to place the HSM.
        
        :type SshKey: string
        :param SshKey: **[REQUIRED]** 
        
          The SSH public key to install on the HSM.
        
        :type EniIp: string
        :param EniIp: 
        
          The IP address to assign to the HSM\'s ENI.
        
          If an IP address is not specified, an IP address will be randomly chosen from the CIDR range of the subnet.
        
        :type IamRoleArn: string
        :param IamRoleArn: **[REQUIRED]** 
        
          The ARN of an IAM role to enable the AWS CloudHSM service to allocate an ENI on your behalf.
        
        :type ExternalId: string
        :param ExternalId: 
        
          The external ID from ``IamRoleArn`` , if present.
        
        :type SubscriptionType: string
        :param SubscriptionType: **[REQUIRED]** 
        
          Specifies the type of subscription for the HSM.
        
          * **PRODUCTION** - The HSM is being used in a production environment. 
           
          * **TRIAL** - The HSM is being used in a product trial. 
           
        :type ClientToken: string
        :param ClientToken: 
        
          A user-defined token to ensure idempotence. Subsequent calls to this operation with the same token will be ignored.
        
        :type SyslogIp: string
        :param SyslogIp: 
        
          The IP address for the syslog monitoring server. The AWS CloudHSM service only supports one syslog monitoring server.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'HsmArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of the ``CreateHsm`` operation.
        
            - **HsmArn** *(string) --* 
        
              The ARN of the HSM.
        
        """
        pass

    def create_luna_client(self, Certificate: str, Label: str = None) -> Dict:
        """
        
         **For information about the current version of AWS CloudHSM** , see `AWS CloudHSM <http://aws.amazon.com/cloudhsm/>`__ , the `AWS CloudHSM User Guide <http://docs.aws.amazon.com/cloudhsm/latest/userguide/>`__ , and the `AWS CloudHSM API Reference <http://docs.aws.amazon.com/cloudhsm/latest/APIReference/>`__ .
        
        Creates an HSM client.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsm-2014-05-30/CreateLunaClient>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_luna_client(
              Label=\'string\',
              Certificate=\'string\'
          )
        :type Label: string
        :param Label: 
        
          The label for the client.
        
        :type Certificate: string
        :param Certificate: **[REQUIRED]** 
        
          The contents of a Base64-Encoded X.509 v3 certificate to be installed on the HSMs used by this client.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ClientArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of the  CreateLunaClient action.
        
            - **ClientArn** *(string) --* 
        
              The ARN of the client.
        
        """
        pass

    def delete_hapg(self, HapgArn: str) -> Dict:
        """
        
         **For information about the current version of AWS CloudHSM** , see `AWS CloudHSM <http://aws.amazon.com/cloudhsm/>`__ , the `AWS CloudHSM User Guide <http://docs.aws.amazon.com/cloudhsm/latest/userguide/>`__ , and the `AWS CloudHSM API Reference <http://docs.aws.amazon.com/cloudhsm/latest/APIReference/>`__ .
        
        Deletes a high-availability partition group.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsm-2014-05-30/DeleteHapg>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_hapg(
              HapgArn=\'string\'
          )
        :type HapgArn: string
        :param HapgArn: **[REQUIRED]** 
        
          The ARN of the high-availability partition group to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Status\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of the  DeleteHapg action.
        
            - **Status** *(string) --* 
        
              The status of the action.
        
        """
        pass

    def delete_hsm(self, HsmArn: str) -> Dict:
        """
        
         **For information about the current version of AWS CloudHSM** , see `AWS CloudHSM <http://aws.amazon.com/cloudhsm/>`__ , the `AWS CloudHSM User Guide <http://docs.aws.amazon.com/cloudhsm/latest/userguide/>`__ , and the `AWS CloudHSM API Reference <http://docs.aws.amazon.com/cloudhsm/latest/APIReference/>`__ .
        
        Deletes an HSM. After completion, this operation cannot be undone and your key material cannot be recovered.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsm-2014-05-30/DeleteHsm>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_hsm(
              HsmArn=\'string\'
          )
        :type HsmArn: string
        :param HsmArn: **[REQUIRED]** 
        
          The ARN of the HSM to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Status\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of the  DeleteHsm operation.
        
            - **Status** *(string) --* 
        
              The status of the operation.
        
        """
        pass

    def delete_luna_client(self, ClientArn: str) -> Dict:
        """
        
         **For information about the current version of AWS CloudHSM** , see `AWS CloudHSM <http://aws.amazon.com/cloudhsm/>`__ , the `AWS CloudHSM User Guide <http://docs.aws.amazon.com/cloudhsm/latest/userguide/>`__ , and the `AWS CloudHSM API Reference <http://docs.aws.amazon.com/cloudhsm/latest/APIReference/>`__ .
        
        Deletes a client.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsm-2014-05-30/DeleteLunaClient>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_luna_client(
              ClientArn=\'string\'
          )
        :type ClientArn: string
        :param ClientArn: **[REQUIRED]** 
        
          The ARN of the client to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Status\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Status** *(string) --* 
        
              The status of the action.
        
        """
        pass

    def describe_hapg(self, HapgArn: str) -> Dict:
        """
        
         **For information about the current version of AWS CloudHSM** , see `AWS CloudHSM <http://aws.amazon.com/cloudhsm/>`__ , the `AWS CloudHSM User Guide <http://docs.aws.amazon.com/cloudhsm/latest/userguide/>`__ , and the `AWS CloudHSM API Reference <http://docs.aws.amazon.com/cloudhsm/latest/APIReference/>`__ .
        
        Retrieves information about a high-availability partition group.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsm-2014-05-30/DescribeHapg>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_hapg(
              HapgArn=\'string\'
          )
        :type HapgArn: string
        :param HapgArn: **[REQUIRED]** 
        
          The ARN of the high-availability partition group to describe.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'HapgArn\': \'string\',
                \'HapgSerial\': \'string\',
                \'HsmsLastActionFailed\': [
                    \'string\',
                ],
                \'HsmsPendingDeletion\': [
                    \'string\',
                ],
                \'HsmsPendingRegistration\': [
                    \'string\',
                ],
                \'Label\': \'string\',
                \'LastModifiedTimestamp\': \'string\',
                \'PartitionSerialList\': [
                    \'string\',
                ],
                \'State\': \'READY\'|\'UPDATING\'|\'DEGRADED\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of the  DescribeHapg action.
        
            - **HapgArn** *(string) --* 
        
              The ARN of the high-availability partition group.
        
            - **HapgSerial** *(string) --* 
        
              The serial number of the high-availability partition group.
        
            - **HsmsLastActionFailed** *(list) --* 
        
              - *(string) --* 
        
                An ARN that identifies an HSM.
        
            - **HsmsPendingDeletion** *(list) --* 
        
              - *(string) --* 
        
                An ARN that identifies an HSM.
        
            - **HsmsPendingRegistration** *(list) --* 
        
              - *(string) --* 
        
                An ARN that identifies an HSM.
        
            - **Label** *(string) --* 
        
              The label for the high-availability partition group.
        
            - **LastModifiedTimestamp** *(string) --* 
        
              The date and time the high-availability partition group was last modified.
        
            - **PartitionSerialList** *(list) --* 
        
              The list of partition serial numbers that belong to the high-availability partition group.
        
              - *(string) --* 
          
            - **State** *(string) --* 
        
              The state of the high-availability partition group.
        
        """
        pass

    def describe_hsm(self, HsmArn: str = None, HsmSerialNumber: str = None) -> Dict:
        """
        
         **For information about the current version of AWS CloudHSM** , see `AWS CloudHSM <http://aws.amazon.com/cloudhsm/>`__ , the `AWS CloudHSM User Guide <http://docs.aws.amazon.com/cloudhsm/latest/userguide/>`__ , and the `AWS CloudHSM API Reference <http://docs.aws.amazon.com/cloudhsm/latest/APIReference/>`__ .
        
        Retrieves information about an HSM. You can identify the HSM by its ARN or its serial number.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsm-2014-05-30/DescribeHsm>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_hsm(
              HsmArn=\'string\',
              HsmSerialNumber=\'string\'
          )
        :type HsmArn: string
        :param HsmArn: 
        
          The ARN of the HSM. Either the ``HsmArn`` or the ``SerialNumber`` parameter must be specified.
        
        :type HsmSerialNumber: string
        :param HsmSerialNumber: 
        
          The serial number of the HSM. Either the ``HsmArn`` or the ``HsmSerialNumber`` parameter must be specified.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'HsmArn\': \'string\',
                \'Status\': \'PENDING\'|\'RUNNING\'|\'UPDATING\'|\'SUSPENDED\'|\'TERMINATING\'|\'TERMINATED\'|\'DEGRADED\',
                \'StatusDetails\': \'string\',
                \'AvailabilityZone\': \'string\',
                \'EniId\': \'string\',
                \'EniIp\': \'string\',
                \'SubscriptionType\': \'PRODUCTION\',
                \'SubscriptionStartDate\': \'string\',
                \'SubscriptionEndDate\': \'string\',
                \'VpcId\': \'string\',
                \'SubnetId\': \'string\',
                \'IamRoleArn\': \'string\',
                \'SerialNumber\': \'string\',
                \'VendorName\': \'string\',
                \'HsmType\': \'string\',
                \'SoftwareVersion\': \'string\',
                \'SshPublicKey\': \'string\',
                \'SshKeyLastUpdated\': \'string\',
                \'ServerCertUri\': \'string\',
                \'ServerCertLastUpdated\': \'string\',
                \'Partitions\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of the  DescribeHsm operation.
        
            - **HsmArn** *(string) --* 
        
              The ARN of the HSM.
        
            - **Status** *(string) --* 
        
              The status of the HSM.
        
            - **StatusDetails** *(string) --* 
        
              Contains additional information about the status of the HSM.
        
            - **AvailabilityZone** *(string) --* 
        
              The Availability Zone that the HSM is in.
        
            - **EniId** *(string) --* 
        
              The identifier of the elastic network interface (ENI) attached to the HSM.
        
            - **EniIp** *(string) --* 
        
              The IP address assigned to the HSM\'s ENI.
        
            - **SubscriptionType** *(string) --* 
        
              Specifies the type of subscription for the HSM.
        
              * **PRODUCTION** - The HSM is being used in a production environment. 
               
              * **TRIAL** - The HSM is being used in a product trial. 
               
            - **SubscriptionStartDate** *(string) --* 
        
              The subscription start date.
        
            - **SubscriptionEndDate** *(string) --* 
        
              The subscription end date.
        
            - **VpcId** *(string) --* 
        
              The identifier of the VPC that the HSM is in.
        
            - **SubnetId** *(string) --* 
        
              The identifier of the subnet that the HSM is in.
        
            - **IamRoleArn** *(string) --* 
        
              The ARN of the IAM role assigned to the HSM.
        
            - **SerialNumber** *(string) --* 
        
              The serial number of the HSM.
        
            - **VendorName** *(string) --* 
        
              The name of the HSM vendor.
        
            - **HsmType** *(string) --* 
        
              The HSM model type.
        
            - **SoftwareVersion** *(string) --* 
        
              The HSM software version.
        
            - **SshPublicKey** *(string) --* 
        
              The public SSH key.
        
            - **SshKeyLastUpdated** *(string) --* 
        
              The date and time that the SSH key was last updated.
        
            - **ServerCertUri** *(string) --* 
        
              The URI of the certificate server.
        
            - **ServerCertLastUpdated** *(string) --* 
        
              The date and time that the server certificate was last updated.
        
            - **Partitions** *(list) --* 
        
              The list of partitions on the HSM.
        
              - *(string) --* 
          
        """
        pass

    def describe_luna_client(self, ClientArn: str = None, CertificateFingerprint: str = None) -> Dict:
        """
        
         **For information about the current version of AWS CloudHSM** , see `AWS CloudHSM <http://aws.amazon.com/cloudhsm/>`__ , the `AWS CloudHSM User Guide <http://docs.aws.amazon.com/cloudhsm/latest/userguide/>`__ , and the `AWS CloudHSM API Reference <http://docs.aws.amazon.com/cloudhsm/latest/APIReference/>`__ .
        
        Retrieves information about an HSM client.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsm-2014-05-30/DescribeLunaClient>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_luna_client(
              ClientArn=\'string\',
              CertificateFingerprint=\'string\'
          )
        :type ClientArn: string
        :param ClientArn: 
        
          The ARN of the client.
        
        :type CertificateFingerprint: string
        :param CertificateFingerprint: 
        
          The certificate fingerprint.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ClientArn\': \'string\',
                \'Certificate\': \'string\',
                \'CertificateFingerprint\': \'string\',
                \'LastModifiedTimestamp\': \'string\',
                \'Label\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ClientArn** *(string) --* 
        
              The ARN of the client.
        
            - **Certificate** *(string) --* 
        
              The certificate installed on the HSMs used by this client.
        
            - **CertificateFingerprint** *(string) --* 
        
              The certificate fingerprint.
        
            - **LastModifiedTimestamp** *(string) --* 
        
              The date and time the client was last modified.
        
            - **Label** *(string) --* 
        
              The label of the client.
        
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

    def get_config(self, ClientArn: str, ClientVersion: str, HapgList: List) -> Dict:
        """
        
         **For information about the current version of AWS CloudHSM** , see `AWS CloudHSM <http://aws.amazon.com/cloudhsm/>`__ , the `AWS CloudHSM User Guide <http://docs.aws.amazon.com/cloudhsm/latest/userguide/>`__ , and the `AWS CloudHSM API Reference <http://docs.aws.amazon.com/cloudhsm/latest/APIReference/>`__ .
        
        Gets the configuration files necessary to connect to all high availability partition groups the client is associated with.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsm-2014-05-30/GetConfig>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_config(
              ClientArn=\'string\',
              ClientVersion=\'5.1\'|\'5.3\',
              HapgList=[
                  \'string\',
              ]
          )
        :type ClientArn: string
        :param ClientArn: **[REQUIRED]** 
        
          The ARN of the client.
        
        :type ClientVersion: string
        :param ClientVersion: **[REQUIRED]** 
        
          The client version.
        
        :type HapgList: list
        :param HapgList: **[REQUIRED]** 
        
          A list of ARNs that identify the high-availability partition groups that are associated with the client.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ConfigType\': \'string\',
                \'ConfigFile\': \'string\',
                \'ConfigCred\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ConfigType** *(string) --* 
        
              The type of credentials.
        
            - **ConfigFile** *(string) --* 
        
              The chrystoki.conf configuration file.
        
            - **ConfigCred** *(string) --* 
        
              The certificate file containing the server.pem files of the HSMs.
        
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

    def list_available_zones(self) -> Dict:
        """
        
         **For information about the current version of AWS CloudHSM** , see `AWS CloudHSM <http://aws.amazon.com/cloudhsm/>`__ , the `AWS CloudHSM User Guide <http://docs.aws.amazon.com/cloudhsm/latest/userguide/>`__ , and the `AWS CloudHSM API Reference <http://docs.aws.amazon.com/cloudhsm/latest/APIReference/>`__ .
        
        Lists the Availability Zones that have available AWS CloudHSM capacity.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsm-2014-05-30/ListAvailableZones>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_available_zones()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AZList\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AZList** *(list) --* 
        
              The list of Availability Zones that have available AWS CloudHSM capacity.
        
              - *(string) --* 
          
        """
        pass

    def list_hapgs(self, NextToken: str = None) -> Dict:
        """
        
         **For information about the current version of AWS CloudHSM** , see `AWS CloudHSM <http://aws.amazon.com/cloudhsm/>`__ , the `AWS CloudHSM User Guide <http://docs.aws.amazon.com/cloudhsm/latest/userguide/>`__ , and the `AWS CloudHSM API Reference <http://docs.aws.amazon.com/cloudhsm/latest/APIReference/>`__ .
        
        Lists the high-availability partition groups for the account.
        
        This operation supports pagination with the use of the ``NextToken`` member. If more results are available, the ``NextToken`` member of the response contains a token that you pass in the next call to ``ListHapgs`` to retrieve the next set of items.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsm-2014-05-30/ListHapgs>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_hapgs(
              NextToken=\'string\'
          )
        :type NextToken: string
        :param NextToken: 
        
          The ``NextToken`` value from a previous call to ``ListHapgs`` . Pass null if this is the first call.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'HapgList\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **HapgList** *(list) --* 
        
              The list of high-availability partition groups.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              If not null, more results are available. Pass this value to ``ListHapgs`` to retrieve the next set of items.
        
        """
        pass

    def list_hsms(self, NextToken: str = None) -> Dict:
        """
        
         **For information about the current version of AWS CloudHSM** , see `AWS CloudHSM <http://aws.amazon.com/cloudhsm/>`__ , the `AWS CloudHSM User Guide <http://docs.aws.amazon.com/cloudhsm/latest/userguide/>`__ , and the `AWS CloudHSM API Reference <http://docs.aws.amazon.com/cloudhsm/latest/APIReference/>`__ .
        
        Retrieves the identifiers of all of the HSMs provisioned for the current customer.
        
        This operation supports pagination with the use of the ``NextToken`` member. If more results are available, the ``NextToken`` member of the response contains a token that you pass in the next call to ``ListHsms`` to retrieve the next set of items.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsm-2014-05-30/ListHsms>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_hsms(
              NextToken=\'string\'
          )
        :type NextToken: string
        :param NextToken: 
        
          The ``NextToken`` value from a previous call to ``ListHsms`` . Pass null if this is the first call.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'HsmList\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of the ``ListHsms`` operation.
        
            - **HsmList** *(list) --* 
        
              The list of ARNs that identify the HSMs.
        
              - *(string) --* 
        
                An ARN that identifies an HSM.
        
            - **NextToken** *(string) --* 
        
              If not null, more results are available. Pass this value to ``ListHsms`` to retrieve the next set of items.
        
        """
        pass

    def list_luna_clients(self, NextToken: str = None) -> Dict:
        """
        
         **For information about the current version of AWS CloudHSM** , see `AWS CloudHSM <http://aws.amazon.com/cloudhsm/>`__ , the `AWS CloudHSM User Guide <http://docs.aws.amazon.com/cloudhsm/latest/userguide/>`__ , and the `AWS CloudHSM API Reference <http://docs.aws.amazon.com/cloudhsm/latest/APIReference/>`__ .
        
        Lists all of the clients.
        
        This operation supports pagination with the use of the ``NextToken`` member. If more results are available, the ``NextToken`` member of the response contains a token that you pass in the next call to ``ListLunaClients`` to retrieve the next set of items.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsm-2014-05-30/ListLunaClients>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_luna_clients(
              NextToken=\'string\'
          )
        :type NextToken: string
        :param NextToken: 
        
          The ``NextToken`` value from a previous call to ``ListLunaClients`` . Pass null if this is the first call.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ClientList\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ClientList** *(list) --* 
        
              The list of clients.
        
              - *(string) --* 
          
            - **NextToken** *(string) --* 
        
              If not null, more results are available. Pass this to ``ListLunaClients`` to retrieve the next set of items.
        
        """
        pass

    def list_tags_for_resource(self, ResourceArn: str) -> Dict:
        """
        
         **For information about the current version of AWS CloudHSM** , see `AWS CloudHSM <http://aws.amazon.com/cloudhsm/>`__ , the `AWS CloudHSM User Guide <http://docs.aws.amazon.com/cloudhsm/latest/userguide/>`__ , and the `AWS CloudHSM API Reference <http://docs.aws.amazon.com/cloudhsm/latest/APIReference/>`__ .
        
        Returns a list of all tags for the specified AWS CloudHSM resource.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsm-2014-05-30/ListTagsForResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_tags_for_resource(
              ResourceArn=\'string\'
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the AWS CloudHSM resource.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'TagList\': [
                    {
                        \'Key\': \'string\',
                        \'Value\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **TagList** *(list) --* 
        
              One or more tags.
        
              - *(dict) --* 
        
                A key-value pair that identifies or specifies metadata about an AWS CloudHSM resource.
        
                - **Key** *(string) --* 
        
                  The key of the tag.
        
                - **Value** *(string) --* 
        
                  The value of the tag.
        
        """
        pass

    def modify_hapg(self, HapgArn: str, Label: str = None, PartitionSerialList: List = None) -> Dict:
        """
        
         **For information about the current version of AWS CloudHSM** , see `AWS CloudHSM <http://aws.amazon.com/cloudhsm/>`__ , the `AWS CloudHSM User Guide <http://docs.aws.amazon.com/cloudhsm/latest/userguide/>`__ , and the `AWS CloudHSM API Reference <http://docs.aws.amazon.com/cloudhsm/latest/APIReference/>`__ .
        
        Modifies an existing high-availability partition group.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsm-2014-05-30/ModifyHapg>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_hapg(
              HapgArn=\'string\',
              Label=\'string\',
              PartitionSerialList=[
                  \'string\',
              ]
          )
        :type HapgArn: string
        :param HapgArn: **[REQUIRED]** 
        
          The ARN of the high-availability partition group to modify.
        
        :type Label: string
        :param Label: 
        
          The new label for the high-availability partition group.
        
        :type PartitionSerialList: list
        :param PartitionSerialList: 
        
          The list of partition serial numbers to make members of the high-availability partition group.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'HapgArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **HapgArn** *(string) --* 
        
              The ARN of the high-availability partition group.
        
        """
        pass

    def modify_hsm(self, HsmArn: str, SubnetId: str = None, EniIp: str = None, IamRoleArn: str = None, ExternalId: str = None, SyslogIp: str = None) -> Dict:
        """
        
         **For information about the current version of AWS CloudHSM** , see `AWS CloudHSM <http://aws.amazon.com/cloudhsm/>`__ , the `AWS CloudHSM User Guide <http://docs.aws.amazon.com/cloudhsm/latest/userguide/>`__ , and the `AWS CloudHSM API Reference <http://docs.aws.amazon.com/cloudhsm/latest/APIReference/>`__ .
        
        Modifies an HSM.
        
        .. warning::
        
          This operation can result in the HSM being offline for up to 15 minutes while the AWS CloudHSM service is reconfigured. If you are modifying a production HSM, you should ensure that your AWS CloudHSM service is configured for high availability, and consider executing this operation during a maintenance window.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsm-2014-05-30/ModifyHsm>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_hsm(
              HsmArn=\'string\',
              SubnetId=\'string\',
              EniIp=\'string\',
              IamRoleArn=\'string\',
              ExternalId=\'string\',
              SyslogIp=\'string\'
          )
        :type HsmArn: string
        :param HsmArn: **[REQUIRED]** 
        
          The ARN of the HSM to modify.
        
        :type SubnetId: string
        :param SubnetId: 
        
          The new identifier of the subnet that the HSM is in. The new subnet must be in the same Availability Zone as the current subnet.
        
        :type EniIp: string
        :param EniIp: 
        
          The new IP address for the elastic network interface (ENI) attached to the HSM.
        
          If the HSM is moved to a different subnet, and an IP address is not specified, an IP address will be randomly chosen from the CIDR range of the new subnet.
        
        :type IamRoleArn: string
        :param IamRoleArn: 
        
          The new IAM role ARN.
        
        :type ExternalId: string
        :param ExternalId: 
        
          The new external ID.
        
        :type SyslogIp: string
        :param SyslogIp: 
        
          The new IP address for the syslog monitoring server. The AWS CloudHSM service only supports one syslog monitoring server.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'HsmArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Contains the output of the  ModifyHsm operation.
        
            - **HsmArn** *(string) --* 
        
              The ARN of the HSM.
        
        """
        pass

    def modify_luna_client(self, ClientArn: str, Certificate: str) -> Dict:
        """
        
         **For information about the current version of AWS CloudHSM** , see `AWS CloudHSM <http://aws.amazon.com/cloudhsm/>`__ , the `AWS CloudHSM User Guide <http://docs.aws.amazon.com/cloudhsm/latest/userguide/>`__ , and the `AWS CloudHSM API Reference <http://docs.aws.amazon.com/cloudhsm/latest/APIReference/>`__ .
        
        Modifies the certificate used by the client.
        
        This action can potentially start a workflow to install the new certificate on the client\'s HSMs.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsm-2014-05-30/ModifyLunaClient>`_
        
        **Request Syntax** 
        ::
        
          response = client.modify_luna_client(
              ClientArn=\'string\',
              Certificate=\'string\'
          )
        :type ClientArn: string
        :param ClientArn: **[REQUIRED]** 
        
          The ARN of the client.
        
        :type Certificate: string
        :param Certificate: **[REQUIRED]** 
        
          The new certificate for the client.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ClientArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **ClientArn** *(string) --* 
        
              The ARN of the client.
        
        """
        pass

    def remove_tags_from_resource(self, ResourceArn: str, TagKeyList: List) -> Dict:
        """
        
         **For information about the current version of AWS CloudHSM** , see `AWS CloudHSM <http://aws.amazon.com/cloudhsm/>`__ , the `AWS CloudHSM User Guide <http://docs.aws.amazon.com/cloudhsm/latest/userguide/>`__ , and the `AWS CloudHSM API Reference <http://docs.aws.amazon.com/cloudhsm/latest/APIReference/>`__ .
        
        Removes one or more tags from the specified AWS CloudHSM resource.
        
        To remove a tag, specify only the tag key to remove (not the value). To overwrite the value for an existing tag, use  AddTagsToResource .
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudhsm-2014-05-30/RemoveTagsFromResource>`_
        
        **Request Syntax** 
        ::
        
          response = client.remove_tags_from_resource(
              ResourceArn=\'string\',
              TagKeyList=[
                  \'string\',
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the AWS CloudHSM resource.
        
        :type TagKeyList: list
        :param TagKeyList: **[REQUIRED]** 
        
          The tag key or keys to remove.
        
          Specify only the tag key to remove (not the value). To overwrite the value for an existing tag, use  AddTagsToResource .
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Status\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Status** *(string) --* 
        
              The status of the operation.
        
        """
        pass
