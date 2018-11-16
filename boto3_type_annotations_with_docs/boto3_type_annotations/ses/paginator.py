from typing import Dict
from botocore.paginate import Paginator


class ListCustomVerificationEmailTemplates(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/ListCustomVerificationEmailTemplates>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
                \'CustomVerificationEmailTemplates\': [
                    {
                        \'TemplateName\': \'string\',
                        \'FromEmailAddress\': \'string\',
                        \'TemplateSubject\': \'string\',
                        \'SuccessRedirectionURL\': \'string\',
                        \'FailureRedirectionURL\': \'string\'
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
        
        """
        pass


class ListIdentities(Paginator):
    def paginate(self, IdentityType: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/ListIdentities>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              IdentityType=\'EmailAddress\'|\'Domain\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
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
          
          **Response Syntax** 
        
          ::
        
            {
                \'Identities\': [
                    \'string\',
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            A list of all identities that you have attempted to verify under your AWS account, regardless of verification status.
        
            - **Identities** *(list) --* 
        
              A list of identities.
        
              - *(string) --* 
          
        """
        pass
