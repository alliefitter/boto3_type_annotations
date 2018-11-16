from typing import Dict
from botocore.paginate import Paginator


class ListDetectors(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListDetectors>`_
        
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
                \'DetectorIds\': [
                    \'string\',
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **DetectorIds** *(list) --* A list of detector Ids.
              
              - *(string) --* The unique identifier for a detector.
          
        """
        pass


class ListFilters(Paginator):
    def paginate(self, DetectorId: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListFilters>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DetectorId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The ID of the detector that specifies the GuardDuty service where you want to list filters.
        
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
                \'FilterNames\': [
                    \'string\',
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **FilterNames** *(list) --* A list of filter names
              
              - *(string) --* The unique identifier for a filter
          
        """
        pass


class ListFindings(Paginator):
    def paginate(self, DetectorId: str, FindingCriteria: Dict = None, SortCriteria: Dict = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListFindings>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DetectorId=\'string\',
              FindingCriteria={
                  \'Criterion\': {
                      \'string\': {
                          \'Eq\': [
                              \'string\',
                          ],
                          \'Gt\': 123,
                          \'Gte\': 123,
                          \'Lt\': 123,
                          \'Lte\': 123,
                          \'Neq\': [
                              \'string\',
                          ]
                      }
                  }
              },
              SortCriteria={
                  \'AttributeName\': \'string\',
                  \'OrderBy\': \'ASC\'|\'DESC\'
              },
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The ID of the detector that specifies the GuardDuty service whose findings you want to list.
        
        :type FindingCriteria: dict
        :param FindingCriteria: Represents the criteria used for querying findings.
        
          - **Criterion** *(dict) --* Represents a map of finding properties that match specified conditions and values when querying findings.
        
            - *(string) --* 
        
              - *(dict) --* Finding attribute (for example, accountId) for which conditions and values must be specified when querying findings.
        
                - **Eq** *(list) --* Represents the equal condition to be applied to a single field when querying for findings.
        
                  - *(string) --* 
        
                - **Gt** *(integer) --* Represents the greater than condition to be applied to a single field when querying for findings.
        
                - **Gte** *(integer) --* Represents the greater than equal condition to be applied to a single field when querying for findings.
        
                - **Lt** *(integer) --* Represents the less than condition to be applied to a single field when querying for findings.
        
                - **Lte** *(integer) --* Represents the less than equal condition to be applied to a single field when querying for findings.
        
                - **Neq** *(list) --* Represents the not equal condition to be applied to a single field when querying for findings.
        
                  - *(string) --* 
        
        :type SortCriteria: dict
        :param SortCriteria: Represents the criteria used for sorting findings.
        
          - **AttributeName** *(string) --* Represents the finding attribute (for example, accountId) by which to sort findings.
        
          - **OrderBy** *(string) --* Order by which the sorted findings are to be displayed.
        
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
                \'FindingIds\': [
                    \'string\',
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **FindingIds** *(list) --* The list of the Findings.
              
              - *(string) --* The unique identifier for the Finding
          
        """
        pass


class ListIPSets(Paginator):
    def paginate(self, DetectorId: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListIPSets>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DetectorId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The unique ID of the detector that you want to retrieve.
        
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
                \'IpSetIds\': [
                    \'string\',
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **IpSetIds** *(list) --* A list of the IP set IDs
              
              - *(string) --* The unique identifier for an IP Set
          
        """
        pass


class ListInvitations(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListInvitations>`_
        
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
                \'Invitations\': [
                    {
                        \'AccountId\': \'string\',
                        \'InvitationId\': \'string\',
                        \'InvitedAt\': \'string\',
                        \'RelationshipStatus\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **Invitations** *(list) --* A list of invitation descriptions.
              
              - *(dict) --* Invitation from an AWS account to become the current account\'s master.
                
                - **AccountId** *(string) --* Inviter account ID
                
                - **InvitationId** *(string) --* This value is used to validate the inviter account to the member account.
                
                - **InvitedAt** *(string) --* Timestamp at which the invitation was sent
                
                - **RelationshipStatus** *(string) --* The status of the relationship between the inviter and invitee accounts.
            
        """
        pass


class ListMembers(Paginator):
    def paginate(self, DetectorId: str, OnlyAssociated: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListMembers>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DetectorId=\'string\',
              OnlyAssociated=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The unique ID of the detector of the GuardDuty account whose members you want to list.
        
        :type OnlyAssociated: string
        :param OnlyAssociated: Specifies what member accounts the response is to include based on their relationship status with the master account. The default value is TRUE. If onlyAssociated is set to TRUE, the response will include member accounts whose relationship status with the master is set to Enabled, Disabled. If onlyAssociated is set to FALSE, the response will include all existing member accounts.
        
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
                \'Members\': [
                    {
                        \'AccountId\': \'string\',
                        \'DetectorId\': \'string\',
                        \'Email\': \'string\',
                        \'InvitedAt\': \'string\',
                        \'MasterId\': \'string\',
                        \'RelationshipStatus\': \'string\',
                        \'UpdatedAt\': \'string\'
                    },
                ],
                
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **Members** *(list) --* A list of member descriptions.
              
              - *(dict) --* Contains details about the member account.
                
                - **AccountId** *(string) --* AWS account ID.
                
                - **DetectorId** *(string) --* The unique identifier for a detector.
                
                - **Email** *(string) --* Member account\'s email address.
                
                - **InvitedAt** *(string) --* Timestamp at which the invitation was sent
                
                - **MasterId** *(string) --* The master account ID.
                
                - **RelationshipStatus** *(string) --* The status of the relationship between the member and the master.
                
                - **UpdatedAt** *(string) --* The first time a resource was created. The format will be ISO-8601.
            
        """
        pass


class ListThreatIntelSets(Paginator):
    def paginate(self, DetectorId: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListThreatIntelSets>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              DetectorId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The detectorID that specifies the GuardDuty service whose ThreatIntelSets you want to list.
        
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
                \'ThreatIntelSetIds\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **ThreatIntelSetIds** *(list) --* The list of the threat intel set IDs
              
              - *(string) --* The unique identifier for an threat intel set
          
        """
        pass
