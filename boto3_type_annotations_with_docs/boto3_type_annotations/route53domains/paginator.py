from datetime import datetime
from typing import Dict
from botocore.paginate import Paginator


class ListDomains(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/ListDomains>`_
        
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
                \'Domains\': [
                    {
                        \'DomainName\': \'string\',
                        \'AutoRenew\': True|False,
                        \'TransferLock\': True|False,
                        \'Expiry\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListOperations(Paginator):
    def paginate(self, SubmittedSince: datetime = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/route53domains-2014-05-15/ListOperations>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              SubmittedSince=datetime(2015, 1, 1),
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type SubmittedSince: datetime
        :param SubmittedSince: 
        
          An optional parameter that lets you get information about all the operations that you submitted after a specified date and time. Specify the date and time in Coordinated Universal time (UTC).
        
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
                \'Operations\': [
                    {
                        \'OperationId\': \'string\',
                        \'Status\': \'SUBMITTED\'|\'IN_PROGRESS\'|\'ERROR\'|\'SUCCESSFUL\'|\'FAILED\',
                        \'Type\': \'REGISTER_DOMAIN\'|\'DELETE_DOMAIN\'|\'TRANSFER_IN_DOMAIN\'|\'UPDATE_DOMAIN_CONTACT\'|\'UPDATE_NAMESERVER\'|\'CHANGE_PRIVACY_PROTECTION\'|\'DOMAIN_LOCK\'|\'ENABLE_AUTORENEW\'|\'DISABLE_AUTORENEW\'|\'ADD_DNSSEC\'|\'REMOVE_DNSSEC\'|\'EXPIRE_DOMAIN\'|\'TRANSFER_OUT_DOMAIN\'|\'CHANGE_DOMAIN_OWNER\'|\'RENEW_DOMAIN\'|\'PUSH_DOMAIN\',
                        \'SubmittedDate\': datetime(2015, 1, 1)
                    },
                ],
                \'NextToken\': \'string\'
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
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass
