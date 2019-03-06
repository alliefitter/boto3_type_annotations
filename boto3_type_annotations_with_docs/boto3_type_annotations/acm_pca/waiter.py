from typing import Dict
from botocore.waiter import Waiter


class AuditReportCreated(Waiter):
    def wait(self, CertificateAuthorityArn: str, AuditReportId: str, WaiterConfig: Dict = None):
        """
        Polls :py:meth:`ACMPCA.Client.describe_certificate_authority_audit_report` every 3 seconds until a successful state is reached. An error is returned after 60 failed checks.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-pca-2017-08-22/DescribeCertificateAuthorityAuditReport>`_
        
        **Request Syntax**
        ::
          waiter.wait(
              CertificateAuthorityArn='string',
              AuditReportId='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type CertificateAuthorityArn: string
        :param CertificateAuthorityArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the private CA. This must be of the form:
           ``arn:aws:acm-pca:*region* :*account* :certificate-authority/*12345678-1234-1234-1234-123456789012* `` .
        :type AuditReportId: string
        :param AuditReportId: **[REQUIRED]**
          The report ID returned by calling the  CreateCertificateAuthorityAuditReport operation.
        :type WaiterConfig: dict
        :param WaiterConfig:
          A dictionary that provides parameters to control waiting behavior.
          - **Delay** *(integer) --*
            The amount of time in seconds to wait between attempts. Default: 3
          - **MaxAttempts** *(integer) --*
            The maximum number of attempts to be made. Default: 60
        :returns: None
        """
        pass


class CertificateAuthorityCSRCreated(Waiter):
    def wait(self, CertificateAuthorityArn: str, WaiterConfig: Dict = None):
        """
        Polls :py:meth:`ACMPCA.Client.get_certificate_authority_csr` every 3 seconds until a successful state is reached. An error is returned after 60 failed checks.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-pca-2017-08-22/GetCertificateAuthorityCsr>`_
        
        **Request Syntax**
        ::
          waiter.wait(
              CertificateAuthorityArn='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type CertificateAuthorityArn: string
        :param CertificateAuthorityArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) that was returned when you called the  CreateCertificateAuthority operation. This must be of the form:
           ``arn:aws:acm-pca:*region* :*account* :certificate-authority/*12345678-1234-1234-1234-123456789012* ``
        :type WaiterConfig: dict
        :param WaiterConfig:
          A dictionary that provides parameters to control waiting behavior.
          - **Delay** *(integer) --*
            The amount of time in seconds to wait between attempts. Default: 3
          - **MaxAttempts** *(integer) --*
            The maximum number of attempts to be made. Default: 60
        :returns: None
        """
        pass


class CertificateIssued(Waiter):
    def wait(self, CertificateAuthorityArn: str, CertificateArn: str, WaiterConfig: Dict = None):
        """
        Polls :py:meth:`ACMPCA.Client.get_certificate` every 3 seconds until a successful state is reached. An error is returned after 60 failed checks.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-pca-2017-08-22/GetCertificate>`_
        
        **Request Syntax**
        ::
          waiter.wait(
              CertificateAuthorityArn='string',
              CertificateArn='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type CertificateAuthorityArn: string
        :param CertificateAuthorityArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) that was returned when you called  CreateCertificateAuthority . This must be of the form:
           ``arn:aws:acm-pca:*region* :*account* :certificate-authority/*12345678-1234-1234-1234-123456789012* `` .
        :type CertificateArn: string
        :param CertificateArn: **[REQUIRED]**
          The ARN of the issued certificate. The ARN contains the certificate serial number and must be in the following form:
           ``arn:aws:acm-pca:*region* :*account* :certificate-authority/*12345678-1234-1234-1234-123456789012* /certificate/*286535153982981100925020015808220737245* ``
        :type WaiterConfig: dict
        :param WaiterConfig:
          A dictionary that provides parameters to control waiting behavior.
          - **Delay** *(integer) --*
            The amount of time in seconds to wait between attempts. Default: 3
          - **MaxAttempts** *(integer) --*
            The maximum number of attempts to be made. Default: 60
        :returns: None
        """
        pass
