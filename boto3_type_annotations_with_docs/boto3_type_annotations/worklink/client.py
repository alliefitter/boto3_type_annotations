from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import Union
from typing import List


class Client(BaseClient):
    def associate_domain(self, FleetArn: str, DomainName: str, AcmCertificateArn: str, DisplayName: str = None) -> Dict:
        """
        Specifies a domain to be associated to Amazon WorkLink.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/AssociateDomain>`_
        
        **Request Syntax**
        ::
          response = client.associate_domain(
              FleetArn='string',
              DomainName='string',
              AcmCertificateArn='string',
              DisplayName='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the fleet.
        :type DomainName: string
        :param DomainName: **[REQUIRED]**
          The fully qualified domain name (FQDN).
        :type AcmCertificateArn: string
        :param AcmCertificateArn: **[REQUIRED]**
          The ARN of an issued ACM certificate that is valid for the domain being associated.
        :type DisplayName: string
        :param DisplayName:
          The name to display.
        :rtype: dict
        :returns:
        """
        pass

    def associate_website_certificate_authority(self, FleetArn: str, Certificate: str, DisplayName: str = None) -> Dict:
        """
        Imports the root certificate of a certificate authority (CA) used to obtain TLS certificates used by associated websites within the company network.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/AssociateWebsiteCertificateAuthority>`_
        
        **Request Syntax**
        ::
          response = client.associate_website_certificate_authority(
              FleetArn='string',
              Certificate='string',
              DisplayName='string'
          )
        
        **Response Syntax**
        ::
            {
                'WebsiteCaId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **WebsiteCaId** *(string) --* 
              A unique identifier for the CA.
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**
          The ARN of the fleet.
        :type Certificate: string
        :param Certificate: **[REQUIRED]**
          The root certificate of the CA.
        :type DisplayName: string
        :param DisplayName:
          The certificate name to display.
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

    def create_fleet(self, FleetName: str, DisplayName: str = None, OptimizeForEndUserLocation: bool = None) -> Dict:
        """
        Creates a fleet. A fleet consists of resources and the configuration that delivers associated websites to authorized users who download and set up the Amazon WorkLink app.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/CreateFleet>`_
        
        **Request Syntax**
        ::
          response = client.create_fleet(
              FleetName='string',
              DisplayName='string',
              OptimizeForEndUserLocation=True|False
          )
        
        **Response Syntax**
        ::
            {
                'FleetArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **FleetArn** *(string) --* 
              The ARN of the fleet.
        :type FleetName: string
        :param FleetName: **[REQUIRED]**
          A unique name for the fleet.
        :type DisplayName: string
        :param DisplayName:
          The fleet name to display.
        :type OptimizeForEndUserLocation: boolean
        :param OptimizeForEndUserLocation:
          The option to optimize for better performance by routing traffic through the closest AWS Region to users, which may be outside of your home Region.
        :rtype: dict
        :returns:
        """
        pass

    def delete_fleet(self, FleetArn: str) -> Dict:
        """
        Deletes a fleet. Prevents users from accessing previously associated websites. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/DeleteFleet>`_
        
        **Request Syntax**
        ::
          response = client.delete_fleet(
              FleetArn='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**
          The ARN of the fleet.
        :rtype: dict
        :returns:
        """
        pass

    def describe_audit_stream_configuration(self, FleetArn: str) -> Dict:
        """
        Describes the configuration for delivering audit streams to the customer account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/DescribeAuditStreamConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.describe_audit_stream_configuration(
              FleetArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'AuditStreamArn': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AuditStreamArn** *(string) --* 
              The ARN of the Amazon Kinesis data stream that will receive the audit events.
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**
          The ARN of the fleet.
        :rtype: dict
        :returns:
        """
        pass

    def describe_company_network_configuration(self, FleetArn: str) -> Dict:
        """
        Describes the networking configuration to access the internal websites associated with the specified fleet.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/DescribeCompanyNetworkConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.describe_company_network_configuration(
              FleetArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'VpcId': 'string',
                'SubnetIds': [
                    'string',
                ],
                'SecurityGroupIds': [
                    'string',
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **VpcId** *(string) --* 
              The VPC with connectivity to associated websites.
            - **SubnetIds** *(list) --* 
              The subnets used for X-ENI connections from Amazon WorkLink rendering containers.
              - *(string) --* 
            - **SecurityGroupIds** *(list) --* 
              The security groups associated with access to the provided subnets.
              - *(string) --* 
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**
          The ARN of the fleet.
        :rtype: dict
        :returns:
        """
        pass

    def describe_device(self, FleetArn: str, DeviceId: str) -> Dict:
        """
        Provides information about a user's device.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/DescribeDevice>`_
        
        **Request Syntax**
        ::
          response = client.describe_device(
              FleetArn='string',
              DeviceId='string'
          )
        
        **Response Syntax**
        ::
            {
                'Status': 'ACTIVE'|'SIGNED_OUT',
                'Model': 'string',
                'Manufacturer': 'string',
                'OperatingSystem': 'string',
                'OperatingSystemVersion': 'string',
                'PatchLevel': 'string',
                'FirstAccessedTime': datetime(2015, 1, 1),
                'LastAccessedTime': datetime(2015, 1, 1),
                'Username': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Status** *(string) --* 
              The current state of the device.
            - **Model** *(string) --* 
              The model of the device.
            - **Manufacturer** *(string) --* 
              The manufacturer of the device.
            - **OperatingSystem** *(string) --* 
              The operating system of the device.
            - **OperatingSystemVersion** *(string) --* 
              The operating system version of the device.
            - **PatchLevel** *(string) --* 
              The operating system patch level of the device.
            - **FirstAccessedTime** *(datetime) --* 
              The date that the device first signed in to Amazon WorkLink.
            - **LastAccessedTime** *(datetime) --* 
              The date that the device last accessed Amazon WorkLink.
            - **Username** *(string) --* 
              The user name associated with the device.
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**
          The ARN of the fleet.
        :type DeviceId: string
        :param DeviceId: **[REQUIRED]**
          A unique identifier for a registered user\'s device.
        :rtype: dict
        :returns:
        """
        pass

    def describe_device_policy_configuration(self, FleetArn: str) -> Dict:
        """
        Describes the device policy configuration for the specified fleet.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/DescribeDevicePolicyConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.describe_device_policy_configuration(
              FleetArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'DeviceCaCertificate': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DeviceCaCertificate** *(string) --* 
              The certificate chain, including intermediate certificates and the root certificate authority certificate used to issue device certificates.
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**
          The ARN of the fleet.
        :rtype: dict
        :returns:
        """
        pass

    def describe_domain(self, FleetArn: str, DomainName: str) -> Dict:
        """
        Provides information about the domain.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/DescribeDomain>`_
        
        **Request Syntax**
        ::
          response = client.describe_domain(
              FleetArn='string',
              DomainName='string'
          )
        
        **Response Syntax**
        ::
            {
                'DisplayName': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'DomainStatus': 'PENDING_VALIDATION'|'ASSOCIATING'|'ACTIVE'|'INACTIVE'|'DISASSOCIATING'|'DISASSOCIATED'|'FAILED_TO_ASSOCIATE'|'FAILED_TO_DISASSOCIATE'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DisplayName** *(string) --* 
              The name to display.
            - **CreatedTime** *(datetime) --* 
              The time that the domain was added.
            - **DomainStatus** *(string) --* 
              The current state for the domain.
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**
          The ARN of the fleet.
        :type DomainName: string
        :param DomainName: **[REQUIRED]**
          The name of the domain.
        :rtype: dict
        :returns:
        """
        pass

    def describe_fleet_metadata(self, FleetArn: str) -> Dict:
        """
        Provides basic information for the specified fleet, excluding identity provider, networking, and device configuration details.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/DescribeFleetMetadata>`_
        
        **Request Syntax**
        ::
          response = client.describe_fleet_metadata(
              FleetArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'CreatedTime': datetime(2015, 1, 1),
                'LastUpdatedTime': datetime(2015, 1, 1),
                'FleetName': 'string',
                'DisplayName': 'string',
                'OptimizeForEndUserLocation': True|False,
                'CompanyCode': 'string',
                'FleetStatus': 'CREATING'|'ACTIVE'|'DELETING'|'DELETED'|'FAILED_TO_CREATE'|'FAILED_TO_DELETE'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **CreatedTime** *(datetime) --* 
              The time that the fleet was created.
            - **LastUpdatedTime** *(datetime) --* 
              The time that the fleet was last updated.
            - **FleetName** *(string) --* 
              The name of the fleet.
            - **DisplayName** *(string) --* 
              The name to display.
            - **OptimizeForEndUserLocation** *(boolean) --* 
              The option to optimize for better performance by routing traffic through the closest AWS Region to users, which may be outside of your home Region.
            - **CompanyCode** *(string) --* 
              The identifier used by users to sign in to the Amazon WorkLink app.
            - **FleetStatus** *(string) --* 
              The current state of the fleet.
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**
          The ARN of the fleet.
        :rtype: dict
        :returns:
        """
        pass

    def describe_identity_provider_configuration(self, FleetArn: str) -> Dict:
        """
        Describes the identity provider configuration of the specified fleet.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/DescribeIdentityProviderConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.describe_identity_provider_configuration(
              FleetArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'IdentityProviderType': 'SAML',
                'ServiceProviderSamlMetadata': 'string',
                'IdentityProviderSamlMetadata': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **IdentityProviderType** *(string) --* 
              The type of identity provider.
            - **ServiceProviderSamlMetadata** *(string) --* 
              The SAML metadata document uploaded to the user’s identity provider.
            - **IdentityProviderSamlMetadata** *(string) --* 
              The SAML metadata document provided by the user’s identity provider.
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**
          The ARN of the fleet.
        :rtype: dict
        :returns:
        """
        pass

    def describe_website_certificate_authority(self, FleetArn: str, WebsiteCaId: str) -> Dict:
        """
        Provides information about the certificate authority.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/DescribeWebsiteCertificateAuthority>`_
        
        **Request Syntax**
        ::
          response = client.describe_website_certificate_authority(
              FleetArn='string',
              WebsiteCaId='string'
          )
        
        **Response Syntax**
        ::
            {
                'Certificate': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'DisplayName': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Certificate** *(string) --* 
              The root certificate of the certificate authority.
            - **CreatedTime** *(datetime) --* 
              The time that the certificate authority was added.
            - **DisplayName** *(string) --* 
              The certificate name to display.
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**
          The ARN of the fleet.
        :type WebsiteCaId: string
        :param WebsiteCaId: **[REQUIRED]**
          A unique identifier for the certificate authority.
        :rtype: dict
        :returns:
        """
        pass

    def disassociate_domain(self, FleetArn: str, DomainName: str) -> Dict:
        """
        Disassociates a domain from Amazon WorkLink. End users lose the ability to access the domain with Amazon WorkLink. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/DisassociateDomain>`_
        
        **Request Syntax**
        ::
          response = client.disassociate_domain(
              FleetArn='string',
              DomainName='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**
          The ARN of the fleet.
        :type DomainName: string
        :param DomainName: **[REQUIRED]**
          The name of the domain.
        :rtype: dict
        :returns:
        """
        pass

    def disassociate_website_certificate_authority(self, FleetArn: str, WebsiteCaId: str) -> Dict:
        """
        Removes a certificate authority (CA).
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/DisassociateWebsiteCertificateAuthority>`_
        
        **Request Syntax**
        ::
          response = client.disassociate_website_certificate_authority(
              FleetArn='string',
              WebsiteCaId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**
          The ARN of the fleet.
        :type WebsiteCaId: string
        :param WebsiteCaId: **[REQUIRED]**
          A unique identifier for the CA.
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

    def list_devices(self, FleetArn: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Retrieves a list of devices registered with the specified fleet.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/ListDevices>`_
        
        **Request Syntax**
        ::
          response = client.list_devices(
              FleetArn='string',
              NextToken='string',
              MaxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'Devices': [
                    {
                        'DeviceId': 'string',
                        'DeviceStatus': 'ACTIVE'|'SIGNED_OUT'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Devices** *(list) --* 
              Information about the devices.
              - *(dict) --* 
                The summary of devices.
                - **DeviceId** *(string) --* 
                  The ID of the device.
                - **DeviceStatus** *(string) --* 
                  The status of the device.
            - **NextToken** *(string) --* 
              The pagination token used to retrieve the next page of results for this operation. If there are no more pages, this value is null.
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**
          The ARN of the fleet.
        :type NextToken: string
        :param NextToken:
          The pagination token used to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of results to be included in the next page.
        :rtype: dict
        :returns:
        """
        pass

    def list_domains(self, FleetArn: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Retrieves a list of domains associated to a specified fleet.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/ListDomains>`_
        
        **Request Syntax**
        ::
          response = client.list_domains(
              FleetArn='string',
              NextToken='string',
              MaxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'Domains': [
                    {
                        'DomainName': 'string',
                        'CreatedTime': datetime(2015, 1, 1),
                        'DomainStatus': 'PENDING_VALIDATION'|'ASSOCIATING'|'ACTIVE'|'INACTIVE'|'DISASSOCIATING'|'DISASSOCIATED'|'FAILED_TO_ASSOCIATE'|'FAILED_TO_DISASSOCIATE',
                        'DisplayName': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Domains** *(list) --* 
              Information about the domains.
              - *(dict) --* 
                The summary of the domain.
                - **DomainName** *(string) --* 
                  The name of the domain.
                - **CreatedTime** *(datetime) --* 
                  The time that the domain was created.
                - **DomainStatus** *(string) --* 
                  The status of the domain.
                - **DisplayName** *(string) --* 
                  The name to display.
            - **NextToken** *(string) --* 
              The pagination token used to retrieve the next page of results for this operation. If there are no more pages, this value is null.
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**
          The ARN of the fleet.
        :type NextToken: string
        :param NextToken:
          The pagination token used to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of results to be included in the next page.
        :rtype: dict
        :returns:
        """
        pass

    def list_fleets(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Retrieves a list of fleets for the current account and Region.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/ListFleets>`_
        
        **Request Syntax**
        ::
          response = client.list_fleets(
              NextToken='string',
              MaxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'FleetSummaryList': [
                    {
                        'FleetArn': 'string',
                        'CreatedTime': datetime(2015, 1, 1),
                        'LastUpdatedTime': datetime(2015, 1, 1),
                        'FleetName': 'string',
                        'DisplayName': 'string',
                        'CompanyCode': 'string',
                        'FleetStatus': 'CREATING'|'ACTIVE'|'DELETING'|'DELETED'|'FAILED_TO_CREATE'|'FAILED_TO_DELETE'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **FleetSummaryList** *(list) --* 
              The summary list of the fleets.
              - *(dict) --* 
                The summary of the fleet.
                - **FleetArn** *(string) --* 
                  The ARN of the fleet.
                - **CreatedTime** *(datetime) --* 
                  The time when the fleet was created.
                - **LastUpdatedTime** *(datetime) --* 
                  The time when the fleet was last updated.
                - **FleetName** *(string) --* 
                  The name of the fleet.
                - **DisplayName** *(string) --* 
                  The name to display.
                - **CompanyCode** *(string) --* 
                  The identifier used by users to sign into the Amazon WorkLink app.
                - **FleetStatus** *(string) --* 
                  The status of the fleet.
            - **NextToken** *(string) --* 
              The pagination token used to retrieve the next page of results for this operation. If there are no more pages, this value is null.
        :type NextToken: string
        :param NextToken:
          The pagination token used to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of results to be included in the next page.
        :rtype: dict
        :returns:
        """
        pass

    def list_website_certificate_authorities(self, FleetArn: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        Retrieves a list of certificate authorities added for the current account and Region.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/ListWebsiteCertificateAuthorities>`_
        
        **Request Syntax**
        ::
          response = client.list_website_certificate_authorities(
              FleetArn='string',
              MaxResults=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'WebsiteCertificateAuthorities': [
                    {
                        'WebsiteCaId': 'string',
                        'CreatedTime': datetime(2015, 1, 1),
                        'DisplayName': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **WebsiteCertificateAuthorities** *(list) --* 
              Information about the certificates.
              - *(dict) --* 
                The summary of the certificate authority (CA).
                - **WebsiteCaId** *(string) --* 
                  A unique identifier for the CA.
                - **CreatedTime** *(datetime) --* 
                  The time when the CA was added.
                - **DisplayName** *(string) --* 
                  The name to display.
            - **NextToken** *(string) --* 
              The pagination token used to retrieve the next page of results for this operation. If there are no more pages, this value is null.
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**
          The ARN of the fleet.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of results to be included in the next page.
        :type NextToken: string
        :param NextToken:
          The pagination token used to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
        :rtype: dict
        :returns:
        """
        pass

    def restore_domain_access(self, FleetArn: str, DomainName: str) -> Dict:
        """
        Moves a domain to ACTIVE status if it was in the INACTIVE status.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/RestoreDomainAccess>`_
        
        **Request Syntax**
        ::
          response = client.restore_domain_access(
              FleetArn='string',
              DomainName='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**
          The ARN of the fleet.
        :type DomainName: string
        :param DomainName: **[REQUIRED]**
          The name of the domain.
        :rtype: dict
        :returns:
        """
        pass

    def revoke_domain_access(self, FleetArn: str, DomainName: str) -> Dict:
        """
        Moves a domain to INACTIVE status if it was in the ACTIVE status.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/RevokeDomainAccess>`_
        
        **Request Syntax**
        ::
          response = client.revoke_domain_access(
              FleetArn='string',
              DomainName='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**
          The ARN of the fleet.
        :type DomainName: string
        :param DomainName: **[REQUIRED]**
          The name of the domain.
        :rtype: dict
        :returns:
        """
        pass

    def sign_out_user(self, FleetArn: str, Username: str) -> Dict:
        """
        Signs the user out from all of their devices. The user can sign in again if they have valid credentials.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/SignOutUser>`_
        
        **Request Syntax**
        ::
          response = client.sign_out_user(
              FleetArn='string',
              Username='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**
          The ARN of the fleet.
        :type Username: string
        :param Username: **[REQUIRED]**
          The name of the user.
        :rtype: dict
        :returns:
        """
        pass

    def update_audit_stream_configuration(self, FleetArn: str, AuditStreamArn: str = None) -> Dict:
        """
        Updates the audit stream configuration for the fleet.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/UpdateAuditStreamConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.update_audit_stream_configuration(
              FleetArn='string',
              AuditStreamArn='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**
          The ARN of the fleet.
        :type AuditStreamArn: string
        :param AuditStreamArn:
          The ARN of the Amazon Kinesis data stream that receives the audit events.
        :rtype: dict
        :returns:
        """
        pass

    def update_company_network_configuration(self, FleetArn: str, VpcId: str, SubnetIds: List, SecurityGroupIds: List) -> Dict:
        """
        Updates the company network configuration for the fleet.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/UpdateCompanyNetworkConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.update_company_network_configuration(
              FleetArn='string',
              VpcId='string',
              SubnetIds=[
                  'string',
              ],
              SecurityGroupIds=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**
          The ARN of the fleet.
        :type VpcId: string
        :param VpcId: **[REQUIRED]**
          The VPC with connectivity to associated websites.
        :type SubnetIds: list
        :param SubnetIds: **[REQUIRED]**
          The subnets used for X-ENI connections from Amazon WorkLink rendering containers.
          - *(string) --*
        :type SecurityGroupIds: list
        :param SecurityGroupIds: **[REQUIRED]**
          The security groups associated with access to the provided subnets.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def update_device_policy_configuration(self, FleetArn: str, DeviceCaCertificate: str = None) -> Dict:
        """
        Updates the device policy configuration for the fleet.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/UpdateDevicePolicyConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.update_device_policy_configuration(
              FleetArn='string',
              DeviceCaCertificate='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**
          The ARN of the fleet.
        :type DeviceCaCertificate: string
        :param DeviceCaCertificate:
          The certificate chain, including intermediate certificates and the root certificate authority certificate used to issue device certificates.
        :rtype: dict
        :returns:
        """
        pass

    def update_domain_metadata(self, FleetArn: str, DomainName: str, DisplayName: str = None) -> Dict:
        """
        Updates domain metadata, such as DisplayName.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/UpdateDomainMetadata>`_
        
        **Request Syntax**
        ::
          response = client.update_domain_metadata(
              FleetArn='string',
              DomainName='string',
              DisplayName='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**
          The ARN of the fleet.
        :type DomainName: string
        :param DomainName: **[REQUIRED]**
          The name of the domain.
        :type DisplayName: string
        :param DisplayName:
          The name to display.
        :rtype: dict
        :returns:
        """
        pass

    def update_fleet_metadata(self, FleetArn: str, DisplayName: str = None, OptimizeForEndUserLocation: bool = None) -> Dict:
        """
        Updates fleet metadata, such as DisplayName.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/UpdateFleetMetadata>`_
        
        **Request Syntax**
        ::
          response = client.update_fleet_metadata(
              FleetArn='string',
              DisplayName='string',
              OptimizeForEndUserLocation=True|False
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**
          The ARN of the fleet.
        :type DisplayName: string
        :param DisplayName:
          The fleet name to display. The existing DisplayName is unset if null is passed.
        :type OptimizeForEndUserLocation: boolean
        :param OptimizeForEndUserLocation:
          The option to optimize for better performance by routing traffic through the closest AWS Region to users, which may be outside of your home Region.
        :rtype: dict
        :returns:
        """
        pass

    def update_identity_provider_configuration(self, FleetArn: str, IdentityProviderType: str, IdentityProviderSamlMetadata: str = None) -> Dict:
        """
        Updates the identity provider configuration for the fleet.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/worklink-2018-09-25/UpdateIdentityProviderConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.update_identity_provider_configuration(
              FleetArn='string',
              IdentityProviderType='SAML',
              IdentityProviderSamlMetadata='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type FleetArn: string
        :param FleetArn: **[REQUIRED]**
          The ARN of the fleet.
        :type IdentityProviderType: string
        :param IdentityProviderType: **[REQUIRED]**
          The type of identity provider.
        :type IdentityProviderSamlMetadata: string
        :param IdentityProviderSamlMetadata:
          The SAML metadata document provided by the customer’s identity provider. The existing IdentityProviderSamlMetadata is unset if null is passed.
        :rtype: dict
        :returns:
        """
        pass
