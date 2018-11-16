from typing import Optional
from typing import Union
from typing import List
from botocore.waiter import Waiter
from botocore.paginate import Paginator
from typing import Dict
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

    def create_certificate_authority(self, CertificateAuthorityConfiguration: Dict, CertificateAuthorityType: str, RevocationConfiguration: Dict = None, IdempotencyToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-pca-2017-08-22/CreateCertificateAuthority>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_certificate_authority(
              CertificateAuthorityConfiguration={
                  \'KeyAlgorithm\': \'RSA_2048\'|\'RSA_4096\'|\'EC_prime256v1\'|\'EC_secp384r1\',
                  \'SigningAlgorithm\': \'SHA256WITHECDSA\'|\'SHA384WITHECDSA\'|\'SHA512WITHECDSA\'|\'SHA256WITHRSA\'|\'SHA384WITHRSA\'|\'SHA512WITHRSA\',
                  \'Subject\': {
                      \'Country\': \'string\',
                      \'Organization\': \'string\',
                      \'OrganizationalUnit\': \'string\',
                      \'DistinguishedNameQualifier\': \'string\',
                      \'State\': \'string\',
                      \'CommonName\': \'string\',
                      \'SerialNumber\': \'string\',
                      \'Locality\': \'string\',
                      \'Title\': \'string\',
                      \'Surname\': \'string\',
                      \'GivenName\': \'string\',
                      \'Initials\': \'string\',
                      \'Pseudonym\': \'string\',
                      \'GenerationQualifier\': \'string\'
                  }
              },
              RevocationConfiguration={
                  \'CrlConfiguration\': {
                      \'Enabled\': True|False,
                      \'ExpirationInDays\': 123,
                      \'CustomCname\': \'string\',
                      \'S3BucketName\': \'string\'
                  }
              },
              CertificateAuthorityType=\'SUBORDINATE\',
              IdempotencyToken=\'string\'
          )
        :type CertificateAuthorityConfiguration: dict
        :param CertificateAuthorityConfiguration: **[REQUIRED]** 
        
          Name and bit size of the private key algorithm, the name of the signing algorithm, and X.500 certificate subject information.
        
          - **KeyAlgorithm** *(string) --* **[REQUIRED]** 
        
            Type of the public key algorithm and size, in bits, of the key pair that your key pair creates when it issues a certificate.
        
          - **SigningAlgorithm** *(string) --* **[REQUIRED]** 
        
            Name of the algorithm your private CA uses to sign certificate requests.
        
          - **Subject** *(dict) --* **[REQUIRED]** 
        
            Structure that contains X.500 distinguished name information for your private CA.
        
            - **Country** *(string) --* 
        
              Two-digit code that specifies the country in which the certificate subject located.
        
            - **Organization** *(string) --* 
        
              Legal name of the organization with which the certificate subject is affiliated. 
        
            - **OrganizationalUnit** *(string) --* 
        
              A subdivision or unit of the organization (such as sales or finance) with which the certificate subject is affiliated.
        
            - **DistinguishedNameQualifier** *(string) --* 
        
              Disambiguating information for the certificate subject.
        
            - **State** *(string) --* 
        
              State in which the subject of the certificate is located.
        
            - **CommonName** *(string) --* 
        
              Fully qualified domain name (FQDN) associated with the certificate subject.
        
            - **SerialNumber** *(string) --* 
        
              The certificate serial number.
        
            - **Locality** *(string) --* 
        
              The locality (such as a city or town) in which the certificate subject is located.
        
            - **Title** *(string) --* 
        
              A title such as Mr. or Ms., which is pre-pended to the name to refer formally to the certificate subject.
        
            - **Surname** *(string) --* 
        
              Family name. In the US and the UK, for example, the surname of an individual is ordered last. In Asian cultures the surname is typically ordered first.
        
            - **GivenName** *(string) --* 
        
              First name.
        
            - **Initials** *(string) --* 
        
              Concatenation that typically contains the first letter of the **GivenName** , the first letter of the middle name if one exists, and the first letter of the **SurName** .
        
            - **Pseudonym** *(string) --* 
        
              Typically a shortened version of a longer **GivenName** . For example, Jonathan is often shortened to John. Elizabeth is often shortened to Beth, Liz, or Eliza.
        
            - **GenerationQualifier** *(string) --* 
        
              Typically a qualifier appended to the name of an individual. Examples include Jr. for junior, Sr. for senior, and III for third.
        
        :type RevocationConfiguration: dict
        :param RevocationConfiguration: 
        
          Contains a Boolean value that you can use to enable a certification revocation list (CRL) for the CA, the name of the S3 bucket to which ACM PCA will write the CRL, and an optional CNAME alias that you can use to hide the name of your bucket in the **CRL Distribution Points** extension of your CA certificate. For more information, see the  CrlConfiguration structure. 
        
          - **CrlConfiguration** *(dict) --* 
        
            Configuration of the certificate revocation list (CRL), if any, maintained by your private CA.
        
            - **Enabled** *(boolean) --* **[REQUIRED]** 
        
              Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. You can use this value to enable certificate revocation for a new CA when you call the  CreateCertificateAuthority operation or for an existing CA when you call the  UpdateCertificateAuthority operation. 
        
            - **ExpirationInDays** *(integer) --* 
        
              Number of days until a certificate expires.
        
            - **CustomCname** *(string) --* 
        
              Name inserted into the certificate **CRL Distribution Points** extension that enables the use of an alias for the CRL distribution point. Use this value if you don\'t want the name of your S3 bucket to be public.
        
            - **S3BucketName** *(string) --* 
        
              Name of the S3 bucket that contains the CRL. If you do not provide a value for the **CustomCname** argument, the name of your S3 bucket is placed into the **CRL Distribution Points** extension of the issued certificate. You can change the name of your bucket by calling the  UpdateCertificateAuthority operation. You must specify a bucket policy that allows ACM PCA to write the CRL to your bucket.
        
        :type CertificateAuthorityType: string
        :param CertificateAuthorityType: **[REQUIRED]** 
        
          The type of the certificate authority. Currently, this must be **SUBORDINATE** .
        
        :type IdempotencyToken: string
        :param IdempotencyToken: 
        
          Alphanumeric string that can be used to distinguish between calls to **CreateCertificateAuthority** . Idempotency tokens time out after five minutes. Therefore, if you call **CreateCertificateAuthority** multiple times with the same idempotency token within a five minute period, ACM PCA recognizes that you are requesting only one certificate. As a result, ACM PCA issues only one. If you change the idempotency token for each call, however, ACM PCA recognizes that you are requesting multiple certificates.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'CertificateAuthorityArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **CertificateAuthorityArn** *(string) --* 
        
              If successful, the Amazon Resource Name (ARN) of the certificate authority (CA). This is of the form: 
        
               ``arn:aws:acm-pca:*region* :*account* :certificate-authority/*12345678-1234-1234-1234-123456789012* `` . 
        
        """
        pass

    def create_certificate_authority_audit_report(self, CertificateAuthorityArn: str, S3BucketName: str, AuditReportResponseFormat: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-pca-2017-08-22/CreateCertificateAuthorityAuditReport>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_certificate_authority_audit_report(
              CertificateAuthorityArn=\'string\',
              S3BucketName=\'string\',
              AuditReportResponseFormat=\'JSON\'|\'CSV\'
          )
        :type CertificateAuthorityArn: string
        :param CertificateAuthorityArn: **[REQUIRED]** 
        
          Amazon Resource Name (ARN) of the CA to be audited. This is of the form:
        
           ``arn:aws:acm-pca:*region* :*account* :certificate-authority/*12345678-1234-1234-1234-123456789012* `` .
        
        :type S3BucketName: string
        :param S3BucketName: **[REQUIRED]** 
        
          Name of the S3 bucket that will contain the audit report.
        
        :type AuditReportResponseFormat: string
        :param AuditReportResponseFormat: **[REQUIRED]** 
        
          Format in which to create the report. This can be either **JSON** or **CSV** .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AuditReportId\': \'string\',
                \'S3Key\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AuditReportId** *(string) --* 
        
              An alphanumeric string that contains a report identifier.
        
            - **S3Key** *(string) --* 
        
              The **key** that uniquely identifies the report file in your S3 bucket.
        
        """
        pass

    def delete_certificate_authority(self, CertificateAuthorityArn: str, PermanentDeletionTimeInDays: int = None):
        """
        
        Additionally, you can delete a CA if you are waiting for it to be created (the **Status** field of the  CertificateAuthority is ``CREATING`` ). You can also delete it if the CA has been created but you haven\'t yet imported the signed certificate (the **Status** is ``PENDING_CERTIFICATE`` ) into ACM PCA. 
        
        If the CA is in one of the aforementioned states and you call  DeleteCertificateAuthority , the CA\'s status changes to ``DELETED`` . However, the CA won\'t be permentantly deleted until the restoration period has passed. By default, if you do not set the ``PermanentDeletionTimeInDays`` parameter, the CA remains restorable for 30 days. You can set the parameter from 7 to 30 days. The  DescribeCertificateAuthority operation returns the time remaining in the restoration window of a Private CA in the ``DELETED`` state. To restore an eligable CA, call the  RestoreCertificateAuthority operation.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-pca-2017-08-22/DeleteCertificateAuthority>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_certificate_authority(
              CertificateAuthorityArn=\'string\',
              PermanentDeletionTimeInDays=123
          )
        :type CertificateAuthorityArn: string
        :param CertificateAuthorityArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that was returned when you called  CreateCertificateAuthority . This must have the following form: 
        
           ``arn:aws:acm-pca:*region* :*account* :certificate-authority/*12345678-1234-1234-1234-123456789012* `` . 
        
        :type PermanentDeletionTimeInDays: integer
        :param PermanentDeletionTimeInDays: 
        
          The number of days to make a CA restorable after it has been deleted. This can be anywhere from 7 to 30 days, with 30 being the default.
        
        :returns: None
        """
        pass

    def describe_certificate_authority(self, CertificateAuthorityArn: str) -> Dict:
        """
        
        * ``CREATING`` - ACM PCA is creating your private certificate authority. 
         
        * ``PENDING_CERTIFICATE`` - The certificate is pending. You must use your on-premises root or subordinate CA to sign your private CA CSR and then import it into PCA.  
         
        * ``ACTIVE`` - Your private CA is active. 
         
        * ``DISABLED`` - Your private CA has been disabled. 
         
        * ``EXPIRED`` - Your private CA certificate has expired. 
         
        * ``FAILED`` - Your private CA has failed. Your CA can fail because of problems such a network outage or backend AWS failure or other errors. A failed CA can never return to the pending state. You must create a new CA.  
         
        * ``DELETED`` - Your private CA is within the restoration period, after which it will be permanently deleted. The length of time remaining in the CA\'s restoration period will also be included in this operation\'s output. 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-pca-2017-08-22/DescribeCertificateAuthority>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_certificate_authority(
              CertificateAuthorityArn=\'string\'
          )
        :type CertificateAuthorityArn: string
        :param CertificateAuthorityArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that was returned when you called  CreateCertificateAuthority . This must be of the form: 
        
           ``arn:aws:acm-pca:*region* :*account* :certificate-authority/*12345678-1234-1234-1234-123456789012* `` . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'CertificateAuthority\': {
                    \'Arn\': \'string\',
                    \'CreatedAt\': datetime(2015, 1, 1),
                    \'LastStateChangeAt\': datetime(2015, 1, 1),
                    \'Type\': \'SUBORDINATE\',
                    \'Serial\': \'string\',
                    \'Status\': \'CREATING\'|\'PENDING_CERTIFICATE\'|\'ACTIVE\'|\'DELETED\'|\'DISABLED\'|\'EXPIRED\'|\'FAILED\',
                    \'NotBefore\': datetime(2015, 1, 1),
                    \'NotAfter\': datetime(2015, 1, 1),
                    \'FailureReason\': \'REQUEST_TIMED_OUT\'|\'UNSUPPORTED_ALGORITHM\'|\'OTHER\',
                    \'CertificateAuthorityConfiguration\': {
                        \'KeyAlgorithm\': \'RSA_2048\'|\'RSA_4096\'|\'EC_prime256v1\'|\'EC_secp384r1\',
                        \'SigningAlgorithm\': \'SHA256WITHECDSA\'|\'SHA384WITHECDSA\'|\'SHA512WITHECDSA\'|\'SHA256WITHRSA\'|\'SHA384WITHRSA\'|\'SHA512WITHRSA\',
                        \'Subject\': {
                            \'Country\': \'string\',
                            \'Organization\': \'string\',
                            \'OrganizationalUnit\': \'string\',
                            \'DistinguishedNameQualifier\': \'string\',
                            \'State\': \'string\',
                            \'CommonName\': \'string\',
                            \'SerialNumber\': \'string\',
                            \'Locality\': \'string\',
                            \'Title\': \'string\',
                            \'Surname\': \'string\',
                            \'GivenName\': \'string\',
                            \'Initials\': \'string\',
                            \'Pseudonym\': \'string\',
                            \'GenerationQualifier\': \'string\'
                        }
                    },
                    \'RevocationConfiguration\': {
                        \'CrlConfiguration\': {
                            \'Enabled\': True|False,
                            \'ExpirationInDays\': 123,
                            \'CustomCname\': \'string\',
                            \'S3BucketName\': \'string\'
                        }
                    },
                    \'RestorableUntil\': datetime(2015, 1, 1)
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **CertificateAuthority** *(dict) --* 
        
              A  CertificateAuthority structure that contains information about your private CA.
        
              - **Arn** *(string) --* 
        
                Amazon Resource Name (ARN) for your private certificate authority (CA). The format is `` *12345678-1234-1234-1234-123456789012* `` .
        
              - **CreatedAt** *(datetime) --* 
        
                Date and time at which your private CA was created.
        
              - **LastStateChangeAt** *(datetime) --* 
        
                Date and time at which your private CA was last updated.
        
              - **Type** *(string) --* 
        
                Type of your private CA.
        
              - **Serial** *(string) --* 
        
                Serial number of your private CA.
        
              - **Status** *(string) --* 
        
                Status of your private CA.
        
              - **NotBefore** *(datetime) --* 
        
                Date and time before which your private CA certificate is not valid.
        
              - **NotAfter** *(datetime) --* 
        
                Date and time after which your private CA certificate is not valid.
        
              - **FailureReason** *(string) --* 
        
                Reason the request to create your private CA failed.
        
              - **CertificateAuthorityConfiguration** *(dict) --* 
        
                Your private CA configuration.
        
                - **KeyAlgorithm** *(string) --* 
        
                  Type of the public key algorithm and size, in bits, of the key pair that your key pair creates when it issues a certificate.
        
                - **SigningAlgorithm** *(string) --* 
        
                  Name of the algorithm your private CA uses to sign certificate requests.
        
                - **Subject** *(dict) --* 
        
                  Structure that contains X.500 distinguished name information for your private CA.
        
                  - **Country** *(string) --* 
        
                    Two-digit code that specifies the country in which the certificate subject located.
        
                  - **Organization** *(string) --* 
        
                    Legal name of the organization with which the certificate subject is affiliated. 
        
                  - **OrganizationalUnit** *(string) --* 
        
                    A subdivision or unit of the organization (such as sales or finance) with which the certificate subject is affiliated.
        
                  - **DistinguishedNameQualifier** *(string) --* 
        
                    Disambiguating information for the certificate subject.
        
                  - **State** *(string) --* 
        
                    State in which the subject of the certificate is located.
        
                  - **CommonName** *(string) --* 
        
                    Fully qualified domain name (FQDN) associated with the certificate subject.
        
                  - **SerialNumber** *(string) --* 
        
                    The certificate serial number.
        
                  - **Locality** *(string) --* 
        
                    The locality (such as a city or town) in which the certificate subject is located.
        
                  - **Title** *(string) --* 
        
                    A title such as Mr. or Ms., which is pre-pended to the name to refer formally to the certificate subject.
        
                  - **Surname** *(string) --* 
        
                    Family name. In the US and the UK, for example, the surname of an individual is ordered last. In Asian cultures the surname is typically ordered first.
        
                  - **GivenName** *(string) --* 
        
                    First name.
        
                  - **Initials** *(string) --* 
        
                    Concatenation that typically contains the first letter of the **GivenName** , the first letter of the middle name if one exists, and the first letter of the **SurName** .
        
                  - **Pseudonym** *(string) --* 
        
                    Typically a shortened version of a longer **GivenName** . For example, Jonathan is often shortened to John. Elizabeth is often shortened to Beth, Liz, or Eliza.
        
                  - **GenerationQualifier** *(string) --* 
        
                    Typically a qualifier appended to the name of an individual. Examples include Jr. for junior, Sr. for senior, and III for third.
        
              - **RevocationConfiguration** *(dict) --* 
        
                Information about the certificate revocation list (CRL) created and maintained by your private CA. 
        
                - **CrlConfiguration** *(dict) --* 
        
                  Configuration of the certificate revocation list (CRL), if any, maintained by your private CA.
        
                  - **Enabled** *(boolean) --* 
        
                    Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. You can use this value to enable certificate revocation for a new CA when you call the  CreateCertificateAuthority operation or for an existing CA when you call the  UpdateCertificateAuthority operation. 
        
                  - **ExpirationInDays** *(integer) --* 
        
                    Number of days until a certificate expires.
        
                  - **CustomCname** *(string) --* 
        
                    Name inserted into the certificate **CRL Distribution Points** extension that enables the use of an alias for the CRL distribution point. Use this value if you don\'t want the name of your S3 bucket to be public.
        
                  - **S3BucketName** *(string) --* 
        
                    Name of the S3 bucket that contains the CRL. If you do not provide a value for the **CustomCname** argument, the name of your S3 bucket is placed into the **CRL Distribution Points** extension of the issued certificate. You can change the name of your bucket by calling the  UpdateCertificateAuthority operation. You must specify a bucket policy that allows ACM PCA to write the CRL to your bucket.
        
              - **RestorableUntil** *(datetime) --* 
        
                The period during which a deleted CA can be restored. For more information, see the ``PermanentDeletionTimeInDays`` parameter of the  DeleteCertificateAuthorityRequest operation. 
        
        """
        pass

    def describe_certificate_authority_audit_report(self, CertificateAuthorityArn: str, AuditReportId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-pca-2017-08-22/DescribeCertificateAuthorityAuditReport>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_certificate_authority_audit_report(
              CertificateAuthorityArn=\'string\',
              AuditReportId=\'string\'
          )
        :type CertificateAuthorityArn: string
        :param CertificateAuthorityArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the private CA. This must be of the form:
        
           ``arn:aws:acm-pca:*region* :*account* :certificate-authority/*12345678-1234-1234-1234-123456789012* `` . 
        
        :type AuditReportId: string
        :param AuditReportId: **[REQUIRED]** 
        
          The report ID returned by calling the  CreateCertificateAuthorityAuditReport operation.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'AuditReportStatus\': \'CREATING\'|\'SUCCESS\'|\'FAILED\',
                \'S3BucketName\': \'string\',
                \'S3Key\': \'string\',
                \'CreatedAt\': datetime(2015, 1, 1)
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **AuditReportStatus** *(string) --* 
        
              Specifies whether report creation is in progress, has succeeded, or has failed.
        
            - **S3BucketName** *(string) --* 
        
              Name of the S3 bucket that contains the report.
        
            - **S3Key** *(string) --* 
        
              S3 **key** that uniquely identifies the report file in your S3 bucket.
        
            - **CreatedAt** *(datetime) --* 
        
              The date and time at which the report was created.
        
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

    def get_certificate(self, CertificateAuthorityArn: str, CertificateArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-pca-2017-08-22/GetCertificate>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_certificate(
              CertificateAuthorityArn=\'string\',
              CertificateArn=\'string\'
          )
        :type CertificateAuthorityArn: string
        :param CertificateAuthorityArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that was returned when you called  CreateCertificateAuthority . This must be of the form: 
        
           ``arn:aws:acm-pca:*region* :*account* :certificate-authority/*12345678-1234-1234-1234-123456789012* `` . 
        
        :type CertificateArn: string
        :param CertificateArn: **[REQUIRED]** 
        
          The ARN of the issued certificate. The ARN contains the certificate serial number and must be in the following form: 
        
           ``arn:aws:acm-pca:*region* :*account* :certificate-authority/*12345678-1234-1234-1234-123456789012* /certificate/*286535153982981100925020015808220737245* ``  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Certificate\': \'string\',
                \'CertificateChain\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Certificate** *(string) --* 
        
              The base64 PEM-encoded certificate specified by the ``CertificateArn`` parameter.
        
            - **CertificateChain** *(string) --* 
        
              The base64 PEM-encoded certificate chain that chains up to the on-premises root CA certificate that you used to sign your private CA certificate. 
        
        """
        pass

    def get_certificate_authority_certificate(self, CertificateAuthorityArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-pca-2017-08-22/GetCertificateAuthorityCertificate>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_certificate_authority_certificate(
              CertificateAuthorityArn=\'string\'
          )
        :type CertificateAuthorityArn: string
        :param CertificateAuthorityArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of your private CA. This is of the form:
        
           ``arn:aws:acm-pca:*region* :*account* :certificate-authority/*12345678-1234-1234-1234-123456789012* `` . 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Certificate\': \'string\',
                \'CertificateChain\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Certificate** *(string) --* 
        
              Base64-encoded certificate authority (CA) certificate.
        
            - **CertificateChain** *(string) --* 
        
              Base64-encoded certificate chain that includes any intermediate certificates and chains up to root on-premises certificate that you used to sign your private CA certificate. The chain does not include your private CA certificate. 
        
        """
        pass

    def get_certificate_authority_csr(self, CertificateAuthorityArn: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-pca-2017-08-22/GetCertificateAuthorityCsr>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_certificate_authority_csr(
              CertificateAuthorityArn=\'string\'
          )
        :type CertificateAuthorityArn: string
        :param CertificateAuthorityArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that was returned when you called the  CreateCertificateAuthority operation. This must be of the form: 
        
           ``arn:aws:acm-pca:*region* :*account* :certificate-authority/*12345678-1234-1234-1234-123456789012* ``  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Csr\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Csr** *(string) --* 
        
              The base64 PEM-encoded certificate signing request (CSR) for your private CA certificate.
        
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

    def import_certificate_authority_certificate(self, CertificateAuthorityArn: str, Certificate: bytes, CertificateChain: bytes):
        """
        
        .. note::
        
          Your certificate chain must not include the private CA certificate that you are importing.
        
        .. note::
        
          Your on-premises CA certificate must be the last certificate in your chain. The subordinate certificate, if any, that your root CA signed must be next to last. The subordinate certificate signed by the preceding subordinate CA must come next, and so on until your chain is built. 
        
        .. note::
        
          The chain must be PEM-encoded.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-pca-2017-08-22/ImportCertificateAuthorityCertificate>`_
        
        **Request Syntax** 
        ::
        
          response = client.import_certificate_authority_certificate(
              CertificateAuthorityArn=\'string\',
              Certificate=b\'bytes\',
              CertificateChain=b\'bytes\'
          )
        :type CertificateAuthorityArn: string
        :param CertificateAuthorityArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that was returned when you called  CreateCertificateAuthority . This must be of the form: 
        
           ``arn:aws:acm-pca:*region* :*account* :certificate-authority/*12345678-1234-1234-1234-123456789012* ``  
        
        :type Certificate: bytes
        :param Certificate: **[REQUIRED]** 
        
          The PEM-encoded certificate for your private CA. This must be signed by using your on-premises CA.
        
        :type CertificateChain: bytes
        :param CertificateChain: **[REQUIRED]** 
        
          A PEM-encoded file that contains all of your certificates, other than the certificate you\'re importing, chaining up to your root CA. Your on-premises root certificate is the last in the chain, and each certificate in the chain signs the one preceding. 
        
        :returns: None
        """
        pass

    def issue_certificate(self, CertificateAuthorityArn: str, Csr: bytes, SigningAlgorithm: str, Validity: Dict, IdempotencyToken: str = None) -> Dict:
        """
        
        .. note::
        
          You cannot use the ACM **ListCertificateAuthorities** operation to retrieve the ARNs of the certificates that you issue by using ACM PCA.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-pca-2017-08-22/IssueCertificate>`_
        
        **Request Syntax** 
        ::
        
          response = client.issue_certificate(
              CertificateAuthorityArn=\'string\',
              Csr=b\'bytes\',
              SigningAlgorithm=\'SHA256WITHECDSA\'|\'SHA384WITHECDSA\'|\'SHA512WITHECDSA\'|\'SHA256WITHRSA\'|\'SHA384WITHRSA\'|\'SHA512WITHRSA\',
              Validity={
                  \'Value\': 123,
                  \'Type\': \'END_DATE\'|\'ABSOLUTE\'|\'DAYS\'|\'MONTHS\'|\'YEARS\'
              },
              IdempotencyToken=\'string\'
          )
        :type CertificateAuthorityArn: string
        :param CertificateAuthorityArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that was returned when you called  CreateCertificateAuthority . This must be of the form:
        
           ``arn:aws:acm-pca:*region* :*account* :certificate-authority/*12345678-1234-1234-1234-123456789012* ``  
        
        :type Csr: bytes
        :param Csr: **[REQUIRED]** 
        
          The certificate signing request (CSR) for the certificate you want to issue. You can use the following OpenSSL command to create the CSR and a 2048 bit RSA private key. 
        
           ``openssl req -new -newkey rsa:2048 -days 365 -keyout private/test_cert_priv_key.pem -out csr/test_cert_.csr``  
        
          If you have a configuration file, you can use the following OpenSSL command. The ``usr_cert`` block in the configuration file contains your X509 version 3 extensions. 
        
           ``openssl req -new -config openssl_rsa.cnf -extensions usr_cert -newkey rsa:2048 -days -365 -keyout private/test_cert_priv_key.pem -out csr/test_cert_.csr``  
        
        :type SigningAlgorithm: string
        :param SigningAlgorithm: **[REQUIRED]** 
        
          The name of the algorithm that will be used to sign the certificate to be issued.
        
        :type Validity: dict
        :param Validity: **[REQUIRED]** 
        
          The type of the validity period.
        
          - **Value** *(integer) --* **[REQUIRED]** 
        
            Time period.
        
          - **Type** *(string) --* **[REQUIRED]** 
        
            Specifies whether the ``Value`` parameter represents days, months, or years.
        
        :type IdempotencyToken: string
        :param IdempotencyToken: 
        
          Custom string that can be used to distinguish between calls to the **IssueCertificate** operation. Idempotency tokens time out after one hour. Therefore, if you call **IssueCertificate** multiple times with the same idempotency token within 5 minutes, ACM PCA recognizes that you are requesting only one certificate and will issue only one. If you change the idempotency token for each call, PCA recognizes that you are requesting multiple certificates.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'CertificateArn\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **CertificateArn** *(string) --* 
        
              The Amazon Resource Name (ARN) of the issued certificate and the certificate serial number. This is of the form:
        
               ``arn:aws:acm-pca:*region* :*account* :certificate-authority/*12345678-1234-1234-1234-123456789012* /certificate/*286535153982981100925020015808220737245* ``  
        
        """
        pass

    def list_certificate_authorities(self, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-pca-2017-08-22/ListCertificateAuthorities>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_certificate_authorities(
              NextToken=\'string\',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken: 
        
          Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the ``NextToken`` parameter from the response you just received.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          Use this parameter when paginating results to specify the maximum number of items to return in the response on each page. If additional items exist beyond the number you specify, the ``NextToken`` element is sent in the response. Use this ``NextToken`` value in a subsequent request to retrieve additional items.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'CertificateAuthorities\': [
                    {
                        \'Arn\': \'string\',
                        \'CreatedAt\': datetime(2015, 1, 1),
                        \'LastStateChangeAt\': datetime(2015, 1, 1),
                        \'Type\': \'SUBORDINATE\',
                        \'Serial\': \'string\',
                        \'Status\': \'CREATING\'|\'PENDING_CERTIFICATE\'|\'ACTIVE\'|\'DELETED\'|\'DISABLED\'|\'EXPIRED\'|\'FAILED\',
                        \'NotBefore\': datetime(2015, 1, 1),
                        \'NotAfter\': datetime(2015, 1, 1),
                        \'FailureReason\': \'REQUEST_TIMED_OUT\'|\'UNSUPPORTED_ALGORITHM\'|\'OTHER\',
                        \'CertificateAuthorityConfiguration\': {
                            \'KeyAlgorithm\': \'RSA_2048\'|\'RSA_4096\'|\'EC_prime256v1\'|\'EC_secp384r1\',
                            \'SigningAlgorithm\': \'SHA256WITHECDSA\'|\'SHA384WITHECDSA\'|\'SHA512WITHECDSA\'|\'SHA256WITHRSA\'|\'SHA384WITHRSA\'|\'SHA512WITHRSA\',
                            \'Subject\': {
                                \'Country\': \'string\',
                                \'Organization\': \'string\',
                                \'OrganizationalUnit\': \'string\',
                                \'DistinguishedNameQualifier\': \'string\',
                                \'State\': \'string\',
                                \'CommonName\': \'string\',
                                \'SerialNumber\': \'string\',
                                \'Locality\': \'string\',
                                \'Title\': \'string\',
                                \'Surname\': \'string\',
                                \'GivenName\': \'string\',
                                \'Initials\': \'string\',
                                \'Pseudonym\': \'string\',
                                \'GenerationQualifier\': \'string\'
                            }
                        },
                        \'RevocationConfiguration\': {
                            \'CrlConfiguration\': {
                                \'Enabled\': True|False,
                                \'ExpirationInDays\': 123,
                                \'CustomCname\': \'string\',
                                \'S3BucketName\': \'string\'
                            }
                        },
                        \'RestorableUntil\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **CertificateAuthorities** *(list) --* 
        
              Summary information about each certificate authority you have created.
        
              - *(dict) --* 
        
                Contains information about your private certificate authority (CA). Your private CA can issue and revoke X.509 digital certificates. Digital certificates verify that the entity named in the certificate **Subject** field owns or controls the public key contained in the **Subject Public Key Info** field. Call the  CreateCertificateAuthority operation to create your private CA. You must then call the  GetCertificateAuthorityCertificate operation to retrieve a private CA certificate signing request (CSR). Take the CSR to your on-premises CA and sign it with the root CA certificate or a subordinate certificate. Call the  ImportCertificateAuthorityCertificate operation to import the signed certificate into AWS Certificate Manager (ACM). 
        
                - **Arn** *(string) --* 
        
                  Amazon Resource Name (ARN) for your private certificate authority (CA). The format is `` *12345678-1234-1234-1234-123456789012* `` .
        
                - **CreatedAt** *(datetime) --* 
        
                  Date and time at which your private CA was created.
        
                - **LastStateChangeAt** *(datetime) --* 
        
                  Date and time at which your private CA was last updated.
        
                - **Type** *(string) --* 
        
                  Type of your private CA.
        
                - **Serial** *(string) --* 
        
                  Serial number of your private CA.
        
                - **Status** *(string) --* 
        
                  Status of your private CA.
        
                - **NotBefore** *(datetime) --* 
        
                  Date and time before which your private CA certificate is not valid.
        
                - **NotAfter** *(datetime) --* 
        
                  Date and time after which your private CA certificate is not valid.
        
                - **FailureReason** *(string) --* 
        
                  Reason the request to create your private CA failed.
        
                - **CertificateAuthorityConfiguration** *(dict) --* 
        
                  Your private CA configuration.
        
                  - **KeyAlgorithm** *(string) --* 
        
                    Type of the public key algorithm and size, in bits, of the key pair that your key pair creates when it issues a certificate.
        
                  - **SigningAlgorithm** *(string) --* 
        
                    Name of the algorithm your private CA uses to sign certificate requests.
        
                  - **Subject** *(dict) --* 
        
                    Structure that contains X.500 distinguished name information for your private CA.
        
                    - **Country** *(string) --* 
        
                      Two-digit code that specifies the country in which the certificate subject located.
        
                    - **Organization** *(string) --* 
        
                      Legal name of the organization with which the certificate subject is affiliated. 
        
                    - **OrganizationalUnit** *(string) --* 
        
                      A subdivision or unit of the organization (such as sales or finance) with which the certificate subject is affiliated.
        
                    - **DistinguishedNameQualifier** *(string) --* 
        
                      Disambiguating information for the certificate subject.
        
                    - **State** *(string) --* 
        
                      State in which the subject of the certificate is located.
        
                    - **CommonName** *(string) --* 
        
                      Fully qualified domain name (FQDN) associated with the certificate subject.
        
                    - **SerialNumber** *(string) --* 
        
                      The certificate serial number.
        
                    - **Locality** *(string) --* 
        
                      The locality (such as a city or town) in which the certificate subject is located.
        
                    - **Title** *(string) --* 
        
                      A title such as Mr. or Ms., which is pre-pended to the name to refer formally to the certificate subject.
        
                    - **Surname** *(string) --* 
        
                      Family name. In the US and the UK, for example, the surname of an individual is ordered last. In Asian cultures the surname is typically ordered first.
        
                    - **GivenName** *(string) --* 
        
                      First name.
        
                    - **Initials** *(string) --* 
        
                      Concatenation that typically contains the first letter of the **GivenName** , the first letter of the middle name if one exists, and the first letter of the **SurName** .
        
                    - **Pseudonym** *(string) --* 
        
                      Typically a shortened version of a longer **GivenName** . For example, Jonathan is often shortened to John. Elizabeth is often shortened to Beth, Liz, or Eliza.
        
                    - **GenerationQualifier** *(string) --* 
        
                      Typically a qualifier appended to the name of an individual. Examples include Jr. for junior, Sr. for senior, and III for third.
        
                - **RevocationConfiguration** *(dict) --* 
        
                  Information about the certificate revocation list (CRL) created and maintained by your private CA. 
        
                  - **CrlConfiguration** *(dict) --* 
        
                    Configuration of the certificate revocation list (CRL), if any, maintained by your private CA.
        
                    - **Enabled** *(boolean) --* 
        
                      Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. You can use this value to enable certificate revocation for a new CA when you call the  CreateCertificateAuthority operation or for an existing CA when you call the  UpdateCertificateAuthority operation. 
        
                    - **ExpirationInDays** *(integer) --* 
        
                      Number of days until a certificate expires.
        
                    - **CustomCname** *(string) --* 
        
                      Name inserted into the certificate **CRL Distribution Points** extension that enables the use of an alias for the CRL distribution point. Use this value if you don\'t want the name of your S3 bucket to be public.
        
                    - **S3BucketName** *(string) --* 
        
                      Name of the S3 bucket that contains the CRL. If you do not provide a value for the **CustomCname** argument, the name of your S3 bucket is placed into the **CRL Distribution Points** extension of the issued certificate. You can change the name of your bucket by calling the  UpdateCertificateAuthority operation. You must specify a bucket policy that allows ACM PCA to write the CRL to your bucket.
        
                - **RestorableUntil** *(datetime) --* 
        
                  The period during which a deleted CA can be restored. For more information, see the ``PermanentDeletionTimeInDays`` parameter of the  DeleteCertificateAuthorityRequest operation. 
        
            - **NextToken** *(string) --* 
        
              When the list is truncated, this value is present and should be used for the ``NextToken`` parameter in a subsequent pagination request.
        
        """
        pass

    def list_tags(self, CertificateAuthorityArn: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-pca-2017-08-22/ListTags>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_tags(
              CertificateAuthorityArn=\'string\',
              NextToken=\'string\',
              MaxResults=123
          )
        :type CertificateAuthorityArn: string
        :param CertificateAuthorityArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that was returned when you called the  CreateCertificateAuthority operation. This must be of the form: 
        
           ``arn:aws:acm-pca:*region* :*account* :certificate-authority/*12345678-1234-1234-1234-123456789012* ``  
        
        :type NextToken: string
        :param NextToken: 
        
          Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of **NextToken** from the response you just received.
        
        :type MaxResults: integer
        :param MaxResults: 
        
          Use this parameter when paginating results to specify the maximum number of items to return in the response. If additional items exist beyond the number you specify, the **NextToken** element is sent in the response. Use this **NextToken** value in a subsequent request to retrieve additional items.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Tags\': [
                    {
                        \'Key\': \'string\',
                        \'Value\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **Tags** *(list) --* 
        
              The tags associated with your private CA.
        
              - *(dict) --* 
        
                Tags are labels that you can use to identify and organize your private CAs. Each tag consists of a key and an optional value. You can associate up to 50 tags with a private CA. To add one or more tags to a private CA, call the  TagCertificateAuthority operation. To remove a tag, call the  UntagCertificateAuthority operation. 
        
                - **Key** *(string) --* 
        
                  Key (name) of the tag.
        
                - **Value** *(string) --* 
        
                  Value of the tag.
        
            - **NextToken** *(string) --* 
        
              When the list is truncated, this value is present and should be used for the **NextToken** parameter in a subsequent pagination request. 
        
        """
        pass

    def restore_certificate_authority(self, CertificateAuthorityArn: str):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-pca-2017-08-22/RestoreCertificateAuthority>`_
        
        **Request Syntax** 
        ::
        
          response = client.restore_certificate_authority(
              CertificateAuthorityArn=\'string\'
          )
        :type CertificateAuthorityArn: string
        :param CertificateAuthorityArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that was returned when you called the  CreateCertificateAuthority operation. This must be of the form: 
        
           ``arn:aws:acm-pca:*region* :*account* :certificate-authority/*12345678-1234-1234-1234-123456789012* ``  
        
        :returns: None
        """
        pass

    def revoke_certificate(self, CertificateAuthorityArn: str, CertificateSerial: str, RevocationReason: str):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-pca-2017-08-22/RevokeCertificate>`_
        
        **Request Syntax** 
        ::
        
          response = client.revoke_certificate(
              CertificateAuthorityArn=\'string\',
              CertificateSerial=\'string\',
              RevocationReason=\'UNSPECIFIED\'|\'KEY_COMPROMISE\'|\'CERTIFICATE_AUTHORITY_COMPROMISE\'|\'AFFILIATION_CHANGED\'|\'SUPERSEDED\'|\'CESSATION_OF_OPERATION\'|\'PRIVILEGE_WITHDRAWN\'|\'A_A_COMPROMISE\'
          )
        :type CertificateAuthorityArn: string
        :param CertificateAuthorityArn: **[REQUIRED]** 
        
          Amazon Resource Name (ARN) of the private CA that issued the certificate to be revoked. This must be of the form:
        
           ``arn:aws:acm-pca:*region* :*account* :certificate-authority/*12345678-1234-1234-1234-123456789012* ``  
        
        :type CertificateSerial: string
        :param CertificateSerial: **[REQUIRED]** 
        
          Serial number of the certificate to be revoked. This must be in hexadecimal format. You can retrieve the serial number by calling  GetCertificate with the Amazon Resource Name (ARN) of the certificate you want and the ARN of your private CA. The **GetCertificate** operation retrieves the certificate in the PEM format. You can use the following OpenSSL command to list the certificate in text format and copy the hexadecimal serial number. 
        
           ``openssl x509 -in *file_path* -text -noout``  
        
          You can also copy the serial number from the console or use the `DescribeCertificate <https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeCertificate.html>`__ operation in the *AWS Certificate Manager API Reference* . 
        
        :type RevocationReason: string
        :param RevocationReason: **[REQUIRED]** 
        
          Specifies why you revoked the certificate.
        
        :returns: None
        """
        pass

    def tag_certificate_authority(self, CertificateAuthorityArn: str, Tags: List):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-pca-2017-08-22/TagCertificateAuthority>`_
        
        **Request Syntax** 
        ::
        
          response = client.tag_certificate_authority(
              CertificateAuthorityArn=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type CertificateAuthorityArn: string
        :param CertificateAuthorityArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that was returned when you called  CreateCertificateAuthority . This must be of the form: 
        
           ``arn:aws:acm-pca:*region* :*account* :certificate-authority/*12345678-1234-1234-1234-123456789012* ``  
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          List of tags to be associated with the CA.
        
          - *(dict) --* 
        
            Tags are labels that you can use to identify and organize your private CAs. Each tag consists of a key and an optional value. You can associate up to 50 tags with a private CA. To add one or more tags to a private CA, call the  TagCertificateAuthority operation. To remove a tag, call the  UntagCertificateAuthority operation. 
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              Key (name) of the tag.
        
            - **Value** *(string) --* 
        
              Value of the tag.
        
        :returns: None
        """
        pass

    def untag_certificate_authority(self, CertificateAuthorityArn: str, Tags: List):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-pca-2017-08-22/UntagCertificateAuthority>`_
        
        **Request Syntax** 
        ::
        
          response = client.untag_certificate_authority(
              CertificateAuthorityArn=\'string\',
              Tags=[
                  {
                      \'Key\': \'string\',
                      \'Value\': \'string\'
                  },
              ]
          )
        :type CertificateAuthorityArn: string
        :param CertificateAuthorityArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) that was returned when you called  CreateCertificateAuthority . This must be of the form: 
        
           ``arn:aws:acm-pca:*region* :*account* :certificate-authority/*12345678-1234-1234-1234-123456789012* ``  
        
        :type Tags: list
        :param Tags: **[REQUIRED]** 
        
          List of tags to be removed from the CA.
        
          - *(dict) --* 
        
            Tags are labels that you can use to identify and organize your private CAs. Each tag consists of a key and an optional value. You can associate up to 50 tags with a private CA. To add one or more tags to a private CA, call the  TagCertificateAuthority operation. To remove a tag, call the  UntagCertificateAuthority operation. 
        
            - **Key** *(string) --* **[REQUIRED]** 
        
              Key (name) of the tag.
        
            - **Value** *(string) --* 
        
              Value of the tag.
        
        :returns: None
        """
        pass

    def update_certificate_authority(self, CertificateAuthorityArn: str, RevocationConfiguration: Dict = None, Status: str = None):
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-pca-2017-08-22/UpdateCertificateAuthority>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_certificate_authority(
              CertificateAuthorityArn=\'string\',
              RevocationConfiguration={
                  \'CrlConfiguration\': {
                      \'Enabled\': True|False,
                      \'ExpirationInDays\': 123,
                      \'CustomCname\': \'string\',
                      \'S3BucketName\': \'string\'
                  }
              },
              Status=\'CREATING\'|\'PENDING_CERTIFICATE\'|\'ACTIVE\'|\'DELETED\'|\'DISABLED\'|\'EXPIRED\'|\'FAILED\'
          )
        :type CertificateAuthorityArn: string
        :param CertificateAuthorityArn: **[REQUIRED]** 
        
          Amazon Resource Name (ARN) of the private CA that issued the certificate to be revoked. This must be of the form:
        
           ``arn:aws:acm-pca:*region* :*account* :certificate-authority/*12345678-1234-1234-1234-123456789012* ``  
        
        :type RevocationConfiguration: dict
        :param RevocationConfiguration: 
        
          Revocation information for your private CA.
        
          - **CrlConfiguration** *(dict) --* 
        
            Configuration of the certificate revocation list (CRL), if any, maintained by your private CA.
        
            - **Enabled** *(boolean) --* **[REQUIRED]** 
        
              Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. You can use this value to enable certificate revocation for a new CA when you call the  CreateCertificateAuthority operation or for an existing CA when you call the  UpdateCertificateAuthority operation. 
        
            - **ExpirationInDays** *(integer) --* 
        
              Number of days until a certificate expires.
        
            - **CustomCname** *(string) --* 
        
              Name inserted into the certificate **CRL Distribution Points** extension that enables the use of an alias for the CRL distribution point. Use this value if you don\'t want the name of your S3 bucket to be public.
        
            - **S3BucketName** *(string) --* 
        
              Name of the S3 bucket that contains the CRL. If you do not provide a value for the **CustomCname** argument, the name of your S3 bucket is placed into the **CRL Distribution Points** extension of the issued certificate. You can change the name of your bucket by calling the  UpdateCertificateAuthority operation. You must specify a bucket policy that allows ACM PCA to write the CRL to your bucket.
        
        :type Status: string
        :param Status: 
        
          Status of your private CA.
        
        :returns: None
        """
        pass
