from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def accept_invitation(self, DetectorId: str, InvitationId: str, MasterId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/AcceptInvitation>`_
        
        **Request Syntax** 
        ::
        
          response = client.accept_invitation(
              DetectorId=\'string\',
              InvitationId=\'string\',
              MasterId=\'string\'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The unique ID of the detector of the GuardDuty member account.
        
        :type InvitationId: string
        :param InvitationId: **[REQUIRED]** This value is used to validate the master account to the member account.
        
        :type MasterId: string
        :param MasterId: **[REQUIRED]** The account ID of the master GuardDuty account whose invitation you\'re accepting.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 200 response
        """
        pass

    def archive_findings(self, DetectorId: str, FindingIds: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ArchiveFindings>`_
        
        **Request Syntax** 
        ::
        
          response = client.archive_findings(
              DetectorId=\'string\',
              FindingIds=[
                  \'string\',
              ]
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The ID of the detector that specifies the GuardDuty service whose findings you want to archive.
        
        :type FindingIds: list
        :param FindingIds: **[REQUIRED]** IDs of the findings that you want to archive.
        
          - *(string) --* The unique identifier for the Finding
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 200 response
        """
        pass

    def can_paginate(self, operation_name: str = None) -> NoReturn:
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

    def create_detector(self, Enable: bool, ClientToken: str = None, FindingPublishingFrequency: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/CreateDetector>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_detector(
              ClientToken=\'string\',
              Enable=True|False,
              FindingPublishingFrequency=\'FIFTEEN_MINUTES\'|\'ONE_HOUR\'|\'SIX_HOURS\'
          )
        :type ClientToken: string
        :param ClientToken: The idempotency token for the create request.This field is autopopulated if not provided.
        
        :type Enable: boolean
        :param Enable: **[REQUIRED]** A boolean value that specifies whether the detector is to be enabled.
        
        :type FindingPublishingFrequency: string
        :param FindingPublishingFrequency: A enum value that specifies how frequently customer got Finding updates published.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DetectorId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **DetectorId** *(string) --* The unique ID of the created detector.
        """
        pass

    def create_filter(self, DetectorId: str, FindingCriteria: Dict, Name: str, Action: str = None, ClientToken: str = None, Description: str = None, Rank: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/CreateFilter>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_filter(
              Action=\'NOOP\'|\'ARCHIVE\',
              ClientToken=\'string\',
              Description=\'string\',
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
              Name=\'string\',
              Rank=123
          )
        :type Action: string
        :param Action: Specifies the action that is to be applied to the findings that match the filter.
        
        :type ClientToken: string
        :param ClientToken: The idempotency token for the create request.This field is autopopulated if not provided.
        
        :type Description: string
        :param Description: The description of the filter.
        
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The unique ID of the detector that you want to update.
        
        :type FindingCriteria: dict
        :param FindingCriteria: **[REQUIRED]** Represents the criteria to be used in the filter for querying findings.
        
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
        
        :type Name: string
        :param Name: **[REQUIRED]** The name of the filter.
        
        :type Rank: integer
        :param Rank: Specifies the position of the filter in the list of current filters. Also specifies the order in which this filter is applied to the findings.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Name\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **Name** *(string) --* The name of the successfully created filter.
        """
        pass

    def create_ip_set(self, Activate: bool, DetectorId: str, Format: str, Location: str, Name: str, ClientToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/CreateIPSet>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_ip_set(
              Activate=True|False,
              ClientToken=\'string\',
              DetectorId=\'string\',
              Format=\'TXT\'|\'STIX\'|\'OTX_CSV\'|\'ALIEN_VAULT\'|\'PROOF_POINT\'|\'FIRE_EYE\',
              Location=\'string\',
              Name=\'string\'
          )
        :type Activate: boolean
        :param Activate: **[REQUIRED]** A boolean value that indicates whether GuardDuty is to start using the uploaded IPSet.
        
        :type ClientToken: string
        :param ClientToken: The idempotency token for the create request.This field is autopopulated if not provided.
        
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The unique ID of the detector that you want to update.
        
        :type Format: string
        :param Format: **[REQUIRED]** The format of the file that contains the IPSet.
        
        :type Location: string
        :param Location: **[REQUIRED]** The URI of the file that contains the IPSet. For example (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key)
        
        :type Name: string
        :param Name: **[REQUIRED]** The user friendly name to identify the IPSet. This name is displayed in all findings that are triggered by activity that involves IP addresses included in this IPSet.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IpSetId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **IpSetId** *(string) --* The unique identifier for an IP Set
        """
        pass

    def create_members(self, AccountDetails: List, DetectorId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/CreateMembers>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_members(
              AccountDetails=[
                  {
                      \'AccountId\': \'string\',
                      \'Email\': \'string\'
                  },
              ],
              DetectorId=\'string\'
          )
        :type AccountDetails: list
        :param AccountDetails: **[REQUIRED]** A list of account ID and email address pairs of the accounts that you want to associate with the master GuardDuty account.
        
          - *(dict) --* An object containing the member\'s accountId and email address.
        
            - **AccountId** *(string) --* **[REQUIRED]** Member account ID.
        
            - **Email** *(string) --* **[REQUIRED]** Member account\'s email address.
        
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The unique ID of the detector of the GuardDuty account with which you want to associate member accounts.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'UnprocessedAccounts\': [
                    {
                        \'AccountId\': \'string\',
                        \'Result\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **UnprocessedAccounts** *(list) --* A list of objects containing the unprocessed account and a result string explaining why it was unprocessed.
              
              - *(dict) --* An object containing the unprocessed account and a result string explaining why it was unprocessed.
                
                - **AccountId** *(string) --* AWS Account ID.
                
                - **Result** *(string) --* A reason why the account hasn\'t been processed.
            
        """
        pass

    def create_sample_findings(self, DetectorId: str, FindingTypes: List = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/CreateSampleFindings>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_sample_findings(
              DetectorId=\'string\',
              FindingTypes=[
                  \'string\',
              ]
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The ID of the detector to create sample findings for.
        
        :type FindingTypes: list
        :param FindingTypes: Types of sample findings that you want to generate.
        
          - *(string) --* The finding type for the finding
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 200 response
        """
        pass

    def create_threat_intel_set(self, Activate: bool, DetectorId: str, Format: str, Location: str, Name: str, ClientToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/CreateThreatIntelSet>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_threat_intel_set(
              Activate=True|False,
              ClientToken=\'string\',
              DetectorId=\'string\',
              Format=\'TXT\'|\'STIX\'|\'OTX_CSV\'|\'ALIEN_VAULT\'|\'PROOF_POINT\'|\'FIRE_EYE\',
              Location=\'string\',
              Name=\'string\'
          )
        :type Activate: boolean
        :param Activate: **[REQUIRED]** A boolean value that indicates whether GuardDuty is to start using the uploaded ThreatIntelSet.
        
        :type ClientToken: string
        :param ClientToken: The idempotency token for the create request.This field is autopopulated if not provided.
        
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The unique ID of the detector that you want to update.
        
        :type Format: string
        :param Format: **[REQUIRED]** The format of the file that contains the ThreatIntelSet.
        
        :type Location: string
        :param Location: **[REQUIRED]** The URI of the file that contains the ThreatIntelSet. For example (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key).
        
        :type Name: string
        :param Name: **[REQUIRED]** A user-friendly ThreatIntelSet name that is displayed in all finding generated by activity that involves IP addresses included in this ThreatIntelSet.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'ThreatIntelSetId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **ThreatIntelSetId** *(string) --* The unique identifier for an threat intel set
        """
        pass

    def decline_invitations(self, AccountIds: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DeclineInvitations>`_
        
        **Request Syntax** 
        ::
        
          response = client.decline_invitations(
              AccountIds=[
                  \'string\',
              ]
          )
        :type AccountIds: list
        :param AccountIds: **[REQUIRED]** A list of account IDs of the AWS accounts that sent invitations to the current member account that you want to decline invitations from.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'UnprocessedAccounts\': [
                    {
                        \'AccountId\': \'string\',
                        \'Result\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **UnprocessedAccounts** *(list) --* A list of objects containing the unprocessed account and a result string explaining why it was unprocessed.
              
              - *(dict) --* An object containing the unprocessed account and a result string explaining why it was unprocessed.
                
                - **AccountId** *(string) --* AWS Account ID.
                
                - **Result** *(string) --* A reason why the account hasn\'t been processed.
            
        """
        pass

    def delete_detector(self, DetectorId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DeleteDetector>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_detector(
              DetectorId=\'string\'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The unique ID that specifies the detector that you want to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 200 response
        """
        pass

    def delete_filter(self, DetectorId: str, FilterName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DeleteFilter>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_filter(
              DetectorId=\'string\',
              FilterName=\'string\'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The unique ID that specifies the detector where you want to delete a filter.
        
        :type FilterName: string
        :param FilterName: **[REQUIRED]** The name of the filter.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 200 response
        """
        pass

    def delete_invitations(self, AccountIds: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DeleteInvitations>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_invitations(
              AccountIds=[
                  \'string\',
              ]
          )
        :type AccountIds: list
        :param AccountIds: **[REQUIRED]** A list of account IDs of the AWS accounts that sent invitations to the current member account that you want to delete invitations from.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'UnprocessedAccounts\': [
                    {
                        \'AccountId\': \'string\',
                        \'Result\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **UnprocessedAccounts** *(list) --* A list of objects containing the unprocessed account and a result string explaining why it was unprocessed.
              
              - *(dict) --* An object containing the unprocessed account and a result string explaining why it was unprocessed.
                
                - **AccountId** *(string) --* AWS Account ID.
                
                - **Result** *(string) --* A reason why the account hasn\'t been processed.
            
        """
        pass

    def delete_ip_set(self, DetectorId: str, IpSetId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DeleteIPSet>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_ip_set(
              DetectorId=\'string\',
              IpSetId=\'string\'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The detectorID that specifies the GuardDuty service whose IPSet you want to delete.
        
        :type IpSetId: string
        :param IpSetId: **[REQUIRED]** The unique ID that specifies the IPSet that you want to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 200 response
        """
        pass

    def delete_members(self, AccountIds: List, DetectorId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DeleteMembers>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_members(
              AccountIds=[
                  \'string\',
              ],
              DetectorId=\'string\'
          )
        :type AccountIds: list
        :param AccountIds: **[REQUIRED]** A list of account IDs of the GuardDuty member accounts that you want to delete.
        
          - *(string) --* 
        
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The unique ID of the detector of the GuardDuty account whose members you want to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'UnprocessedAccounts\': [
                    {
                        \'AccountId\': \'string\',
                        \'Result\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **UnprocessedAccounts** *(list) --* A list of objects containing the unprocessed account and a result string explaining why it was unprocessed.
              
              - *(dict) --* An object containing the unprocessed account and a result string explaining why it was unprocessed.
                
                - **AccountId** *(string) --* AWS Account ID.
                
                - **Result** *(string) --* A reason why the account hasn\'t been processed.
            
        """
        pass

    def delete_threat_intel_set(self, DetectorId: str, ThreatIntelSetId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DeleteThreatIntelSet>`_
        
        **Request Syntax** 
        ::
        
          response = client.delete_threat_intel_set(
              DetectorId=\'string\',
              ThreatIntelSetId=\'string\'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The detectorID that specifies the GuardDuty service whose ThreatIntelSet you want to delete.
        
        :type ThreatIntelSetId: string
        :param ThreatIntelSetId: **[REQUIRED]** The unique ID that specifies the ThreatIntelSet that you want to delete.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 200 response
        """
        pass

    def disassociate_from_master_account(self, DetectorId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DisassociateFromMasterAccount>`_
        
        **Request Syntax** 
        ::
        
          response = client.disassociate_from_master_account(
              DetectorId=\'string\'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The unique ID of the detector of the GuardDuty member account.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 200 response
        """
        pass

    def disassociate_members(self, AccountIds: List, DetectorId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DisassociateMembers>`_
        
        **Request Syntax** 
        ::
        
          response = client.disassociate_members(
              AccountIds=[
                  \'string\',
              ],
              DetectorId=\'string\'
          )
        :type AccountIds: list
        :param AccountIds: **[REQUIRED]** A list of account IDs of the GuardDuty member accounts that you want to disassociate from master.
        
          - *(string) --* 
        
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The unique ID of the detector of the GuardDuty account whose members you want to disassociate from master.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'UnprocessedAccounts\': [
                    {
                        \'AccountId\': \'string\',
                        \'Result\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **UnprocessedAccounts** *(list) --* A list of objects containing the unprocessed account and a result string explaining why it was unprocessed.
              
              - *(dict) --* An object containing the unprocessed account and a result string explaining why it was unprocessed.
                
                - **AccountId** *(string) --* AWS Account ID.
                
                - **Result** *(string) --* A reason why the account hasn\'t been processed.
            
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> NoReturn:
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

    def get_detector(self, DetectorId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetDetector>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_detector(
              DetectorId=\'string\'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The unique ID of the detector that you want to retrieve.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'CreatedAt\': \'string\',
                \'FindingPublishingFrequency\': \'FIFTEEN_MINUTES\'|\'ONE_HOUR\'|\'SIX_HOURS\',
                \'ServiceRole\': \'string\',
                \'Status\': \'ENABLED\'|\'DISABLED\',
                \'UpdatedAt\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **CreatedAt** *(string) --* The first time a resource was created. The format will be ISO-8601.
            
            - **FindingPublishingFrequency** *(string) --* A enum value that specifies how frequently customer got Finding updates published.
            
            - **ServiceRole** *(string) --* Customer serviceRole name or ARN for accessing customer resources
            
            - **Status** *(string) --* The status of detector.
            
            - **UpdatedAt** *(string) --* The first time a resource was created. The format will be ISO-8601.
        """
        pass

    def get_filter(self, DetectorId: str, FilterName: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetFilter>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_filter(
              DetectorId=\'string\',
              FilterName=\'string\'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The detector ID that specifies the GuardDuty service where you want to list the details of the specified filter.
        
        :type FilterName: string
        :param FilterName: **[REQUIRED]** The name of the filter whose details you want to get.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Action\': \'NOOP\'|\'ARCHIVE\',
                \'Description\': \'string\',
                \'FindingCriteria\': {
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
                \'Name\': \'string\',
                \'Rank\': 123
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **Action** *(string) --* Specifies the action that is to be applied to the findings that match the filter.
            
            - **Description** *(string) --* The description of the filter.
            
            - **FindingCriteria** *(dict) --* Represents the criteria to be used in the filter for querying findings.
              
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
                  
            - **Name** *(string) --* The name of the filter.
            
            - **Rank** *(integer) --* Specifies the position of the filter in the list of current filters. Also specifies the order in which this filter is applied to the findings.
        """
        pass

    def get_findings(self, DetectorId: str, FindingIds: List, SortCriteria: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetFindings>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_findings(
              DetectorId=\'string\',
              FindingIds=[
                  \'string\',
              ],
              SortCriteria={
                  \'AttributeName\': \'string\',
                  \'OrderBy\': \'ASC\'|\'DESC\'
              }
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The ID of the detector that specifies the GuardDuty service whose findings you want to retrieve.
        
        :type FindingIds: list
        :param FindingIds: **[REQUIRED]** IDs of the findings that you want to retrieve.
        
          - *(string) --* The unique identifier for the Finding
        
        :type SortCriteria: dict
        :param SortCriteria: Represents the criteria used for sorting findings.
        
          - **AttributeName** *(string) --* Represents the finding attribute (for example, accountId) by which to sort findings.
        
          - **OrderBy** *(string) --* Order by which the sorted findings are to be displayed.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Findings\': [
                    {
                        \'AccountId\': \'string\',
                        \'Arn\': \'string\',
                        \'Confidence\': 123.0,
                        \'CreatedAt\': \'string\',
                        \'Description\': \'string\',
                        \'Id\': \'string\',
                        \'Partition\': \'string\',
                        \'Region\': \'string\',
                        \'Resource\': {
                            \'AccessKeyDetails\': {
                                \'AccessKeyId\': \'string\',
                                \'PrincipalId\': \'string\',
                                \'UserName\': \'string\',
                                \'UserType\': \'string\'
                            },
                            \'InstanceDetails\': {
                                \'AvailabilityZone\': \'string\',
                                \'IamInstanceProfile\': {
                                    \'Arn\': \'string\',
                                    \'Id\': \'string\'
                                },
                                \'ImageDescription\': \'string\',
                                \'ImageId\': \'string\',
                                \'InstanceId\': \'string\',
                                \'InstanceState\': \'string\',
                                \'InstanceType\': \'string\',
                                \'LaunchTime\': \'string\',
                                \'NetworkInterfaces\': [
                                    {
                                        \'Ipv6Addresses\': [
                                            \'string\',
                                        ],
                                        \'NetworkInterfaceId\': \'string\',
                                        \'PrivateDnsName\': \'string\',
                                        \'PrivateIpAddress\': \'string\',
                                        \'PrivateIpAddresses\': [
                                            {
                                                \'PrivateDnsName\': \'string\',
                                                \'PrivateIpAddress\': \'string\'
                                            },
                                        ],
                                        \'PublicDnsName\': \'string\',
                                        \'PublicIp\': \'string\',
                                        \'SecurityGroups\': [
                                            {
                                                \'GroupId\': \'string\',
                                                \'GroupName\': \'string\'
                                            },
                                        ],
                                        \'SubnetId\': \'string\',
                                        \'VpcId\': \'string\'
                                    },
                                ],
                                \'Platform\': \'string\',
                                \'ProductCodes\': [
                                    {
                                        \'Code\': \'string\',
                                        \'ProductType\': \'string\'
                                    },
                                ],
                                \'Tags\': [
                                    {
                                        \'Key\': \'string\',
                                        \'Value\': \'string\'
                                    },
                                ]
                            },
                            \'ResourceType\': \'string\'
                        },
                        \'SchemaVersion\': \'string\',
                        \'Service\': {
                            \'Action\': {
                                \'ActionType\': \'string\',
                                \'AwsApiCallAction\': {
                                    \'Api\': \'string\',
                                    \'CallerType\': \'string\',
                                    \'DomainDetails\': {},
                                    \'RemoteIpDetails\': {
                                        \'City\': {
                                            \'CityName\': \'string\'
                                        },
                                        \'Country\': {
                                            \'CountryCode\': \'string\',
                                            \'CountryName\': \'string\'
                                        },
                                        \'GeoLocation\': {
                                            \'Lat\': 123.0,
                                            \'Lon\': 123.0
                                        },
                                        \'IpAddressV4\': \'string\',
                                        \'Organization\': {
                                            \'Asn\': \'string\',
                                            \'AsnOrg\': \'string\',
                                            \'Isp\': \'string\',
                                            \'Org\': \'string\'
                                        }
                                    },
                                    \'ServiceName\': \'string\'
                                },
                                \'DnsRequestAction\': {
                                    \'Domain\': \'string\'
                                },
                                \'NetworkConnectionAction\': {
                                    \'Blocked\': True|False,
                                    \'ConnectionDirection\': \'string\',
                                    \'LocalPortDetails\': {
                                        \'Port\': 123,
                                        \'PortName\': \'string\'
                                    },
                                    \'Protocol\': \'string\',
                                    \'RemoteIpDetails\': {
                                        \'City\': {
                                            \'CityName\': \'string\'
                                        },
                                        \'Country\': {
                                            \'CountryCode\': \'string\',
                                            \'CountryName\': \'string\'
                                        },
                                        \'GeoLocation\': {
                                            \'Lat\': 123.0,
                                            \'Lon\': 123.0
                                        },
                                        \'IpAddressV4\': \'string\',
                                        \'Organization\': {
                                            \'Asn\': \'string\',
                                            \'AsnOrg\': \'string\',
                                            \'Isp\': \'string\',
                                            \'Org\': \'string\'
                                        }
                                    },
                                    \'RemotePortDetails\': {
                                        \'Port\': 123,
                                        \'PortName\': \'string\'
                                    }
                                },
                                \'PortProbeAction\': {
                                    \'Blocked\': True|False,
                                    \'PortProbeDetails\': [
                                        {
                                            \'LocalPortDetails\': {
                                                \'Port\': 123,
                                                \'PortName\': \'string\'
                                            },
                                            \'RemoteIpDetails\': {
                                                \'City\': {
                                                    \'CityName\': \'string\'
                                                },
                                                \'Country\': {
                                                    \'CountryCode\': \'string\',
                                                    \'CountryName\': \'string\'
                                                },
                                                \'GeoLocation\': {
                                                    \'Lat\': 123.0,
                                                    \'Lon\': 123.0
                                                },
                                                \'IpAddressV4\': \'string\',
                                                \'Organization\': {
                                                    \'Asn\': \'string\',
                                                    \'AsnOrg\': \'string\',
                                                    \'Isp\': \'string\',
                                                    \'Org\': \'string\'
                                                }
                                            }
                                        },
                                    ]
                                }
                            },
                            \'Archived\': True|False,
                            \'Count\': 123,
                            \'DetectorId\': \'string\',
                            \'EventFirstSeen\': \'string\',
                            \'EventLastSeen\': \'string\',
                            \'ResourceRole\': \'string\',
                            \'ServiceName\': \'string\',
                            \'UserFeedback\': \'string\'
                        },
                        \'Severity\': 123.0,
                        \'Title\': \'string\',
                        \'Type\': \'string\',
                        \'UpdatedAt\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **Findings** *(list) --* A list of findings.
              
              - *(dict) --* Representation of a abnormal or suspicious activity.
                
                - **AccountId** *(string) --* AWS account ID where the activity occurred that prompted GuardDuty to generate a finding.
                
                - **Arn** *(string) --* The ARN of a finding described by the action.
                
                - **Confidence** *(float) --* The confidence level of a finding.
                
                - **CreatedAt** *(string) --* The time stamp at which a finding was generated.
                
                - **Description** *(string) --* The description of a finding.
                
                - **Id** *(string) --* The identifier that corresponds to a finding described by the action.
                
                - **Partition** *(string) --* The AWS resource partition.
                
                - **Region** *(string) --* The AWS region where the activity occurred that prompted GuardDuty to generate a finding.
                
                - **Resource** *(dict) --* The AWS resource associated with the activity that prompted GuardDuty to generate a finding.
                  
                  - **AccessKeyDetails** *(dict) --* The IAM access key details (IAM user information) of a user that engaged in the activity that prompted GuardDuty to generate a finding.
                    
                    - **AccessKeyId** *(string) --* Access key ID of the user.
                    
                    - **PrincipalId** *(string) --* The principal ID of the user.
                    
                    - **UserName** *(string) --* The name of the user.
                    
                    - **UserType** *(string) --* The type of the user.
                
                  - **InstanceDetails** *(dict) --* The information about the EC2 instance associated with the activity that prompted GuardDuty to generate a finding.
                    
                    - **AvailabilityZone** *(string) --* The availability zone of the EC2 instance.
                    
                    - **IamInstanceProfile** *(dict) --* The profile information of the EC2 instance.
                      
                      - **Arn** *(string) --* AWS EC2 instance profile ARN.
                      
                      - **Id** *(string) --* AWS EC2 instance profile ID.
                  
                    - **ImageDescription** *(string) --* The image description of the EC2 instance.
                    
                    - **ImageId** *(string) --* The image ID of the EC2 instance.
                    
                    - **InstanceId** *(string) --* The ID of the EC2 instance.
                    
                    - **InstanceState** *(string) --* The state of the EC2 instance.
                    
                    - **InstanceType** *(string) --* The type of the EC2 instance.
                    
                    - **LaunchTime** *(string) --* The launch time of the EC2 instance.
                    
                    - **NetworkInterfaces** *(list) --* The network interface information of the EC2 instance.
                      
                      - *(dict) --* The network interface information of the EC2 instance.
                        
                        - **Ipv6Addresses** *(list) --* A list of EC2 instance IPv6 address information.
                          
                          - *(string) --* IpV6 address of the EC2 instance.
                      
                        - **NetworkInterfaceId** *(string) --* The ID of the network interface
                        
                        - **PrivateDnsName** *(string) --* Private DNS name of the EC2 instance.
                        
                        - **PrivateIpAddress** *(string) --* Private IP address of the EC2 instance.
                        
                        - **PrivateIpAddresses** *(list) --* Other private IP address information of the EC2 instance.
                          
                          - *(dict) --* Other private IP address information of the EC2 instance.
                            
                            - **PrivateDnsName** *(string) --* Private DNS name of the EC2 instance.
                            
                            - **PrivateIpAddress** *(string) --* Private IP address of the EC2 instance.
                        
                        - **PublicDnsName** *(string) --* Public DNS name of the EC2 instance.
                        
                        - **PublicIp** *(string) --* Public IP address of the EC2 instance.
                        
                        - **SecurityGroups** *(list) --* Security groups associated with the EC2 instance.
                          
                          - *(dict) --* Security groups associated with the EC2 instance.
                            
                            - **GroupId** *(string) --* EC2 instance\'s security group ID.
                            
                            - **GroupName** *(string) --* EC2 instance\'s security group name.
                        
                        - **SubnetId** *(string) --* The subnet ID of the EC2 instance.
                        
                        - **VpcId** *(string) --* The VPC ID of the EC2 instance.
                    
                    - **Platform** *(string) --* The platform of the EC2 instance.
                    
                    - **ProductCodes** *(list) --* The product code of the EC2 instance.
                      
                      - *(dict) --* The product code of the EC2 instance.
                        
                        - **Code** *(string) --* Product code information.
                        
                        - **ProductType** *(string) --* Product code type.
                    
                    - **Tags** *(list) --* The tags of the EC2 instance.
                      
                      - *(dict) --* A tag of the EC2 instance.
                        
                        - **Key** *(string) --* EC2 instance tag key.
                        
                        - **Value** *(string) --* EC2 instance tag value.
                    
                  - **ResourceType** *(string) --* The type of the AWS resource.
              
                - **SchemaVersion** *(string) --* Findings\' schema version.
                
                - **Service** *(dict) --* Additional information assigned to the generated finding by GuardDuty.
                  
                  - **Action** *(dict) --* Information about the activity described in a finding.
                    
                    - **ActionType** *(string) --* GuardDuty Finding activity type.
                    
                    - **AwsApiCallAction** *(dict) --* Information about the AWS_API_CALL action described in this finding.
                      
                      - **Api** *(string) --* AWS API name.
                      
                      - **CallerType** *(string) --* AWS API caller type.
                      
                      - **DomainDetails** *(dict) --* Domain information for the AWS API call.
                    
                      - **RemoteIpDetails** *(dict) --* Remote IP information of the connection.
                        
                        - **City** *(dict) --* City information of the remote IP address.
                          
                          - **CityName** *(string) --* City name of the remote IP address.
                      
                        - **Country** *(dict) --* Country code of the remote IP address.
                          
                          - **CountryCode** *(string) --* Country code of the remote IP address.
                          
                          - **CountryName** *(string) --* Country name of the remote IP address.
                      
                        - **GeoLocation** *(dict) --* Location information of the remote IP address.
                          
                          - **Lat** *(float) --* Latitude information of remote IP address.
                          
                          - **Lon** *(float) --* Longitude information of remote IP address.
                      
                        - **IpAddressV4** *(string) --* IPV4 remote address of the connection.
                        
                        - **Organization** *(dict) --* ISP Organization information of the remote IP address.
                          
                          - **Asn** *(string) --* Autonomous system number of the internet provider of the remote IP address.
                          
                          - **AsnOrg** *(string) --* Organization that registered this ASN.
                          
                          - **Isp** *(string) --* ISP information for the internet provider.
                          
                          - **Org** *(string) --* Name of the internet provider.
                      
                      - **ServiceName** *(string) --* AWS service name whose API was invoked.
                  
                    - **DnsRequestAction** *(dict) --* Information about the DNS_REQUEST action described in this finding.
                      
                      - **Domain** *(string) --* Domain information for the DNS request.
                  
                    - **NetworkConnectionAction** *(dict) --* Information about the NETWORK_CONNECTION action described in this finding.
                      
                      - **Blocked** *(boolean) --* Network connection blocked information.
                      
                      - **ConnectionDirection** *(string) --* Network connection direction.
                      
                      - **LocalPortDetails** *(dict) --* Local port information of the connection.
                        
                        - **Port** *(integer) --* Port number of the local connection.
                        
                        - **PortName** *(string) --* Port name of the local connection.
                    
                      - **Protocol** *(string) --* Network connection protocol.
                      
                      - **RemoteIpDetails** *(dict) --* Remote IP information of the connection.
                        
                        - **City** *(dict) --* City information of the remote IP address.
                          
                          - **CityName** *(string) --* City name of the remote IP address.
                      
                        - **Country** *(dict) --* Country code of the remote IP address.
                          
                          - **CountryCode** *(string) --* Country code of the remote IP address.
                          
                          - **CountryName** *(string) --* Country name of the remote IP address.
                      
                        - **GeoLocation** *(dict) --* Location information of the remote IP address.
                          
                          - **Lat** *(float) --* Latitude information of remote IP address.
                          
                          - **Lon** *(float) --* Longitude information of remote IP address.
                      
                        - **IpAddressV4** *(string) --* IPV4 remote address of the connection.
                        
                        - **Organization** *(dict) --* ISP Organization information of the remote IP address.
                          
                          - **Asn** *(string) --* Autonomous system number of the internet provider of the remote IP address.
                          
                          - **AsnOrg** *(string) --* Organization that registered this ASN.
                          
                          - **Isp** *(string) --* ISP information for the internet provider.
                          
                          - **Org** *(string) --* Name of the internet provider.
                      
                      - **RemotePortDetails** *(dict) --* Remote port information of the connection.
                        
                        - **Port** *(integer) --* Port number of the remote connection.
                        
                        - **PortName** *(string) --* Port name of the remote connection.
                    
                    - **PortProbeAction** *(dict) --* Information about the PORT_PROBE action described in this finding.
                      
                      - **Blocked** *(boolean) --* Port probe blocked information.
                      
                      - **PortProbeDetails** *(list) --* A list of port probe details objects.
                        
                        - *(dict) --* Details about the port probe finding.
                          
                          - **LocalPortDetails** *(dict) --* Local port information of the connection.
                            
                            - **Port** *(integer) --* Port number of the local connection.
                            
                            - **PortName** *(string) --* Port name of the local connection.
                        
                          - **RemoteIpDetails** *(dict) --* Remote IP information of the connection.
                            
                            - **City** *(dict) --* City information of the remote IP address.
                              
                              - **CityName** *(string) --* City name of the remote IP address.
                          
                            - **Country** *(dict) --* Country code of the remote IP address.
                              
                              - **CountryCode** *(string) --* Country code of the remote IP address.
                              
                              - **CountryName** *(string) --* Country name of the remote IP address.
                          
                            - **GeoLocation** *(dict) --* Location information of the remote IP address.
                              
                              - **Lat** *(float) --* Latitude information of remote IP address.
                              
                              - **Lon** *(float) --* Longitude information of remote IP address.
                          
                            - **IpAddressV4** *(string) --* IPV4 remote address of the connection.
                            
                            - **Organization** *(dict) --* ISP Organization information of the remote IP address.
                              
                              - **Asn** *(string) --* Autonomous system number of the internet provider of the remote IP address.
                              
                              - **AsnOrg** *(string) --* Organization that registered this ASN.
                              
                              - **Isp** *(string) --* ISP information for the internet provider.
                              
                              - **Org** *(string) --* Name of the internet provider.
                          
                  - **Archived** *(boolean) --* Indicates whether this finding is archived.
                  
                  - **Count** *(integer) --* Total count of the occurrences of this finding type.
                  
                  - **DetectorId** *(string) --* Detector ID for the GuardDuty service.
                  
                  - **EventFirstSeen** *(string) --* First seen timestamp of the activity that prompted GuardDuty to generate this finding.
                  
                  - **EventLastSeen** *(string) --* Last seen timestamp of the activity that prompted GuardDuty to generate this finding.
                  
                  - **ResourceRole** *(string) --* Resource role information for this finding.
                  
                  - **ServiceName** *(string) --* The name of the AWS service (GuardDuty) that generated a finding.
                  
                  - **UserFeedback** *(string) --* Feedback left about the finding.
              
                - **Severity** *(float) --* The severity of a finding.
                
                - **Title** *(string) --* The title of a finding.
                
                - **Type** *(string) --* The type of a finding described by the action.
                
                - **UpdatedAt** *(string) --* The time stamp at which a finding was last updated.
            
        """
        pass

    def get_findings_statistics(self, DetectorId: str, FindingStatisticTypes: List, FindingCriteria: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetFindingsStatistics>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_findings_statistics(
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
              FindingStatisticTypes=[
                  \'COUNT_BY_SEVERITY\',
              ]
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The ID of the detector that specifies the GuardDuty service whose findings\' statistics you want to retrieve.
        
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
        
        :type FindingStatisticTypes: list
        :param FindingStatisticTypes: **[REQUIRED]** Types of finding statistics to retrieve.
        
          - *(string) --* The types of finding statistics.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'FindingStatistics\': {
                    \'CountBySeverity\': {
                        \'string\': 123
                    }
                }
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **FindingStatistics** *(dict) --* Finding statistics object.
              
              - **CountBySeverity** *(dict) --* Represents a map of severity to count statistic for a set of findings
                
                - *(string) --* 
                  
                  - *(integer) --* The count of findings for the given severity.
            
        """
        pass

    def get_invitations_count(self) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetInvitationsCount>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_invitations_count()
          
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'InvitationsCount\': 123
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **InvitationsCount** *(integer) --* The number of received invitations.
        """
        pass

    def get_ip_set(self, DetectorId: str, IpSetId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetIPSet>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_ip_set(
              DetectorId=\'string\',
              IpSetId=\'string\'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The detectorID that specifies the GuardDuty service whose IPSet you want to retrieve.
        
        :type IpSetId: string
        :param IpSetId: **[REQUIRED]** The unique ID that specifies the IPSet that you want to describe.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Format\': \'TXT\'|\'STIX\'|\'OTX_CSV\'|\'ALIEN_VAULT\'|\'PROOF_POINT\'|\'FIRE_EYE\',
                \'Location\': \'string\',
                \'Name\': \'string\',
                \'Status\': \'INACTIVE\'|\'ACTIVATING\'|\'ACTIVE\'|\'DEACTIVATING\'|\'ERROR\'|\'DELETE_PENDING\'|\'DELETED\'
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **Format** *(string) --* The format of the file that contains the IPSet.
            
            - **Location** *(string) --* The URI of the file that contains the IPSet. For example (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key)
            
            - **Name** *(string) --* The user friendly name to identify the IPSet. This name is displayed in all findings that are triggered by activity that involves IP addresses included in this IPSet.
            
            - **Status** *(string) --* The status of ipSet file uploaded.
        """
        pass

    def get_master_account(self, DetectorId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetMasterAccount>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_master_account(
              DetectorId=\'string\'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The unique ID of the detector of the GuardDuty member account.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Master\': {
                    \'AccountId\': \'string\',
                    \'InvitationId\': \'string\',
                    \'InvitedAt\': \'string\',
                    \'RelationshipStatus\': \'string\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **Master** *(dict) --* Contains details about the master account.
              
              - **AccountId** *(string) --* Master account ID
              
              - **InvitationId** *(string) --* This value is used to validate the master account to the member account.
              
              - **InvitedAt** *(string) --* Timestamp at which the invitation was sent
              
              - **RelationshipStatus** *(string) --* The status of the relationship between the master and member accounts.
          
        """
        pass

    def get_members(self, AccountIds: List, DetectorId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetMembers>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_members(
              AccountIds=[
                  \'string\',
              ],
              DetectorId=\'string\'
          )
        :type AccountIds: list
        :param AccountIds: **[REQUIRED]** A list of account IDs of the GuardDuty member accounts that you want to describe.
        
          - *(string) --* 
        
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The unique ID of the detector of the GuardDuty account whose members you want to retrieve.
        
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
                \'UnprocessedAccounts\': [
                    {
                        \'AccountId\': \'string\',
                        \'Result\': \'string\'
                    },
                ]
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
            
            - **UnprocessedAccounts** *(list) --* A list of objects containing the unprocessed account and a result string explaining why it was unprocessed.
              
              - *(dict) --* An object containing the unprocessed account and a result string explaining why it was unprocessed.
                
                - **AccountId** *(string) --* AWS Account ID.
                
                - **Result** *(string) --* A reason why the account hasn\'t been processed.
            
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

    def get_threat_intel_set(self, DetectorId: str, ThreatIntelSetId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetThreatIntelSet>`_
        
        **Request Syntax** 
        ::
        
          response = client.get_threat_intel_set(
              DetectorId=\'string\',
              ThreatIntelSetId=\'string\'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The detectorID that specifies the GuardDuty service whose ThreatIntelSet you want to describe.
        
        :type ThreatIntelSetId: string
        :param ThreatIntelSetId: **[REQUIRED]** The unique ID that specifies the ThreatIntelSet that you want to describe.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Format\': \'TXT\'|\'STIX\'|\'OTX_CSV\'|\'ALIEN_VAULT\'|\'PROOF_POINT\'|\'FIRE_EYE\',
                \'Location\': \'string\',
                \'Name\': \'string\',
                \'Status\': \'INACTIVE\'|\'ACTIVATING\'|\'ACTIVE\'|\'DEACTIVATING\'|\'ERROR\'|\'DELETE_PENDING\'|\'DELETED\'
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **Format** *(string) --* The format of the threatIntelSet.
            
            - **Location** *(string) --* The URI of the file that contains the ThreatIntelSet. For example (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key).
            
            - **Name** *(string) --* A user-friendly ThreatIntelSet name that is displayed in all finding generated by activity that involves IP addresses included in this ThreatIntelSet.
            
            - **Status** *(string) --* The status of threatIntelSet file uploaded.
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

    def invite_members(self, AccountIds: List, DetectorId: str, DisableEmailNotification: bool = None, Message: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/InviteMembers>`_
        
        **Request Syntax** 
        ::
        
          response = client.invite_members(
              AccountIds=[
                  \'string\',
              ],
              DetectorId=\'string\',
              DisableEmailNotification=True|False,
              Message=\'string\'
          )
        :type AccountIds: list
        :param AccountIds: **[REQUIRED]** A list of account IDs of the accounts that you want to invite to GuardDuty as members.
        
          - *(string) --* 
        
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The unique ID of the detector of the GuardDuty account with which you want to invite members.
        
        :type DisableEmailNotification: boolean
        :param DisableEmailNotification: A boolean value that specifies whether you want to disable email notification to the accounts that you’re inviting to GuardDuty as members.
        
        :type Message: string
        :param Message: The invitation message that you want to send to the accounts that you’re inviting to GuardDuty as members.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'UnprocessedAccounts\': [
                    {
                        \'AccountId\': \'string\',
                        \'Result\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **UnprocessedAccounts** *(list) --* A list of objects containing the unprocessed account and a result string explaining why it was unprocessed.
              
              - *(dict) --* An object containing the unprocessed account and a result string explaining why it was unprocessed.
                
                - **AccountId** *(string) --* AWS Account ID.
                
                - **Result** *(string) --* A reason why the account hasn\'t been processed.
            
        """
        pass

    def list_detectors(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListDetectors>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_detectors(
              MaxResults=123,
              NextToken=\'string\'
          )
        :type MaxResults: integer
        :param MaxResults: You can use this parameter to indicate the maximum number of detectors that you want in the response.
        
        :type NextToken: string
        :param NextToken: You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the ListDetectors action. For subsequent calls to the action fill nextToken in the request with the value of nextToken from the previous response to continue listing data.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'DetectorIds\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **DetectorIds** *(list) --* A list of detector Ids.
              
              - *(string) --* The unique identifier for a detector.
          
            - **NextToken** *(string) --* You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action fill nextToken in the request with the value of NextToken from the previous response to continue listing data.
        """
        pass

    def list_filters(self, DetectorId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListFilters>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_filters(
              DetectorId=\'string\',
              MaxResults=123,
              NextToken=\'string\'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The ID of the detector that specifies the GuardDuty service where you want to list filters.
        
        :type MaxResults: integer
        :param MaxResults: Indicates the maximum number of items that you want in the response. The maximum value is 50.
        
        :type NextToken: string
        :param NextToken: Paginates results. Set the value of this parameter to NULL on your first call to the ListFilters operation.For subsequent calls to the operation, fill nextToken in the request with the value of nextToken from the previous response to continue listing data.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'FilterNames\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **FilterNames** *(list) --* A list of filter names
              
              - *(string) --* The unique identifier for a filter
          
            - **NextToken** *(string) --* You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action fill nextToken in the request with the value of NextToken from the previous response to continue listing data.
        """
        pass

    def list_findings(self, DetectorId: str, FindingCriteria: Dict = None, MaxResults: int = None, NextToken: str = None, SortCriteria: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListFindings>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_findings(
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
              MaxResults=123,
              NextToken=\'string\',
              SortCriteria={
                  \'AttributeName\': \'string\',
                  \'OrderBy\': \'ASC\'|\'DESC\'
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
        
        :type MaxResults: integer
        :param MaxResults: You can use this parameter to indicate the maximum number of items you want in the response. The default value is 50. The maximum value is 50.
        
        :type NextToken: string
        :param NextToken: You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the ListFindings action. For subsequent calls to the action fill nextToken in the request with the value of nextToken from the previous response to continue listing data.
        
        :type SortCriteria: dict
        :param SortCriteria: Represents the criteria used for sorting findings.
        
          - **AttributeName** *(string) --* Represents the finding attribute (for example, accountId) by which to sort findings.
        
          - **OrderBy** *(string) --* Order by which the sorted findings are to be displayed.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'FindingIds\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **FindingIds** *(list) --* The list of the Findings.
              
              - *(string) --* The unique identifier for the Finding
          
            - **NextToken** *(string) --* You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action fill nextToken in the request with the value of NextToken from the previous response to continue listing data.
        """
        pass

    def list_invitations(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListInvitations>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_invitations(
              MaxResults=123,
              NextToken=\'string\'
          )
        :type MaxResults: integer
        :param MaxResults: You can use this parameter to indicate the maximum number of invitations you want in the response. The default value is 50. The maximum value is 50.
        
        :type NextToken: string
        :param NextToken: You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the ListInvitations action. Subsequent calls to the action fill nextToken in the request with the value of NextToken from the previous response to continue listing data.
        
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
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **Invitations** *(list) --* A list of invitation descriptions.
              
              - *(dict) --* Invitation from an AWS account to become the current account\'s master.
                
                - **AccountId** *(string) --* Inviter account ID
                
                - **InvitationId** *(string) --* This value is used to validate the inviter account to the member account.
                
                - **InvitedAt** *(string) --* Timestamp at which the invitation was sent
                
                - **RelationshipStatus** *(string) --* The status of the relationship between the inviter and invitee accounts.
            
            - **NextToken** *(string) --* You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action fill nextToken in the request with the value of NextToken from the previous response to continue listing data.
        """
        pass

    def list_ip_sets(self, DetectorId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListIPSets>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_ip_sets(
              DetectorId=\'string\',
              MaxResults=123,
              NextToken=\'string\'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The unique ID of the detector that you want to retrieve.
        
        :type MaxResults: integer
        :param MaxResults: You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 7. The maximum value is 7.
        
        :type NextToken: string
        :param NextToken: You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the ListIPSet action. For subsequent calls to the action fill nextToken in the request with the value of NextToken from the previous response to continue listing data.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'IpSetIds\': [
                    \'string\',
                ],
                \'NextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **IpSetIds** *(list) --* A list of the IP set IDs
              
              - *(string) --* The unique identifier for an IP Set
          
            - **NextToken** *(string) --* You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action fill nextToken in the request with the value of NextToken from the previous response to continue listing data.
        """
        pass

    def list_members(self, DetectorId: str, MaxResults: int = None, NextToken: str = None, OnlyAssociated: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListMembers>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_members(
              DetectorId=\'string\',
              MaxResults=123,
              NextToken=\'string\',
              OnlyAssociated=\'string\'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The unique ID of the detector of the GuardDuty account whose members you want to list.
        
        :type MaxResults: integer
        :param MaxResults: You can use this parameter to indicate the maximum number of items you want in the response. The default value is 1. The maximum value is 50.
        
        :type NextToken: string
        :param NextToken: You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the ListMembers action. Subsequent calls to the action fill nextToken in the request with the value of NextToken from the previous response to continue listing data.
        
        :type OnlyAssociated: string
        :param OnlyAssociated: Specifies what member accounts the response is to include based on their relationship status with the master account. The default value is TRUE. If onlyAssociated is set to TRUE, the response will include member accounts whose relationship status with the master is set to Enabled, Disabled. If onlyAssociated is set to FALSE, the response will include all existing member accounts.
        
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
                \'NextToken\': \'string\'
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
            
            - **NextToken** *(string) --* You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action fill nextToken in the request with the value of NextToken from the previous response to continue listing data.
        """
        pass

    def list_threat_intel_sets(self, DetectorId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListThreatIntelSets>`_
        
        **Request Syntax** 
        ::
        
          response = client.list_threat_intel_sets(
              DetectorId=\'string\',
              MaxResults=123,
              NextToken=\'string\'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The detectorID that specifies the GuardDuty service whose ThreatIntelSets you want to list.
        
        :type MaxResults: integer
        :param MaxResults: You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 7. The maximum value is 7.
        
        :type NextToken: string
        :param NextToken: Pagination token to start retrieving threat intel sets from.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'NextToken\': \'string\',
                \'ThreatIntelSetIds\': [
                    \'string\',
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **NextToken** *(string) --* You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action fill nextToken in the request with the value of NextToken from the previous response to continue listing data.
            
            - **ThreatIntelSetIds** *(list) --* The list of the threat intel set IDs
              
              - *(string) --* The unique identifier for an threat intel set
          
        """
        pass

    def start_monitoring_members(self, AccountIds: List, DetectorId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/StartMonitoringMembers>`_
        
        **Request Syntax** 
        ::
        
          response = client.start_monitoring_members(
              AccountIds=[
                  \'string\',
              ],
              DetectorId=\'string\'
          )
        :type AccountIds: list
        :param AccountIds: **[REQUIRED]** A list of account IDs of the GuardDuty member accounts whose findings you want the master account to monitor.
        
          - *(string) --* 
        
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The unique ID of the detector of the GuardDuty account whom you want to re-enable to monitor members\' findings.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'UnprocessedAccounts\': [
                    {
                        \'AccountId\': \'string\',
                        \'Result\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **UnprocessedAccounts** *(list) --* A list of objects containing the unprocessed account and a result string explaining why it was unprocessed.
              
              - *(dict) --* An object containing the unprocessed account and a result string explaining why it was unprocessed.
                
                - **AccountId** *(string) --* AWS Account ID.
                
                - **Result** *(string) --* A reason why the account hasn\'t been processed.
            
        """
        pass

    def stop_monitoring_members(self, AccountIds: List, DetectorId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/StopMonitoringMembers>`_
        
        **Request Syntax** 
        ::
        
          response = client.stop_monitoring_members(
              AccountIds=[
                  \'string\',
              ],
              DetectorId=\'string\'
          )
        :type AccountIds: list
        :param AccountIds: **[REQUIRED]** A list of account IDs of the GuardDuty member accounts whose findings you want the master account to stop monitoring.
        
          - *(string) --* 
        
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The unique ID of the detector of the GuardDuty account that you want to stop from monitor members\' findings.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'UnprocessedAccounts\': [
                    {
                        \'AccountId\': \'string\',
                        \'Result\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **UnprocessedAccounts** *(list) --* A list of objects containing the unprocessed account and a result string explaining why it was unprocessed.
              
              - *(dict) --* An object containing the unprocessed account and a result string explaining why it was unprocessed.
                
                - **AccountId** *(string) --* AWS Account ID.
                
                - **Result** *(string) --* A reason why the account hasn\'t been processed.
            
        """
        pass

    def unarchive_findings(self, DetectorId: str, FindingIds: List) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/UnarchiveFindings>`_
        
        **Request Syntax** 
        ::
        
          response = client.unarchive_findings(
              DetectorId=\'string\',
              FindingIds=[
                  \'string\',
              ]
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The ID of the detector that specifies the GuardDuty service whose findings you want to unarchive.
        
        :type FindingIds: list
        :param FindingIds: **[REQUIRED]** IDs of the findings that you want to unarchive.
        
          - *(string) --* The unique identifier for the Finding
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 200 response
        """
        pass

    def update_detector(self, DetectorId: str, Enable: bool = None, FindingPublishingFrequency: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/UpdateDetector>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_detector(
              DetectorId=\'string\',
              Enable=True|False,
              FindingPublishingFrequency=\'FIFTEEN_MINUTES\'|\'ONE_HOUR\'|\'SIX_HOURS\'
          )
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The unique ID of the detector that you want to update.
        
        :type Enable: boolean
        :param Enable: Updated boolean value for the detector that specifies whether the detector is enabled.
        
        :type FindingPublishingFrequency: string
        :param FindingPublishingFrequency: A enum value that specifies how frequently customer got Finding updates published.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 200 response
        """
        pass

    def update_filter(self, DetectorId: str, FilterName: str, Action: str = None, Description: str = None, FindingCriteria: Dict = None, Rank: int = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/UpdateFilter>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_filter(
              Action=\'NOOP\'|\'ARCHIVE\',
              Description=\'string\',
              DetectorId=\'string\',
              FilterName=\'string\',
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
              Rank=123
          )
        :type Action: string
        :param Action: Specifies the action that is to be applied to the findings that match the filter.
        
        :type Description: string
        :param Description: The description of the filter.
        
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The unique ID of the detector that specifies the GuardDuty service where you want to update a filter.
        
        :type FilterName: string
        :param FilterName: **[REQUIRED]** The name of the filter.
        
        :type FindingCriteria: dict
        :param FindingCriteria: Represents the criteria to be used in the filter for querying findings.
        
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
        
        :type Rank: integer
        :param Rank: Specifies the position of the filter in the list of current filters. Also specifies the order in which this filter is applied to the findings.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'Name\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 200 response
            
            - **Name** *(string) --* The name of the filter.
        """
        pass

    def update_findings_feedback(self, DetectorId: str, Feedback: str, FindingIds: List, Comments: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/UpdateFindingsFeedback>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_findings_feedback(
              Comments=\'string\',
              DetectorId=\'string\',
              Feedback=\'USEFUL\'|\'NOT_USEFUL\',
              FindingIds=[
                  \'string\',
              ]
          )
        :type Comments: string
        :param Comments: Additional feedback about the GuardDuty findings.
        
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The ID of the detector that specifies the GuardDuty service whose findings you want to mark as useful or not useful.
        
        :type Feedback: string
        :param Feedback: **[REQUIRED]** Valid values: USEFUL | NOT_USEFUL
        
        :type FindingIds: list
        :param FindingIds: **[REQUIRED]** IDs of the findings that you want to mark as useful or not useful.
        
          - *(string) --* The unique identifier for the Finding
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 200 response
        """
        pass

    def update_ip_set(self, DetectorId: str, IpSetId: str, Activate: bool = None, Location: str = None, Name: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/UpdateIPSet>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_ip_set(
              Activate=True|False,
              DetectorId=\'string\',
              IpSetId=\'string\',
              Location=\'string\',
              Name=\'string\'
          )
        :type Activate: boolean
        :param Activate: The updated boolean value that specifies whether the IPSet is active or not.
        
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The detectorID that specifies the GuardDuty service whose IPSet you want to update.
        
        :type IpSetId: string
        :param IpSetId: **[REQUIRED]** The unique ID that specifies the IPSet that you want to update.
        
        :type Location: string
        :param Location: The updated URI of the file that contains the IPSet. For example (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key).
        
        :type Name: string
        :param Name: The unique ID that specifies the IPSet that you want to update.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 200 response
        """
        pass

    def update_threat_intel_set(self, DetectorId: str, ThreatIntelSetId: str, Activate: bool = None, Location: str = None, Name: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/UpdateThreatIntelSet>`_
        
        **Request Syntax** 
        ::
        
          response = client.update_threat_intel_set(
              Activate=True|False,
              DetectorId=\'string\',
              Location=\'string\',
              Name=\'string\',
              ThreatIntelSetId=\'string\'
          )
        :type Activate: boolean
        :param Activate: The updated boolean value that specifies whether the ThreateIntelSet is active or not.
        
        :type DetectorId: string
        :param DetectorId: **[REQUIRED]** The detectorID that specifies the GuardDuty service whose ThreatIntelSet you want to update.
        
        :type Location: string
        :param Location: The updated URI of the file that contains the ThreateIntelSet. For example (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key)
        
        :type Name: string
        :param Name: The unique ID that specifies the ThreatIntelSet that you want to update.
        
        :type ThreatIntelSetId: string
        :param ThreatIntelSetId: **[REQUIRED]** The unique ID that specifies the ThreatIntelSet that you want to update.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {}
          **Response Structure** 
        
          - *(dict) --* 200 response
        """
        pass
