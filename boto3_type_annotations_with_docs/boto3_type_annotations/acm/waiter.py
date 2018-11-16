from typing import NoReturn
from typing import Dict
from botocore.waiter import Waiter


class CertificateValidated(Waiter):
    def wait(self, CertificateArn: str, WaiterConfig: Dict = None) -> NoReturn:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/DescribeCertificate>`_
        
        **Request Syntax** 
        ::
        
          waiter.wait(
              CertificateArn=\'string\',
              WaiterConfig={
                  \'Delay\': 123,
                  \'MaxAttempts\': 123
              }
          )
        :type CertificateArn: string
        :param CertificateArn: **[REQUIRED]** 
        
          The Amazon Resource Name (ARN) of the ACM certificate. The ARN must have the following form:
        
           ``arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012``  
        
          For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .
        
        :type WaiterConfig: dict
        :param WaiterConfig: 
        
          A dictionary that provides parameters to control waiting behavior.
        
          - **Delay** *(integer) --* 
        
            The amount of time in seconds to wait between attempts. Default: 60
        
          - **MaxAttempts** *(integer) --* 
        
            The maximum number of attempts to be made. Default: 40
        
        :returns: None
        """
        pass
