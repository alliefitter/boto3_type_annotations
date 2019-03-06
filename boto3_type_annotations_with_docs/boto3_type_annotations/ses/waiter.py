from typing import List
from typing import Dict
from botocore.waiter import Waiter


class IdentityExists(Waiter):
    def wait(self, Identities: List, WaiterConfig: Dict = None):
        """
        Polls :py:meth:`SES.Client.get_identity_verification_attributes` every 3 seconds until a successful state is reached. An error is returned after 20 failed checks.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/GetIdentityVerificationAttributes>`_
        
        **Request Syntax**
        ::
          waiter.wait(
              Identities=[
                  'string',
              ],
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type Identities: list
        :param Identities: **[REQUIRED]**
          A list of identities.
          - *(string) --*
        :type WaiterConfig: dict
        :param WaiterConfig:
          A dictionary that provides parameters to control waiting behavior.
          - **Delay** *(integer) --*
            The amount of time in seconds to wait between attempts. Default: 3
          - **MaxAttempts** *(integer) --*
            The maximum number of attempts to be made. Default: 20
        :returns: None
        """
        pass
