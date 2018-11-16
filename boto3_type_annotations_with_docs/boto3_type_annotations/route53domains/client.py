from datetime import datetime
from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
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

    def check_domain_availability(self, DomainName: str, IdnLangCode: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/CheckDomainAvailability>`_
        
        **Request Syntax** 
        ::
        
          response = client.check_domain_availability(
              DomainName=\'string\',
              IdnLangCode=\'string\'
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]** 
        
          The name of the domain that you want to get availability for.
        
          Constraints: The domain name can contain only the letters a through z, the numbers 0 through 9, and hyphen (-). Internationalized Domain Names are not supported.
        
        :type IdnLangCode: string
        :param IdnLangCode: 
        
          Reserved for future use.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Availability\': \'AVAILABLE\'|\'AVAILABLE_RESERVED\'|\'AVAILABLE_PREORDER\'|\'UNAVAILABLE\'|\'UNAVAILABLE_PREMIUM\'|\'UNAVAILABLE_RESTRICTED\'|\'RESERVED\'|\'DONT_KNOW\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The CheckDomainAvailability response includes the following elements.
        
            - **Availability** *(string) --* 
        
              Whether the domain name is available for registering.
        
              .. note::
        
                You can register only domains designated as ``AVAILABLE`` .
        
              Valid values:
        
                AVAILABLE  
        
              The domain name is available.
        
                AVAILABLE_RESERVED  
        
              The domain name is reserved under specific conditions.
        
                AVAILABLE_PREORDER  
        
              The domain name is available and can be preordered.
        
                DONT_KNOW  
        
              The TLD registry didn\'t reply with a definitive answer about whether the domain name is available. Amazon Route 53 can return this response for a variety of reasons, for example, the registry is performing maintenance. Try again later.
        
                PENDING  
        
              The TLD registry didn\'t return a response in the expected amount of time. When the response is delayed, it usually takes just a few extra seconds. You can resubmit the request immediately.
        
                RESERVED  
        
              The domain name has been reserved for another person or organization.
        
                UNAVAILABLE  
        
              The domain name is not available.
        
                UNAVAILABLE_PREMIUM  
        
              The domain name is not available.
        
                UNAVAILABLE_RESTRICTED  
        
              The domain name is forbidden.
        
        """
        pass

    def check_domain_transferability(self, DomainName: str, AuthCode: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/CheckDomainTransferability>`_
        
        **Request Syntax** 
        ::
        
          response = client.check_domain_transferability(
              DomainName=\'string\',
              AuthCode=\'string\'
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]** 
        
          The name of the domain that you want to transfer to Amazon Route 53.
        
          Constraints: The domain name can contain only the letters a through z, the numbers 0 through 9, and hyphen (-). Internationalized Domain Names are not supported.
        
        :type AuthCode: string
        :param AuthCode: 
        
          If the registrar for the top-level domain (TLD) requires an authorization code to transfer the domain, the code that you got from the current registrar for the domain.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Transferability\': {
                    \'Transferable\': \'TRANSFERABLE\'|\'UNTRANSFERABLE\'|\'DONT_KNOW\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The CheckDomainTransferability response includes the following elements.
        
            - **Transferability** *(dict) --* 
        
              A complex type that contains information about whether the specified domain can be transferred to Amazon Route 53.
        
              - **Transferable** *(string) --* 
        
                Whether the domain name can be transferred to Amazon Route 53.
        
                .. note::
        
                  You can transfer only domains that have a value of ``TRANSFERABLE`` for ``Transferable`` .
        
                Valid values:
        
                  TRANSFERABLE  
        
                The domain name can be transferred to Amazon Route 53.
        
                  UNTRANSFERRABLE  
        
                The domain name can\'t be transferred to Amazon Route 53.
        
                  DONT_KNOW  
        
                Reserved for future use.
        
        """
        pass

    def delete_tags_for_domain(self, DomainName: str, TagsToDelete: List) -> Dict:
        """
        
        All tag operations are eventually consistent; subsequent operations might not immediately represent all issued operations.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/DeleteTagsForDomain>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_tags_for_domain(
              DomainName=\'string\',
              TagsToDelete=[
                  \'string\',
              ]
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]** 
        
          The domain for which you want to delete one or more tags.
        
        :type TagsToDelete: list
        :param TagsToDelete: **[REQUIRED]** 
        
          A list of tag keys to delete.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def disable_domain_auto_renew(self, DomainName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/DisableDomainAutoRenew>`_
        
        **Request Syntax** 
        ::
        
          response = client.disable_domain_auto_renew(
              DomainName=\'string\'
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]** 
        
          The name of the domain that you want to disable automatic renewal for.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def disable_domain_transfer_lock(self, DomainName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/DisableDomainTransferLock>`_
        
        **Request Syntax** 
        ::
        
          response = client.disable_domain_transfer_lock(
              DomainName=\'string\'
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]** 
        
          The name of the domain that you want to remove the transfer lock for.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'OperationId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The DisableDomainTransferLock response includes the following element.
        
            - **OperationId** *(string) --* 
        
              Identifier for tracking the progress of the request. To use this ID to query the operation status, use  GetOperationDetail .
        
        """
        pass

    def enable_domain_auto_renew(self, DomainName: str) -> Dict:
        """
        
        The period during which you can renew a domain name varies by TLD. For a list of TLDs and their renewal policies, see `\"Renewal, restoration, and deletion times\" <http://wiki.gandi.net/en/domains/renew#renewal_restoration_and_deletion_times>`__ on the website for our registrar associate, Gandi. Amazon Route 53 requires that you renew before the end of the renewal period that is listed on the Gandi website so we can complete processing before the deadline.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/EnableDomainAutoRenew>`_
        
        **Request Syntax** 
        ::
        
          response = client.enable_domain_auto_renew(
              DomainName=\'string\'
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]** 
        
          The name of the domain that you want to enable automatic renewal for.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def enable_domain_transfer_lock(self, DomainName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/EnableDomainTransferLock>`_
        
        **Request Syntax** 
        ::
        
          response = client.enable_domain_transfer_lock(
              DomainName=\'string\'
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]** 
        
          The name of the domain that you want to set the transfer lock for.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'OperationId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The EnableDomainTransferLock response includes the following elements.
        
            - **OperationId** *(string) --* 
        
              Identifier for tracking the progress of the request. To use this ID to query the operation status, use GetOperationDetail.
        
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

    def get_contact_reachability_status(self, domainName: str = None) -> Dict:
        """
        
        If you want us to resend the email, use the ``ResendContactReachabilityEmail`` operation.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/GetContactReachabilityStatus>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_contact_reachability_status(
              domainName=\'string\'
          )
        :type domainName: string
        :param domainName: 
        
          The name of the domain for which you want to know whether the registrant contact has confirmed that the email address is valid.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'domainName\': \'string\',
                \'status\': \'PENDING\'|\'DONE\'|\'EXPIRED\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **domainName** *(string) --* 
        
              The domain name for which you requested the reachability status.
        
            - **status** *(string) --* 
        
              Whether the registrant contact has responded. Values include the following:
        
                PENDING  
        
              We sent the confirmation email and haven\'t received a response yet.
        
                DONE  
        
              We sent the email and got confirmation from the registrant contact.
        
                EXPIRED  
        
              The time limit expired before the registrant contact responded.
        
        """
        pass

    def get_domain_detail(self, DomainName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/GetDomainDetail>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_domain_detail(
              DomainName=\'string\'
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]** 
        
          The name of the domain that you want to get detailed information about.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DomainName\': \'string\',
                \'Nameservers\': [
                    {
                        \'Name\': \'string\',
                        \'GlueIps\': [
                            \'string\',
                        ]
                    },
                ],
                \'AutoRenew\': True|False,
                \'AdminContact\': {
                    \'FirstName\': \'string\',
                    \'LastName\': \'string\',
                    \'ContactType\': \'PERSON\'|\'COMPANY\'|\'ASSOCIATION\'|\'PUBLIC_BODY\'|\'RESELLER\',
                    \'OrganizationName\': \'string\',
                    \'AddressLine1\': \'string\',
                    \'AddressLine2\': \'string\',
                    \'City\': \'string\',
                    \'State\': \'string\',
                    \'CountryCode\': \'AD\'|\'AE\'|\'AF\'|\'AG\'|\'AI\'|\'AL\'|\'AM\'|\'AN\'|\'AO\'|\'AQ\'|\'AR\'|\'AS\'|\'AT\'|\'AU\'|\'AW\'|\'AZ\'|\'BA\'|\'BB\'|\'BD\'|\'BE\'|\'BF\'|\'BG\'|\'BH\'|\'BI\'|\'BJ\'|\'BL\'|\'BM\'|\'BN\'|\'BO\'|\'BR\'|\'BS\'|\'BT\'|\'BW\'|\'BY\'|\'BZ\'|\'CA\'|\'CC\'|\'CD\'|\'CF\'|\'CG\'|\'CH\'|\'CI\'|\'CK\'|\'CL\'|\'CM\'|\'CN\'|\'CO\'|\'CR\'|\'CU\'|\'CV\'|\'CX\'|\'CY\'|\'CZ\'|\'DE\'|\'DJ\'|\'DK\'|\'DM\'|\'DO\'|\'DZ\'|\'EC\'|\'EE\'|\'EG\'|\'ER\'|\'ES\'|\'ET\'|\'FI\'|\'FJ\'|\'FK\'|\'FM\'|\'FO\'|\'FR\'|\'GA\'|\'GB\'|\'GD\'|\'GE\'|\'GH\'|\'GI\'|\'GL\'|\'GM\'|\'GN\'|\'GQ\'|\'GR\'|\'GT\'|\'GU\'|\'GW\'|\'GY\'|\'HK\'|\'HN\'|\'HR\'|\'HT\'|\'HU\'|\'ID\'|\'IE\'|\'IL\'|\'IM\'|\'IN\'|\'IQ\'|\'IR\'|\'IS\'|\'IT\'|\'JM\'|\'JO\'|\'JP\'|\'KE\'|\'KG\'|\'KH\'|\'KI\'|\'KM\'|\'KN\'|\'KP\'|\'KR\'|\'KW\'|\'KY\'|\'KZ\'|\'LA\'|\'LB\'|\'LC\'|\'LI\'|\'LK\'|\'LR\'|\'LS\'|\'LT\'|\'LU\'|\'LV\'|\'LY\'|\'MA\'|\'MC\'|\'MD\'|\'ME\'|\'MF\'|\'MG\'|\'MH\'|\'MK\'|\'ML\'|\'MM\'|\'MN\'|\'MO\'|\'MP\'|\'MR\'|\'MS\'|\'MT\'|\'MU\'|\'MV\'|\'MW\'|\'MX\'|\'MY\'|\'MZ\'|\'NA\'|\'NC\'|\'NE\'|\'NG\'|\'NI\'|\'NL\'|\'NO\'|\'NP\'|\'NR\'|\'NU\'|\'NZ\'|\'OM\'|\'PA\'|\'PE\'|\'PF\'|\'PG\'|\'PH\'|\'PK\'|\'PL\'|\'PM\'|\'PN\'|\'PR\'|\'PT\'|\'PW\'|\'PY\'|\'QA\'|\'RO\'|\'RS\'|\'RU\'|\'RW\'|\'SA\'|\'SB\'|\'SC\'|\'SD\'|\'SE\'|\'SG\'|\'SH\'|\'SI\'|\'SK\'|\'SL\'|\'SM\'|\'SN\'|\'SO\'|\'SR\'|\'ST\'|\'SV\'|\'SY\'|\'SZ\'|\'TC\'|\'TD\'|\'TG\'|\'TH\'|\'TJ\'|\'TK\'|\'TL\'|\'TM\'|\'TN\'|\'TO\'|\'TR\'|\'TT\'|\'TV\'|\'TW\'|\'TZ\'|\'UA\'|\'UG\'|\'US\'|\'UY\'|\'UZ\'|\'VA\'|\'VC\'|\'VE\'|\'VG\'|\'VI\'|\'VN\'|\'VU\'|\'WF\'|\'WS\'|\'YE\'|\'YT\'|\'ZA\'|\'ZM\'|\'ZW\',
                    \'ZipCode\': \'string\',
                    \'PhoneNumber\': \'string\',
                    \'Email\': \'string\',
                    \'Fax\': \'string\',
                    \'ExtraParams\': [
                        {
                            \'Name\': \'DUNS_NUMBER\'|\'BRAND_NUMBER\'|\'BIRTH_DEPARTMENT\'|\'BIRTH_DATE_IN_YYYY_MM_DD\'|\'BIRTH_COUNTRY\'|\'BIRTH_CITY\'|\'DOCUMENT_NUMBER\'|\'AU_ID_NUMBER\'|\'AU_ID_TYPE\'|\'CA_LEGAL_TYPE\'|\'CA_BUSINESS_ENTITY_TYPE\'|\'ES_IDENTIFICATION\'|\'ES_IDENTIFICATION_TYPE\'|\'ES_LEGAL_FORM\'|\'FI_BUSINESS_NUMBER\'|\'FI_ID_NUMBER\'|\'FI_NATIONALITY\'|\'FI_ORGANIZATION_TYPE\'|\'IT_PIN\'|\'IT_REGISTRANT_ENTITY_TYPE\'|\'RU_PASSPORT_DATA\'|\'SE_ID_NUMBER\'|\'SG_ID_NUMBER\'|\'VAT_NUMBER\'|\'UK_CONTACT_TYPE\'|\'UK_COMPANY_NUMBER\',
                            \'Value\': \'string\'
                        },
                    ]
                },
                \'RegistrantContact\': {
                    \'FirstName\': \'string\',
                    \'LastName\': \'string\',
                    \'ContactType\': \'PERSON\'|\'COMPANY\'|\'ASSOCIATION\'|\'PUBLIC_BODY\'|\'RESELLER\',
                    \'OrganizationName\': \'string\',
                    \'AddressLine1\': \'string\',
                    \'AddressLine2\': \'string\',
                    \'City\': \'string\',
                    \'State\': \'string\',
                    \'CountryCode\': \'AD\'|\'AE\'|\'AF\'|\'AG\'|\'AI\'|\'AL\'|\'AM\'|\'AN\'|\'AO\'|\'AQ\'|\'AR\'|\'AS\'|\'AT\'|\'AU\'|\'AW\'|\'AZ\'|\'BA\'|\'BB\'|\'BD\'|\'BE\'|\'BF\'|\'BG\'|\'BH\'|\'BI\'|\'BJ\'|\'BL\'|\'BM\'|\'BN\'|\'BO\'|\'BR\'|\'BS\'|\'BT\'|\'BW\'|\'BY\'|\'BZ\'|\'CA\'|\'CC\'|\'CD\'|\'CF\'|\'CG\'|\'CH\'|\'CI\'|\'CK\'|\'CL\'|\'CM\'|\'CN\'|\'CO\'|\'CR\'|\'CU\'|\'CV\'|\'CX\'|\'CY\'|\'CZ\'|\'DE\'|\'DJ\'|\'DK\'|\'DM\'|\'DO\'|\'DZ\'|\'EC\'|\'EE\'|\'EG\'|\'ER\'|\'ES\'|\'ET\'|\'FI\'|\'FJ\'|\'FK\'|\'FM\'|\'FO\'|\'FR\'|\'GA\'|\'GB\'|\'GD\'|\'GE\'|\'GH\'|\'GI\'|\'GL\'|\'GM\'|\'GN\'|\'GQ\'|\'GR\'|\'GT\'|\'GU\'|\'GW\'|\'GY\'|\'HK\'|\'HN\'|\'HR\'|\'HT\'|\'HU\'|\'ID\'|\'IE\'|\'IL\'|\'IM\'|\'IN\'|\'IQ\'|\'IR\'|\'IS\'|\'IT\'|\'JM\'|\'JO\'|\'JP\'|\'KE\'|\'KG\'|\'KH\'|\'KI\'|\'KM\'|\'KN\'|\'KP\'|\'KR\'|\'KW\'|\'KY\'|\'KZ\'|\'LA\'|\'LB\'|\'LC\'|\'LI\'|\'LK\'|\'LR\'|\'LS\'|\'LT\'|\'LU\'|\'LV\'|\'LY\'|\'MA\'|\'MC\'|\'MD\'|\'ME\'|\'MF\'|\'MG\'|\'MH\'|\'MK\'|\'ML\'|\'MM\'|\'MN\'|\'MO\'|\'MP\'|\'MR\'|\'MS\'|\'MT\'|\'MU\'|\'MV\'|\'MW\'|\'MX\'|\'MY\'|\'MZ\'|\'NA\'|\'NC\'|\'NE\'|\'NG\'|\'NI\'|\'NL\'|\'NO\'|\'NP\'|\'NR\'|\'NU\'|\'NZ\'|\'OM\'|\'PA\'|\'PE\'|\'PF\'|\'PG\'|\'PH\'|\'PK\'|\'PL\'|\'PM\'|\'PN\'|\'PR\'|\'PT\'|\'PW\'|\'PY\'|\'QA\'|\'RO\'|\'RS\'|\'RU\'|\'RW\'|\'SA\'|\'SB\'|\'SC\'|\'SD\'|\'SE\'|\'SG\'|\'SH\'|\'SI\'|\'SK\'|\'SL\'|\'SM\'|\'SN\'|\'SO\'|\'SR\'|\'ST\'|\'SV\'|\'SY\'|\'SZ\'|\'TC\'|\'TD\'|\'TG\'|\'TH\'|\'TJ\'|\'TK\'|\'TL\'|\'TM\'|\'TN\'|\'TO\'|\'TR\'|\'TT\'|\'TV\'|\'TW\'|\'TZ\'|\'UA\'|\'UG\'|\'US\'|\'UY\'|\'UZ\'|\'VA\'|\'VC\'|\'VE\'|\'VG\'|\'VI\'|\'VN\'|\'VU\'|\'WF\'|\'WS\'|\'YE\'|\'YT\'|\'ZA\'|\'ZM\'|\'ZW\',
                    \'ZipCode\': \'string\',
                    \'PhoneNumber\': \'string\',
                    \'Email\': \'string\',
                    \'Fax\': \'string\',
                    \'ExtraParams\': [
                        {
                            \'Name\': \'DUNS_NUMBER\'|\'BRAND_NUMBER\'|\'BIRTH_DEPARTMENT\'|\'BIRTH_DATE_IN_YYYY_MM_DD\'|\'BIRTH_COUNTRY\'|\'BIRTH_CITY\'|\'DOCUMENT_NUMBER\'|\'AU_ID_NUMBER\'|\'AU_ID_TYPE\'|\'CA_LEGAL_TYPE\'|\'CA_BUSINESS_ENTITY_TYPE\'|\'ES_IDENTIFICATION\'|\'ES_IDENTIFICATION_TYPE\'|\'ES_LEGAL_FORM\'|\'FI_BUSINESS_NUMBER\'|\'FI_ID_NUMBER\'|\'FI_NATIONALITY\'|\'FI_ORGANIZATION_TYPE\'|\'IT_PIN\'|\'IT_REGISTRANT_ENTITY_TYPE\'|\'RU_PASSPORT_DATA\'|\'SE_ID_NUMBER\'|\'SG_ID_NUMBER\'|\'VAT_NUMBER\'|\'UK_CONTACT_TYPE\'|\'UK_COMPANY_NUMBER\',
                            \'Value\': \'string\'
                        },
                    ]
                },
                \'TechContact\': {
                    \'FirstName\': \'string\',
                    \'LastName\': \'string\',
                    \'ContactType\': \'PERSON\'|\'COMPANY\'|\'ASSOCIATION\'|\'PUBLIC_BODY\'|\'RESELLER\',
                    \'OrganizationName\': \'string\',
                    \'AddressLine1\': \'string\',
                    \'AddressLine2\': \'string\',
                    \'City\': \'string\',
                    \'State\': \'string\',
                    \'CountryCode\': \'AD\'|\'AE\'|\'AF\'|\'AG\'|\'AI\'|\'AL\'|\'AM\'|\'AN\'|\'AO\'|\'AQ\'|\'AR\'|\'AS\'|\'AT\'|\'AU\'|\'AW\'|\'AZ\'|\'BA\'|\'BB\'|\'BD\'|\'BE\'|\'BF\'|\'BG\'|\'BH\'|\'BI\'|\'BJ\'|\'BL\'|\'BM\'|\'BN\'|\'BO\'|\'BR\'|\'BS\'|\'BT\'|\'BW\'|\'BY\'|\'BZ\'|\'CA\'|\'CC\'|\'CD\'|\'CF\'|\'CG\'|\'CH\'|\'CI\'|\'CK\'|\'CL\'|\'CM\'|\'CN\'|\'CO\'|\'CR\'|\'CU\'|\'CV\'|\'CX\'|\'CY\'|\'CZ\'|\'DE\'|\'DJ\'|\'DK\'|\'DM\'|\'DO\'|\'DZ\'|\'EC\'|\'EE\'|\'EG\'|\'ER\'|\'ES\'|\'ET\'|\'FI\'|\'FJ\'|\'FK\'|\'FM\'|\'FO\'|\'FR\'|\'GA\'|\'GB\'|\'GD\'|\'GE\'|\'GH\'|\'GI\'|\'GL\'|\'GM\'|\'GN\'|\'GQ\'|\'GR\'|\'GT\'|\'GU\'|\'GW\'|\'GY\'|\'HK\'|\'HN\'|\'HR\'|\'HT\'|\'HU\'|\'ID\'|\'IE\'|\'IL\'|\'IM\'|\'IN\'|\'IQ\'|\'IR\'|\'IS\'|\'IT\'|\'JM\'|\'JO\'|\'JP\'|\'KE\'|\'KG\'|\'KH\'|\'KI\'|\'KM\'|\'KN\'|\'KP\'|\'KR\'|\'KW\'|\'KY\'|\'KZ\'|\'LA\'|\'LB\'|\'LC\'|\'LI\'|\'LK\'|\'LR\'|\'LS\'|\'LT\'|\'LU\'|\'LV\'|\'LY\'|\'MA\'|\'MC\'|\'MD\'|\'ME\'|\'MF\'|\'MG\'|\'MH\'|\'MK\'|\'ML\'|\'MM\'|\'MN\'|\'MO\'|\'MP\'|\'MR\'|\'MS\'|\'MT\'|\'MU\'|\'MV\'|\'MW\'|\'MX\'|\'MY\'|\'MZ\'|\'NA\'|\'NC\'|\'NE\'|\'NG\'|\'NI\'|\'NL\'|\'NO\'|\'NP\'|\'NR\'|\'NU\'|\'NZ\'|\'OM\'|\'PA\'|\'PE\'|\'PF\'|\'PG\'|\'PH\'|\'PK\'|\'PL\'|\'PM\'|\'PN\'|\'PR\'|\'PT\'|\'PW\'|\'PY\'|\'QA\'|\'RO\'|\'RS\'|\'RU\'|\'RW\'|\'SA\'|\'SB\'|\'SC\'|\'SD\'|\'SE\'|\'SG\'|\'SH\'|\'SI\'|\'SK\'|\'SL\'|\'SM\'|\'SN\'|\'SO\'|\'SR\'|\'ST\'|\'SV\'|\'SY\'|\'SZ\'|\'TC\'|\'TD\'|\'TG\'|\'TH\'|\'TJ\'|\'TK\'|\'TL\'|\'TM\'|\'TN\'|\'TO\'|\'TR\'|\'TT\'|\'TV\'|\'TW\'|\'TZ\'|\'UA\'|\'UG\'|\'US\'|\'UY\'|\'UZ\'|\'VA\'|\'VC\'|\'VE\'|\'VG\'|\'VI\'|\'VN\'|\'VU\'|\'WF\'|\'WS\'|\'YE\'|\'YT\'|\'ZA\'|\'ZM\'|\'ZW\',
                    \'ZipCode\': \'string\',
                    \'PhoneNumber\': \'string\',
                    \'Email\': \'string\',
                    \'Fax\': \'string\',
                    \'ExtraParams\': [
                        {
                            \'Name\': \'DUNS_NUMBER\'|\'BRAND_NUMBER\'|\'BIRTH_DEPARTMENT\'|\'BIRTH_DATE_IN_YYYY_MM_DD\'|\'BIRTH_COUNTRY\'|\'BIRTH_CITY\'|\'DOCUMENT_NUMBER\'|\'AU_ID_NUMBER\'|\'AU_ID_TYPE\'|\'CA_LEGAL_TYPE\'|\'CA_BUSINESS_ENTITY_TYPE\'|\'ES_IDENTIFICATION\'|\'ES_IDENTIFICATION_TYPE\'|\'ES_LEGAL_FORM\'|\'FI_BUSINESS_NUMBER\'|\'FI_ID_NUMBER\'|\'FI_NATIONALITY\'|\'FI_ORGANIZATION_TYPE\'|\'IT_PIN\'|\'IT_REGISTRANT_ENTITY_TYPE\'|\'RU_PASSPORT_DATA\'|\'SE_ID_NUMBER\'|\'SG_ID_NUMBER\'|\'VAT_NUMBER\'|\'UK_CONTACT_TYPE\'|\'UK_COMPANY_NUMBER\',
                            \'Value\': \'string\'
                        },
                    ]
                },
                \'AdminPrivacy\': True|False,
                \'RegistrantPrivacy\': True|False,
                \'TechPrivacy\': True|False,
                \'RegistrarName\': \'string\',
                \'WhoIsServer\': \'string\',
                \'RegistrarUrl\': \'string\',
                \'AbuseContactEmail\': \'string\',
                \'AbuseContactPhone\': \'string\',
                \'RegistryDomainId\': \'string\',
                \'CreationDate\': datetime(2015, 1, 1),
                \'UpdatedDate\': datetime(2015, 1, 1),
                \'ExpirationDate\': datetime(2015, 1, 1),
                \'Reseller\': \'string\',
                \'DnsSec\': \'string\',
                \'StatusList\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The GetDomainDetail response includes the following elements.
        
            - **DomainName** *(string) --* 
        
              The name of a domain.
        
            - **Nameservers** *(list) --* 
        
              The name of the domain.
        
              - *(dict) --* 
        
                Nameserver includes the following elements.
        
                - **Name** *(string) --* 
        
                  The fully qualified host name of the name server.
        
                  Constraint: Maximum 255 characters
        
                - **GlueIps** *(list) --* 
        
                  Glue IP address of a name server entry. Glue IP addresses are required only when the name of the name server is a subdomain of the domain. For example, if your domain is example.com and the name server for the domain is ns.example.com, you need to specify the IP address for ns.example.com.
        
                  Constraints: The list can contain only one IPv4 and one IPv6 address.
        
                  - *(string) --* 
              
            - **AutoRenew** *(boolean) --* 
        
              Specifies whether the domain registration is set to renew automatically.
        
            - **AdminContact** *(dict) --* 
        
              Provides details about the domain administrative contact.
        
              - **FirstName** *(string) --* 
        
                First name of contact.
        
              - **LastName** *(string) --* 
        
                Last name of contact.
        
              - **ContactType** *(string) --* 
        
                Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than ``PERSON`` , you must enter an organization name, and you can\'t enable privacy protection for the contact.
        
              - **OrganizationName** *(string) --* 
        
                Name of the organization for contact types other than ``PERSON`` .
        
              - **AddressLine1** *(string) --* 
        
                First line of the contact\'s address.
        
              - **AddressLine2** *(string) --* 
        
                Second line of contact\'s address, if any.
        
              - **City** *(string) --* 
        
                The city of the contact\'s address.
        
              - **State** *(string) --* 
        
                The state or province of the contact\'s city.
        
              - **CountryCode** *(string) --* 
        
                Code for the country of the contact\'s address.
        
              - **ZipCode** *(string) --* 
        
                The zip or postal code of the contact\'s address.
        
              - **PhoneNumber** *(string) --* 
        
                The phone number of the contact.
        
                Constraints: Phone number must be specified in the format \"+[country dialing code].[number including any area code>]\". For example, a US phone number might appear as ``\"+1.1234567890\"`` .
        
              - **Email** *(string) --* 
        
                Email address of the contact.
        
              - **Fax** *(string) --* 
        
                Fax number of the contact.
        
                Constraints: Phone number must be specified in the format \"+[country dialing code].[number including any area code]\". For example, a US phone number might appear as ``\"+1.1234567890\"`` .
        
              - **ExtraParams** *(list) --* 
        
                A list of name-value pairs for parameters required by certain top-level domains.
        
                - *(dict) --* 
        
                  ExtraParam includes the following elements.
        
                  - **Name** *(string) --* 
        
                    Name of the additional parameter required by the top-level domain. Here are the top-level domains that require additional parameters and which parameters they require:
        
                    * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``   
                     
                    * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``   
                     
                    * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``   
                     
                    * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` , ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``   
                     
                    * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``   
                     
                    * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``   
                     
                    * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``   
                     
                    * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``   
                     
                    * **.sg:**  ``SG_ID_NUMBER``   
                     
                    * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``   
                     
                    In addition, many TLDs require ``VAT_NUMBER`` .
        
                  - **Value** *(string) --* 
        
                    Values corresponding to the additional parameter names required by some top-level domains.
        
            - **RegistrantContact** *(dict) --* 
        
              Provides details about the domain registrant.
        
              - **FirstName** *(string) --* 
        
                First name of contact.
        
              - **LastName** *(string) --* 
        
                Last name of contact.
        
              - **ContactType** *(string) --* 
        
                Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than ``PERSON`` , you must enter an organization name, and you can\'t enable privacy protection for the contact.
        
              - **OrganizationName** *(string) --* 
        
                Name of the organization for contact types other than ``PERSON`` .
        
              - **AddressLine1** *(string) --* 
        
                First line of the contact\'s address.
        
              - **AddressLine2** *(string) --* 
        
                Second line of contact\'s address, if any.
        
              - **City** *(string) --* 
        
                The city of the contact\'s address.
        
              - **State** *(string) --* 
        
                The state or province of the contact\'s city.
        
              - **CountryCode** *(string) --* 
        
                Code for the country of the contact\'s address.
        
              - **ZipCode** *(string) --* 
        
                The zip or postal code of the contact\'s address.
        
              - **PhoneNumber** *(string) --* 
        
                The phone number of the contact.
        
                Constraints: Phone number must be specified in the format \"+[country dialing code].[number including any area code>]\". For example, a US phone number might appear as ``\"+1.1234567890\"`` .
        
              - **Email** *(string) --* 
        
                Email address of the contact.
        
              - **Fax** *(string) --* 
        
                Fax number of the contact.
        
                Constraints: Phone number must be specified in the format \"+[country dialing code].[number including any area code]\". For example, a US phone number might appear as ``\"+1.1234567890\"`` .
        
              - **ExtraParams** *(list) --* 
        
                A list of name-value pairs for parameters required by certain top-level domains.
        
                - *(dict) --* 
        
                  ExtraParam includes the following elements.
        
                  - **Name** *(string) --* 
        
                    Name of the additional parameter required by the top-level domain. Here are the top-level domains that require additional parameters and which parameters they require:
        
                    * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``   
                     
                    * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``   
                     
                    * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``   
                     
                    * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` , ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``   
                     
                    * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``   
                     
                    * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``   
                     
                    * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``   
                     
                    * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``   
                     
                    * **.sg:**  ``SG_ID_NUMBER``   
                     
                    * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``   
                     
                    In addition, many TLDs require ``VAT_NUMBER`` .
        
                  - **Value** *(string) --* 
        
                    Values corresponding to the additional parameter names required by some top-level domains.
        
            - **TechContact** *(dict) --* 
        
              Provides details about the domain technical contact.
        
              - **FirstName** *(string) --* 
        
                First name of contact.
        
              - **LastName** *(string) --* 
        
                Last name of contact.
        
              - **ContactType** *(string) --* 
        
                Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than ``PERSON`` , you must enter an organization name, and you can\'t enable privacy protection for the contact.
        
              - **OrganizationName** *(string) --* 
        
                Name of the organization for contact types other than ``PERSON`` .
        
              - **AddressLine1** *(string) --* 
        
                First line of the contact\'s address.
        
              - **AddressLine2** *(string) --* 
        
                Second line of contact\'s address, if any.
        
              - **City** *(string) --* 
        
                The city of the contact\'s address.
        
              - **State** *(string) --* 
        
                The state or province of the contact\'s city.
        
              - **CountryCode** *(string) --* 
        
                Code for the country of the contact\'s address.
        
              - **ZipCode** *(string) --* 
        
                The zip or postal code of the contact\'s address.
        
              - **PhoneNumber** *(string) --* 
        
                The phone number of the contact.
        
                Constraints: Phone number must be specified in the format \"+[country dialing code].[number including any area code>]\". For example, a US phone number might appear as ``\"+1.1234567890\"`` .
        
              - **Email** *(string) --* 
        
                Email address of the contact.
        
              - **Fax** *(string) --* 
        
                Fax number of the contact.
        
                Constraints: Phone number must be specified in the format \"+[country dialing code].[number including any area code]\". For example, a US phone number might appear as ``\"+1.1234567890\"`` .
        
              - **ExtraParams** *(list) --* 
        
                A list of name-value pairs for parameters required by certain top-level domains.
        
                - *(dict) --* 
        
                  ExtraParam includes the following elements.
        
                  - **Name** *(string) --* 
        
                    Name of the additional parameter required by the top-level domain. Here are the top-level domains that require additional parameters and which parameters they require:
        
                    * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``   
                     
                    * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``   
                     
                    * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``   
                     
                    * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` , ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``   
                     
                    * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``   
                     
                    * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``   
                     
                    * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``   
                     
                    * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``   
                     
                    * **.sg:**  ``SG_ID_NUMBER``   
                     
                    * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``   
                     
                    In addition, many TLDs require ``VAT_NUMBER`` .
        
                  - **Value** *(string) --* 
        
                    Values corresponding to the additional parameter names required by some top-level domains.
        
            - **AdminPrivacy** *(boolean) --* 
        
              Specifies whether contact information is concealed from WHOIS queries. If the value is ``true`` , WHOIS (\"who is\") queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If the value is ``false`` , WHOIS queries return the information that you entered for the admin contact.
        
            - **RegistrantPrivacy** *(boolean) --* 
        
              Specifies whether contact information is concealed from WHOIS queries. If the value is ``true`` , WHOIS (\"who is\") queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If the value is ``false`` , WHOIS queries return the information that you entered for the registrant contact (domain owner).
        
            - **TechPrivacy** *(boolean) --* 
        
              Specifies whether contact information is concealed from WHOIS queries. If the value is ``true`` , WHOIS (\"who is\") queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If the value is ``false`` , WHOIS queries return the information that you entered for the technical contact.
        
            - **RegistrarName** *(string) --* 
        
              Name of the registrar of the domain as identified in the registry. Domains with a .com, .net, or .org TLD are registered by Amazon Registrar. All other domains are registered by our registrar associate, Gandi. The value for domains that are registered by Gandi is ``\"GANDI SAS\"`` . 
        
            - **WhoIsServer** *(string) --* 
        
              The fully qualified name of the WHOIS server that can answer the WHOIS query for the domain.
        
            - **RegistrarUrl** *(string) --* 
        
              Web address of the registrar.
        
            - **AbuseContactEmail** *(string) --* 
        
              Email address to contact to report incorrect contact information for a domain, to report that the domain is being used to send spam, to report that someone is cybersquatting on a domain name, or report some other type of abuse.
        
            - **AbuseContactPhone** *(string) --* 
        
              Phone number for reporting abuse.
        
            - **RegistryDomainId** *(string) --* 
        
              Reserved for future use.
        
            - **CreationDate** *(datetime) --* 
        
              The date when the domain was created as found in the response to a WHOIS query. The date and time is in Coordinated Universal time (UTC).
        
            - **UpdatedDate** *(datetime) --* 
        
              The last updated date of the domain as found in the response to a WHOIS query. The date and time is in Coordinated Universal time (UTC).
        
            - **ExpirationDate** *(datetime) --* 
        
              The date when the registration for the domain is set to expire. The date and time is in Coordinated Universal time (UTC).
        
            - **Reseller** *(string) --* 
        
              Reseller of the domain. Domains registered or transferred using Amazon Route 53 domains will have ``\"Amazon\"`` as the reseller. 
        
            - **DnsSec** *(string) --* 
        
              Reserved for future use.
        
            - **StatusList** *(list) --* 
        
              An array of domain name status codes, also known as Extensible Provisioning Protocol (EPP) status codes.
        
              ICANN, the organization that maintains a central database of domain names, has developed a set of domain name status codes that tell you the status of a variety of operations on a domain name, for example, registering a domain name, transferring a domain name to another registrar, renewing the registration for a domain name, and so on. All registrars use this same set of status codes.
        
              For a current list of domain name status codes and an explanation of what each code means, go to the `ICANN website <https://www.icann.org/>`__ and search for ``epp status codes`` . (Search on the ICANN website; web searches sometimes return an old version of the document.)
        
              - *(string) --* 
          
        """
        pass

    def get_domain_suggestions(self, DomainName: str, SuggestionCount: int, OnlyAvailable: bool) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/GetDomainSuggestions>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_domain_suggestions(
              DomainName=\'string\',
              SuggestionCount=123,
              OnlyAvailable=True|False
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]** 
        
          A domain name that you want to use as the basis for a list of possible domain names. The domain name must contain a top-level domain (TLD), such as .com, that Amazon Route 53 supports. For a list of TLDs, see `Domains that You Can Register with Amazon Route 53 <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html>`__ in the *Amazon Route 53 Developer Guide* .
        
        :type SuggestionCount: integer
        :param SuggestionCount: **[REQUIRED]** 
        
          The number of suggested domain names that you want Amazon Route 53 to return.
        
        :type OnlyAvailable: boolean
        :param OnlyAvailable: **[REQUIRED]** 
        
          If ``OnlyAvailable`` is ``true`` , Amazon Route 53 returns only domain names that are available. If ``OnlyAvailable`` is ``false`` , Amazon Route 53 returns domain names without checking whether they\'re available to be registered. To determine whether the domain is available, you can call ``checkDomainAvailability`` for each suggestion.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'SuggestionsList\': [
                    {
                        \'DomainName\': \'string\',
                        \'Availability\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **SuggestionsList** *(list) --* 
        
              A list of possible domain names. If you specified ``true`` for ``OnlyAvailable`` in the request, the list contains only domains that are available for registration.
        
              - *(dict) --* 
        
                Information about one suggested domain name.
        
                - **DomainName** *(string) --* 
        
                  A suggested domain name.
        
                - **Availability** *(string) --* 
        
                  Whether the domain name is available for registering.
        
                  .. note::
        
                    You can register only the domains that are designated as ``AVAILABLE`` .
        
                  Valid values:
        
                    AVAILABLE  
        
                  The domain name is available.
        
                    AVAILABLE_RESERVED  
        
                  The domain name is reserved under specific conditions.
        
                    AVAILABLE_PREORDER  
        
                  The domain name is available and can be preordered.
        
                    DONT_KNOW  
        
                  The TLD registry didn\'t reply with a definitive answer about whether the domain name is available. Amazon Route 53 can return this response for a variety of reasons, for example, the registry is performing maintenance. Try again later.
        
                    PENDING  
        
                  The TLD registry didn\'t return a response in the expected amount of time. When the response is delayed, it usually takes just a few extra seconds. You can resubmit the request immediately.
        
                    RESERVED  
        
                  The domain name has been reserved for another person or organization.
        
                    UNAVAILABLE  
        
                  The domain name is not available.
        
                    UNAVAILABLE_PREMIUM  
        
                  The domain name is not available.
        
                    UNAVAILABLE_RESTRICTED  
        
                  The domain name is forbidden.
        
        """
        pass

    def get_operation_detail(self, OperationId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/GetOperationDetail>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_operation_detail(
              OperationId=\'string\'
          )
        :type OperationId: string
        :param OperationId: **[REQUIRED]** 
        
          The identifier for the operation for which you want to get the status. Amazon Route 53 returned the identifier in the response to the original request.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'OperationId\': \'string\',
                \'Status\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'ERROR\'|\'SUCCESSFUL\'|\'FAILED\',
                \'Message\': \'string\',
                \'DomainName\': \'string\',
                \'Type\': \'REGISTER_DOMAIN\'|\'DELETE_DOMAIN\'|\'TRANSFER_IN_DOMAIN\'|\'UPDATE_DOMAIN_CONTACT\'|\'UPDATE_NAMESERVER\'|\'CHANGE_PRIVACY_PROTECTION\'|\'DOMAIN_LOCK\'|\'ENABLE_AUTORENEW\'|\'DISABLE_AUTORENEW\'|\'ADD_DNSSEC\'|\'REMOVE_DNSSEC\'|\'EXPIRE_DOMAIN\'|\'TRANSFER_OUT_DOMAIN\'|\'CHANGE_DOMAIN_OWNER\'|\'RENEW_DOMAIN\'|\'PUSH_DOMAIN\',
                \'SubmittedDate\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The GetOperationDetail response includes the following elements.
        
            - **OperationId** *(string) --* 
        
              The identifier for the operation.
        
            - **Status** *(string) --* 
        
              The current status of the requested operation in the system.
        
            - **Message** *(string) --* 
        
              Detailed information on the status including possible errors.
        
            - **DomainName** *(string) --* 
        
              The name of a domain.
        
            - **Type** *(string) --* 
        
              The type of operation that was requested.
        
            - **SubmittedDate** *(datetime) --* 
        
              The date when the request was submitted.
        
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

    def list_domains(self, Marker: str = None, MaxItems: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/ListDomains>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_domains(
              Marker=\'string\',
              MaxItems=123
          )
        :type Marker: string
        :param Marker: 
        
          For an initial request for a list of domains, omit this element. If the number of domains that are associated with the current AWS account is greater than the value that you specified for ``MaxItems`` , you can use ``Marker`` to return additional domains. Get the value of ``NextPageMarker`` from the previous response, and submit another request that includes the value of ``NextPageMarker`` in the ``Marker`` element.
        
          Constraints: The marker must match the value specified in the previous request.
        
        :type MaxItems: integer
        :param MaxItems: 
        
          Number of domains to be returned.
        
          Default: 20
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Domains\': [
                    {
                        \'DomainName\': \'string\',
                        \'AutoRenew\': True|False,
                        \'TransferLock\': True|False,
                        \'Expiry\': datetime(2015, 1, 1)
                    },
                ],
                \'NextPageMarker\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The ListDomains response includes the following elements.
        
            - **Domains** *(list) --* 
        
              A summary of domains.
        
              - *(dict) --* 
        
                Summary information about one domain.
        
                - **DomainName** *(string) --* 
        
                  The name of the domain that the summary information applies to.
        
                - **AutoRenew** *(boolean) --* 
        
                  Indicates whether the domain is automatically renewed upon expiration.
        
                - **TransferLock** *(boolean) --* 
        
                  Indicates whether a domain is locked from unauthorized transfer to another party.
        
                - **Expiry** *(datetime) --* 
        
                  Expiration date of the domain in Coordinated Universal Time (UTC).
        
            - **NextPageMarker** *(string) --* 
        
              If there are more domains than you specified for ``MaxItems`` in the request, submit another request and include the value of ``NextPageMarker`` in the value of ``Marker`` .
        
        """
        pass

    def list_operations(self, SubmittedSince: datetime = None, Marker: str = None, MaxItems: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/ListOperations>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_operations(
              SubmittedSince=datetime(2015, 1, 1),
              Marker=\'string\',
              MaxItems=123
          )
        :type SubmittedSince: datetime
        :param SubmittedSince: 
        
          An optional parameter that lets you get information about all the operations that you submitted after a specified date and time. Specify the date and time in Coordinated Universal time (UTC).
        
        :type Marker: string
        :param Marker: 
        
          For an initial request for a list of operations, omit this element. If the number of operations that are not yet complete is greater than the value that you specified for ``MaxItems`` , you can use ``Marker`` to return additional operations. Get the value of ``NextPageMarker`` from the previous response, and submit another request that includes the value of ``NextPageMarker`` in the ``Marker`` element.
        
        :type MaxItems: integer
        :param MaxItems: 
        
          Number of domains to be returned.
        
          Default: 20
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Operations\': [
                    {
                        \'OperationId\': \'string\',
                        \'Status\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'ERROR\'|\'SUCCESSFUL\'|\'FAILED\',
                        \'Type\': \'REGISTER_DOMAIN\'|\'DELETE_DOMAIN\'|\'TRANSFER_IN_DOMAIN\'|\'UPDATE_DOMAIN_CONTACT\'|\'UPDATE_NAMESERVER\'|\'CHANGE_PRIVACY_PROTECTION\'|\'DOMAIN_LOCK\'|\'ENABLE_AUTORENEW\'|\'DISABLE_AUTORENEW\'|\'ADD_DNSSEC\'|\'REMOVE_DNSSEC\'|\'EXPIRE_DOMAIN\'|\'TRANSFER_OUT_DOMAIN\'|\'CHANGE_DOMAIN_OWNER\'|\'RENEW_DOMAIN\'|\'PUSH_DOMAIN\',
                        \'SubmittedDate\': datetime(2015, 1, 1)
                    },
                ],
                \'NextPageMarker\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The ListOperations response includes the following elements.
        
            - **Operations** *(list) --* 
        
              Lists summaries of the operations.
        
              - *(dict) --* 
        
                OperationSummary includes the following elements.
        
                - **OperationId** *(string) --* 
        
                  Identifier returned to track the requested action.
        
                - **Status** *(string) --* 
        
                  The current status of the requested operation in the system.
        
                - **Type** *(string) --* 
        
                  Type of the action requested.
        
                - **SubmittedDate** *(datetime) --* 
        
                  The date when the request was submitted.
        
            - **NextPageMarker** *(string) --* 
        
              If there are more operations than you specified for ``MaxItems`` in the request, submit another request and include the value of ``NextPageMarker`` in the value of ``Marker`` .
        
        """
        pass

    def list_tags_for_domain(self, DomainName: str) -> Dict:
        """
        
        All tag operations are eventually consistent; subsequent operations might not immediately represent all issued operations.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/ListTagsForDomain>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_tags_for_domain(
              DomainName=\'string\'
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]** 
        
          The domain for which you want to get a list of tags.
        
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
        
            The ListTagsForDomain response includes the following elements.
        
            - **TagList** *(list) --* 
        
              A list of the tags that are associated with the specified domain.
        
              - *(dict) --* 
        
                Each tag includes the following elements.
        
                - **Key** *(string) --* 
        
                  The key (name) of a tag.
        
                  Valid values: A-Z, a-z, 0-9, space, \".:/=+\-@\"
        
                  Constraints: Each key can be 1-128 characters long.
        
                - **Value** *(string) --* 
        
                  The value of a tag.
        
                  Valid values: A-Z, a-z, 0-9, space, \".:/=+\-@\"
        
                  Constraints: Each value can be 0-256 characters long.
        
        """
        pass

    def register_domain(self, DomainName: str, DurationInYears: int, AdminContact: Dict, RegistrantContact: Dict, TechContact: Dict, IdnLangCode: str = None, AutoRenew: bool = None, PrivacyProtectAdminContact: bool = None, PrivacyProtectRegistrantContact: bool = None, PrivacyProtectTechContact: bool = None) -> Dict:
        """
        
        When you register a domain, Amazon Route 53 does the following:
        
        * Creates a Amazon Route 53 hosted zone that has the same name as the domain. Amazon Route 53 assigns four name servers to your hosted zone and automatically updates your domain registration with the names of these name servers. 
         
        * Enables autorenew, so your domain registration will renew automatically each year. We\'ll notify you in advance of the renewal date so you can choose whether to renew the registration. 
         
        * Optionally enables privacy protection, so WHOIS queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If you don\'t enable privacy protection, WHOIS queries return the information that you entered for the registrant, admin, and tech contacts. 
         
        * If registration is successful, returns an operation ID that you can use to track the progress and completion of the action. If the request is not completed successfully, the domain registrant is notified by email. 
         
        * Charges your AWS account an amount based on the top-level domain. For more information, see `Amazon Route 53 Pricing <http://aws.amazon.com/route53/pricing/>`__ . 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/RegisterDomain>`_
        
        **Request Syntax** 
        ::
        
          response = client.register_domain(
              DomainName=\'string\',
              IdnLangCode=\'string\',
              DurationInYears=123,
              AutoRenew=True|False,
              AdminContact={
                  \'FirstName\': \'string\',
                  \'LastName\': \'string\',
                  \'ContactType\': \'PERSON\'|\'COMPANY\'|\'ASSOCIATION\'|\'PUBLIC_BODY\'|\'RESELLER\',
                  \'OrganizationName\': \'string\',
                  \'AddressLine1\': \'string\',
                  \'AddressLine2\': \'string\',
                  \'City\': \'string\',
                  \'State\': \'string\',
                  \'CountryCode\': \'AD\'|\'AE\'|\'AF\'|\'AG\'|\'AI\'|\'AL\'|\'AM\'|\'AN\'|\'AO\'|\'AQ\'|\'AR\'|\'AS\'|\'AT\'|\'AU\'|\'AW\'|\'AZ\'|\'BA\'|\'BB\'|\'BD\'|\'BE\'|\'BF\'|\'BG\'|\'BH\'|\'BI\'|\'BJ\'|\'BL\'|\'BM\'|\'BN\'|\'BO\'|\'BR\'|\'BS\'|\'BT\'|\'BW\'|\'BY\'|\'BZ\'|\'CA\'|\'CC\'|\'CD\'|\'CF\'|\'CG\'|\'CH\'|\'CI\'|\'CK\'|\'CL\'|\'CM\'|\'CN\'|\'CO\'|\'CR\'|\'CU\'|\'CV\'|\'CX\'|\'CY\'|\'CZ\'|\'DE\'|\'DJ\'|\'DK\'|\'DM\'|\'DO\'|\'DZ\'|\'EC\'|\'EE\'|\'EG\'|\'ER\'|\'ES\'|\'ET\'|\'FI\'|\'FJ\'|\'FK\'|\'FM\'|\'FO\'|\'FR\'|\'GA\'|\'GB\'|\'GD\'|\'GE\'|\'GH\'|\'GI\'|\'GL\'|\'GM\'|\'GN\'|\'GQ\'|\'GR\'|\'GT\'|\'GU\'|\'GW\'|\'GY\'|\'HK\'|\'HN\'|\'HR\'|\'HT\'|\'HU\'|\'ID\'|\'IE\'|\'IL\'|\'IM\'|\'IN\'|\'IQ\'|\'IR\'|\'IS\'|\'IT\'|\'JM\'|\'JO\'|\'JP\'|\'KE\'|\'KG\'|\'KH\'|\'KI\'|\'KM\'|\'KN\'|\'KP\'|\'KR\'|\'KW\'|\'KY\'|\'KZ\'|\'LA\'|\'LB\'|\'LC\'|\'LI\'|\'LK\'|\'LR\'|\'LS\'|\'LT\'|\'LU\'|\'LV\'|\'LY\'|\'MA\'|\'MC\'|\'MD\'|\'ME\'|\'MF\'|\'MG\'|\'MH\'|\'MK\'|\'ML\'|\'MM\'|\'MN\'|\'MO\'|\'MP\'|\'MR\'|\'MS\'|\'MT\'|\'MU\'|\'MV\'|\'MW\'|\'MX\'|\'MY\'|\'MZ\'|\'NA\'|\'NC\'|\'NE\'|\'NG\'|\'NI\'|\'NL\'|\'NO\'|\'NP\'|\'NR\'|\'NU\'|\'NZ\'|\'OM\'|\'PA\'|\'PE\'|\'PF\'|\'PG\'|\'PH\'|\'PK\'|\'PL\'|\'PM\'|\'PN\'|\'PR\'|\'PT\'|\'PW\'|\'PY\'|\'QA\'|\'RO\'|\'RS\'|\'RU\'|\'RW\'|\'SA\'|\'SB\'|\'SC\'|\'SD\'|\'SE\'|\'SG\'|\'SH\'|\'SI\'|\'SK\'|\'SL\'|\'SM\'|\'SN\'|\'SO\'|\'SR\'|\'ST\'|\'SV\'|\'SY\'|\'SZ\'|\'TC\'|\'TD\'|\'TG\'|\'TH\'|\'TJ\'|\'TK\'|\'TL\'|\'TM\'|\'TN\'|\'TO\'|\'TR\'|\'TT\'|\'TV\'|\'TW\'|\'TZ\'|\'UA\'|\'UG\'|\'US\'|\'UY\'|\'UZ\'|\'VA\'|\'VC\'|\'VE\'|\'VG\'|\'VI\'|\'VN\'|\'VU\'|\'WF\'|\'WS\'|\'YE\'|\'YT\'|\'ZA\'|\'ZM\'|\'ZW\',
                  \'ZipCode\': \'string\',
                  \'PhoneNumber\': \'string\',
                  \'Email\': \'string\',
                  \'Fax\': \'string\',
                  \'ExtraParams\': [
                      {
                          \'Name\': \'DUNS_NUMBER\'|\'BRAND_NUMBER\'|\'BIRTH_DEPARTMENT\'|\'BIRTH_DATE_IN_YYYY_MM_DD\'|\'BIRTH_COUNTRY\'|\'BIRTH_CITY\'|\'DOCUMENT_NUMBER\'|\'AU_ID_NUMBER\'|\'AU_ID_TYPE\'|\'CA_LEGAL_TYPE\'|\'CA_BUSINESS_ENTITY_TYPE\'|\'ES_IDENTIFICATION\'|\'ES_IDENTIFICATION_TYPE\'|\'ES_LEGAL_FORM\'|\'FI_BUSINESS_NUMBER\'|\'FI_ID_NUMBER\'|\'FI_NATIONALITY\'|\'FI_ORGANIZATION_TYPE\'|\'IT_PIN\'|\'IT_REGISTRANT_ENTITY_TYPE\'|\'RU_PASSPORT_DATA\'|\'SE_ID_NUMBER\'|\'SG_ID_NUMBER\'|\'VAT_NUMBER\'|\'UK_CONTACT_TYPE\'|\'UK_COMPANY_NUMBER\',
                          \'Value\': \'string\'
                      },
                  ]
              },
              RegistrantContact={
                  \'FirstName\': \'string\',
                  \'LastName\': \'string\',
                  \'ContactType\': \'PERSON\'|\'COMPANY\'|\'ASSOCIATION\'|\'PUBLIC_BODY\'|\'RESELLER\',
                  \'OrganizationName\': \'string\',
                  \'AddressLine1\': \'string\',
                  \'AddressLine2\': \'string\',
                  \'City\': \'string\',
                  \'State\': \'string\',
                  \'CountryCode\': \'AD\'|\'AE\'|\'AF\'|\'AG\'|\'AI\'|\'AL\'|\'AM\'|\'AN\'|\'AO\'|\'AQ\'|\'AR\'|\'AS\'|\'AT\'|\'AU\'|\'AW\'|\'AZ\'|\'BA\'|\'BB\'|\'BD\'|\'BE\'|\'BF\'|\'BG\'|\'BH\'|\'BI\'|\'BJ\'|\'BL\'|\'BM\'|\'BN\'|\'BO\'|\'BR\'|\'BS\'|\'BT\'|\'BW\'|\'BY\'|\'BZ\'|\'CA\'|\'CC\'|\'CD\'|\'CF\'|\'CG\'|\'CH\'|\'CI\'|\'CK\'|\'CL\'|\'CM\'|\'CN\'|\'CO\'|\'CR\'|\'CU\'|\'CV\'|\'CX\'|\'CY\'|\'CZ\'|\'DE\'|\'DJ\'|\'DK\'|\'DM\'|\'DO\'|\'DZ\'|\'EC\'|\'EE\'|\'EG\'|\'ER\'|\'ES\'|\'ET\'|\'FI\'|\'FJ\'|\'FK\'|\'FM\'|\'FO\'|\'FR\'|\'GA\'|\'GB\'|\'GD\'|\'GE\'|\'GH\'|\'GI\'|\'GL\'|\'GM\'|\'GN\'|\'GQ\'|\'GR\'|\'GT\'|\'GU\'|\'GW\'|\'GY\'|\'HK\'|\'HN\'|\'HR\'|\'HT\'|\'HU\'|\'ID\'|\'IE\'|\'IL\'|\'IM\'|\'IN\'|\'IQ\'|\'IR\'|\'IS\'|\'IT\'|\'JM\'|\'JO\'|\'JP\'|\'KE\'|\'KG\'|\'KH\'|\'KI\'|\'KM\'|\'KN\'|\'KP\'|\'KR\'|\'KW\'|\'KY\'|\'KZ\'|\'LA\'|\'LB\'|\'LC\'|\'LI\'|\'LK\'|\'LR\'|\'LS\'|\'LT\'|\'LU\'|\'LV\'|\'LY\'|\'MA\'|\'MC\'|\'MD\'|\'ME\'|\'MF\'|\'MG\'|\'MH\'|\'MK\'|\'ML\'|\'MM\'|\'MN\'|\'MO\'|\'MP\'|\'MR\'|\'MS\'|\'MT\'|\'MU\'|\'MV\'|\'MW\'|\'MX\'|\'MY\'|\'MZ\'|\'NA\'|\'NC\'|\'NE\'|\'NG\'|\'NI\'|\'NL\'|\'NO\'|\'NP\'|\'NR\'|\'NU\'|\'NZ\'|\'OM\'|\'PA\'|\'PE\'|\'PF\'|\'PG\'|\'PH\'|\'PK\'|\'PL\'|\'PM\'|\'PN\'|\'PR\'|\'PT\'|\'PW\'|\'PY\'|\'QA\'|\'RO\'|\'RS\'|\'RU\'|\'RW\'|\'SA\'|\'SB\'|\'SC\'|\'SD\'|\'SE\'|\'SG\'|\'SH\'|\'SI\'|\'SK\'|\'SL\'|\'SM\'|\'SN\'|\'SO\'|\'SR\'|\'ST\'|\'SV\'|\'SY\'|\'SZ\'|\'TC\'|\'TD\'|\'TG\'|\'TH\'|\'TJ\'|\'TK\'|\'TL\'|\'TM\'|\'TN\'|\'TO\'|\'TR\'|\'TT\'|\'TV\'|\'TW\'|\'TZ\'|\'UA\'|\'UG\'|\'US\'|\'UY\'|\'UZ\'|\'VA\'|\'VC\'|\'VE\'|\'VG\'|\'VI\'|\'VN\'|\'VU\'|\'WF\'|\'WS\'|\'YE\'|\'YT\'|\'ZA\'|\'ZM\'|\'ZW\',
                  \'ZipCode\': \'string\',
                  \'PhoneNumber\': \'string\',
                  \'Email\': \'string\',
                  \'Fax\': \'string\',
                  \'ExtraParams\': [
                      {
                          \'Name\': \'DUNS_NUMBER\'|\'BRAND_NUMBER\'|\'BIRTH_DEPARTMENT\'|\'BIRTH_DATE_IN_YYYY_MM_DD\'|\'BIRTH_COUNTRY\'|\'BIRTH_CITY\'|\'DOCUMENT_NUMBER\'|\'AU_ID_NUMBER\'|\'AU_ID_TYPE\'|\'CA_LEGAL_TYPE\'|\'CA_BUSINESS_ENTITY_TYPE\'|\'ES_IDENTIFICATION\'|\'ES_IDENTIFICATION_TYPE\'|\'ES_LEGAL_FORM\'|\'FI_BUSINESS_NUMBER\'|\'FI_ID_NUMBER\'|\'FI_NATIONALITY\'|\'FI_ORGANIZATION_TYPE\'|\'IT_PIN\'|\'IT_REGISTRANT_ENTITY_TYPE\'|\'RU_PASSPORT_DATA\'|\'SE_ID_NUMBER\'|\'SG_ID_NUMBER\'|\'VAT_NUMBER\'|\'UK_CONTACT_TYPE\'|\'UK_COMPANY_NUMBER\',
                          \'Value\': \'string\'
                      },
                  ]
              },
              TechContact={
                  \'FirstName\': \'string\',
                  \'LastName\': \'string\',
                  \'ContactType\': \'PERSON\'|\'COMPANY\'|\'ASSOCIATION\'|\'PUBLIC_BODY\'|\'RESELLER\',
                  \'OrganizationName\': \'string\',
                  \'AddressLine1\': \'string\',
                  \'AddressLine2\': \'string\',
                  \'City\': \'string\',
                  \'State\': \'string\',
                  \'CountryCode\': \'AD\'|\'AE\'|\'AF\'|\'AG\'|\'AI\'|\'AL\'|\'AM\'|\'AN\'|\'AO\'|\'AQ\'|\'AR\'|\'AS\'|\'AT\'|\'AU\'|\'AW\'|\'AZ\'|\'BA\'|\'BB\'|\'BD\'|\'BE\'|\'BF\'|\'BG\'|\'BH\'|\'BI\'|\'BJ\'|\'BL\'|\'BM\'|\'BN\'|\'BO\'|\'BR\'|\'BS\'|\'BT\'|\'BW\'|\'BY\'|\'BZ\'|\'CA\'|\'CC\'|\'CD\'|\'CF\'|\'CG\'|\'CH\'|\'CI\'|\'CK\'|\'CL\'|\'CM\'|\'CN\'|\'CO\'|\'CR\'|\'CU\'|\'CV\'|\'CX\'|\'CY\'|\'CZ\'|\'DE\'|\'DJ\'|\'DK\'|\'DM\'|\'DO\'|\'DZ\'|\'EC\'|\'EE\'|\'EG\'|\'ER\'|\'ES\'|\'ET\'|\'FI\'|\'FJ\'|\'FK\'|\'FM\'|\'FO\'|\'FR\'|\'GA\'|\'GB\'|\'GD\'|\'GE\'|\'GH\'|\'GI\'|\'GL\'|\'GM\'|\'GN\'|\'GQ\'|\'GR\'|\'GT\'|\'GU\'|\'GW\'|\'GY\'|\'HK\'|\'HN\'|\'HR\'|\'HT\'|\'HU\'|\'ID\'|\'IE\'|\'IL\'|\'IM\'|\'IN\'|\'IQ\'|\'IR\'|\'IS\'|\'IT\'|\'JM\'|\'JO\'|\'JP\'|\'KE\'|\'KG\'|\'KH\'|\'KI\'|\'KM\'|\'KN\'|\'KP\'|\'KR\'|\'KW\'|\'KY\'|\'KZ\'|\'LA\'|\'LB\'|\'LC\'|\'LI\'|\'LK\'|\'LR\'|\'LS\'|\'LT\'|\'LU\'|\'LV\'|\'LY\'|\'MA\'|\'MC\'|\'MD\'|\'ME\'|\'MF\'|\'MG\'|\'MH\'|\'MK\'|\'ML\'|\'MM\'|\'MN\'|\'MO\'|\'MP\'|\'MR\'|\'MS\'|\'MT\'|\'MU\'|\'MV\'|\'MW\'|\'MX\'|\'MY\'|\'MZ\'|\'NA\'|\'NC\'|\'NE\'|\'NG\'|\'NI\'|\'NL\'|\'NO\'|\'NP\'|\'NR\'|\'NU\'|\'NZ\'|\'OM\'|\'PA\'|\'PE\'|\'PF\'|\'PG\'|\'PH\'|\'PK\'|\'PL\'|\'PM\'|\'PN\'|\'PR\'|\'PT\'|\'PW\'|\'PY\'|\'QA\'|\'RO\'|\'RS\'|\'RU\'|\'RW\'|\'SA\'|\'SB\'|\'SC\'|\'SD\'|\'SE\'|\'SG\'|\'SH\'|\'SI\'|\'SK\'|\'SL\'|\'SM\'|\'SN\'|\'SO\'|\'SR\'|\'ST\'|\'SV\'|\'SY\'|\'SZ\'|\'TC\'|\'TD\'|\'TG\'|\'TH\'|\'TJ\'|\'TK\'|\'TL\'|\'TM\'|\'TN\'|\'TO\'|\'TR\'|\'TT\'|\'TV\'|\'TW\'|\'TZ\'|\'UA\'|\'UG\'|\'US\'|\'UY\'|\'UZ\'|\'VA\'|\'VC\'|\'VE\'|\'VG\'|\'VI\'|\'VN\'|\'VU\'|\'WF\'|\'WS\'|\'YE\'|\'YT\'|\'ZA\'|\'ZM\'|\'ZW\',
                  \'ZipCode\': \'string\',
                  \'PhoneNumber\': \'string\',
                  \'Email\': \'string\',
                  \'Fax\': \'string\',
                  \'ExtraParams\': [
                      {
                          \'Name\': \'DUNS_NUMBER\'|\'BRAND_NUMBER\'|\'BIRTH_DEPARTMENT\'|\'BIRTH_DATE_IN_YYYY_MM_DD\'|\'BIRTH_COUNTRY\'|\'BIRTH_CITY\'|\'DOCUMENT_NUMBER\'|\'AU_ID_NUMBER\'|\'AU_ID_TYPE\'|\'CA_LEGAL_TYPE\'|\'CA_BUSINESS_ENTITY_TYPE\'|\'ES_IDENTIFICATION\'|\'ES_IDENTIFICATION_TYPE\'|\'ES_LEGAL_FORM\'|\'FI_BUSINESS_NUMBER\'|\'FI_ID_NUMBER\'|\'FI_NATIONALITY\'|\'FI_ORGANIZATION_TYPE\'|\'IT_PIN\'|\'IT_REGISTRANT_ENTITY_TYPE\'|\'RU_PASSPORT_DATA\'|\'SE_ID_NUMBER\'|\'SG_ID_NUMBER\'|\'VAT_NUMBER\'|\'UK_CONTACT_TYPE\'|\'UK_COMPANY_NUMBER\',
                          \'Value\': \'string\'
                      },
                  ]
              },
              PrivacyProtectAdminContact=True|False,
              PrivacyProtectRegistrantContact=True|False,
              PrivacyProtectTechContact=True|False
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]** 
        
          The domain name that you want to register.
        
          Constraints: The domain name can contain only the letters a through z, the numbers 0 through 9, and hyphen (-). Internationalized Domain Names are not supported.
        
        :type IdnLangCode: string
        :param IdnLangCode: 
        
          Reserved for future use.
        
        :type DurationInYears: integer
        :param DurationInYears: **[REQUIRED]** 
        
          The number of years that you want to register the domain for. Domains are registered for a minimum of one year. The maximum period depends on the top-level domain. For the range of valid values for your domain, see `Domains that You Can Register with Amazon Route 53 <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html>`__ in the *Amazon Route 53 Developer Guide* .
        
          Default: 1
        
        :type AutoRenew: boolean
        :param AutoRenew: 
        
          Indicates whether the domain will be automatically renewed (``true`` ) or not (``false`` ). Autorenewal only takes effect after the account is charged.
        
          Default: ``true``  
        
        :type AdminContact: dict
        :param AdminContact: **[REQUIRED]** 
        
          Provides detailed contact information.
        
          - **FirstName** *(string) --* 
        
            First name of contact.
        
          - **LastName** *(string) --* 
        
            Last name of contact.
        
          - **ContactType** *(string) --* 
        
            Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than ``PERSON`` , you must enter an organization name, and you can\'t enable privacy protection for the contact.
        
          - **OrganizationName** *(string) --* 
        
            Name of the organization for contact types other than ``PERSON`` .
        
          - **AddressLine1** *(string) --* 
        
            First line of the contact\'s address.
        
          - **AddressLine2** *(string) --* 
        
            Second line of contact\'s address, if any.
        
          - **City** *(string) --* 
        
            The city of the contact\'s address.
        
          - **State** *(string) --* 
        
            The state or province of the contact\'s city.
        
          - **CountryCode** *(string) --* 
        
            Code for the country of the contact\'s address.
        
          - **ZipCode** *(string) --* 
        
            The zip or postal code of the contact\'s address.
        
          - **PhoneNumber** *(string) --* 
        
            The phone number of the contact.
        
            Constraints: Phone number must be specified in the format \"+[country dialing code].[number including any area code>]\". For example, a US phone number might appear as ``\"+1.1234567890\"`` .
        
          - **Email** *(string) --* 
        
            Email address of the contact.
        
          - **Fax** *(string) --* 
        
            Fax number of the contact.
        
            Constraints: Phone number must be specified in the format \"+[country dialing code].[number including any area code]\". For example, a US phone number might appear as ``\"+1.1234567890\"`` .
        
          - **ExtraParams** *(list) --* 
        
            A list of name-value pairs for parameters required by certain top-level domains.
        
            - *(dict) --* 
        
              ExtraParam includes the following elements.
        
              - **Name** *(string) --* **[REQUIRED]** 
        
                Name of the additional parameter required by the top-level domain. Here are the top-level domains that require additional parameters and which parameters they require:
        
                * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``   
                 
                * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``   
                 
                * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``   
                 
                * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` , ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``   
                 
                * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``   
                 
                * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``   
                 
                * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``   
                 
                * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``   
                 
                * **.sg:**  ``SG_ID_NUMBER``   
                 
                * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``   
                 
                In addition, many TLDs require ``VAT_NUMBER`` .
        
              - **Value** *(string) --* **[REQUIRED]** 
        
                Values corresponding to the additional parameter names required by some top-level domains.
        
        :type RegistrantContact: dict
        :param RegistrantContact: **[REQUIRED]** 
        
          Provides detailed contact information.
        
          - **FirstName** *(string) --* 
        
            First name of contact.
        
          - **LastName** *(string) --* 
        
            Last name of contact.
        
          - **ContactType** *(string) --* 
        
            Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than ``PERSON`` , you must enter an organization name, and you can\'t enable privacy protection for the contact.
        
          - **OrganizationName** *(string) --* 
        
            Name of the organization for contact types other than ``PERSON`` .
        
          - **AddressLine1** *(string) --* 
        
            First line of the contact\'s address.
        
          - **AddressLine2** *(string) --* 
        
            Second line of contact\'s address, if any.
        
          - **City** *(string) --* 
        
            The city of the contact\'s address.
        
          - **State** *(string) --* 
        
            The state or province of the contact\'s city.
        
          - **CountryCode** *(string) --* 
        
            Code for the country of the contact\'s address.
        
          - **ZipCode** *(string) --* 
        
            The zip or postal code of the contact\'s address.
        
          - **PhoneNumber** *(string) --* 
        
            The phone number of the contact.
        
            Constraints: Phone number must be specified in the format \"+[country dialing code].[number including any area code>]\". For example, a US phone number might appear as ``\"+1.1234567890\"`` .
        
          - **Email** *(string) --* 
        
            Email address of the contact.
        
          - **Fax** *(string) --* 
        
            Fax number of the contact.
        
            Constraints: Phone number must be specified in the format \"+[country dialing code].[number including any area code]\". For example, a US phone number might appear as ``\"+1.1234567890\"`` .
        
          - **ExtraParams** *(list) --* 
        
            A list of name-value pairs for parameters required by certain top-level domains.
        
            - *(dict) --* 
        
              ExtraParam includes the following elements.
        
              - **Name** *(string) --* **[REQUIRED]** 
        
                Name of the additional parameter required by the top-level domain. Here are the top-level domains that require additional parameters and which parameters they require:
        
                * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``   
                 
                * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``   
                 
                * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``   
                 
                * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` , ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``   
                 
                * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``   
                 
                * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``   
                 
                * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``   
                 
                * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``   
                 
                * **.sg:**  ``SG_ID_NUMBER``   
                 
                * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``   
                 
                In addition, many TLDs require ``VAT_NUMBER`` .
        
              - **Value** *(string) --* **[REQUIRED]** 
        
                Values corresponding to the additional parameter names required by some top-level domains.
        
        :type TechContact: dict
        :param TechContact: **[REQUIRED]** 
        
          Provides detailed contact information.
        
          - **FirstName** *(string) --* 
        
            First name of contact.
        
          - **LastName** *(string) --* 
        
            Last name of contact.
        
          - **ContactType** *(string) --* 
        
            Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than ``PERSON`` , you must enter an organization name, and you can\'t enable privacy protection for the contact.
        
          - **OrganizationName** *(string) --* 
        
            Name of the organization for contact types other than ``PERSON`` .
        
          - **AddressLine1** *(string) --* 
        
            First line of the contact\'s address.
        
          - **AddressLine2** *(string) --* 
        
            Second line of contact\'s address, if any.
        
          - **City** *(string) --* 
        
            The city of the contact\'s address.
        
          - **State** *(string) --* 
        
            The state or province of the contact\'s city.
        
          - **CountryCode** *(string) --* 
        
            Code for the country of the contact\'s address.
        
          - **ZipCode** *(string) --* 
        
            The zip or postal code of the contact\'s address.
        
          - **PhoneNumber** *(string) --* 
        
            The phone number of the contact.
        
            Constraints: Phone number must be specified in the format \"+[country dialing code].[number including any area code>]\". For example, a US phone number might appear as ``\"+1.1234567890\"`` .
        
          - **Email** *(string) --* 
        
            Email address of the contact.
        
          - **Fax** *(string) --* 
        
            Fax number of the contact.
        
            Constraints: Phone number must be specified in the format \"+[country dialing code].[number including any area code]\". For example, a US phone number might appear as ``\"+1.1234567890\"`` .
        
          - **ExtraParams** *(list) --* 
        
            A list of name-value pairs for parameters required by certain top-level domains.
        
            - *(dict) --* 
        
              ExtraParam includes the following elements.
        
              - **Name** *(string) --* **[REQUIRED]** 
        
                Name of the additional parameter required by the top-level domain. Here are the top-level domains that require additional parameters and which parameters they require:
        
                * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``   
                 
                * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``   
                 
                * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``   
                 
                * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` , ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``   
                 
                * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``   
                 
                * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``   
                 
                * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``   
                 
                * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``   
                 
                * **.sg:**  ``SG_ID_NUMBER``   
                 
                * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``   
                 
                In addition, many TLDs require ``VAT_NUMBER`` .
        
              - **Value** *(string) --* **[REQUIRED]** 
        
                Values corresponding to the additional parameter names required by some top-level domains.
        
        :type PrivacyProtectAdminContact: boolean
        :param PrivacyProtectAdminContact: 
        
          Whether you want to conceal contact information from WHOIS queries. If you specify ``true`` , WHOIS (\"who is\") queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If you specify ``false`` , WHOIS queries return the information that you entered for the admin contact.
        
          Default: ``true``  
        
        :type PrivacyProtectRegistrantContact: boolean
        :param PrivacyProtectRegistrantContact: 
        
          Whether you want to conceal contact information from WHOIS queries. If you specify ``true`` , WHOIS (\"who is\") queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If you specify ``false`` , WHOIS queries return the information that you entered for the registrant contact (the domain owner).
        
          Default: ``true``  
        
        :type PrivacyProtectTechContact: boolean
        :param PrivacyProtectTechContact: 
        
          Whether you want to conceal contact information from WHOIS queries. If you specify ``true`` , WHOIS (\"who is\") queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If you specify ``false`` , WHOIS queries return the information that you entered for the technical contact.
        
          Default: ``true``  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'OperationId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The RegisterDomain response includes the following element.
        
            - **OperationId** *(string) --* 
        
              Identifier for tracking the progress of the request. To use this ID to query the operation status, use  GetOperationDetail .
        
        """
        pass

    def renew_domain(self, DomainName: str, CurrentExpiryYear: int, DurationInYears: int = None) -> Dict:
        """
        
        We recommend that you renew your domain several weeks before the expiration date. Some TLD registries delete domains before the expiration date if you haven\'t renewed far enough in advance. For more information about renewing domain registration, see `Renewing Registration for a Domain <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-renew.html>`__ in the Amazon Route 53 Developer Guide.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/RenewDomain>`_
        
        **Request Syntax** 
        ::
        
          response = client.renew_domain(
              DomainName=\'string\',
              DurationInYears=123,
              CurrentExpiryYear=123
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]** 
        
          The name of the domain that you want to renew.
        
        :type DurationInYears: integer
        :param DurationInYears: 
        
          The number of years that you want to renew the domain for. The maximum number of years depends on the top-level domain. For the range of valid values for your domain, see `Domains that You Can Register with Amazon Route 53 <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html>`__ in the *Amazon Route 53 Developer Guide* .
        
          Default: 1
        
        :type CurrentExpiryYear: integer
        :param CurrentExpiryYear: **[REQUIRED]** 
        
          The year when the registration for the domain is set to expire. This value must match the current expiration date for the domain.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'OperationId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **OperationId** *(string) --* 
        
              The identifier for tracking the progress of the request. To use this ID to query the operation status, use  GetOperationDetail .
        
        """
        pass

    def resend_contact_reachability_email(self, domainName: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/ResendContactReachabilityEmail>`_
        
        **Request Syntax** 
        ::
        
          response = client.resend_contact_reachability_email(
              domainName=\'string\'
          )
        :type domainName: string
        :param domainName: 
        
          The name of the domain for which you want Amazon Route 53 to resend a confirmation email to the registrant contact.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'domainName\': \'string\',
                \'emailAddress\': \'string\',
                \'isAlreadyVerified\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **domainName** *(string) --* 
        
              The domain name for which you requested a confirmation email.
        
            - **emailAddress** *(string) --* 
        
              The email address for the registrant contact at the time that we sent the verification email.
        
            - **isAlreadyVerified** *(boolean) --* 
        
               ``True`` if the email address for the registrant contact has already been verified, and ``false`` otherwise. If the email address has already been verified, we don\'t send another confirmation email.
        
        """
        pass

    def retrieve_domain_auth_code(self, DomainName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/RetrieveDomainAuthCode>`_
        
        **Request Syntax** 
        ::
        
          response = client.retrieve_domain_auth_code(
              DomainName=\'string\'
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]** 
        
          The name of the domain that you want to get an authorization code for.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AuthCode\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The RetrieveDomainAuthCode response includes the following element.
        
            - **AuthCode** *(string) --* 
        
              The authorization code for the domain.
        
        """
        pass

    def transfer_domain(self, DomainName: str, DurationInYears: int, AdminContact: Dict, RegistrantContact: Dict, TechContact: Dict, IdnLangCode: str = None, Nameservers: List = None, AuthCode: str = None, AutoRenew: bool = None, PrivacyProtectAdminContact: bool = None, PrivacyProtectRegistrantContact: bool = None, PrivacyProtectTechContact: bool = None) -> Dict:
        """
        
        For transfer requirements, a detailed procedure, and information about viewing the status of a domain transfer, see `Transferring Registration for a Domain to Amazon Route 53 <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-to-route-53.html>`__ in the *Amazon Route 53 Developer Guide* .
        
        If the registrar for your domain is also the DNS service provider for the domain, we highly recommend that you consider transferring your DNS service to Amazon Route 53 or to another DNS service provider before you transfer your registration. Some registrars provide free DNS service when you purchase a domain registration. When you transfer the registration, the previous registrar will not renew your domain registration and could end your DNS service at any time.
        
        .. warning::
        
          If the registrar for your domain is also the DNS service provider for the domain and you don\'t transfer DNS service to another provider, your website, email, and the web applications associated with the domain might become unavailable.
        
        If the transfer is successful, this method returns an operation ID that you can use to track the progress and completion of the action. If the transfer doesn\'t complete successfully, the domain registrant will be notified by email.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/TransferDomain>`_
        
        **Request Syntax** 
        ::
        
          response = client.transfer_domain(
              DomainName=\'string\',
              IdnLangCode=\'string\',
              DurationInYears=123,
              Nameservers=[
                  {
                      \'Name\': \'string\',
                      \'GlueIps\': [
                          \'string\',
                      ]
                  },
              ],
              AuthCode=\'string\',
              AutoRenew=True|False,
              AdminContact={
                  \'FirstName\': \'string\',
                  \'LastName\': \'string\',
                  \'ContactType\': \'PERSON\'|\'COMPANY\'|\'ASSOCIATION\'|\'PUBLIC_BODY\'|\'RESELLER\',
                  \'OrganizationName\': \'string\',
                  \'AddressLine1\': \'string\',
                  \'AddressLine2\': \'string\',
                  \'City\': \'string\',
                  \'State\': \'string\',
                  \'CountryCode\': \'AD\'|\'AE\'|\'AF\'|\'AG\'|\'AI\'|\'AL\'|\'AM\'|\'AN\'|\'AO\'|\'AQ\'|\'AR\'|\'AS\'|\'AT\'|\'AU\'|\'AW\'|\'AZ\'|\'BA\'|\'BB\'|\'BD\'|\'BE\'|\'BF\'|\'BG\'|\'BH\'|\'BI\'|\'BJ\'|\'BL\'|\'BM\'|\'BN\'|\'BO\'|\'BR\'|\'BS\'|\'BT\'|\'BW\'|\'BY\'|\'BZ\'|\'CA\'|\'CC\'|\'CD\'|\'CF\'|\'CG\'|\'CH\'|\'CI\'|\'CK\'|\'CL\'|\'CM\'|\'CN\'|\'CO\'|\'CR\'|\'CU\'|\'CV\'|\'CX\'|\'CY\'|\'CZ\'|\'DE\'|\'DJ\'|\'DK\'|\'DM\'|\'DO\'|\'DZ\'|\'EC\'|\'EE\'|\'EG\'|\'ER\'|\'ES\'|\'ET\'|\'FI\'|\'FJ\'|\'FK\'|\'FM\'|\'FO\'|\'FR\'|\'GA\'|\'GB\'|\'GD\'|\'GE\'|\'GH\'|\'GI\'|\'GL\'|\'GM\'|\'GN\'|\'GQ\'|\'GR\'|\'GT\'|\'GU\'|\'GW\'|\'GY\'|\'HK\'|\'HN\'|\'HR\'|\'HT\'|\'HU\'|\'ID\'|\'IE\'|\'IL\'|\'IM\'|\'IN\'|\'IQ\'|\'IR\'|\'IS\'|\'IT\'|\'JM\'|\'JO\'|\'JP\'|\'KE\'|\'KG\'|\'KH\'|\'KI\'|\'KM\'|\'KN\'|\'KP\'|\'KR\'|\'KW\'|\'KY\'|\'KZ\'|\'LA\'|\'LB\'|\'LC\'|\'LI\'|\'LK\'|\'LR\'|\'LS\'|\'LT\'|\'LU\'|\'LV\'|\'LY\'|\'MA\'|\'MC\'|\'MD\'|\'ME\'|\'MF\'|\'MG\'|\'MH\'|\'MK\'|\'ML\'|\'MM\'|\'MN\'|\'MO\'|\'MP\'|\'MR\'|\'MS\'|\'MT\'|\'MU\'|\'MV\'|\'MW\'|\'MX\'|\'MY\'|\'MZ\'|\'NA\'|\'NC\'|\'NE\'|\'NG\'|\'NI\'|\'NL\'|\'NO\'|\'NP\'|\'NR\'|\'NU\'|\'NZ\'|\'OM\'|\'PA\'|\'PE\'|\'PF\'|\'PG\'|\'PH\'|\'PK\'|\'PL\'|\'PM\'|\'PN\'|\'PR\'|\'PT\'|\'PW\'|\'PY\'|\'QA\'|\'RO\'|\'RS\'|\'RU\'|\'RW\'|\'SA\'|\'SB\'|\'SC\'|\'SD\'|\'SE\'|\'SG\'|\'SH\'|\'SI\'|\'SK\'|\'SL\'|\'SM\'|\'SN\'|\'SO\'|\'SR\'|\'ST\'|\'SV\'|\'SY\'|\'SZ\'|\'TC\'|\'TD\'|\'TG\'|\'TH\'|\'TJ\'|\'TK\'|\'TL\'|\'TM\'|\'TN\'|\'TO\'|\'TR\'|\'TT\'|\'TV\'|\'TW\'|\'TZ\'|\'UA\'|\'UG\'|\'US\'|\'UY\'|\'UZ\'|\'VA\'|\'VC\'|\'VE\'|\'VG\'|\'VI\'|\'VN\'|\'VU\'|\'WF\'|\'WS\'|\'YE\'|\'YT\'|\'ZA\'|\'ZM\'|\'ZW\',
                  \'ZipCode\': \'string\',
                  \'PhoneNumber\': \'string\',
                  \'Email\': \'string\',
                  \'Fax\': \'string\',
                  \'ExtraParams\': [
                      {
                          \'Name\': \'DUNS_NUMBER\'|\'BRAND_NUMBER\'|\'BIRTH_DEPARTMENT\'|\'BIRTH_DATE_IN_YYYY_MM_DD\'|\'BIRTH_COUNTRY\'|\'BIRTH_CITY\'|\'DOCUMENT_NUMBER\'|\'AU_ID_NUMBER\'|\'AU_ID_TYPE\'|\'CA_LEGAL_TYPE\'|\'CA_BUSINESS_ENTITY_TYPE\'|\'ES_IDENTIFICATION\'|\'ES_IDENTIFICATION_TYPE\'|\'ES_LEGAL_FORM\'|\'FI_BUSINESS_NUMBER\'|\'FI_ID_NUMBER\'|\'FI_NATIONALITY\'|\'FI_ORGANIZATION_TYPE\'|\'IT_PIN\'|\'IT_REGISTRANT_ENTITY_TYPE\'|\'RU_PASSPORT_DATA\'|\'SE_ID_NUMBER\'|\'SG_ID_NUMBER\'|\'VAT_NUMBER\'|\'UK_CONTACT_TYPE\'|\'UK_COMPANY_NUMBER\',
                          \'Value\': \'string\'
                      },
                  ]
              },
              RegistrantContact={
                  \'FirstName\': \'string\',
                  \'LastName\': \'string\',
                  \'ContactType\': \'PERSON\'|\'COMPANY\'|\'ASSOCIATION\'|\'PUBLIC_BODY\'|\'RESELLER\',
                  \'OrganizationName\': \'string\',
                  \'AddressLine1\': \'string\',
                  \'AddressLine2\': \'string\',
                  \'City\': \'string\',
                  \'State\': \'string\',
                  \'CountryCode\': \'AD\'|\'AE\'|\'AF\'|\'AG\'|\'AI\'|\'AL\'|\'AM\'|\'AN\'|\'AO\'|\'AQ\'|\'AR\'|\'AS\'|\'AT\'|\'AU\'|\'AW\'|\'AZ\'|\'BA\'|\'BB\'|\'BD\'|\'BE\'|\'BF\'|\'BG\'|\'BH\'|\'BI\'|\'BJ\'|\'BL\'|\'BM\'|\'BN\'|\'BO\'|\'BR\'|\'BS\'|\'BT\'|\'BW\'|\'BY\'|\'BZ\'|\'CA\'|\'CC\'|\'CD\'|\'CF\'|\'CG\'|\'CH\'|\'CI\'|\'CK\'|\'CL\'|\'CM\'|\'CN\'|\'CO\'|\'CR\'|\'CU\'|\'CV\'|\'CX\'|\'CY\'|\'CZ\'|\'DE\'|\'DJ\'|\'DK\'|\'DM\'|\'DO\'|\'DZ\'|\'EC\'|\'EE\'|\'EG\'|\'ER\'|\'ES\'|\'ET\'|\'FI\'|\'FJ\'|\'FK\'|\'FM\'|\'FO\'|\'FR\'|\'GA\'|\'GB\'|\'GD\'|\'GE\'|\'GH\'|\'GI\'|\'GL\'|\'GM\'|\'GN\'|\'GQ\'|\'GR\'|\'GT\'|\'GU\'|\'GW\'|\'GY\'|\'HK\'|\'HN\'|\'HR\'|\'HT\'|\'HU\'|\'ID\'|\'IE\'|\'IL\'|\'IM\'|\'IN\'|\'IQ\'|\'IR\'|\'IS\'|\'IT\'|\'JM\'|\'JO\'|\'JP\'|\'KE\'|\'KG\'|\'KH\'|\'KI\'|\'KM\'|\'KN\'|\'KP\'|\'KR\'|\'KW\'|\'KY\'|\'KZ\'|\'LA\'|\'LB\'|\'LC\'|\'LI\'|\'LK\'|\'LR\'|\'LS\'|\'LT\'|\'LU\'|\'LV\'|\'LY\'|\'MA\'|\'MC\'|\'MD\'|\'ME\'|\'MF\'|\'MG\'|\'MH\'|\'MK\'|\'ML\'|\'MM\'|\'MN\'|\'MO\'|\'MP\'|\'MR\'|\'MS\'|\'MT\'|\'MU\'|\'MV\'|\'MW\'|\'MX\'|\'MY\'|\'MZ\'|\'NA\'|\'NC\'|\'NE\'|\'NG\'|\'NI\'|\'NL\'|\'NO\'|\'NP\'|\'NR\'|\'NU\'|\'NZ\'|\'OM\'|\'PA\'|\'PE\'|\'PF\'|\'PG\'|\'PH\'|\'PK\'|\'PL\'|\'PM\'|\'PN\'|\'PR\'|\'PT\'|\'PW\'|\'PY\'|\'QA\'|\'RO\'|\'RS\'|\'RU\'|\'RW\'|\'SA\'|\'SB\'|\'SC\'|\'SD\'|\'SE\'|\'SG\'|\'SH\'|\'SI\'|\'SK\'|\'SL\'|\'SM\'|\'SN\'|\'SO\'|\'SR\'|\'ST\'|\'SV\'|\'SY\'|\'SZ\'|\'TC\'|\'TD\'|\'TG\'|\'TH\'|\'TJ\'|\'TK\'|\'TL\'|\'TM\'|\'TN\'|\'TO\'|\'TR\'|\'TT\'|\'TV\'|\'TW\'|\'TZ\'|\'UA\'|\'UG\'|\'US\'|\'UY\'|\'UZ\'|\'VA\'|\'VC\'|\'VE\'|\'VG\'|\'VI\'|\'VN\'|\'VU\'|\'WF\'|\'WS\'|\'YE\'|\'YT\'|\'ZA\'|\'ZM\'|\'ZW\',
                  \'ZipCode\': \'string\',
                  \'PhoneNumber\': \'string\',
                  \'Email\': \'string\',
                  \'Fax\': \'string\',
                  \'ExtraParams\': [
                      {
                          \'Name\': \'DUNS_NUMBER\'|\'BRAND_NUMBER\'|\'BIRTH_DEPARTMENT\'|\'BIRTH_DATE_IN_YYYY_MM_DD\'|\'BIRTH_COUNTRY\'|\'BIRTH_CITY\'|\'DOCUMENT_NUMBER\'|\'AU_ID_NUMBER\'|\'AU_ID_TYPE\'|\'CA_LEGAL_TYPE\'|\'CA_BUSINESS_ENTITY_TYPE\'|\'ES_IDENTIFICATION\'|\'ES_IDENTIFICATION_TYPE\'|\'ES_LEGAL_FORM\'|\'FI_BUSINESS_NUMBER\'|\'FI_ID_NUMBER\'|\'FI_NATIONALITY\'|\'FI_ORGANIZATION_TYPE\'|\'IT_PIN\'|\'IT_REGISTRANT_ENTITY_TYPE\'|\'RU_PASSPORT_DATA\'|\'SE_ID_NUMBER\'|\'SG_ID_NUMBER\'|\'VAT_NUMBER\'|\'UK_CONTACT_TYPE\'|\'UK_COMPANY_NUMBER\',
                          \'Value\': \'string\'
                      },
                  ]
              },
              TechContact={
                  \'FirstName\': \'string\',
                  \'LastName\': \'string\',
                  \'ContactType\': \'PERSON\'|\'COMPANY\'|\'ASSOCIATION\'|\'PUBLIC_BODY\'|\'RESELLER\',
                  \'OrganizationName\': \'string\',
                  \'AddressLine1\': \'string\',
                  \'AddressLine2\': \'string\',
                  \'City\': \'string\',
                  \'State\': \'string\',
                  \'CountryCode\': \'AD\'|\'AE\'|\'AF\'|\'AG\'|\'AI\'|\'AL\'|\'AM\'|\'AN\'|\'AO\'|\'AQ\'|\'AR\'|\'AS\'|\'AT\'|\'AU\'|\'AW\'|\'AZ\'|\'BA\'|\'BB\'|\'BD\'|\'BE\'|\'BF\'|\'BG\'|\'BH\'|\'BI\'|\'BJ\'|\'BL\'|\'BM\'|\'BN\'|\'BO\'|\'BR\'|\'BS\'|\'BT\'|\'BW\'|\'BY\'|\'BZ\'|\'CA\'|\'CC\'|\'CD\'|\'CF\'|\'CG\'|\'CH\'|\'CI\'|\'CK\'|\'CL\'|\'CM\'|\'CN\'|\'CO\'|\'CR\'|\'CU\'|\'CV\'|\'CX\'|\'CY\'|\'CZ\'|\'DE\'|\'DJ\'|\'DK\'|\'DM\'|\'DO\'|\'DZ\'|\'EC\'|\'EE\'|\'EG\'|\'ER\'|\'ES\'|\'ET\'|\'FI\'|\'FJ\'|\'FK\'|\'FM\'|\'FO\'|\'FR\'|\'GA\'|\'GB\'|\'GD\'|\'GE\'|\'GH\'|\'GI\'|\'GL\'|\'GM\'|\'GN\'|\'GQ\'|\'GR\'|\'GT\'|\'GU\'|\'GW\'|\'GY\'|\'HK\'|\'HN\'|\'HR\'|\'HT\'|\'HU\'|\'ID\'|\'IE\'|\'IL\'|\'IM\'|\'IN\'|\'IQ\'|\'IR\'|\'IS\'|\'IT\'|\'JM\'|\'JO\'|\'JP\'|\'KE\'|\'KG\'|\'KH\'|\'KI\'|\'KM\'|\'KN\'|\'KP\'|\'KR\'|\'KW\'|\'KY\'|\'KZ\'|\'LA\'|\'LB\'|\'LC\'|\'LI\'|\'LK\'|\'LR\'|\'LS\'|\'LT\'|\'LU\'|\'LV\'|\'LY\'|\'MA\'|\'MC\'|\'MD\'|\'ME\'|\'MF\'|\'MG\'|\'MH\'|\'MK\'|\'ML\'|\'MM\'|\'MN\'|\'MO\'|\'MP\'|\'MR\'|\'MS\'|\'MT\'|\'MU\'|\'MV\'|\'MW\'|\'MX\'|\'MY\'|\'MZ\'|\'NA\'|\'NC\'|\'NE\'|\'NG\'|\'NI\'|\'NL\'|\'NO\'|\'NP\'|\'NR\'|\'NU\'|\'NZ\'|\'OM\'|\'PA\'|\'PE\'|\'PF\'|\'PG\'|\'PH\'|\'PK\'|\'PL\'|\'PM\'|\'PN\'|\'PR\'|\'PT\'|\'PW\'|\'PY\'|\'QA\'|\'RO\'|\'RS\'|\'RU\'|\'RW\'|\'SA\'|\'SB\'|\'SC\'|\'SD\'|\'SE\'|\'SG\'|\'SH\'|\'SI\'|\'SK\'|\'SL\'|\'SM\'|\'SN\'|\'SO\'|\'SR\'|\'ST\'|\'SV\'|\'SY\'|\'SZ\'|\'TC\'|\'TD\'|\'TG\'|\'TH\'|\'TJ\'|\'TK\'|\'TL\'|\'TM\'|\'TN\'|\'TO\'|\'TR\'|\'TT\'|\'TV\'|\'TW\'|\'TZ\'|\'UA\'|\'UG\'|\'US\'|\'UY\'|\'UZ\'|\'VA\'|\'VC\'|\'VE\'|\'VG\'|\'VI\'|\'VN\'|\'VU\'|\'WF\'|\'WS\'|\'YE\'|\'YT\'|\'ZA\'|\'ZM\'|\'ZW\',
                  \'ZipCode\': \'string\',
                  \'PhoneNumber\': \'string\',
                  \'Email\': \'string\',
                  \'Fax\': \'string\',
                  \'ExtraParams\': [
                      {
                          \'Name\': \'DUNS_NUMBER\'|\'BRAND_NUMBER\'|\'BIRTH_DEPARTMENT\'|\'BIRTH_DATE_IN_YYYY_MM_DD\'|\'BIRTH_COUNTRY\'|\'BIRTH_CITY\'|\'DOCUMENT_NUMBER\'|\'AU_ID_NUMBER\'|\'AU_ID_TYPE\'|\'CA_LEGAL_TYPE\'|\'CA_BUSINESS_ENTITY_TYPE\'|\'ES_IDENTIFICATION\'|\'ES_IDENTIFICATION_TYPE\'|\'ES_LEGAL_FORM\'|\'FI_BUSINESS_NUMBER\'|\'FI_ID_NUMBER\'|\'FI_NATIONALITY\'|\'FI_ORGANIZATION_TYPE\'|\'IT_PIN\'|\'IT_REGISTRANT_ENTITY_TYPE\'|\'RU_PASSPORT_DATA\'|\'SE_ID_NUMBER\'|\'SG_ID_NUMBER\'|\'VAT_NUMBER\'|\'UK_CONTACT_TYPE\'|\'UK_COMPANY_NUMBER\',
                          \'Value\': \'string\'
                      },
                  ]
              },
              PrivacyProtectAdminContact=True|False,
              PrivacyProtectRegistrantContact=True|False,
              PrivacyProtectTechContact=True|False
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]** 
        
          The name of the domain that you want to transfer to Amazon Route 53.
        
          Constraints: The domain name can contain only the letters a through z, the numbers 0 through 9, and hyphen (-). Internationalized Domain Names are not supported.
        
        :type IdnLangCode: string
        :param IdnLangCode: 
        
          Reserved for future use.
        
        :type DurationInYears: integer
        :param DurationInYears: **[REQUIRED]** 
        
          The number of years that you want to register the domain for. Domains are registered for a minimum of one year. The maximum period depends on the top-level domain.
        
          Default: 1
        
        :type Nameservers: list
        :param Nameservers: 
        
          Contains details for the host and glue IP addresses.
        
          - *(dict) --* 
        
            Nameserver includes the following elements.
        
            - **Name** *(string) --* **[REQUIRED]** 
        
              The fully qualified host name of the name server.
        
              Constraint: Maximum 255 characters
        
            - **GlueIps** *(list) --* 
        
              Glue IP address of a name server entry. Glue IP addresses are required only when the name of the name server is a subdomain of the domain. For example, if your domain is example.com and the name server for the domain is ns.example.com, you need to specify the IP address for ns.example.com.
        
              Constraints: The list can contain only one IPv4 and one IPv6 address.
        
              - *(string) --* 
        
        :type AuthCode: string
        :param AuthCode: 
        
          The authorization code for the domain. You get this value from the current registrar.
        
        :type AutoRenew: boolean
        :param AutoRenew: 
        
          Indicates whether the domain will be automatically renewed (true) or not (false). Autorenewal only takes effect after the account is charged.
        
          Default: true
        
        :type AdminContact: dict
        :param AdminContact: **[REQUIRED]** 
        
          Provides detailed contact information.
        
          - **FirstName** *(string) --* 
        
            First name of contact.
        
          - **LastName** *(string) --* 
        
            Last name of contact.
        
          - **ContactType** *(string) --* 
        
            Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than ``PERSON`` , you must enter an organization name, and you can\'t enable privacy protection for the contact.
        
          - **OrganizationName** *(string) --* 
        
            Name of the organization for contact types other than ``PERSON`` .
        
          - **AddressLine1** *(string) --* 
        
            First line of the contact\'s address.
        
          - **AddressLine2** *(string) --* 
        
            Second line of contact\'s address, if any.
        
          - **City** *(string) --* 
        
            The city of the contact\'s address.
        
          - **State** *(string) --* 
        
            The state or province of the contact\'s city.
        
          - **CountryCode** *(string) --* 
        
            Code for the country of the contact\'s address.
        
          - **ZipCode** *(string) --* 
        
            The zip or postal code of the contact\'s address.
        
          - **PhoneNumber** *(string) --* 
        
            The phone number of the contact.
        
            Constraints: Phone number must be specified in the format \"+[country dialing code].[number including any area code>]\". For example, a US phone number might appear as ``\"+1.1234567890\"`` .
        
          - **Email** *(string) --* 
        
            Email address of the contact.
        
          - **Fax** *(string) --* 
        
            Fax number of the contact.
        
            Constraints: Phone number must be specified in the format \"+[country dialing code].[number including any area code]\". For example, a US phone number might appear as ``\"+1.1234567890\"`` .
        
          - **ExtraParams** *(list) --* 
        
            A list of name-value pairs for parameters required by certain top-level domains.
        
            - *(dict) --* 
        
              ExtraParam includes the following elements.
        
              - **Name** *(string) --* **[REQUIRED]** 
        
                Name of the additional parameter required by the top-level domain. Here are the top-level domains that require additional parameters and which parameters they require:
        
                * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``   
                 
                * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``   
                 
                * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``   
                 
                * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` , ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``   
                 
                * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``   
                 
                * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``   
                 
                * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``   
                 
                * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``   
                 
                * **.sg:**  ``SG_ID_NUMBER``   
                 
                * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``   
                 
                In addition, many TLDs require ``VAT_NUMBER`` .
        
              - **Value** *(string) --* **[REQUIRED]** 
        
                Values corresponding to the additional parameter names required by some top-level domains.
        
        :type RegistrantContact: dict
        :param RegistrantContact: **[REQUIRED]** 
        
          Provides detailed contact information.
        
          - **FirstName** *(string) --* 
        
            First name of contact.
        
          - **LastName** *(string) --* 
        
            Last name of contact.
        
          - **ContactType** *(string) --* 
        
            Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than ``PERSON`` , you must enter an organization name, and you can\'t enable privacy protection for the contact.
        
          - **OrganizationName** *(string) --* 
        
            Name of the organization for contact types other than ``PERSON`` .
        
          - **AddressLine1** *(string) --* 
        
            First line of the contact\'s address.
        
          - **AddressLine2** *(string) --* 
        
            Second line of contact\'s address, if any.
        
          - **City** *(string) --* 
        
            The city of the contact\'s address.
        
          - **State** *(string) --* 
        
            The state or province of the contact\'s city.
        
          - **CountryCode** *(string) --* 
        
            Code for the country of the contact\'s address.
        
          - **ZipCode** *(string) --* 
        
            The zip or postal code of the contact\'s address.
        
          - **PhoneNumber** *(string) --* 
        
            The phone number of the contact.
        
            Constraints: Phone number must be specified in the format \"+[country dialing code].[number including any area code>]\". For example, a US phone number might appear as ``\"+1.1234567890\"`` .
        
          - **Email** *(string) --* 
        
            Email address of the contact.
        
          - **Fax** *(string) --* 
        
            Fax number of the contact.
        
            Constraints: Phone number must be specified in the format \"+[country dialing code].[number including any area code]\". For example, a US phone number might appear as ``\"+1.1234567890\"`` .
        
          - **ExtraParams** *(list) --* 
        
            A list of name-value pairs for parameters required by certain top-level domains.
        
            - *(dict) --* 
        
              ExtraParam includes the following elements.
        
              - **Name** *(string) --* **[REQUIRED]** 
        
                Name of the additional parameter required by the top-level domain. Here are the top-level domains that require additional parameters and which parameters they require:
        
                * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``   
                 
                * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``   
                 
                * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``   
                 
                * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` , ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``   
                 
                * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``   
                 
                * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``   
                 
                * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``   
                 
                * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``   
                 
                * **.sg:**  ``SG_ID_NUMBER``   
                 
                * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``   
                 
                In addition, many TLDs require ``VAT_NUMBER`` .
        
              - **Value** *(string) --* **[REQUIRED]** 
        
                Values corresponding to the additional parameter names required by some top-level domains.
        
        :type TechContact: dict
        :param TechContact: **[REQUIRED]** 
        
          Provides detailed contact information.
        
          - **FirstName** *(string) --* 
        
            First name of contact.
        
          - **LastName** *(string) --* 
        
            Last name of contact.
        
          - **ContactType** *(string) --* 
        
            Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than ``PERSON`` , you must enter an organization name, and you can\'t enable privacy protection for the contact.
        
          - **OrganizationName** *(string) --* 
        
            Name of the organization for contact types other than ``PERSON`` .
        
          - **AddressLine1** *(string) --* 
        
            First line of the contact\'s address.
        
          - **AddressLine2** *(string) --* 
        
            Second line of contact\'s address, if any.
        
          - **City** *(string) --* 
        
            The city of the contact\'s address.
        
          - **State** *(string) --* 
        
            The state or province of the contact\'s city.
        
          - **CountryCode** *(string) --* 
        
            Code for the country of the contact\'s address.
        
          - **ZipCode** *(string) --* 
        
            The zip or postal code of the contact\'s address.
        
          - **PhoneNumber** *(string) --* 
        
            The phone number of the contact.
        
            Constraints: Phone number must be specified in the format \"+[country dialing code].[number including any area code>]\". For example, a US phone number might appear as ``\"+1.1234567890\"`` .
        
          - **Email** *(string) --* 
        
            Email address of the contact.
        
          - **Fax** *(string) --* 
        
            Fax number of the contact.
        
            Constraints: Phone number must be specified in the format \"+[country dialing code].[number including any area code]\". For example, a US phone number might appear as ``\"+1.1234567890\"`` .
        
          - **ExtraParams** *(list) --* 
        
            A list of name-value pairs for parameters required by certain top-level domains.
        
            - *(dict) --* 
        
              ExtraParam includes the following elements.
        
              - **Name** *(string) --* **[REQUIRED]** 
        
                Name of the additional parameter required by the top-level domain. Here are the top-level domains that require additional parameters and which parameters they require:
        
                * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``   
                 
                * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``   
                 
                * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``   
                 
                * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` , ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``   
                 
                * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``   
                 
                * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``   
                 
                * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``   
                 
                * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``   
                 
                * **.sg:**  ``SG_ID_NUMBER``   
                 
                * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``   
                 
                In addition, many TLDs require ``VAT_NUMBER`` .
        
              - **Value** *(string) --* **[REQUIRED]** 
        
                Values corresponding to the additional parameter names required by some top-level domains.
        
        :type PrivacyProtectAdminContact: boolean
        :param PrivacyProtectAdminContact: 
        
          Whether you want to conceal contact information from WHOIS queries. If you specify ``true`` , WHOIS (\"who is\") queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If you specify ``false`` , WHOIS queries return the information that you entered for the admin contact.
        
          Default: ``true``  
        
        :type PrivacyProtectRegistrantContact: boolean
        :param PrivacyProtectRegistrantContact: 
        
          Whether you want to conceal contact information from WHOIS queries. If you specify ``true`` , WHOIS (\"who is\") queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If you specify ``false`` , WHOIS queries return the information that you entered for the registrant contact (domain owner).
        
          Default: ``true``  
        
        :type PrivacyProtectTechContact: boolean
        :param PrivacyProtectTechContact: 
        
          Whether you want to conceal contact information from WHOIS queries. If you specify ``true`` , WHOIS (\"who is\") queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If you specify ``false`` , WHOIS queries return the information that you entered for the technical contact.
        
          Default: ``true``  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'OperationId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The TranserDomain response includes the following element.
        
            - **OperationId** *(string) --* 
        
              Identifier for tracking the progress of the request. To use this ID to query the operation status, use  GetOperationDetail .
        
        """
        pass

    def update_domain_contact(self, DomainName: str, AdminContact: Dict = None, RegistrantContact: Dict = None, TechContact: Dict = None) -> Dict:
        """
        
        If the update is successful, this method returns an operation ID that you can use to track the progress and completion of the action. If the request is not completed successfully, the domain registrant will be notified by email.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/UpdateDomainContact>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_domain_contact(
              DomainName=\'string\',
              AdminContact={
                  \'FirstName\': \'string\',
                  \'LastName\': \'string\',
                  \'ContactType\': \'PERSON\'|\'COMPANY\'|\'ASSOCIATION\'|\'PUBLIC_BODY\'|\'RESELLER\',
                  \'OrganizationName\': \'string\',
                  \'AddressLine1\': \'string\',
                  \'AddressLine2\': \'string\',
                  \'City\': \'string\',
                  \'State\': \'string\',
                  \'CountryCode\': \'AD\'|\'AE\'|\'AF\'|\'AG\'|\'AI\'|\'AL\'|\'AM\'|\'AN\'|\'AO\'|\'AQ\'|\'AR\'|\'AS\'|\'AT\'|\'AU\'|\'AW\'|\'AZ\'|\'BA\'|\'BB\'|\'BD\'|\'BE\'|\'BF\'|\'BG\'|\'BH\'|\'BI\'|\'BJ\'|\'BL\'|\'BM\'|\'BN\'|\'BO\'|\'BR\'|\'BS\'|\'BT\'|\'BW\'|\'BY\'|\'BZ\'|\'CA\'|\'CC\'|\'CD\'|\'CF\'|\'CG\'|\'CH\'|\'CI\'|\'CK\'|\'CL\'|\'CM\'|\'CN\'|\'CO\'|\'CR\'|\'CU\'|\'CV\'|\'CX\'|\'CY\'|\'CZ\'|\'DE\'|\'DJ\'|\'DK\'|\'DM\'|\'DO\'|\'DZ\'|\'EC\'|\'EE\'|\'EG\'|\'ER\'|\'ES\'|\'ET\'|\'FI\'|\'FJ\'|\'FK\'|\'FM\'|\'FO\'|\'FR\'|\'GA\'|\'GB\'|\'GD\'|\'GE\'|\'GH\'|\'GI\'|\'GL\'|\'GM\'|\'GN\'|\'GQ\'|\'GR\'|\'GT\'|\'GU\'|\'GW\'|\'GY\'|\'HK\'|\'HN\'|\'HR\'|\'HT\'|\'HU\'|\'ID\'|\'IE\'|\'IL\'|\'IM\'|\'IN\'|\'IQ\'|\'IR\'|\'IS\'|\'IT\'|\'JM\'|\'JO\'|\'JP\'|\'KE\'|\'KG\'|\'KH\'|\'KI\'|\'KM\'|\'KN\'|\'KP\'|\'KR\'|\'KW\'|\'KY\'|\'KZ\'|\'LA\'|\'LB\'|\'LC\'|\'LI\'|\'LK\'|\'LR\'|\'LS\'|\'LT\'|\'LU\'|\'LV\'|\'LY\'|\'MA\'|\'MC\'|\'MD\'|\'ME\'|\'MF\'|\'MG\'|\'MH\'|\'MK\'|\'ML\'|\'MM\'|\'MN\'|\'MO\'|\'MP\'|\'MR\'|\'MS\'|\'MT\'|\'MU\'|\'MV\'|\'MW\'|\'MX\'|\'MY\'|\'MZ\'|\'NA\'|\'NC\'|\'NE\'|\'NG\'|\'NI\'|\'NL\'|\'NO\'|\'NP\'|\'NR\'|\'NU\'|\'NZ\'|\'OM\'|\'PA\'|\'PE\'|\'PF\'|\'PG\'|\'PH\'|\'PK\'|\'PL\'|\'PM\'|\'PN\'|\'PR\'|\'PT\'|\'PW\'|\'PY\'|\'QA\'|\'RO\'|\'RS\'|\'RU\'|\'RW\'|\'SA\'|\'SB\'|\'SC\'|\'SD\'|\'SE\'|\'SG\'|\'SH\'|\'SI\'|\'SK\'|\'SL\'|\'SM\'|\'SN\'|\'SO\'|\'SR\'|\'ST\'|\'SV\'|\'SY\'|\'SZ\'|\'TC\'|\'TD\'|\'TG\'|\'TH\'|\'TJ\'|\'TK\'|\'TL\'|\'TM\'|\'TN\'|\'TO\'|\'TR\'|\'TT\'|\'TV\'|\'TW\'|\'TZ\'|\'UA\'|\'UG\'|\'US\'|\'UY\'|\'UZ\'|\'VA\'|\'VC\'|\'VE\'|\'VG\'|\'VI\'|\'VN\'|\'VU\'|\'WF\'|\'WS\'|\'YE\'|\'YT\'|\'ZA\'|\'ZM\'|\'ZW\',
                  \'ZipCode\': \'string\',
                  \'PhoneNumber\': \'string\',
                  \'Email\': \'string\',
                  \'Fax\': \'string\',
                  \'ExtraParams\': [
                      {
                          \'Name\': \'DUNS_NUMBER\'|\'BRAND_NUMBER\'|\'BIRTH_DEPARTMENT\'|\'BIRTH_DATE_IN_YYYY_MM_DD\'|\'BIRTH_COUNTRY\'|\'BIRTH_CITY\'|\'DOCUMENT_NUMBER\'|\'AU_ID_NUMBER\'|\'AU_ID_TYPE\'|\'CA_LEGAL_TYPE\'|\'CA_BUSINESS_ENTITY_TYPE\'|\'ES_IDENTIFICATION\'|\'ES_IDENTIFICATION_TYPE\'|\'ES_LEGAL_FORM\'|\'FI_BUSINESS_NUMBER\'|\'FI_ID_NUMBER\'|\'FI_NATIONALITY\'|\'FI_ORGANIZATION_TYPE\'|\'IT_PIN\'|\'IT_REGISTRANT_ENTITY_TYPE\'|\'RU_PASSPORT_DATA\'|\'SE_ID_NUMBER\'|\'SG_ID_NUMBER\'|\'VAT_NUMBER\'|\'UK_CONTACT_TYPE\'|\'UK_COMPANY_NUMBER\',
                          \'Value\': \'string\'
                      },
                  ]
              },
              RegistrantContact={
                  \'FirstName\': \'string\',
                  \'LastName\': \'string\',
                  \'ContactType\': \'PERSON\'|\'COMPANY\'|\'ASSOCIATION\'|\'PUBLIC_BODY\'|\'RESELLER\',
                  \'OrganizationName\': \'string\',
                  \'AddressLine1\': \'string\',
                  \'AddressLine2\': \'string\',
                  \'City\': \'string\',
                  \'State\': \'string\',
                  \'CountryCode\': \'AD\'|\'AE\'|\'AF\'|\'AG\'|\'AI\'|\'AL\'|\'AM\'|\'AN\'|\'AO\'|\'AQ\'|\'AR\'|\'AS\'|\'AT\'|\'AU\'|\'AW\'|\'AZ\'|\'BA\'|\'BB\'|\'BD\'|\'BE\'|\'BF\'|\'BG\'|\'BH\'|\'BI\'|\'BJ\'|\'BL\'|\'BM\'|\'BN\'|\'BO\'|\'BR\'|\'BS\'|\'BT\'|\'BW\'|\'BY\'|\'BZ\'|\'CA\'|\'CC\'|\'CD\'|\'CF\'|\'CG\'|\'CH\'|\'CI\'|\'CK\'|\'CL\'|\'CM\'|\'CN\'|\'CO\'|\'CR\'|\'CU\'|\'CV\'|\'CX\'|\'CY\'|\'CZ\'|\'DE\'|\'DJ\'|\'DK\'|\'DM\'|\'DO\'|\'DZ\'|\'EC\'|\'EE\'|\'EG\'|\'ER\'|\'ES\'|\'ET\'|\'FI\'|\'FJ\'|\'FK\'|\'FM\'|\'FO\'|\'FR\'|\'GA\'|\'GB\'|\'GD\'|\'GE\'|\'GH\'|\'GI\'|\'GL\'|\'GM\'|\'GN\'|\'GQ\'|\'GR\'|\'GT\'|\'GU\'|\'GW\'|\'GY\'|\'HK\'|\'HN\'|\'HR\'|\'HT\'|\'HU\'|\'ID\'|\'IE\'|\'IL\'|\'IM\'|\'IN\'|\'IQ\'|\'IR\'|\'IS\'|\'IT\'|\'JM\'|\'JO\'|\'JP\'|\'KE\'|\'KG\'|\'KH\'|\'KI\'|\'KM\'|\'KN\'|\'KP\'|\'KR\'|\'KW\'|\'KY\'|\'KZ\'|\'LA\'|\'LB\'|\'LC\'|\'LI\'|\'LK\'|\'LR\'|\'LS\'|\'LT\'|\'LU\'|\'LV\'|\'LY\'|\'MA\'|\'MC\'|\'MD\'|\'ME\'|\'MF\'|\'MG\'|\'MH\'|\'MK\'|\'ML\'|\'MM\'|\'MN\'|\'MO\'|\'MP\'|\'MR\'|\'MS\'|\'MT\'|\'MU\'|\'MV\'|\'MW\'|\'MX\'|\'MY\'|\'MZ\'|\'NA\'|\'NC\'|\'NE\'|\'NG\'|\'NI\'|\'NL\'|\'NO\'|\'NP\'|\'NR\'|\'NU\'|\'NZ\'|\'OM\'|\'PA\'|\'PE\'|\'PF\'|\'PG\'|\'PH\'|\'PK\'|\'PL\'|\'PM\'|\'PN\'|\'PR\'|\'PT\'|\'PW\'|\'PY\'|\'QA\'|\'RO\'|\'RS\'|\'RU\'|\'RW\'|\'SA\'|\'SB\'|\'SC\'|\'SD\'|\'SE\'|\'SG\'|\'SH\'|\'SI\'|\'SK\'|\'SL\'|\'SM\'|\'SN\'|\'SO\'|\'SR\'|\'ST\'|\'SV\'|\'SY\'|\'SZ\'|\'TC\'|\'TD\'|\'TG\'|\'TH\'|\'TJ\'|\'TK\'|\'TL\'|\'TM\'|\'TN\'|\'TO\'|\'TR\'|\'TT\'|\'TV\'|\'TW\'|\'TZ\'|\'UA\'|\'UG\'|\'US\'|\'UY\'|\'UZ\'|\'VA\'|\'VC\'|\'VE\'|\'VG\'|\'VI\'|\'VN\'|\'VU\'|\'WF\'|\'WS\'|\'YE\'|\'YT\'|\'ZA\'|\'ZM\'|\'ZW\',
                  \'ZipCode\': \'string\',
                  \'PhoneNumber\': \'string\',
                  \'Email\': \'string\',
                  \'Fax\': \'string\',
                  \'ExtraParams\': [
                      {
                          \'Name\': \'DUNS_NUMBER\'|\'BRAND_NUMBER\'|\'BIRTH_DEPARTMENT\'|\'BIRTH_DATE_IN_YYYY_MM_DD\'|\'BIRTH_COUNTRY\'|\'BIRTH_CITY\'|\'DOCUMENT_NUMBER\'|\'AU_ID_NUMBER\'|\'AU_ID_TYPE\'|\'CA_LEGAL_TYPE\'|\'CA_BUSINESS_ENTITY_TYPE\'|\'ES_IDENTIFICATION\'|\'ES_IDENTIFICATION_TYPE\'|\'ES_LEGAL_FORM\'|\'FI_BUSINESS_NUMBER\'|\'FI_ID_NUMBER\'|\'FI_NATIONALITY\'|\'FI_ORGANIZATION_TYPE\'|\'IT_PIN\'|\'IT_REGISTRANT_ENTITY_TYPE\'|\'RU_PASSPORT_DATA\'|\'SE_ID_NUMBER\'|\'SG_ID_NUMBER\'|\'VAT_NUMBER\'|\'UK_CONTACT_TYPE\'|\'UK_COMPANY_NUMBER\',
                          \'Value\': \'string\'
                      },
                  ]
              },
              TechContact={
                  \'FirstName\': \'string\',
                  \'LastName\': \'string\',
                  \'ContactType\': \'PERSON\'|\'COMPANY\'|\'ASSOCIATION\'|\'PUBLIC_BODY\'|\'RESELLER\',
                  \'OrganizationName\': \'string\',
                  \'AddressLine1\': \'string\',
                  \'AddressLine2\': \'string\',
                  \'City\': \'string\',
                  \'State\': \'string\',
                  \'CountryCode\': \'AD\'|\'AE\'|\'AF\'|\'AG\'|\'AI\'|\'AL\'|\'AM\'|\'AN\'|\'AO\'|\'AQ\'|\'AR\'|\'AS\'|\'AT\'|\'AU\'|\'AW\'|\'AZ\'|\'BA\'|\'BB\'|\'BD\'|\'BE\'|\'BF\'|\'BG\'|\'BH\'|\'BI\'|\'BJ\'|\'BL\'|\'BM\'|\'BN\'|\'BO\'|\'BR\'|\'BS\'|\'BT\'|\'BW\'|\'BY\'|\'BZ\'|\'CA\'|\'CC\'|\'CD\'|\'CF\'|\'CG\'|\'CH\'|\'CI\'|\'CK\'|\'CL\'|\'CM\'|\'CN\'|\'CO\'|\'CR\'|\'CU\'|\'CV\'|\'CX\'|\'CY\'|\'CZ\'|\'DE\'|\'DJ\'|\'DK\'|\'DM\'|\'DO\'|\'DZ\'|\'EC\'|\'EE\'|\'EG\'|\'ER\'|\'ES\'|\'ET\'|\'FI\'|\'FJ\'|\'FK\'|\'FM\'|\'FO\'|\'FR\'|\'GA\'|\'GB\'|\'GD\'|\'GE\'|\'GH\'|\'GI\'|\'GL\'|\'GM\'|\'GN\'|\'GQ\'|\'GR\'|\'GT\'|\'GU\'|\'GW\'|\'GY\'|\'HK\'|\'HN\'|\'HR\'|\'HT\'|\'HU\'|\'ID\'|\'IE\'|\'IL\'|\'IM\'|\'IN\'|\'IQ\'|\'IR\'|\'IS\'|\'IT\'|\'JM\'|\'JO\'|\'JP\'|\'KE\'|\'KG\'|\'KH\'|\'KI\'|\'KM\'|\'KN\'|\'KP\'|\'KR\'|\'KW\'|\'KY\'|\'KZ\'|\'LA\'|\'LB\'|\'LC\'|\'LI\'|\'LK\'|\'LR\'|\'LS\'|\'LT\'|\'LU\'|\'LV\'|\'LY\'|\'MA\'|\'MC\'|\'MD\'|\'ME\'|\'MF\'|\'MG\'|\'MH\'|\'MK\'|\'ML\'|\'MM\'|\'MN\'|\'MO\'|\'MP\'|\'MR\'|\'MS\'|\'MT\'|\'MU\'|\'MV\'|\'MW\'|\'MX\'|\'MY\'|\'MZ\'|\'NA\'|\'NC\'|\'NE\'|\'NG\'|\'NI\'|\'NL\'|\'NO\'|\'NP\'|\'NR\'|\'NU\'|\'NZ\'|\'OM\'|\'PA\'|\'PE\'|\'PF\'|\'PG\'|\'PH\'|\'PK\'|\'PL\'|\'PM\'|\'PN\'|\'PR\'|\'PT\'|\'PW\'|\'PY\'|\'QA\'|\'RO\'|\'RS\'|\'RU\'|\'RW\'|\'SA\'|\'SB\'|\'SC\'|\'SD\'|\'SE\'|\'SG\'|\'SH\'|\'SI\'|\'SK\'|\'SL\'|\'SM\'|\'SN\'|\'SO\'|\'SR\'|\'ST\'|\'SV\'|\'SY\'|\'SZ\'|\'TC\'|\'TD\'|\'TG\'|\'TH\'|\'TJ\'|\'TK\'|\'TL\'|\'TM\'|\'TN\'|\'TO\'|\'TR\'|\'TT\'|\'TV\'|\'TW\'|\'TZ\'|\'UA\'|\'UG\'|\'US\'|\'UY\'|\'UZ\'|\'VA\'|\'VC\'|\'VE\'|\'VG\'|\'VI\'|\'VN\'|\'VU\'|\'WF\'|\'WS\'|\'YE\'|\'YT\'|\'ZA\'|\'ZM\'|\'ZW\',
                  \'ZipCode\': \'string\',
                  \'PhoneNumber\': \'string\',
                  \'Email\': \'string\',
                  \'Fax\': \'string\',
                  \'ExtraParams\': [
                      {
                          \'Name\': \'DUNS_NUMBER\'|\'BRAND_NUMBER\'|\'BIRTH_DEPARTMENT\'|\'BIRTH_DATE_IN_YYYY_MM_DD\'|\'BIRTH_COUNTRY\'|\'BIRTH_CITY\'|\'DOCUMENT_NUMBER\'|\'AU_ID_NUMBER\'|\'AU_ID_TYPE\'|\'CA_LEGAL_TYPE\'|\'CA_BUSINESS_ENTITY_TYPE\'|\'ES_IDENTIFICATION\'|\'ES_IDENTIFICATION_TYPE\'|\'ES_LEGAL_FORM\'|\'FI_BUSINESS_NUMBER\'|\'FI_ID_NUMBER\'|\'FI_NATIONALITY\'|\'FI_ORGANIZATION_TYPE\'|\'IT_PIN\'|\'IT_REGISTRANT_ENTITY_TYPE\'|\'RU_PASSPORT_DATA\'|\'SE_ID_NUMBER\'|\'SG_ID_NUMBER\'|\'VAT_NUMBER\'|\'UK_CONTACT_TYPE\'|\'UK_COMPANY_NUMBER\',
                          \'Value\': \'string\'
                      },
                  ]
              }
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]** 
        
          The name of the domain that you want to update contact information for.
        
        :type AdminContact: dict
        :param AdminContact: 
        
          Provides detailed contact information.
        
          - **FirstName** *(string) --* 
        
            First name of contact.
        
          - **LastName** *(string) --* 
        
            Last name of contact.
        
          - **ContactType** *(string) --* 
        
            Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than ``PERSON`` , you must enter an organization name, and you can\'t enable privacy protection for the contact.
        
          - **OrganizationName** *(string) --* 
        
            Name of the organization for contact types other than ``PERSON`` .
        
          - **AddressLine1** *(string) --* 
        
            First line of the contact\'s address.
        
          - **AddressLine2** *(string) --* 
        
            Second line of contact\'s address, if any.
        
          - **City** *(string) --* 
        
            The city of the contact\'s address.
        
          - **State** *(string) --* 
        
            The state or province of the contact\'s city.
        
          - **CountryCode** *(string) --* 
        
            Code for the country of the contact\'s address.
        
          - **ZipCode** *(string) --* 
        
            The zip or postal code of the contact\'s address.
        
          - **PhoneNumber** *(string) --* 
        
            The phone number of the contact.
        
            Constraints: Phone number must be specified in the format \"+[country dialing code].[number including any area code>]\". For example, a US phone number might appear as ``\"+1.1234567890\"`` .
        
          - **Email** *(string) --* 
        
            Email address of the contact.
        
          - **Fax** *(string) --* 
        
            Fax number of the contact.
        
            Constraints: Phone number must be specified in the format \"+[country dialing code].[number including any area code]\". For example, a US phone number might appear as ``\"+1.1234567890\"`` .
        
          - **ExtraParams** *(list) --* 
        
            A list of name-value pairs for parameters required by certain top-level domains.
        
            - *(dict) --* 
        
              ExtraParam includes the following elements.
        
              - **Name** *(string) --* **[REQUIRED]** 
        
                Name of the additional parameter required by the top-level domain. Here are the top-level domains that require additional parameters and which parameters they require:
        
                * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``   
                 
                * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``   
                 
                * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``   
                 
                * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` , ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``   
                 
                * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``   
                 
                * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``   
                 
                * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``   
                 
                * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``   
                 
                * **.sg:**  ``SG_ID_NUMBER``   
                 
                * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``   
                 
                In addition, many TLDs require ``VAT_NUMBER`` .
        
              - **Value** *(string) --* **[REQUIRED]** 
        
                Values corresponding to the additional parameter names required by some top-level domains.
        
        :type RegistrantContact: dict
        :param RegistrantContact: 
        
          Provides detailed contact information.
        
          - **FirstName** *(string) --* 
        
            First name of contact.
        
          - **LastName** *(string) --* 
        
            Last name of contact.
        
          - **ContactType** *(string) --* 
        
            Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than ``PERSON`` , you must enter an organization name, and you can\'t enable privacy protection for the contact.
        
          - **OrganizationName** *(string) --* 
        
            Name of the organization for contact types other than ``PERSON`` .
        
          - **AddressLine1** *(string) --* 
        
            First line of the contact\'s address.
        
          - **AddressLine2** *(string) --* 
        
            Second line of contact\'s address, if any.
        
          - **City** *(string) --* 
        
            The city of the contact\'s address.
        
          - **State** *(string) --* 
        
            The state or province of the contact\'s city.
        
          - **CountryCode** *(string) --* 
        
            Code for the country of the contact\'s address.
        
          - **ZipCode** *(string) --* 
        
            The zip or postal code of the contact\'s address.
        
          - **PhoneNumber** *(string) --* 
        
            The phone number of the contact.
        
            Constraints: Phone number must be specified in the format \"+[country dialing code].[number including any area code>]\". For example, a US phone number might appear as ``\"+1.1234567890\"`` .
        
          - **Email** *(string) --* 
        
            Email address of the contact.
        
          - **Fax** *(string) --* 
        
            Fax number of the contact.
        
            Constraints: Phone number must be specified in the format \"+[country dialing code].[number including any area code]\". For example, a US phone number might appear as ``\"+1.1234567890\"`` .
        
          - **ExtraParams** *(list) --* 
        
            A list of name-value pairs for parameters required by certain top-level domains.
        
            - *(dict) --* 
        
              ExtraParam includes the following elements.
        
              - **Name** *(string) --* **[REQUIRED]** 
        
                Name of the additional parameter required by the top-level domain. Here are the top-level domains that require additional parameters and which parameters they require:
        
                * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``   
                 
                * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``   
                 
                * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``   
                 
                * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` , ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``   
                 
                * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``   
                 
                * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``   
                 
                * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``   
                 
                * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``   
                 
                * **.sg:**  ``SG_ID_NUMBER``   
                 
                * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``   
                 
                In addition, many TLDs require ``VAT_NUMBER`` .
        
              - **Value** *(string) --* **[REQUIRED]** 
        
                Values corresponding to the additional parameter names required by some top-level domains.
        
        :type TechContact: dict
        :param TechContact: 
        
          Provides detailed contact information.
        
          - **FirstName** *(string) --* 
        
            First name of contact.
        
          - **LastName** *(string) --* 
        
            Last name of contact.
        
          - **ContactType** *(string) --* 
        
            Indicates whether the contact is a person, company, association, or public organization. If you choose an option other than ``PERSON`` , you must enter an organization name, and you can\'t enable privacy protection for the contact.
        
          - **OrganizationName** *(string) --* 
        
            Name of the organization for contact types other than ``PERSON`` .
        
          - **AddressLine1** *(string) --* 
        
            First line of the contact\'s address.
        
          - **AddressLine2** *(string) --* 
        
            Second line of contact\'s address, if any.
        
          - **City** *(string) --* 
        
            The city of the contact\'s address.
        
          - **State** *(string) --* 
        
            The state or province of the contact\'s city.
        
          - **CountryCode** *(string) --* 
        
            Code for the country of the contact\'s address.
        
          - **ZipCode** *(string) --* 
        
            The zip or postal code of the contact\'s address.
        
          - **PhoneNumber** *(string) --* 
        
            The phone number of the contact.
        
            Constraints: Phone number must be specified in the format \"+[country dialing code].[number including any area code>]\". For example, a US phone number might appear as ``\"+1.1234567890\"`` .
        
          - **Email** *(string) --* 
        
            Email address of the contact.
        
          - **Fax** *(string) --* 
        
            Fax number of the contact.
        
            Constraints: Phone number must be specified in the format \"+[country dialing code].[number including any area code]\". For example, a US phone number might appear as ``\"+1.1234567890\"`` .
        
          - **ExtraParams** *(list) --* 
        
            A list of name-value pairs for parameters required by certain top-level domains.
        
            - *(dict) --* 
        
              ExtraParam includes the following elements.
        
              - **Name** *(string) --* **[REQUIRED]** 
        
                Name of the additional parameter required by the top-level domain. Here are the top-level domains that require additional parameters and which parameters they require:
        
                * **.com.au and .net.au:**  ``AU_ID_NUMBER`` and ``AU_ID_TYPE``   
                 
                * **.ca:**  ``BRAND_NUMBER`` , ``CA_LEGAL_TYPE`` , and ``CA_BUSINESS_ENTITY_TYPE``   
                 
                * **.es:**  ``ES_IDENTIFICATION`` , ``ES_IDENTIFICATION_TYPE`` , and ``ES_LEGAL_FORM``   
                 
                * **.fi:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``FI_BUSINESS_NUMBER`` , ``FI_ID_NUMBER`` , ``FI_NATIONALITY`` , and ``FI_ORGANIZATION_TYPE``   
                 
                * **.fr:**  ``BRAND_NUMBER`` , ``BIRTH_DEPARTMENT`` , ``BIRTH_DATE_IN_YYYY_MM_DD`` , ``BIRTH_COUNTRY`` , and ``BIRTH_CITY``   
                 
                * **.it:**  ``BIRTH_COUNTRY`` , ``IT_PIN`` , and ``IT_REGISTRANT_ENTITY_TYPE``   
                 
                * **.ru:**  ``BIRTH_DATE_IN_YYYY_MM_DD`` and ``RU_PASSPORT_DATA``   
                 
                * **.se:**  ``BIRTH_COUNTRY`` and ``SE_ID_NUMBER``   
                 
                * **.sg:**  ``SG_ID_NUMBER``   
                 
                * **.co.uk, .me.uk, and .org.uk:**  ``UK_CONTACT_TYPE`` and ``UK_COMPANY_NUMBER``   
                 
                In addition, many TLDs require ``VAT_NUMBER`` .
        
              - **Value** *(string) --* **[REQUIRED]** 
        
                Values corresponding to the additional parameter names required by some top-level domains.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'OperationId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The UpdateDomainContact response includes the following element.
        
            - **OperationId** *(string) --* 
        
              Identifier for tracking the progress of the request. To use this ID to query the operation status, use  GetOperationDetail .
        
        """
        pass

    def update_domain_contact_privacy(self, DomainName: str, AdminPrivacy: bool = None, RegistrantPrivacy: bool = None, TechPrivacy: bool = None) -> Dict:
        """
        
        This operation affects only the contact information for the specified contact type (registrant, administrator, or tech). If the request succeeds, Amazon Route 53 returns an operation ID that you can use with  GetOperationDetail to track the progress and completion of the action. If the request doesn\'t complete successfully, the domain registrant will be notified by email.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/UpdateDomainContactPrivacy>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_domain_contact_privacy(
              DomainName=\'string\',
              AdminPrivacy=True|False,
              RegistrantPrivacy=True|False,
              TechPrivacy=True|False
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]** 
        
          The name of the domain that you want to update the privacy setting for.
        
        :type AdminPrivacy: boolean
        :param AdminPrivacy: 
        
          Whether you want to conceal contact information from WHOIS queries. If you specify ``true`` , WHOIS (\"who is\") queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If you specify ``false`` , WHOIS queries return the information that you entered for the admin contact.
        
        :type RegistrantPrivacy: boolean
        :param RegistrantPrivacy: 
        
          Whether you want to conceal contact information from WHOIS queries. If you specify ``true`` , WHOIS (\"who is\") queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If you specify ``false`` , WHOIS queries return the information that you entered for the registrant contact (domain owner).
        
        :type TechPrivacy: boolean
        :param TechPrivacy: 
        
          Whether you want to conceal contact information from WHOIS queries. If you specify ``true`` , WHOIS (\"who is\") queries return contact information either for Amazon Registrar (for .com, .net, and .org domains) or for our registrar associate, Gandi (for all other TLDs). If you specify ``false`` , WHOIS queries return the information that you entered for the technical contact.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'OperationId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The UpdateDomainContactPrivacy response includes the following element.
        
            - **OperationId** *(string) --* 
        
              Identifier for tracking the progress of the request. To use this ID to query the operation status, use GetOperationDetail.
        
        """
        pass

    def update_domain_nameservers(self, DomainName: str, Nameservers: List, FIAuthKey: str = None) -> Dict:
        """
        
        If successful, this operation returns an operation ID that you can use to track the progress and completion of the action. If the request is not completed successfully, the domain registrant will be notified by email.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/UpdateDomainNameservers>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_domain_nameservers(
              DomainName=\'string\',
              FIAuthKey=\'string\',
              Nameservers=[
                  {
                      \'Name\': \'string\',
                      \'GlueIps\': [
                          \'string\',
                      ]
                  },
              ]
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]** 
        
          The name of the domain that you want to change name servers for.
        
        :type FIAuthKey: string
        :param FIAuthKey: 
        
          The authorization key for .fi domains
        
        :type Nameservers: list
        :param Nameservers: **[REQUIRED]** 
        
          A list of new name servers for the domain.
        
          - *(dict) --* 
        
            Nameserver includes the following elements.
        
            - **Name** *(string) --* **[REQUIRED]** 
        
              The fully qualified host name of the name server.
        
              Constraint: Maximum 255 characters
        
            - **GlueIps** *(list) --* 
        
              Glue IP address of a name server entry. Glue IP addresses are required only when the name of the name server is a subdomain of the domain. For example, if your domain is example.com and the name server for the domain is ns.example.com, you need to specify the IP address for ns.example.com.
        
              Constraints: The list can contain only one IPv4 and one IPv6 address.
        
              - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'OperationId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The UpdateDomainNameservers response includes the following element.
        
            - **OperationId** *(string) --* 
        
              Identifier for tracking the progress of the request. To use this ID to query the operation status, use  GetOperationDetail .
        
        """
        pass

    def update_tags_for_domain(self, DomainName: str, TagsToUpdate: List = None) -> Dict:
        """
        
        All tag operations are eventually consistent; subsequent operations might not immediately represent all issued operations.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/UpdateTagsForDomain>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_tags_for_domain(
              DomainName=\'string\',
              TagsToUpdate=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]** 
        
          The domain for which you want to add or update tags.
        
        :type TagsToUpdate: list
        :param TagsToUpdate: 
        
          A list of the tag keys and values that you want to add or update. If you specify a key that already exists, the corresponding value will be replaced.
        
          - *(dict) --* 
        
            Each tag includes the following elements.
        
            - **Key** *(string) --* 
        
              The key (name) of a tag.
        
              Valid values: A-Z, a-z, 0-9, space, \".:/=+\-@\"
        
              Constraints: Each key can be 1-128 characters long.
        
            - **Value** *(string) --* 
        
              The value of a tag.
        
              Valid values: A-Z, a-z, 0-9, space, \".:/=+\-@\"
        
              Constraints: Each value can be 0-256 characters long.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 
        """
        pass

    def view_billing(self, Start: datetime = None, End: datetime = None, Marker: str = None, MaxItems: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/ViewBilling>`_
        
        **Request Syntax** 
        ::
        
          response = client.view_billing(
              Start=datetime(2015, 1, 1),
              End=datetime(2015, 1, 1),
              Marker=\'string\',
              MaxItems=123
          )
        :type Start: datetime
        :param Start: 
        
          The beginning date and time for the time period for which you want a list of billing records. Specify the date and time in Coordinated Universal time (UTC).
        
        :type End: datetime
        :param End: 
        
          The end date and time for the time period for which you want a list of billing records. Specify the date and time in Coordinated Universal time (UTC).
        
        :type Marker: string
        :param Marker: 
        
          For an initial request for a list of billing records, omit this element. If the number of billing records that are associated with the current AWS account during the specified period is greater than the value that you specified for ``MaxItems`` , you can use ``Marker`` to return additional billing records. Get the value of ``NextPageMarker`` from the previous response, and submit another request that includes the value of ``NextPageMarker`` in the ``Marker`` element. 
        
          Constraints: The marker must match the value of ``NextPageMarker`` that was returned in the previous response.
        
        :type MaxItems: integer
        :param MaxItems: 
        
          The number of billing records to be returned.
        
          Default: 20
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextPageMarker\': \'string\',
                \'BillingRecords\': [
                    {
                        \'DomainName\': \'string\',
                        \'Operation\': \'REGISTER_DOMAIN\'|\'DELETE_DOMAIN\'|\'TRANSFER_IN_DOMAIN\'|\'UPDATE_DOMAIN_CONTACT\'|\'UPDATE_NAMESERVER\'|\'CHANGE_PRIVACY_PROTECTION\'|\'DOMAIN_LOCK\'|\'ENABLE_AUTORENEW\'|\'DISABLE_AUTORENEW\'|\'ADD_DNSSEC\'|\'REMOVE_DNSSEC\'|\'EXPIRE_DOMAIN\'|\'TRANSFER_OUT_DOMAIN\'|\'CHANGE_DOMAIN_OWNER\'|\'RENEW_DOMAIN\'|\'PUSH_DOMAIN\',
                        \'InvoiceId\': \'string\',
                        \'BillDate\': datetime(2015, 1, 1),
                        \'Price\': 123.0
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The ViewBilling response includes the following elements.
        
            - **NextPageMarker** *(string) --* 
        
              If there are more billing records than you specified for ``MaxItems`` in the request, submit another request and include the value of ``NextPageMarker`` in the value of ``Marker`` .
        
            - **BillingRecords** *(list) --* 
        
              A summary of billing records.
        
              - *(dict) --* 
        
                Information for one billing record.
        
                - **DomainName** *(string) --* 
        
                  The name of the domain that the billing record applies to. If the domain name contains characters other than a-z, 0-9, and - (hyphen), such as an internationalized domain name, then this value is in Punycode. For more information, see `DNS Domain Name Format <http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html>`__ in the *Amazon Route 53 Developer Guidezzz* .
        
                - **Operation** *(string) --* 
        
                  The operation that you were charged for.
        
                - **InvoiceId** *(string) --* 
        
                  The ID of the invoice that is associated with the billing record.
        
                - **BillDate** *(datetime) --* 
        
                  The date that the operation was billed, in Unix format.
        
                - **Price** *(float) --* 
        
                  The price that you were charged for the operation, in US dollars.
        
                  Example value: 12.0
        
        """
        pass
