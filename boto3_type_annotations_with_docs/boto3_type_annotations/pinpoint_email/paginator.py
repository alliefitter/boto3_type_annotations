from typing import Dict
from botocore.paginate import Paginator


class GetDedicatedIps(Paginator):
    def paginate(self, PoolName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`PinpointEmail.Client.get_dedicated_ips`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/GetDedicatedIps>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PoolName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'DedicatedIps': [
                    {
                        'Ip': 'string',
                        'WarmupStatus': 'IN_PROGRESS'|'DONE',
                        'WarmupPercentage': 123,
                        'PoolName': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            Information about the dedicated IP addresses that are associated with your Amazon Pinpoint account.
            - **DedicatedIps** *(list) --* 
              A list of dedicated IP addresses that are reserved for use by your Amazon Pinpoint account.
              - *(dict) --* 
                Contains information about a dedicated IP address that is associated with your Amazon Pinpoint account.
                - **Ip** *(string) --* 
                  An IP address that is reserved for use by your Amazon Pinpoint account.
                - **WarmupStatus** *(string) --* 
                  The warm-up status of a dedicated IP address. The status can have one of the following values:
                  * ``IN_PROGRESS`` – The IP address isn't ready to use because the dedicated IP warm-up process is ongoing. 
                  * ``DONE`` – The dedicated IP warm-up process is complete, and the IP address is ready to use. 
                - **WarmupPercentage** *(integer) --* 
                  Indicates how complete the dedicated IP warm-up process is. When this value equals 1, the address has completed the warm-up process and is ready for use.
                - **PoolName** *(string) --* 
                  The name of the dedicated IP pool that the IP address is associated with.
        :type PoolName: string
        :param PoolName:
          The name of the IP pool that the dedicated IP address is associated with.
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
        """
        pass


class ListConfigurationSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`PinpointEmail.Client.list_configuration_sets`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/ListConfigurationSets>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ConfigurationSets': [
                    'string',
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            A list of configuration sets in your Amazon Pinpoint account in the current AWS Region.
            - **ConfigurationSets** *(list) --* 
              An array that contains all of the configuration sets in your Amazon Pinpoint account in the current AWS Region.
              - *(string) --* 
                The name of a configuration set.
                In Amazon Pinpoint, *configuration sets* are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.
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
        """
        pass


class ListDedicatedIpPools(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`PinpointEmail.Client.list_dedicated_ip_pools`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/ListDedicatedIpPools>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'DedicatedIpPools': [
                    'string',
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            A list of dedicated IP pools.
            - **DedicatedIpPools** *(list) --* 
              A list of all of the dedicated IP pools that are associated with your Amazon Pinpoint account.
              - *(string) --* 
                The name of a dedicated IP pool.
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
        """
        pass


class ListDeliverabilityTestReports(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`PinpointEmail.Client.list_deliverability_test_reports`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/ListDeliverabilityTestReports>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'DeliverabilityTestReports': [
                    {
                        'ReportId': 'string',
                        'ReportName': 'string',
                        'Subject': 'string',
                        'FromEmailAddress': 'string',
                        'CreateDate': datetime(2015, 1, 1),
                        'DeliverabilityTestStatus': 'IN_PROGRESS'|'COMPLETED'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            A list of the predictive inbox placement test reports that are available for your account, regardless of whether or not those tests are complete.
            - **DeliverabilityTestReports** *(list) --* 
              An object that contains a lists of predictive inbox placement tests that you've performed.
              - *(dict) --* 
                An object that contains metadata related to a predictive inbox placement test.
                - **ReportId** *(string) --* 
                  A unique string that identifies the predictive inbox placement test.
                - **ReportName** *(string) --* 
                  A name that helps you identify a predictive inbox placement test report.
                - **Subject** *(string) --* 
                  The subject line for an email that you submitted in a predictive inbox placement test.
                - **FromEmailAddress** *(string) --* 
                  The sender address that you specified for the predictive inbox placement test.
                - **CreateDate** *(datetime) --* 
                  The date and time when the predictive inbox placement test was created, in Unix time format.
                - **DeliverabilityTestStatus** *(string) --* 
                  The status of the predictive inbox placement test. If the status is ``IN_PROGRESS`` , then the predictive inbox placement test is currently running. Predictive inbox placement tests are usually complete within 24 hours of creating the test. If the status is ``COMPLETE`` , then the test is finished, and you can use the ``GetDeliverabilityTestReport`` to view the results of the test.
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
        """
        pass


class ListEmailIdentities(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`PinpointEmail.Client.list_email_identities`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/ListEmailIdentities>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'EmailIdentities': [
                    {
                        'IdentityType': 'EMAIL_ADDRESS'|'DOMAIN'|'MANAGED_DOMAIN',
                        'IdentityName': 'string',
                        'SendingEnabled': True|False
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            A list of all of the identities that you've attempted to verify for use with Amazon Pinpoint, regardless of whether or not those identities were successfully verified.
            - **EmailIdentities** *(list) --* 
              An array that includes all of the identities associated with your Amazon Pinpoint account.
              - *(dict) --* 
                Information about an email identity.
                - **IdentityType** *(string) --* 
                  The email identity type. The identity type can be one of the following:
                  * ``EMAIL_ADDRESS`` – The identity is an email address. 
                  * ``DOMAIN`` – The identity is a domain. 
                  * ``MANAGED_DOMAIN`` – The identity is a domain that is managed by AWS. 
                - **IdentityName** *(string) --* 
                  The address or domain of the identity.
                - **SendingEnabled** *(boolean) --* 
                  Indicates whether or not you can send email from the identity.
                  In Amazon Pinpoint, an identity is an email address or domain that you send email from. Before you can send email from an identity, you have to demostrate that you own the identity, and that you authorize Amazon Pinpoint to send email from that identity.
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
        """
        pass
