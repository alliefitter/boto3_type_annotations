from typing import Dict
from botocore.waiter import Waiter


class InstanceProfileExists(Waiter):
    def wait(self, InstanceProfileName: str, WaiterConfig: Dict = None):
        """
        Polls :py:meth:`IAM.Client.get_instance_profile` every 1 seconds until a successful state is reached. An error is returned after 40 failed checks.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/GetInstanceProfile>`_
        
        **Request Syntax**
        ::
          waiter.wait(
              InstanceProfileName='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type InstanceProfileName: string
        :param InstanceProfileName: **[REQUIRED]**
          The name of the instance profile to get information about.
          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :type WaiterConfig: dict
        :param WaiterConfig:
          A dictionary that provides parameters to control waiting behavior.
          - **Delay** *(integer) --*
            The amount of time in seconds to wait between attempts. Default: 1
          - **MaxAttempts** *(integer) --*
            The maximum number of attempts to be made. Default: 40
        :returns: None
        """
        pass


class PolicyExists(Waiter):
    def wait(self, PolicyArn: str, WaiterConfig: Dict = None):
        """
        Polls :py:meth:`IAM.Client.get_policy` every 1 seconds until a successful state is reached. An error is returned after 20 failed checks.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/GetPolicy>`_
        
        **Request Syntax**
        ::
          waiter.wait(
              PolicyArn='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type PolicyArn: string
        :param PolicyArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the managed policy that you want information about.
          For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the *AWS General Reference* .
        :type WaiterConfig: dict
        :param WaiterConfig:
          A dictionary that provides parameters to control waiting behavior.
          - **Delay** *(integer) --*
            The amount of time in seconds to wait between attempts. Default: 1
          - **MaxAttempts** *(integer) --*
            The maximum number of attempts to be made. Default: 20
        :returns: None
        """
        pass


class RoleExists(Waiter):
    def wait(self, RoleName: str, WaiterConfig: Dict = None):
        """
        Polls :py:meth:`IAM.Client.get_role` every 1 seconds until a successful state is reached. An error is returned after 20 failed checks.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/GetRole>`_
        
        **Request Syntax**
        ::
          waiter.wait(
              RoleName='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type RoleName: string
        :param RoleName: **[REQUIRED]**
          The name of the IAM role to get information about.
          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :type WaiterConfig: dict
        :param WaiterConfig:
          A dictionary that provides parameters to control waiting behavior.
          - **Delay** *(integer) --*
            The amount of time in seconds to wait between attempts. Default: 1
          - **MaxAttempts** *(integer) --*
            The maximum number of attempts to be made. Default: 20
        :returns: None
        """
        pass


class UserExists(Waiter):
    def wait(self, UserName: str = None, WaiterConfig: Dict = None):
        """
        Polls :py:meth:`IAM.Client.get_user` every 1 seconds until a successful state is reached. An error is returned after 20 failed checks.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/GetUser>`_
        
        **Request Syntax**
        ::
          waiter.wait(
              UserName='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type UserName: string
        :param UserName:
          The name of the user to get information about.
          This parameter is optional. If it is not included, it defaults to the user making the request. This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
        :type WaiterConfig: dict
        :param WaiterConfig:
          A dictionary that provides parameters to control waiting behavior.
          - **Delay** *(integer) --*
            The amount of time in seconds to wait between attempts. Default: 1
          - **MaxAttempts** *(integer) --*
            The maximum number of attempts to be made. Default: 20
        :returns: None
        """
        pass
