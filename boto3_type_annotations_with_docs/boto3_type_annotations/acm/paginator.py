from typing import List
from typing import Dict
from botocore.paginate import Paginator


class ListCertificates(Paginator):
    def paginate(self, CertificateStatuses: List = None, Includes: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/ListCertificates>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              CertificateStatuses=[
                  \'PENDING_VALIDATION\'|\'ISSUED\'|\'INACTIVE\'|\'EXPIRED\'|\'VALIDATION_TIMED_OUT\'|\'REVOKED\'|\'FAILED\',
              ],
              Includes={
                  \'extendedKeyUsage\': [
                      \'TLS_WEB_SERVER_AUTHENTICATION\'|\'TLS_WEB_CLIENT_AUTHENTICATION\'|\'CODE_SIGNING\'|\'EMAIL_PROTECTION\'|\'TIME_STAMPING\'|\'OCSP_SIGNING\'|\'IPSEC_END_SYSTEM\'|\'IPSEC_TUNNEL\'|\'IPSEC_USER\'|\'ANY\'|\'NONE\'|\'CUSTOM\',
                  ],
                  \'keyUsage\': [
                      \'DIGITAL_SIGNATURE\'|\'NON_REPUDIATION\'|\'KEY_ENCIPHERMENT\'|\'DATA_ENCIPHERMENT\'|\'KEY_AGREEMENT\'|\'CERTIFICATE_SIGNING\'|\'CRL_SIGNING\'|\'ENCIPHER_ONLY\'|\'DECIPHER_ONLY\'|\'ANY\'|\'CUSTOM\',
                  ],
                  \'keyTypes\': [
                      \'RSA_2048\'|\'RSA_1024\'|\'RSA_4096\'|\'EC_prime256v1\'|\'EC_secp384r1\'|\'EC_secp521r1\',
                  ]
              },
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type CertificateStatuses: list
        :param CertificateStatuses: 
        
          Filter the certificate list by status value.
        
          - *(string) --* 
        
        :type Includes: dict
        :param Includes: 
        
          Filter the certificate list. For more information, see the  Filters structure.
        
          - **extendedKeyUsage** *(list) --* 
        
            Specify one or more  ExtendedKeyUsage extension values.
        
            - *(string) --* 
        
          - **keyUsage** *(list) --* 
        
            Specify one or more  KeyUsage extension values.
        
            - *(string) --* 
        
          - **keyTypes** *(list) --* 
        
            Specify one or more algorithms that can be used to generate key pairs.
        
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
                \'CertificateSummaryList\': [
                    {
                        \'CertificateArn\': \'string\',
                        \'DomainName\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **CertificateSummaryList** *(list) --* 
        
              A list of ACM certificates.
        
              - *(dict) --* 
        
                This structure is returned in the response object of  ListCertificates action. 
        
                - **CertificateArn** *(string) --* 
        
                  Amazon Resource Name (ARN) of the certificate. This is of the form:
        
                   ``arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012``  
        
                  For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ . 
        
                - **DomainName** *(string) --* 
        
                  Fully qualified domain name (FQDN), such as www.example.com or example.com, for the certificate.
        
        """
        pass
