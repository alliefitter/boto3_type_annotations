from typing import Dict
from botocore.paginate import Paginator


class ListConfigurationSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SES.Client.list_configuration_sets`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/ListConfigurationSets>`_
        
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
                    {
                        'Name': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            A list of configuration sets associated with your AWS account. Configuration sets enable you to publish email sending events. For information about using configuration sets, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .
            - **ConfigurationSets** *(list) --* 
              A list of configuration sets.
              - *(dict) --* 
                The name of the configuration set.
                Configuration sets let you create groups of rules that you can apply to the emails you send using Amazon SES. For more information about using configuration sets, see `Using Amazon SES Configuration Sets <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/using-configuration-sets.html>`__ in the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/>`__ .
                - **Name** *(string) --* 
                  The name of the configuration set. The name must meet the following requirements:
                  * Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
                  * Contain 64 characters or fewer. 
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


class ListCustomVerificationEmailTemplates(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SES.Client.list_custom_verification_email_templates`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/ListCustomVerificationEmailTemplates>`_
        
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
                'CustomVerificationEmailTemplates': [
                    {
                        'TemplateName': 'string',
                        'FromEmailAddress': 'string',
                        'TemplateSubject': 'string',
                        'SuccessRedirectionURL': 'string',
                        'FailureRedirectionURL': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            A paginated list of custom verification email templates.
            - **CustomVerificationEmailTemplates** *(list) --* 
              A list of the custom verification email templates that exist in your account.
              - *(dict) --* 
                Contains information about a custom verification email template.
                - **TemplateName** *(string) --* 
                  The name of the custom verification email template.
                - **FromEmailAddress** *(string) --* 
                  The email address that the custom verification email is sent from.
                - **TemplateSubject** *(string) --* 
                  The subject line of the custom verification email.
                - **SuccessRedirectionURL** *(string) --* 
                  The URL that the recipient of the verification email is sent to if his or her address is successfully verified.
                - **FailureRedirectionURL** *(string) --* 
                  The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.
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


class ListIdentities(Paginator):
    def paginate(self, IdentityType: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SES.Client.list_identities`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/ListIdentities>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              IdentityType='EmailAddress'|'Domain',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Identities': [
                    'string',
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            A list of all identities that you have attempted to verify under your AWS account, regardless of verification status.
            - **Identities** *(list) --* 
              A list of identities.
              - *(string) --* 
        :type IdentityType: string
        :param IdentityType:
          The type of the identities to list. Possible values are \"EmailAddress\" and \"Domain\". If this parameter is omitted, then all identities will be listed.
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


class ListReceiptRuleSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SES.Client.list_receipt_rule_sets`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/ListReceiptRuleSets>`_
        
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
                'RuleSets': [
                    {
                        'Name': 'string',
                        'CreatedTimestamp': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            A list of receipt rule sets that exist under your AWS account.
            - **RuleSets** *(list) --* 
              The metadata for the currently active receipt rule set. The metadata consists of the rule set name and the timestamp of when the rule set was created.
              - *(dict) --* 
                Information about a receipt rule set.
                A receipt rule set is a collection of rules that specify what Amazon SES should do with mail it receives on behalf of your account's verified domains.
                For information about setting up receipt rule sets, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rule-set.html>`__ .
                - **Name** *(string) --* 
                  The name of the receipt rule set. The name must:
                  * This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
                  * Start and end with a letter or number. 
                  * Contain less than 64 characters. 
                - **CreatedTimestamp** *(datetime) --* 
                  The date and time the receipt rule set was created.
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


class ListTemplates(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`SES.Client.list_templates`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/ListTemplates>`_
        
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
                'TemplatesMetadata': [
                    {
                        'Name': 'string',
                        'CreatedTimestamp': datetime(2015, 1, 1)
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TemplatesMetadata** *(list) --* 
              An array the contains the name and creation time stamp for each template in your Amazon SES account.
              - *(dict) --* 
                Contains information about an email template.
                - **Name** *(string) --* 
                  The name of the template.
                - **CreatedTimestamp** *(datetime) --* 
                  The time and date the template was created.
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
