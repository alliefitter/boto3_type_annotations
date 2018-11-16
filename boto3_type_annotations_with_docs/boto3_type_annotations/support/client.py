from typing import Union
from botocore.paginate import Paginator
from typing import NoReturn
from botocore.client import BaseClient
from typing import Optional
from typing import List
from botocore.waiter import Waiter
from typing import Dict


class Client(BaseClient):
    def add_attachments_to_set(self, attachments: List, attachmentSetId: str = None) -> Dict:
        """
        
        An attachment set is a temporary container for attachments that are to be added to a case or case communication. The set is available for one hour after it is created; the ``expiryTime`` returned in the response indicates when the set expires. The maximum number of attachments in a set is 3, and the maximum size of any attachment in the set is 5 MB.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/AddAttachmentsToSet>`_
        
        **Request Syntax** 
        ::
        
          response = client.add_attachments_to_set(
              attachmentSetId=\'string\',
              attachments=[
                  {
                      \'fileName\': \'string\',
                      \'data\': b\'bytes\'
                  },
              ]
          )
        :type attachmentSetId: string
        :param attachmentSetId: 
        
          The ID of the attachment set. If an ``attachmentSetId`` is not specified, a new attachment set is created, and the ID of the set is returned in the response. If an ``attachmentSetId`` is specified, the attachments are added to the specified set, if it exists.
        
        :type attachments: list
        :param attachments: **[REQUIRED]** 
        
          One or more attachments to add to the set. The limit is 3 attachments per set, and the size limit is 5 MB per attachment.
        
          - *(dict) --* 
        
            An attachment to a case communication. The attachment consists of the file name and the content of the file.
        
            - **fileName** *(string) --* 
        
              The name of the attachment file.
        
            - **data** *(bytes) --* 
        
              The content of the attachment file.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'attachmentSetId\': \'string\',
                \'expiryTime\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The ID and expiry time of the attachment set returned by the  AddAttachmentsToSet operation.
        
            - **attachmentSetId** *(string) --* 
        
              The ID of the attachment set. If an ``attachmentSetId`` was not specified, a new attachment set is created, and the ID of the set is returned in the response. If an ``attachmentSetId`` was specified, the attachments are added to the specified set, if it exists.
        
            - **expiryTime** *(string) --* 
        
              The time and date when the attachment set expires.
        
        """
        pass

    def add_communication_to_case(self, communicationBody: str, caseId: str = None, ccEmailAddresses: List = None, attachmentSetId: str = None) -> Dict:
        """
        
        The response indicates the success or failure of the request.
        
        This operation implements a subset of the features of the AWS Support Center.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/AddCommunicationToCase>`_
        
        **Request Syntax** 
        ::
        
          response = client.add_communication_to_case(
              caseId=\'string\',
              communicationBody=\'string\',
              ccEmailAddresses=[
                  \'string\',
              ],
              attachmentSetId=\'string\'
          )
        :type caseId: string
        :param caseId: 
        
          The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-*12345678910-2013-c4c1d2bf33c5cf47*  
        
        :type communicationBody: string
        :param communicationBody: **[REQUIRED]** 
        
          The body of an email communication to add to the support case.
        
        :type ccEmailAddresses: list
        :param ccEmailAddresses: 
        
          The email addresses in the CC line of an email to be added to the support case.
        
          - *(string) --* 
        
        :type attachmentSetId: string
        :param attachmentSetId: 
        
          The ID of a set of one or more attachments for the communication to add to the case. Create the set by calling  AddAttachmentsToSet  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'result\': True|False
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The result of the  AddCommunicationToCase operation.
        
            - **result** *(boolean) --* 
        
              True if  AddCommunicationToCase succeeds. Otherwise, returns an error.
        
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

    def create_case(self, subject: str, communicationBody: str, serviceCode: str = None, severityCode: str = None, categoryCode: str = None, ccEmailAddresses: List = None, language: str = None, issueType: str = None, attachmentSetId: str = None) -> Dict:
        """
        
        * **issueType.** The type of issue for the case. You can specify either \"customer-service\" or \"technical.\" If you do not indicate a value, the default is \"technical.\"  
         
        * **serviceCode.** The code for an AWS service. You obtain the ``serviceCode`` by calling  DescribeServices .  
         
        * **categoryCode.** The category for the service defined for the ``serviceCode`` value. You also obtain the category code for a service by calling  DescribeServices . Each AWS service defines its own set of category codes.  
         
        * **severityCode.** A value that indicates the urgency of the case, which in turn determines the response time according to your service level agreement with AWS Support. You obtain the SeverityCode by calling  DescribeSeverityLevels . 
         
        * **subject.** The **Subject** field on the AWS Support Center `Create Case <https://console.aws.amazon.com/support/home#/case/create>`__ page. 
         
        * **communicationBody.** The **Description** field on the AWS Support Center `Create Case <https://console.aws.amazon.com/support/home#/case/create>`__ page. 
         
        * **attachmentSetId.** The ID of a set of attachments that has been created by using  AddAttachmentsToSet . 
         
        * **language.** The human language in which AWS Support handles the case. English and Japanese are currently supported. 
         
        * **ccEmailAddresses.** The AWS Support Center **CC** field on the `Create Case <https://console.aws.amazon.com/support/home#/case/create>`__ page. You can list email addresses to be copied on any correspondence about the case. The account that opens the case is already identified by passing the AWS Credentials in the HTTP POST method or in a method or function call from one of the programming languages supported by an `AWS SDK <http://aws.amazon.com/tools/>`__ .  
         
        .. note::
        
          To add additional communication or attachments to an existing case, use  AddCommunicationToCase .
        
        A successful  CreateCase request returns an AWS Support case number. Case numbers are used by the  DescribeCases operation to retrieve existing AWS Support cases. 
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/CreateCase>`_
        
        **Request Syntax** 
        ::
        
          response = client.create_case(
              subject=\'string\',
              serviceCode=\'string\',
              severityCode=\'string\',
              categoryCode=\'string\',
              communicationBody=\'string\',
              ccEmailAddresses=[
                  \'string\',
              ],
              language=\'string\',
              issueType=\'string\',
              attachmentSetId=\'string\'
          )
        :type subject: string
        :param subject: **[REQUIRED]** 
        
          The title of the AWS Support case.
        
        :type serviceCode: string
        :param serviceCode: 
        
          The code for the AWS service returned by the call to  DescribeServices .
        
        :type severityCode: string
        :param severityCode: 
        
          The code for the severity level returned by the call to  DescribeSeverityLevels .
        
          .. note::
        
            The availability of severity levels depends on each customer\'s support subscription. In other words, your subscription may not necessarily require the urgent level of response time.
        
        :type categoryCode: string
        :param categoryCode: 
        
          The category of problem for the AWS Support case.
        
        :type communicationBody: string
        :param communicationBody: **[REQUIRED]** 
        
          The communication body text when you create an AWS Support case by calling  CreateCase .
        
        :type ccEmailAddresses: list
        :param ccEmailAddresses: 
        
          A list of email addresses that AWS Support copies on case correspondence.
        
          - *(string) --* 
        
        :type language: string
        :param language: 
        
          The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English (\"en\") and Japanese (\"ja\"). Language parameters must be passed explicitly for operations that take them.
        
        :type issueType: string
        :param issueType: 
        
          The type of issue for the case. You can specify either \"customer-service\" or \"technical.\" If you do not indicate a value, the default is \"technical.\"
        
        :type attachmentSetId: string
        :param attachmentSetId: 
        
          The ID of a set of one or more attachments for the case. Create the set by using  AddAttachmentsToSet .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'caseId\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The AWS Support case ID returned by a successful completion of the  CreateCase operation. 
        
            - **caseId** *(string) --* 
        
              The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-*12345678910-2013-c4c1d2bf33c5cf47*  
        
        """
        pass

    def describe_attachment(self, attachmentId: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/DescribeAttachment>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_attachment(
              attachmentId=\'string\'
          )
        :type attachmentId: string
        :param attachmentId: **[REQUIRED]** 
        
          The ID of the attachment to return. Attachment IDs are returned by the  DescribeCommunications operation.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'attachment\': {
                    \'fileName\': \'string\',
                    \'data\': b\'bytes\'
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The content and file name of the attachment returned by the  DescribeAttachment operation.
        
            - **attachment** *(dict) --* 
        
              The attachment content and file name.
        
              - **fileName** *(string) --* 
        
                The name of the attachment file.
        
              - **data** *(bytes) --* 
        
                The content of the attachment file.
        
        """
        pass

    def describe_cases(self, caseIdList: List = None, displayId: str = None, afterTime: str = None, beforeTime: str = None, includeResolvedCases: bool = None, nextToken: str = None, maxResults: int = None, language: str = None, includeCommunications: bool = None) -> Dict:
        """
        
        Case data is available for 12 months after creation. If a case was created more than 12 months ago, a request for data might cause an error.
        
        The response returns the following in JSON format:
        
        * One or more  CaseDetails data types.  
         
        * One or more ``nextToken`` values, which specify where to paginate the returned records represented by the ``CaseDetails`` objects. 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/DescribeCases>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_cases(
              caseIdList=[
                  \'string\',
              ],
              displayId=\'string\',
              afterTime=\'string\',
              beforeTime=\'string\',
              includeResolvedCases=True|False,
              nextToken=\'string\',
              maxResults=123,
              language=\'string\',
              includeCommunications=True|False
          )
        :type caseIdList: list
        :param caseIdList: 
        
          A list of ID numbers of the support cases you want returned. The maximum number of cases is 100.
        
          - *(string) --* 
        
        :type displayId: string
        :param displayId: 
        
          The ID displayed for a case in the AWS Support Center user interface.
        
        :type afterTime: string
        :param afterTime: 
        
          The start date for a filtered date search on support case communications. Case communications are available for 12 months after creation.
        
        :type beforeTime: string
        :param beforeTime: 
        
          The end date for a filtered date search on support case communications. Case communications are available for 12 months after creation.
        
        :type includeResolvedCases: boolean
        :param includeResolvedCases: 
        
          Specifies whether resolved support cases should be included in the  DescribeCases results. The default is *false* .
        
        :type nextToken: string
        :param nextToken: 
        
          A resumption point for pagination.
        
        :type maxResults: integer
        :param maxResults: 
        
          The maximum number of results to return before paginating.
        
        :type language: string
        :param language: 
        
          The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English (\"en\") and Japanese (\"ja\"). Language parameters must be passed explicitly for operations that take them.
        
        :type includeCommunications: boolean
        :param includeCommunications: 
        
          Specifies whether communications should be included in the  DescribeCases results. The default is *true* .
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'cases\': [
                    {
                        \'caseId\': \'string\',
                        \'displayId\': \'string\',
                        \'subject\': \'string\',
                        \'status\': \'string\',
                        \'serviceCode\': \'string\',
                        \'categoryCode\': \'string\',
                        \'severityCode\': \'string\',
                        \'submittedBy\': \'string\',
                        \'timeCreated\': \'string\',
                        \'recentCommunications\': {
                            \'communications\': [
                                {
                                    \'caseId\': \'string\',
                                    \'body\': \'string\',
                                    \'submittedBy\': \'string\',
                                    \'timeCreated\': \'string\',
                                    \'attachmentSet\': [
                                        {
                                            \'attachmentId\': \'string\',
                                            \'fileName\': \'string\'
                                        },
                                    ]
                                },
                            ],
                            \'nextToken\': \'string\'
                        },
                        \'ccEmailAddresses\': [
                            \'string\',
                        ],
                        \'language\': \'string\'
                    },
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Returns an array of  CaseDetails objects and a ``nextToken`` that defines a point for pagination in the result set.
        
            - **cases** *(list) --* 
        
              The details for the cases that match the request.
        
              - *(dict) --* 
        
                A JSON-formatted object that contains the metadata for a support case. It is contained the response from a  DescribeCases request. **CaseDetails** contains the following fields:
        
                * **caseId.** The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-*12345678910-2013-c4c1d2bf33c5cf47* . 
                 
                * **categoryCode.** The category of problem for the AWS Support case. Corresponds to the CategoryCode values returned by a call to  DescribeServices . 
                 
                * **displayId.** The identifier for the case on pages in the AWS Support Center. 
                 
                * **language.** The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English (\"en\") and Japanese (\"ja\"). Language parameters must be passed explicitly for operations that take them. 
                 
                * **recentCommunications.** One or more  Communication objects. Fields of these objects are ``attachments`` , ``body`` , ``caseId`` , ``submittedBy`` , and ``timeCreated`` . 
                 
                * **nextToken.** A resumption point for pagination. 
                 
                * **serviceCode.** The identifier for the AWS service that corresponds to the service code defined in the call to  DescribeServices . 
                 
                * **severityCode.** The severity code assigned to the case. Contains one of the values returned by the call to  DescribeSeverityLevels . 
                 
                * **status.** The status of the case in the AWS Support Center. 
                 
                * **subject.** The subject line of the case. 
                 
                * **submittedBy.** The email address of the account that submitted the case. 
                 
                * **timeCreated.** The time the case was created, in ISO-8601 format. 
                 
                - **caseId** *(string) --* 
        
                  The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-*12345678910-2013-c4c1d2bf33c5cf47*  
        
                - **displayId** *(string) --* 
        
                  The ID displayed for the case in the AWS Support Center. This is a numeric string.
        
                - **subject** *(string) --* 
        
                  The subject line for the case in the AWS Support Center.
        
                - **status** *(string) --* 
        
                  The status of the case.
        
                - **serviceCode** *(string) --* 
        
                  The code for the AWS service returned by the call to  DescribeServices .
        
                - **categoryCode** *(string) --* 
        
                  The category of problem for the AWS Support case.
        
                - **severityCode** *(string) --* 
        
                  The code for the severity level returned by the call to  DescribeSeverityLevels .
        
                - **submittedBy** *(string) --* 
        
                  The email address of the account that submitted the case.
        
                - **timeCreated** *(string) --* 
        
                  The time that the case was case created in the AWS Support Center.
        
                - **recentCommunications** *(dict) --* 
        
                  The five most recent communications between you and AWS Support Center, including the IDs of any attachments to the communications. Also includes a ``nextToken`` that you can use to retrieve earlier communications.
        
                  - **communications** *(list) --* 
        
                    The five most recent communications associated with the case.
        
                    - *(dict) --* 
        
                      A communication associated with an AWS Support case. The communication consists of the case ID, the message body, attachment information, the account email address, and the date and time of the communication.
        
                      - **caseId** *(string) --* 
        
                        The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-*12345678910-2013-c4c1d2bf33c5cf47*  
        
                      - **body** *(string) --* 
        
                        The text of the communication between the customer and AWS Support.
        
                      - **submittedBy** *(string) --* 
        
                        The email address of the account that submitted the AWS Support case.
        
                      - **timeCreated** *(string) --* 
        
                        The time the communication was created.
        
                      - **attachmentSet** *(list) --* 
        
                        Information about the attachments to the case communication.
        
                        - *(dict) --* 
        
                          The file name and ID of an attachment to a case communication. You can use the ID to retrieve the attachment with the  DescribeAttachment operation.
        
                          - **attachmentId** *(string) --* 
        
                            The ID of the attachment.
        
                          - **fileName** *(string) --* 
        
                            The file name of the attachment.
        
                  - **nextToken** *(string) --* 
        
                    A resumption point for pagination.
        
                - **ccEmailAddresses** *(list) --* 
        
                  The email addresses that receive copies of communication about the case.
        
                  - *(string) --* 
              
                - **language** *(string) --* 
        
                  The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English (\"en\") and Japanese (\"ja\"). Language parameters must be passed explicitly for operations that take them.
        
            - **nextToken** *(string) --* 
        
              A resumption point for pagination.
        
        """
        pass

    def describe_communications(self, caseId: str, beforeTime: str = None, afterTime: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        
        Case data is available for 12 months after creation. If a case was created more than 12 months ago, a request for data might cause an error.
        
        You can use the ``maxResults`` and ``nextToken`` parameters to control the pagination of the result set. Set ``maxResults`` to the number of cases you want displayed on each page, and use ``nextToken`` to specify the resumption of pagination.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/DescribeCommunications>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_communications(
              caseId=\'string\',
              beforeTime=\'string\',
              afterTime=\'string\',
              nextToken=\'string\',
              maxResults=123
          )
        :type caseId: string
        :param caseId: **[REQUIRED]** 
        
          The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-*12345678910-2013-c4c1d2bf33c5cf47*  
        
        :type beforeTime: string
        :param beforeTime: 
        
          The end date for a filtered date search on support case communications. Case communications are available for 12 months after creation.
        
        :type afterTime: string
        :param afterTime: 
        
          The start date for a filtered date search on support case communications. Case communications are available for 12 months after creation.
        
        :type nextToken: string
        :param nextToken: 
        
          A resumption point for pagination.
        
        :type maxResults: integer
        :param maxResults: 
        
          The maximum number of results to return before paginating.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'communications\': [
                    {
                        \'caseId\': \'string\',
                        \'body\': \'string\',
                        \'submittedBy\': \'string\',
                        \'timeCreated\': \'string\',
                        \'attachmentSet\': [
                            {
                                \'attachmentId\': \'string\',
                                \'fileName\': \'string\'
                            },
                        ]
                    },
                ],
                \'nextToken\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The communications returned by the  DescribeCommunications operation.
        
            - **communications** *(list) --* 
        
              The communications for the case.
        
              - *(dict) --* 
        
                A communication associated with an AWS Support case. The communication consists of the case ID, the message body, attachment information, the account email address, and the date and time of the communication.
        
                - **caseId** *(string) --* 
        
                  The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-*12345678910-2013-c4c1d2bf33c5cf47*  
        
                - **body** *(string) --* 
        
                  The text of the communication between the customer and AWS Support.
        
                - **submittedBy** *(string) --* 
        
                  The email address of the account that submitted the AWS Support case.
        
                - **timeCreated** *(string) --* 
        
                  The time the communication was created.
        
                - **attachmentSet** *(list) --* 
        
                  Information about the attachments to the case communication.
        
                  - *(dict) --* 
        
                    The file name and ID of an attachment to a case communication. You can use the ID to retrieve the attachment with the  DescribeAttachment operation.
        
                    - **attachmentId** *(string) --* 
        
                      The ID of the attachment.
        
                    - **fileName** *(string) --* 
        
                      The file name of the attachment.
        
            - **nextToken** *(string) --* 
        
              A resumption point for pagination.
        
        """
        pass

    def describe_services(self, serviceCodeList: List = None, language: str = None) -> Dict:
        """
        
        The service codes and category codes correspond to the values that are displayed in the **Service** and **Category** drop-down lists on the AWS Support Center `Create Case <https://console.aws.amazon.com/support/home#/case/create>`__ page. The values in those fields, however, do not necessarily match the service codes and categories returned by the ``DescribeServices`` request. Always use the service codes and categories obtained programmatically. This practice ensures that you always have the most recent set of service and category codes.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/DescribeServices>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_services(
              serviceCodeList=[
                  \'string\',
              ],
              language=\'string\'
          )
        :type serviceCodeList: list
        :param serviceCodeList: 
        
          A JSON-formatted list of service codes available for AWS services.
        
          - *(string) --* 
        
        :type language: string
        :param language: 
        
          The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English (\"en\") and Japanese (\"ja\"). Language parameters must be passed explicitly for operations that take them.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'services\': [
                    {
                        \'code\': \'string\',
                        \'name\': \'string\',
                        \'categories\': [
                            {
                                \'code\': \'string\',
                                \'name\': \'string\'
                            },
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The list of AWS services returned by the  DescribeServices operation.
        
            - **services** *(list) --* 
        
              A JSON-formatted list of AWS services.
        
              - *(dict) --* 
        
                Information about an AWS service returned by the  DescribeServices operation. 
        
                - **code** *(string) --* 
        
                  The code for an AWS service returned by the  DescribeServices response. The ``name`` element contains the corresponding friendly name.
        
                - **name** *(string) --* 
        
                  The friendly name for an AWS service. The ``code`` element contains the corresponding code.
        
                - **categories** *(list) --* 
        
                  A list of categories that describe the type of support issue a case describes. Categories consist of a category name and a category code. Category names and codes are passed to AWS Support when you call  CreateCase .
        
                  - *(dict) --* 
        
                    A JSON-formatted name/value pair that represents the category name and category code of the problem, selected from the  DescribeServices response for each AWS service.
        
                    - **code** *(string) --* 
        
                      The category code for the support case.
        
                    - **name** *(string) --* 
        
                      The category name for the support case.
        
        """
        pass

    def describe_severity_levels(self, language: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/DescribeSeverityLevels>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_severity_levels(
              language=\'string\'
          )
        :type language: string
        :param language: 
        
          The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English (\"en\") and Japanese (\"ja\"). Language parameters must be passed explicitly for operations that take them.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'severityLevels\': [
                    {
                        \'code\': \'string\',
                        \'name\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The list of severity levels returned by the  DescribeSeverityLevels operation.
        
            - **severityLevels** *(list) --* 
        
              The available severity levels for the support case. Available severity levels are defined by your service level agreement with AWS.
        
              - *(dict) --* 
        
                A code and name pair that represent a severity level that can be applied to a support case.
        
                - **code** *(string) --* 
        
                  One of four values: \"low,\" \"medium,\" \"high,\" and \"urgent\". These values correspond to response times returned to the caller in ``severityLevel.name`` . 
        
                - **name** *(string) --* 
        
                  The name of the severity level that corresponds to the severity level code.
        
        """
        pass

    def describe_trusted_advisor_check_refresh_statuses(self, checkIds: List) -> Dict:
        """
        
        .. note::
        
          Some checks are refreshed automatically, and their refresh statuses cannot be retrieved by using this operation. Use of the ``DescribeTrustedAdvisorCheckRefreshStatuses`` operation for these checks causes an ``InvalidParameterValue`` error.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/DescribeTrustedAdvisorCheckRefreshStatuses>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_trusted_advisor_check_refresh_statuses(
              checkIds=[
                  \'string\',
              ]
          )
        :type checkIds: list
        :param checkIds: **[REQUIRED]** 
        
          The IDs of the Trusted Advisor checks to get the status of. **Note:** Specifying the check ID of a check that is automatically refreshed causes an ``InvalidParameterValue`` error.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'statuses\': [
                    {
                        \'checkId\': \'string\',
                        \'status\': \'string\',
                        \'millisUntilNextRefreshable\': 123
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The statuses of the Trusted Advisor checks returned by the  DescribeTrustedAdvisorCheckRefreshStatuses operation.
        
            - **statuses** *(list) --* 
        
              The refresh status of the specified Trusted Advisor checks.
        
              - *(dict) --* 
        
                The refresh status of a Trusted Advisor check.
        
                - **checkId** *(string) --* 
        
                  The unique identifier for the Trusted Advisor check.
        
                - **status** *(string) --* 
        
                  The status of the Trusted Advisor check for which a refresh has been requested: \"none\", \"enqueued\", \"processing\", \"success\", or \"abandoned\".
        
                - **millisUntilNextRefreshable** *(integer) --* 
        
                  The amount of time, in milliseconds, until the Trusted Advisor check is eligible for refresh.
        
        """
        pass

    def describe_trusted_advisor_check_result(self, checkId: str, language: str = None) -> Dict:
        """
        
        The response contains a  TrustedAdvisorCheckResult object, which contains these three objects:
        
        *  TrustedAdvisorCategorySpecificSummary   
         
        *  TrustedAdvisorResourceDetail   
         
        *  TrustedAdvisorResourcesSummary   
         
        In addition, the response contains these fields:
        
        * **status.** The alert status of the check: \"ok\" (green), \"warning\" (yellow), \"error\" (red), or \"not_available\". 
         
        * **timestamp.** The time of the last refresh of the check. 
         
        * **checkId.** The unique identifier for the check. 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/DescribeTrustedAdvisorCheckResult>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_trusted_advisor_check_result(
              checkId=\'string\',
              language=\'string\'
          )
        :type checkId: string
        :param checkId: **[REQUIRED]** 
        
          The unique identifier for the Trusted Advisor check.
        
        :type language: string
        :param language: 
        
          The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English (\"en\") and Japanese (\"ja\"). Language parameters must be passed explicitly for operations that take them.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'result\': {
                    \'checkId\': \'string\',
                    \'timestamp\': \'string\',
                    \'status\': \'string\',
                    \'resourcesSummary\': {
                        \'resourcesProcessed\': 123,
                        \'resourcesFlagged\': 123,
                        \'resourcesIgnored\': 123,
                        \'resourcesSuppressed\': 123
                    },
                    \'categorySpecificSummary\': {
                        \'costOptimizing\': {
                            \'estimatedMonthlySavings\': 123.0,
                            \'estimatedPercentMonthlySavings\': 123.0
                        }
                    },
                    \'flaggedResources\': [
                        {
                            \'status\': \'string\',
                            \'region\': \'string\',
                            \'resourceId\': \'string\',
                            \'isSuppressed\': True|False,
                            \'metadata\': [
                                \'string\',
                            ]
                        },
                    ]
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The result of the Trusted Advisor check returned by the  DescribeTrustedAdvisorCheckResult operation.
        
            - **result** *(dict) --* 
        
              The detailed results of the Trusted Advisor check.
        
              - **checkId** *(string) --* 
        
                The unique identifier for the Trusted Advisor check.
        
              - **timestamp** *(string) --* 
        
                The time of the last refresh of the check.
        
              - **status** *(string) --* 
        
                The alert status of the check: \"ok\" (green), \"warning\" (yellow), \"error\" (red), or \"not_available\".
        
              - **resourcesSummary** *(dict) --* 
        
                Details about AWS resources that were analyzed in a call to Trusted Advisor  DescribeTrustedAdvisorCheckSummaries . 
        
                - **resourcesProcessed** *(integer) --* 
        
                  The number of AWS resources that were analyzed by the Trusted Advisor check.
        
                - **resourcesFlagged** *(integer) --* 
        
                  The number of AWS resources that were flagged (listed) by the Trusted Advisor check.
        
                - **resourcesIgnored** *(integer) --* 
        
                  The number of AWS resources ignored by Trusted Advisor because information was unavailable.
        
                - **resourcesSuppressed** *(integer) --* 
        
                  The number of AWS resources ignored by Trusted Advisor because they were marked as suppressed by the user.
        
              - **categorySpecificSummary** *(dict) --* 
        
                Summary information that relates to the category of the check. Cost Optimizing is the only category that is currently supported.
        
                - **costOptimizing** *(dict) --* 
        
                  The summary information about cost savings for a Trusted Advisor check that is in the Cost Optimizing category.
        
                  - **estimatedMonthlySavings** *(float) --* 
        
                    The estimated monthly savings that might be realized if the recommended actions are taken.
        
                  - **estimatedPercentMonthlySavings** *(float) --* 
        
                    The estimated percentage of savings that might be realized if the recommended actions are taken.
        
              - **flaggedResources** *(list) --* 
        
                The details about each resource listed in the check result.
        
                - *(dict) --* 
        
                  Contains information about a resource identified by a Trusted Advisor check.
        
                  - **status** *(string) --* 
        
                    The status code for the resource identified in the Trusted Advisor check.
        
                  - **region** *(string) --* 
        
                    The AWS region in which the identified resource is located.
        
                  - **resourceId** *(string) --* 
        
                    The unique identifier for the identified resource.
        
                  - **isSuppressed** *(boolean) --* 
        
                    Specifies whether the AWS resource was ignored by Trusted Advisor because it was marked as suppressed by the user.
        
                  - **metadata** *(list) --* 
        
                    Additional information about the identified resource. The exact metadata and its order can be obtained by inspecting the  TrustedAdvisorCheckDescription object returned by the call to  DescribeTrustedAdvisorChecks . **Metadata** contains all the data that is shown in the Excel download, even in those cases where the UI shows just summary data. 
        
                    - *(string) --* 
                
        """
        pass

    def describe_trusted_advisor_check_summaries(self, checkIds: List) -> Dict:
        """
        
        The response contains an array of  TrustedAdvisorCheckSummary objects.
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/DescribeTrustedAdvisorCheckSummaries>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_trusted_advisor_check_summaries(
              checkIds=[
                  \'string\',
              ]
          )
        :type checkIds: list
        :param checkIds: **[REQUIRED]** 
        
          The IDs of the Trusted Advisor checks.
        
          - *(string) --* 
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'summaries\': [
                    {
                        \'checkId\': \'string\',
                        \'timestamp\': \'string\',
                        \'status\': \'string\',
                        \'hasFlaggedResources\': True|False,
                        \'resourcesSummary\': {
                            \'resourcesProcessed\': 123,
                            \'resourcesFlagged\': 123,
                            \'resourcesIgnored\': 123,
                            \'resourcesSuppressed\': 123
                        },
                        \'categorySpecificSummary\': {
                            \'costOptimizing\': {
                                \'estimatedMonthlySavings\': 123.0,
                                \'estimatedPercentMonthlySavings\': 123.0
                            }
                        }
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The summaries of the Trusted Advisor checks returned by the  DescribeTrustedAdvisorCheckSummaries operation.
        
            - **summaries** *(list) --* 
        
              The summary information for the requested Trusted Advisor checks.
        
              - *(dict) --* 
        
                A summary of a Trusted Advisor check result, including the alert status, last refresh, and number of resources examined.
        
                - **checkId** *(string) --* 
        
                  The unique identifier for the Trusted Advisor check.
        
                - **timestamp** *(string) --* 
        
                  The time of the last refresh of the check.
        
                - **status** *(string) --* 
        
                  The alert status of the check: \"ok\" (green), \"warning\" (yellow), \"error\" (red), or \"not_available\".
        
                - **hasFlaggedResources** *(boolean) --* 
        
                  Specifies whether the Trusted Advisor check has flagged resources.
        
                - **resourcesSummary** *(dict) --* 
        
                  Details about AWS resources that were analyzed in a call to Trusted Advisor  DescribeTrustedAdvisorCheckSummaries . 
        
                  - **resourcesProcessed** *(integer) --* 
        
                    The number of AWS resources that were analyzed by the Trusted Advisor check.
        
                  - **resourcesFlagged** *(integer) --* 
        
                    The number of AWS resources that were flagged (listed) by the Trusted Advisor check.
        
                  - **resourcesIgnored** *(integer) --* 
        
                    The number of AWS resources ignored by Trusted Advisor because information was unavailable.
        
                  - **resourcesSuppressed** *(integer) --* 
        
                    The number of AWS resources ignored by Trusted Advisor because they were marked as suppressed by the user.
        
                - **categorySpecificSummary** *(dict) --* 
        
                  Summary information that relates to the category of the check. Cost Optimizing is the only category that is currently supported.
        
                  - **costOptimizing** *(dict) --* 
        
                    The summary information about cost savings for a Trusted Advisor check that is in the Cost Optimizing category.
        
                    - **estimatedMonthlySavings** *(float) --* 
        
                      The estimated monthly savings that might be realized if the recommended actions are taken.
        
                    - **estimatedPercentMonthlySavings** *(float) --* 
        
                      The estimated percentage of savings that might be realized if the recommended actions are taken.
        
        """
        pass

    def describe_trusted_advisor_checks(self, language: str) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/DescribeTrustedAdvisorChecks>`_
        
        **Request Syntax** 
        ::
        
          response = client.describe_trusted_advisor_checks(
              language=\'string\'
          )
        :type language: string
        :param language: **[REQUIRED]** 
        
          The ISO 639-1 code for the language in which AWS provides support. AWS Support currently supports English (\"en\") and Japanese (\"ja\"). Language parameters must be passed explicitly for operations that take them.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'checks\': [
                    {
                        \'id\': \'string\',
                        \'name\': \'string\',
                        \'description\': \'string\',
                        \'category\': \'string\',
                        \'metadata\': [
                            \'string\',
                        ]
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            Information about the Trusted Advisor checks returned by the  DescribeTrustedAdvisorChecks operation.
        
            - **checks** *(list) --* 
        
              Information about all available Trusted Advisor checks.
        
              - *(dict) --* 
        
                The description and metadata for a Trusted Advisor check.
        
                - **id** *(string) --* 
        
                  The unique identifier for the Trusted Advisor check.
        
                - **name** *(string) --* 
        
                  The display name for the Trusted Advisor check.
        
                - **description** *(string) --* 
        
                  The description of the Trusted Advisor check, which includes the alert criteria and recommended actions (contains HTML markup).
        
                - **category** *(string) --* 
        
                  The category of the Trusted Advisor check.
        
                - **metadata** *(list) --* 
        
                  The column headings for the data returned by the Trusted Advisor check. The order of the headings corresponds to the order of the data in the **Metadata** element of the  TrustedAdvisorResourceDetail for the check. **Metadata** contains all the data that is shown in the Excel download, even in those cases where the UI shows just summary data. 
        
                  - *(string) --* 
              
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

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        """
        
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass

    def refresh_trusted_advisor_check(self, checkId: str) -> Dict:
        """
        
        .. note::
        
          Some checks are refreshed automatically, and they cannot be refreshed by using this operation. Use of the ``RefreshTrustedAdvisorCheck`` operation for these checks causes an ``InvalidParameterValue`` error.
        
        The response contains a  TrustedAdvisorCheckRefreshStatus object, which contains these fields:
        
        * **status.** The refresh status of the check: \"none\", \"enqueued\", \"processing\", \"success\", or \"abandoned\". 
         
        * **millisUntilNextRefreshable.** The amount of time, in milliseconds, until the check is eligible for refresh. 
         
        * **checkId.** The unique identifier for the check. 
         
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/RefreshTrustedAdvisorCheck>`_
        
        **Request Syntax** 
        ::
        
          response = client.refresh_trusted_advisor_check(
              checkId=\'string\'
          )
        :type checkId: string
        :param checkId: **[REQUIRED]** 
        
          The unique identifier for the Trusted Advisor check to refresh. **Note:** Specifying the check ID of a check that is automatically refreshed causes an ``InvalidParameterValue`` error.
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'status\': {
                    \'checkId\': \'string\',
                    \'status\': \'string\',
                    \'millisUntilNextRefreshable\': 123
                }
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The current refresh status of a Trusted Advisor check.
        
            - **status** *(dict) --* 
        
              The current refresh status for a check, including the amount of time until the check is eligible for refresh.
        
              - **checkId** *(string) --* 
        
                The unique identifier for the Trusted Advisor check.
        
              - **status** *(string) --* 
        
                The status of the Trusted Advisor check for which a refresh has been requested: \"none\", \"enqueued\", \"processing\", \"success\", or \"abandoned\".
        
              - **millisUntilNextRefreshable** *(integer) --* 
        
                The amount of time, in milliseconds, until the Trusted Advisor check is eligible for refresh.
        
        """
        pass

    def resolve_case(self, caseId: str = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/ResolveCase>`_
        
        **Request Syntax** 
        ::
        
          response = client.resolve_case(
              caseId=\'string\'
          )
        :type caseId: string
        :param caseId: 
        
          The AWS Support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-*12345678910-2013-c4c1d2bf33c5cf47*  
        
        :rtype: dict
        :returns: 
          
          **Response Syntax** 
        
          ::
        
            {
                \'initialCaseStatus\': \'string\',
                \'finalCaseStatus\': \'string\'
            }
          **Response Structure** 
        
          - *(dict) --* 
        
            The status of the case returned by the  ResolveCase operation.
        
            - **initialCaseStatus** *(string) --* 
        
              The status of the case when the  ResolveCase request was sent.
        
            - **finalCaseStatus** *(string) --* 
        
              The status of the case after the  ResolveCase request was processed.
        
        """
        pass
