from typing import List
from typing import Dict
from botocore.paginate import Paginator


class ListAssignmentsForHIT(Paginator):
    def paginate(self, HITId: str, AssignmentStatuses: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mturk-requester-2017-01-17/ListAssignmentsForHIT>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              HITId=\'string\',
              AssignmentStatuses=[
                  \'Submitted\'|\'Approved\'|\'Rejected\',
              ],
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type HITId: string
        :param HITId: **[REQUIRED]** 
        
          The ID of the HIT.
        
        :type AssignmentStatuses: list
        :param AssignmentStatuses: 
        
          The status of the assignments to return: Submitted | Approved | Rejected
        
          - *(string) --* 
        
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
                \'NumResults\': 123,
                \'Assignments\': [
                    {
                        \'AssignmentId\': \'string\',
                        \'WorkerId\': \'string\',
                        \'HITId\': \'string\',
                        \'AssignmentStatus\': \'Submitted\'|\'Approved\'|\'Rejected\',
                        \'AutoApprovalTime\': datetime(2015, 1, 1),
                        \'AcceptTime\': datetime(2015, 1, 1),
                        \'SubmitTime\': datetime(2015, 1, 1),
                        \'ApprovalTime\': datetime(2015, 1, 1),
                        \'RejectionTime\': datetime(2015, 1, 1),
                        \'Deadline\': datetime(2015, 1, 1),
                        \'Answer\': \'string\',
                        \'RequesterFeedback\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NumResults** *(integer) --* 
        
              The number of assignments on the page in the filtered results list, equivalent to the number of assignments returned by this call.
        
            - **Assignments** *(list) --* 
        
              The collection of Assignment data structures returned by this call.
        
              - *(dict) --* 
        
                The Assignment data structure represents a single assignment of a HIT to a Worker. The assignment tracks the Worker\'s efforts to complete the HIT, and contains the results for later retrieval. 
        
                - **AssignmentId** *(string) --* 
        
                  A unique identifier for the assignment.
        
                - **WorkerId** *(string) --* 
        
                  The ID of the Worker who accepted the HIT.
        
                - **HITId** *(string) --* 
        
                  The ID of the HIT.
        
                - **AssignmentStatus** *(string) --* 
        
                  The status of the assignment.
        
                - **AutoApprovalTime** *(datetime) --* 
        
                  If results have been submitted, AutoApprovalTime is the date and time the results of the assignment results are considered Approved automatically if they have not already been explicitly approved or rejected by the Requester. This value is derived from the auto-approval delay specified by the Requester in the HIT. This value is omitted from the assignment if the Worker has not yet submitted results.
        
                - **AcceptTime** *(datetime) --* 
        
                  The date and time the Worker accepted the assignment.
        
                - **SubmitTime** *(datetime) --* 
        
                  If the Worker has submitted results, SubmitTime is the date and time the assignment was submitted. This value is omitted from the assignment if the Worker has not yet submitted results.
        
                - **ApprovalTime** *(datetime) --* 
        
                  If the Worker has submitted results and the Requester has approved the results, ApprovalTime is the date and time the Requester approved the results. This value is omitted from the assignment if the Requester has not yet approved the results.
        
                - **RejectionTime** *(datetime) --* 
        
                  If the Worker has submitted results and the Requester has rejected the results, RejectionTime is the date and time the Requester rejected the results.
        
                - **Deadline** *(datetime) --* 
        
                  The date and time of the deadline for the assignment. This value is derived from the deadline specification for the HIT and the date and time the Worker accepted the HIT.
        
                - **Answer** *(string) --* 
        
                  The Worker\'s answers submitted for the HIT contained in a QuestionFormAnswers document, if the Worker provides an answer. If the Worker does not provide any answers, Answer may contain a QuestionFormAnswers document, or Answer may be empty.
        
                - **RequesterFeedback** *(string) --* 
        
                  The feedback string included with the call to the ApproveAssignment operation or the RejectAssignment operation, if the Requester approved or rejected the assignment and specified feedback.
        
        """
        pass


class ListBonusPayments(Paginator):
    def paginate(self, HITId: str = None, AssignmentId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mturk-requester-2017-01-17/ListBonusPayments>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              HITId=\'string\',
              AssignmentId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type HITId: string
        :param HITId: 
        
          The ID of the HIT associated with the bonus payments to retrieve. If not specified, all bonus payments for all assignments for the given HIT are returned. Either the HITId parameter or the AssignmentId parameter must be specified
        
        :type AssignmentId: string
        :param AssignmentId: 
        
          The ID of the assignment associated with the bonus payments to retrieve. If specified, only bonus payments for the given assignment are returned. Either the HITId parameter or the AssignmentId parameter must be specified
        
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
                \'NumResults\': 123,
                \'BonusPayments\': [
                    {
                        \'WorkerId\': \'string\',
                        \'BonusAmount\': \'string\',
                        \'AssignmentId\': \'string\',
                        \'Reason\': \'string\',
                        \'GrantTime\': datetime(2015, 1, 1)
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NumResults** *(integer) --* 
        
              The number of bonus payments on this page in the filtered results list, equivalent to the number of bonus payments being returned by this call. 
        
            - **BonusPayments** *(list) --* 
        
              A successful request to the ListBonusPayments operation returns a list of BonusPayment objects. 
        
              - *(dict) --* 
        
                An object representing a Bonus payment paid to a Worker.
        
                - **WorkerId** *(string) --* 
        
                  The ID of the Worker to whom the bonus was paid.
        
                - **BonusAmount** *(string) --* 
        
                  A string representing a currency amount.
        
                - **AssignmentId** *(string) --* 
        
                  The ID of the assignment associated with this bonus payment.
        
                - **Reason** *(string) --* 
        
                  The Reason text given when the bonus was granted, if any.
        
                - **GrantTime** *(datetime) --* 
        
                  The date and time of when the bonus was granted.
        
        """
        pass


class ListHITs(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mturk-requester-2017-01-17/ListHITs>`_
        
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
                \'NumResults\': 123,
                \'HITs\': [
                    {
                        \'HITId\': \'string\',
                        \'HITTypeId\': \'string\',
                        \'HITGroupId\': \'string\',
                        \'HITLayoutId\': \'string\',
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'Title\': \'string\',
                        \'Description\': \'string\',
                        \'Question\': \'string\',
                        \'Keywords\': \'string\',
                        \'HITStatus\': \'Assignable\'|\'Unassignable\'|\'Reviewable\'|\'Reviewing\'|\'Disposed\',
                        \'MaxAssignments\': 123,
                        \'Reward\': \'string\',
                        \'AutoApprovalDelayInSeconds\': 123,
                        \'Expiration\': datetime(2015, 1, 1),
                        \'AssignmentDurationInSeconds\': 123,
                        \'RequesterAnnotation\': \'string\',
                        \'QualificationRequirements\': [
                            {
                                \'QualificationTypeId\': \'string\',
                                \'Comparator\': \'LessThan\'|\'LessThanOrEqualTo\'|\'GreaterThan\'|\'GreaterThanOrEqualTo\'|\'EqualTo\'|\'NotEqualTo\'|\'Exists\'|\'DoesNotExist\'|\'In\'|\'NotIn\',
                                \'IntegerValues\': [
                                    123,
                                ],
                                \'LocaleValues\': [
                                    {
                                        \'Country\': \'string\',
                                        \'Subdivision\': \'string\'
                                    },
                                ],
                                \'RequiredToPreview\': True|False,
                                \'ActionsGuarded\': \'Accept\'|\'PreviewAndAccept\'|\'DiscoverPreviewAndAccept\'
                            },
                        ],
                        \'HITReviewStatus\': \'NotReviewed\'|\'MarkedForReview\'|\'ReviewedAppropriate\'|\'ReviewedInappropriate\',
                        \'NumberOfAssignmentsPending\': 123,
                        \'NumberOfAssignmentsAvailable\': 123,
                        \'NumberOfAssignmentsCompleted\': 123
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NumResults** *(integer) --* 
        
              The number of HITs on this page in the filtered results list, equivalent to the number of HITs being returned by this call.
        
            - **HITs** *(list) --* 
        
              The list of HIT elements returned by the query.
        
              - *(dict) --* 
        
                The HIT data structure represents a single HIT, including all the information necessary for a Worker to accept and complete the HIT.
        
                - **HITId** *(string) --* 
        
                  A unique identifier for the HIT.
        
                - **HITTypeId** *(string) --* 
        
                  The ID of the HIT type of this HIT
        
                - **HITGroupId** *(string) --* 
        
                  The ID of the HIT Group of this HIT.
        
                - **HITLayoutId** *(string) --* 
        
                  The ID of the HIT Layout of this HIT.
        
                - **CreationTime** *(datetime) --* 
        
                  The date and time the HIT was created.
        
                - **Title** *(string) --* 
        
                  The title of the HIT.
        
                - **Description** *(string) --* 
        
                  A general description of the HIT.
        
                - **Question** *(string) --* 
        
                  The data the Worker completing the HIT uses produce the results. This is either either a QuestionForm, HTMLQuestion or an ExternalQuestion data structure.
        
                - **Keywords** *(string) --* 
        
                  One or more words or phrases that describe the HIT, separated by commas. Search terms similar to the keywords of a HIT are more likely to have the HIT in the search results.
        
                - **HITStatus** *(string) --* 
        
                  The status of the HIT and its assignments. Valid Values are Assignable | Unassignable | Reviewable | Reviewing | Disposed. 
        
                - **MaxAssignments** *(integer) --* 
        
                  The number of times the HIT can be accepted and completed before the HIT becomes unavailable. 
        
                - **Reward** *(string) --* 
        
                  A string representing a currency amount.
        
                - **AutoApprovalDelayInSeconds** *(integer) --* 
        
                  The amount of time, in seconds, after the Worker submits an assignment for the HIT that the results are automatically approved by Amazon Mechanical Turk. This is the amount of time the Requester has to reject an assignment submitted by a Worker before the assignment is auto-approved and the Worker is paid. 
        
                - **Expiration** *(datetime) --* 
        
                  The date and time the HIT expires.
        
                - **AssignmentDurationInSeconds** *(integer) --* 
        
                  The length of time, in seconds, that a Worker has to complete the HIT after accepting it.
        
                - **RequesterAnnotation** *(string) --* 
        
                  An arbitrary data field the Requester who created the HIT can use. This field is visible only to the creator of the HIT.
        
                - **QualificationRequirements** *(list) --* 
        
                  Conditions that a Worker\'s Qualifications must meet in order to accept the HIT. A HIT can have between zero and ten Qualification requirements. All requirements must be met in order for a Worker to accept the HIT. Additionally, other actions can be restricted using the ``ActionsGuarded`` field on each ``QualificationRequirement`` structure. 
        
                  - *(dict) --* 
        
                    The QualificationRequirement data structure describes a Qualification that a Worker must have before the Worker is allowed to accept a HIT. A requirement may optionally state that a Worker must have the Qualification in order to preview the HIT, or see the HIT in search results. 
        
                    - **QualificationTypeId** *(string) --* 
        
                      The ID of the Qualification type for the requirement.
        
                    - **Comparator** *(string) --* 
        
                      The kind of comparison to make against a Qualification\'s value. You can compare a Qualification\'s value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo, GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue values. Lastly, a Qualification requirement can also test if a Qualification Exists or DoesNotExist in the user\'s profile, regardless of its value. 
        
                    - **IntegerValues** *(list) --* 
        
                      The integer value to compare against the Qualification\'s value. IntegerValue must not be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if the Qualification type has an integer value; it cannot be used with the Worker_Locale QualificationType ID. When performing a set comparison by using the In or the NotIn comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement data structure. 
        
                      - *(integer) --* 
                  
                    - **LocaleValues** *(list) --* 
        
                      The locale value to compare against the Qualification\'s value. The local value must be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a set comparison by using the In or the NotIn comparator, you can use up to 30 LocaleValue elements in a QualificationRequirement data structure. 
        
                      - *(dict) --* 
        
                        The Locale data structure represents a geographical region or location.
        
                        - **Country** *(string) --* 
        
                          The country of the locale. Must be a valid ISO 3166 country code. For example, the code US refers to the United States of America. 
        
                        - **Subdivision** *(string) --* 
        
                          The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For example, the code WA refers to the state of Washington.
        
                    - **RequiredToPreview** *(boolean) --* 
        
                      DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true, the question data for the HIT will not be shown when a Worker whose Qualifications do not meet this requirement tries to preview the HIT. That is, a Worker\'s Qualifications must meet all of the requirements for which RequiredToPreview is true in order to preview the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or if there are no such requirements), but does not meet all of the requirements for the HIT, the Worker will be allowed to preview the HIT\'s question data, but will not be allowed to accept and complete the HIT. The default is false. This should not be used in combination with the ``ActionsGuarded`` field. 
        
                    - **ActionsGuarded** *(string) --* 
        
                      Setting this attribute prevents Workers whose Qualifications do not meet this QualificationRequirement from taking the specified action. Valid arguments include \"Accept\" (Worker cannot accept the HIT, but can preview the HIT and see it in their search results), \"PreviewAndAccept\" (Worker cannot accept or preview the HIT, but can see the HIT in their search results), and \"DiscoverPreviewAndAccept\" (Worker cannot accept, preview, or see the HIT in their search results). It\'s possible for you to create a HIT with multiple QualificationRequirements (which can have different values for the ActionGuarded attribute). In this case, the Worker is only permitted to perform an action when they have met all QualificationRequirements guarding the action. The actions in the order of least restrictive to most restrictive are Discover, Preview and Accept. For example, if a Worker meets all QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet all requirements that are set with PreviewAndAccept, then the Worker will be able to Discover, i.e. see the HIT in their search result, but will not be able to Preview or Accept the HIT. ActionsGuarded should not be used in combination with the ``RequiredToPreview`` field. 
        
                - **HITReviewStatus** *(string) --* 
        
                  Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview | ReviewedAppropriate | ReviewedInappropriate.
        
                - **NumberOfAssignmentsPending** *(integer) --* 
        
                  The number of assignments for this HIT that are being previewed or have been accepted by Workers, but have not yet been submitted, returned, or abandoned.
        
                - **NumberOfAssignmentsAvailable** *(integer) --* 
        
                  The number of assignments for this HIT that are available for Workers to accept.
        
                - **NumberOfAssignmentsCompleted** *(integer) --* 
        
                  The number of assignments for this HIT that have been approved or rejected.
        
        """
        pass


class ListHITsForQualificationType(Paginator):
    def paginate(self, QualificationTypeId: str, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mturk-requester-2017-01-17/ListHITsForQualificationType>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              QualificationTypeId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type QualificationTypeId: string
        :param QualificationTypeId: **[REQUIRED]** 
        
          The ID of the Qualification type to use when querying HITs. 
        
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
                \'NumResults\': 123,
                \'HITs\': [
                    {
                        \'HITId\': \'string\',
                        \'HITTypeId\': \'string\',
                        \'HITGroupId\': \'string\',
                        \'HITLayoutId\': \'string\',
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'Title\': \'string\',
                        \'Description\': \'string\',
                        \'Question\': \'string\',
                        \'Keywords\': \'string\',
                        \'HITStatus\': \'Assignable\'|\'Unassignable\'|\'Reviewable\'|\'Reviewing\'|\'Disposed\',
                        \'MaxAssignments\': 123,
                        \'Reward\': \'string\',
                        \'AutoApprovalDelayInSeconds\': 123,
                        \'Expiration\': datetime(2015, 1, 1),
                        \'AssignmentDurationInSeconds\': 123,
                        \'RequesterAnnotation\': \'string\',
                        \'QualificationRequirements\': [
                            {
                                \'QualificationTypeId\': \'string\',
                                \'Comparator\': \'LessThan\'|\'LessThanOrEqualTo\'|\'GreaterThan\'|\'GreaterThanOrEqualTo\'|\'EqualTo\'|\'NotEqualTo\'|\'Exists\'|\'DoesNotExist\'|\'In\'|\'NotIn\',
                                \'IntegerValues\': [
                                    123,
                                ],
                                \'LocaleValues\': [
                                    {
                                        \'Country\': \'string\',
                                        \'Subdivision\': \'string\'
                                    },
                                ],
                                \'RequiredToPreview\': True|False,
                                \'ActionsGuarded\': \'Accept\'|\'PreviewAndAccept\'|\'DiscoverPreviewAndAccept\'
                            },
                        ],
                        \'HITReviewStatus\': \'NotReviewed\'|\'MarkedForReview\'|\'ReviewedAppropriate\'|\'ReviewedInappropriate\',
                        \'NumberOfAssignmentsPending\': 123,
                        \'NumberOfAssignmentsAvailable\': 123,
                        \'NumberOfAssignmentsCompleted\': 123
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NumResults** *(integer) --* 
        
              The number of HITs on this page in the filtered results list, equivalent to the number of HITs being returned by this call. 
        
            - **HITs** *(list) --* 
        
              The list of HIT elements returned by the query.
        
              - *(dict) --* 
        
                The HIT data structure represents a single HIT, including all the information necessary for a Worker to accept and complete the HIT.
        
                - **HITId** *(string) --* 
        
                  A unique identifier for the HIT.
        
                - **HITTypeId** *(string) --* 
        
                  The ID of the HIT type of this HIT
        
                - **HITGroupId** *(string) --* 
        
                  The ID of the HIT Group of this HIT.
        
                - **HITLayoutId** *(string) --* 
        
                  The ID of the HIT Layout of this HIT.
        
                - **CreationTime** *(datetime) --* 
        
                  The date and time the HIT was created.
        
                - **Title** *(string) --* 
        
                  The title of the HIT.
        
                - **Description** *(string) --* 
        
                  A general description of the HIT.
        
                - **Question** *(string) --* 
        
                  The data the Worker completing the HIT uses produce the results. This is either either a QuestionForm, HTMLQuestion or an ExternalQuestion data structure.
        
                - **Keywords** *(string) --* 
        
                  One or more words or phrases that describe the HIT, separated by commas. Search terms similar to the keywords of a HIT are more likely to have the HIT in the search results.
        
                - **HITStatus** *(string) --* 
        
                  The status of the HIT and its assignments. Valid Values are Assignable | Unassignable | Reviewable | Reviewing | Disposed. 
        
                - **MaxAssignments** *(integer) --* 
        
                  The number of times the HIT can be accepted and completed before the HIT becomes unavailable. 
        
                - **Reward** *(string) --* 
        
                  A string representing a currency amount.
        
                - **AutoApprovalDelayInSeconds** *(integer) --* 
        
                  The amount of time, in seconds, after the Worker submits an assignment for the HIT that the results are automatically approved by Amazon Mechanical Turk. This is the amount of time the Requester has to reject an assignment submitted by a Worker before the assignment is auto-approved and the Worker is paid. 
        
                - **Expiration** *(datetime) --* 
        
                  The date and time the HIT expires.
        
                - **AssignmentDurationInSeconds** *(integer) --* 
        
                  The length of time, in seconds, that a Worker has to complete the HIT after accepting it.
        
                - **RequesterAnnotation** *(string) --* 
        
                  An arbitrary data field the Requester who created the HIT can use. This field is visible only to the creator of the HIT.
        
                - **QualificationRequirements** *(list) --* 
        
                  Conditions that a Worker\'s Qualifications must meet in order to accept the HIT. A HIT can have between zero and ten Qualification requirements. All requirements must be met in order for a Worker to accept the HIT. Additionally, other actions can be restricted using the ``ActionsGuarded`` field on each ``QualificationRequirement`` structure. 
        
                  - *(dict) --* 
        
                    The QualificationRequirement data structure describes a Qualification that a Worker must have before the Worker is allowed to accept a HIT. A requirement may optionally state that a Worker must have the Qualification in order to preview the HIT, or see the HIT in search results. 
        
                    - **QualificationTypeId** *(string) --* 
        
                      The ID of the Qualification type for the requirement.
        
                    - **Comparator** *(string) --* 
        
                      The kind of comparison to make against a Qualification\'s value. You can compare a Qualification\'s value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo, GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue values. Lastly, a Qualification requirement can also test if a Qualification Exists or DoesNotExist in the user\'s profile, regardless of its value. 
        
                    - **IntegerValues** *(list) --* 
        
                      The integer value to compare against the Qualification\'s value. IntegerValue must not be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if the Qualification type has an integer value; it cannot be used with the Worker_Locale QualificationType ID. When performing a set comparison by using the In or the NotIn comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement data structure. 
        
                      - *(integer) --* 
                  
                    - **LocaleValues** *(list) --* 
        
                      The locale value to compare against the Qualification\'s value. The local value must be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a set comparison by using the In or the NotIn comparator, you can use up to 30 LocaleValue elements in a QualificationRequirement data structure. 
        
                      - *(dict) --* 
        
                        The Locale data structure represents a geographical region or location.
        
                        - **Country** *(string) --* 
        
                          The country of the locale. Must be a valid ISO 3166 country code. For example, the code US refers to the United States of America. 
        
                        - **Subdivision** *(string) --* 
        
                          The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For example, the code WA refers to the state of Washington.
        
                    - **RequiredToPreview** *(boolean) --* 
        
                      DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true, the question data for the HIT will not be shown when a Worker whose Qualifications do not meet this requirement tries to preview the HIT. That is, a Worker\'s Qualifications must meet all of the requirements for which RequiredToPreview is true in order to preview the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or if there are no such requirements), but does not meet all of the requirements for the HIT, the Worker will be allowed to preview the HIT\'s question data, but will not be allowed to accept and complete the HIT. The default is false. This should not be used in combination with the ``ActionsGuarded`` field. 
        
                    - **ActionsGuarded** *(string) --* 
        
                      Setting this attribute prevents Workers whose Qualifications do not meet this QualificationRequirement from taking the specified action. Valid arguments include \"Accept\" (Worker cannot accept the HIT, but can preview the HIT and see it in their search results), \"PreviewAndAccept\" (Worker cannot accept or preview the HIT, but can see the HIT in their search results), and \"DiscoverPreviewAndAccept\" (Worker cannot accept, preview, or see the HIT in their search results). It\'s possible for you to create a HIT with multiple QualificationRequirements (which can have different values for the ActionGuarded attribute). In this case, the Worker is only permitted to perform an action when they have met all QualificationRequirements guarding the action. The actions in the order of least restrictive to most restrictive are Discover, Preview and Accept. For example, if a Worker meets all QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet all requirements that are set with PreviewAndAccept, then the Worker will be able to Discover, i.e. see the HIT in their search result, but will not be able to Preview or Accept the HIT. ActionsGuarded should not be used in combination with the ``RequiredToPreview`` field. 
        
                - **HITReviewStatus** *(string) --* 
        
                  Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview | ReviewedAppropriate | ReviewedInappropriate.
        
                - **NumberOfAssignmentsPending** *(integer) --* 
        
                  The number of assignments for this HIT that are being previewed or have been accepted by Workers, but have not yet been submitted, returned, or abandoned.
        
                - **NumberOfAssignmentsAvailable** *(integer) --* 
        
                  The number of assignments for this HIT that are available for Workers to accept.
        
                - **NumberOfAssignmentsCompleted** *(integer) --* 
        
                  The number of assignments for this HIT that have been approved or rejected.
        
        """
        pass


class ListQualificationRequests(Paginator):
    def paginate(self, QualificationTypeId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mturk-requester-2017-01-17/ListQualificationRequests>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              QualificationTypeId=\'string\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type QualificationTypeId: string
        :param QualificationTypeId: 
        
          The ID of the QualificationType.
        
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
                \'NumResults\': 123,
                \'QualificationRequests\': [
                    {
                        \'QualificationRequestId\': \'string\',
                        \'QualificationTypeId\': \'string\',
                        \'WorkerId\': \'string\',
                        \'Test\': \'string\',
                        \'Answer\': \'string\',
                        \'SubmitTime\': datetime(2015, 1, 1)
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NumResults** *(integer) --* 
        
              The number of Qualification requests on this page in the filtered results list, equivalent to the number of Qualification requests being returned by this call.
        
            - **QualificationRequests** *(list) --* 
        
              The Qualification request. The response includes one QualificationRequest element for each Qualification request returned by the query.
        
              - *(dict) --* 
        
                The QualificationRequest data structure represents a request a Worker has made for a Qualification. 
        
                - **QualificationRequestId** *(string) --* 
        
                  The ID of the Qualification request, a unique identifier generated when the request was submitted. 
        
                - **QualificationTypeId** *(string) --* 
        
                  The ID of the Qualification type the Worker is requesting, as returned by the CreateQualificationType operation. 
        
                - **WorkerId** *(string) --* 
        
                  The ID of the Worker requesting the Qualification.
        
                - **Test** *(string) --* 
        
                  The contents of the Qualification test that was presented to the Worker, if the type has a test and the Worker has submitted answers. This value is identical to the QuestionForm associated with the Qualification type at the time the Worker requests the Qualification.
        
                - **Answer** *(string) --* 
        
                  The Worker\'s answers for the Qualification type\'s test contained in a QuestionFormAnswers document, if the type has a test and the Worker has submitted answers. If the Worker does not provide any answers, Answer may be empty. 
        
                - **SubmitTime** *(datetime) --* 
        
                  The date and time the Qualification request had a status of Submitted. This is either the time the Worker submitted answers for a Qualification test, or the time the Worker requested the Qualification if the Qualification type does not have a test. 
        
        """
        pass


class ListQualificationTypes(Paginator):
    def paginate(self, MustBeRequestable: bool, Query: str = None, MustBeOwnedByCaller: bool = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mturk-requester-2017-01-17/ListQualificationTypes>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              Query=\'string\',
              MustBeRequestable=True|False,
              MustBeOwnedByCaller=True|False,
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type Query: string
        :param Query: 
        
          A text query against all of the searchable attributes of Qualification types. 
        
        :type MustBeRequestable: boolean
        :param MustBeRequestable: **[REQUIRED]** 
        
          Specifies that only Qualification types that a user can request through the Amazon Mechanical Turk web site, such as by taking a Qualification test, are returned as results of the search. Some Qualification types, such as those assigned automatically by the system, cannot be requested directly by users. If false, all Qualification types, including those managed by the system, are considered. Valid values are True | False. 
        
        :type MustBeOwnedByCaller: boolean
        :param MustBeOwnedByCaller: 
        
          Specifies that only Qualification types that the Requester created are returned. If false, the operation returns all Qualification types. 
        
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
                \'NumResults\': 123,
                \'QualificationTypes\': [
                    {
                        \'QualificationTypeId\': \'string\',
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'Name\': \'string\',
                        \'Description\': \'string\',
                        \'Keywords\': \'string\',
                        \'QualificationTypeStatus\': \'Active\'|\'Inactive\',
                        \'Test\': \'string\',
                        \'TestDurationInSeconds\': 123,
                        \'AnswerKey\': \'string\',
                        \'RetryDelayInSeconds\': 123,
                        \'IsRequestable\': True|False,
                        \'AutoGranted\': True|False,
                        \'AutoGrantedValue\': 123
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NumResults** *(integer) --* 
        
              The number of Qualification types on this page in the filtered results list, equivalent to the number of types this operation returns. 
        
            - **QualificationTypes** *(list) --* 
        
              The list of QualificationType elements returned by the query. 
        
              - *(dict) --* 
        
                The QualificationType data structure represents a Qualification type, a description of a property of a Worker that must match the requirements of a HIT for the Worker to be able to accept the HIT. The type also describes how a Worker can obtain a Qualification of that type, such as through a Qualification test. 
        
                - **QualificationTypeId** *(string) --* 
        
                  A unique identifier for the Qualification type. A Qualification type is given a Qualification type ID when you call the CreateQualificationType operation. 
        
                - **CreationTime** *(datetime) --* 
        
                  The date and time the Qualification type was created. 
        
                - **Name** *(string) --* 
        
                  The name of the Qualification type. The type name is used to identify the type, and to find the type using a Qualification type search. 
        
                - **Description** *(string) --* 
        
                  A long description for the Qualification type. 
        
                - **Keywords** *(string) --* 
        
                  One or more words or phrases that describe theQualification type, separated by commas. The Keywords make the type easier to find using a search. 
        
                - **QualificationTypeStatus** *(string) --* 
        
                  The status of the Qualification type. A Qualification type\'s status determines if users can apply to receive a Qualification of this type, and if HITs can be created with requirements based on this type. Valid values are Active | Inactive. 
        
                - **Test** *(string) --* 
        
                  The questions for a Qualification test associated with this Qualification type that a user can take to obtain a Qualification of this type. This parameter must be specified if AnswerKey is present. A Qualification type cannot have both a specified Test parameter and an AutoGranted value of true. 
        
                - **TestDurationInSeconds** *(integer) --* 
        
                  The amount of time, in seconds, given to a Worker to complete the Qualification test, beginning from the time the Worker requests the Qualification. 
        
                - **AnswerKey** *(string) --* 
        
                  The answers to the Qualification test specified in the Test parameter.
        
                - **RetryDelayInSeconds** *(integer) --* 
        
                  The amount of time, in seconds, Workers must wait after taking the Qualification test before they can take it again. Workers can take a Qualification test multiple times if they were not granted the Qualification from a previous attempt, or if the test offers a gradient score and they want a better score. If not specified, retries are disabled and Workers can request a Qualification only once. 
        
                - **IsRequestable** *(boolean) --* 
        
                  Specifies whether the Qualification type is one that a user can request through the Amazon Mechanical Turk web site, such as by taking a Qualification test. This value is False for Qualifications assigned automatically by the system. Valid values are True | False. 
        
                - **AutoGranted** *(boolean) --* 
        
                  Specifies that requests for the Qualification type are granted immediately, without prompting the Worker with a Qualification test. Valid values are True | False.
        
                - **AutoGrantedValue** *(integer) --* 
        
                  The Qualification integer value to use for automatically granted Qualifications, if AutoGranted is true. This is 1 by default. 
        
        """
        pass


class ListReviewableHITs(Paginator):
    def paginate(self, HITTypeId: str = None, Status: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mturk-requester-2017-01-17/ListReviewableHITs>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              HITTypeId=\'string\',
              Status=\'Reviewable\'|\'Reviewing\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type HITTypeId: string
        :param HITTypeId: 
        
          The ID of the HIT type of the HITs to consider for the query. If not specified, all HITs for the Reviewer are considered 
        
        :type Status: string
        :param Status: 
        
          Can be either ``Reviewable`` or ``Reviewing`` . Reviewable is the default value. 
        
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
                \'NumResults\': 123,
                \'HITs\': [
                    {
                        \'HITId\': \'string\',
                        \'HITTypeId\': \'string\',
                        \'HITGroupId\': \'string\',
                        \'HITLayoutId\': \'string\',
                        \'CreationTime\': datetime(2015, 1, 1),
                        \'Title\': \'string\',
                        \'Description\': \'string\',
                        \'Question\': \'string\',
                        \'Keywords\': \'string\',
                        \'HITStatus\': \'Assignable\'|\'Unassignable\'|\'Reviewable\'|\'Reviewing\'|\'Disposed\',
                        \'MaxAssignments\': 123,
                        \'Reward\': \'string\',
                        \'AutoApprovalDelayInSeconds\': 123,
                        \'Expiration\': datetime(2015, 1, 1),
                        \'AssignmentDurationInSeconds\': 123,
                        \'RequesterAnnotation\': \'string\',
                        \'QualificationRequirements\': [
                            {
                                \'QualificationTypeId\': \'string\',
                                \'Comparator\': \'LessThan\'|\'LessThanOrEqualTo\'|\'GreaterThan\'|\'GreaterThanOrEqualTo\'|\'EqualTo\'|\'NotEqualTo\'|\'Exists\'|\'DoesNotExist\'|\'In\'|\'NotIn\',
                                \'IntegerValues\': [
                                    123,
                                ],
                                \'LocaleValues\': [
                                    {
                                        \'Country\': \'string\',
                                        \'Subdivision\': \'string\'
                                    },
                                ],
                                \'RequiredToPreview\': True|False,
                                \'ActionsGuarded\': \'Accept\'|\'PreviewAndAccept\'|\'DiscoverPreviewAndAccept\'
                            },
                        ],
                        \'HITReviewStatus\': \'NotReviewed\'|\'MarkedForReview\'|\'ReviewedAppropriate\'|\'ReviewedInappropriate\',
                        \'NumberOfAssignmentsPending\': 123,
                        \'NumberOfAssignmentsAvailable\': 123,
                        \'NumberOfAssignmentsCompleted\': 123
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NumResults** *(integer) --* 
        
              The number of HITs on this page in the filtered results list, equivalent to the number of HITs being returned by this call. 
        
            - **HITs** *(list) --* 
        
              The list of HIT elements returned by the query.
        
              - *(dict) --* 
        
                The HIT data structure represents a single HIT, including all the information necessary for a Worker to accept and complete the HIT.
        
                - **HITId** *(string) --* 
        
                  A unique identifier for the HIT.
        
                - **HITTypeId** *(string) --* 
        
                  The ID of the HIT type of this HIT
        
                - **HITGroupId** *(string) --* 
        
                  The ID of the HIT Group of this HIT.
        
                - **HITLayoutId** *(string) --* 
        
                  The ID of the HIT Layout of this HIT.
        
                - **CreationTime** *(datetime) --* 
        
                  The date and time the HIT was created.
        
                - **Title** *(string) --* 
        
                  The title of the HIT.
        
                - **Description** *(string) --* 
        
                  A general description of the HIT.
        
                - **Question** *(string) --* 
        
                  The data the Worker completing the HIT uses produce the results. This is either either a QuestionForm, HTMLQuestion or an ExternalQuestion data structure.
        
                - **Keywords** *(string) --* 
        
                  One or more words or phrases that describe the HIT, separated by commas. Search terms similar to the keywords of a HIT are more likely to have the HIT in the search results.
        
                - **HITStatus** *(string) --* 
        
                  The status of the HIT and its assignments. Valid Values are Assignable | Unassignable | Reviewable | Reviewing | Disposed. 
        
                - **MaxAssignments** *(integer) --* 
        
                  The number of times the HIT can be accepted and completed before the HIT becomes unavailable. 
        
                - **Reward** *(string) --* 
        
                  A string representing a currency amount.
        
                - **AutoApprovalDelayInSeconds** *(integer) --* 
        
                  The amount of time, in seconds, after the Worker submits an assignment for the HIT that the results are automatically approved by Amazon Mechanical Turk. This is the amount of time the Requester has to reject an assignment submitted by a Worker before the assignment is auto-approved and the Worker is paid. 
        
                - **Expiration** *(datetime) --* 
        
                  The date and time the HIT expires.
        
                - **AssignmentDurationInSeconds** *(integer) --* 
        
                  The length of time, in seconds, that a Worker has to complete the HIT after accepting it.
        
                - **RequesterAnnotation** *(string) --* 
        
                  An arbitrary data field the Requester who created the HIT can use. This field is visible only to the creator of the HIT.
        
                - **QualificationRequirements** *(list) --* 
        
                  Conditions that a Worker\'s Qualifications must meet in order to accept the HIT. A HIT can have between zero and ten Qualification requirements. All requirements must be met in order for a Worker to accept the HIT. Additionally, other actions can be restricted using the ``ActionsGuarded`` field on each ``QualificationRequirement`` structure. 
        
                  - *(dict) --* 
        
                    The QualificationRequirement data structure describes a Qualification that a Worker must have before the Worker is allowed to accept a HIT. A requirement may optionally state that a Worker must have the Qualification in order to preview the HIT, or see the HIT in search results. 
        
                    - **QualificationTypeId** *(string) --* 
        
                      The ID of the Qualification type for the requirement.
        
                    - **Comparator** *(string) --* 
        
                      The kind of comparison to make against a Qualification\'s value. You can compare a Qualification\'s value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo, GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue values. Lastly, a Qualification requirement can also test if a Qualification Exists or DoesNotExist in the user\'s profile, regardless of its value. 
        
                    - **IntegerValues** *(list) --* 
        
                      The integer value to compare against the Qualification\'s value. IntegerValue must not be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if the Qualification type has an integer value; it cannot be used with the Worker_Locale QualificationType ID. When performing a set comparison by using the In or the NotIn comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement data structure. 
        
                      - *(integer) --* 
                  
                    - **LocaleValues** *(list) --* 
        
                      The locale value to compare against the Qualification\'s value. The local value must be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a set comparison by using the In or the NotIn comparator, you can use up to 30 LocaleValue elements in a QualificationRequirement data structure. 
        
                      - *(dict) --* 
        
                        The Locale data structure represents a geographical region or location.
        
                        - **Country** *(string) --* 
        
                          The country of the locale. Must be a valid ISO 3166 country code. For example, the code US refers to the United States of America. 
        
                        - **Subdivision** *(string) --* 
        
                          The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For example, the code WA refers to the state of Washington.
        
                    - **RequiredToPreview** *(boolean) --* 
        
                      DEPRECATED: Use the ``ActionsGuarded`` field instead. If RequiredToPreview is true, the question data for the HIT will not be shown when a Worker whose Qualifications do not meet this requirement tries to preview the HIT. That is, a Worker\'s Qualifications must meet all of the requirements for which RequiredToPreview is true in order to preview the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or if there are no such requirements), but does not meet all of the requirements for the HIT, the Worker will be allowed to preview the HIT\'s question data, but will not be allowed to accept and complete the HIT. The default is false. This should not be used in combination with the ``ActionsGuarded`` field. 
        
                    - **ActionsGuarded** *(string) --* 
        
                      Setting this attribute prevents Workers whose Qualifications do not meet this QualificationRequirement from taking the specified action. Valid arguments include \"Accept\" (Worker cannot accept the HIT, but can preview the HIT and see it in their search results), \"PreviewAndAccept\" (Worker cannot accept or preview the HIT, but can see the HIT in their search results), and \"DiscoverPreviewAndAccept\" (Worker cannot accept, preview, or see the HIT in their search results). It\'s possible for you to create a HIT with multiple QualificationRequirements (which can have different values for the ActionGuarded attribute). In this case, the Worker is only permitted to perform an action when they have met all QualificationRequirements guarding the action. The actions in the order of least restrictive to most restrictive are Discover, Preview and Accept. For example, if a Worker meets all QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet all requirements that are set with PreviewAndAccept, then the Worker will be able to Discover, i.e. see the HIT in their search result, but will not be able to Preview or Accept the HIT. ActionsGuarded should not be used in combination with the ``RequiredToPreview`` field. 
        
                - **HITReviewStatus** *(string) --* 
        
                  Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview | ReviewedAppropriate | ReviewedInappropriate.
        
                - **NumberOfAssignmentsPending** *(integer) --* 
        
                  The number of assignments for this HIT that are being previewed or have been accepted by Workers, but have not yet been submitted, returned, or abandoned.
        
                - **NumberOfAssignmentsAvailable** *(integer) --* 
        
                  The number of assignments for this HIT that are available for Workers to accept.
        
                - **NumberOfAssignmentsCompleted** *(integer) --* 
        
                  The number of assignments for this HIT that have been approved or rejected.
        
        """
        pass


class ListWorkerBlocks(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mturk-requester-2017-01-17/ListWorkerBlocks>`_
        
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
                \'NumResults\': 123,
                \'WorkerBlocks\': [
                    {
                        \'WorkerId\': \'string\',
                        \'Reason\': \'string\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NumResults** *(integer) --* 
        
              The number of assignments on the page in the filtered results list, equivalent to the number of assignments returned by this call.
        
            - **WorkerBlocks** *(list) --* 
        
              The list of WorkerBlocks, containing the collection of Worker IDs and reasons for blocking.
        
              - *(dict) --* 
        
                The WorkerBlock data structure represents a Worker who has been blocked. It has two elements: the WorkerId and the Reason for the block. 
        
                - **WorkerId** *(string) --* 
        
                  The ID of the Worker who accepted the HIT.
        
                - **Reason** *(string) --* 
        
                  A message explaining the reason the Worker was blocked. 
        
        """
        pass


class ListWorkersWithQualificationType(Paginator):
    def paginate(self, QualificationTypeId: str, Status: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/mturk-requester-2017-01-17/ListWorkersWithQualificationType>`_
        
        **Request Syntax** 
        ::
        
          response_iterator = paginator.paginate(
              QualificationTypeId=\'string\',
              Status=\'Granted\'|\'Revoked\',
              PaginationConfig={
                  \'MaxItems\': 123,
                  \'PageSize\': 123,
                  \'StartingToken\': \'string\'
              }
          )
        :type QualificationTypeId: string
        :param QualificationTypeId: **[REQUIRED]** 
        
          The ID of the Qualification type of the Qualifications to return.
        
        :type Status: string
        :param Status: 
        
          The status of the Qualifications to return. Can be ``Granted | Revoked`` . 
        
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
                \'NumResults\': 123,
                \'Qualifications\': [
                    {
                        \'QualificationTypeId\': \'string\',
                        \'WorkerId\': \'string\',
                        \'GrantTime\': datetime(2015, 1, 1),
                        \'IntegerValue\': 123,
                        \'LocaleValue\': {
                            \'Country\': \'string\',
                            \'Subdivision\': \'string\'
                        },
                        \'Status\': \'Granted\'|\'Revoked\'
                    },
                ]
            }
          **Response Structure** 
        
          - *(dict) --* 
            
            - **NumResults** *(integer) --* 
        
              The number of Qualifications on this page in the filtered results list, equivalent to the number of Qualifications being returned by this call.
        
            - **Qualifications** *(list) --* 
        
              The list of Qualification elements returned by this call. 
        
              - *(dict) --* 
        
                The Qualification data structure represents a Qualification assigned to a user, including the Qualification type and the value (score).
        
                - **QualificationTypeId** *(string) --* 
        
                  The ID of the Qualification type for the Qualification.
        
                - **WorkerId** *(string) --* 
        
                  The ID of the Worker who possesses the Qualification. 
        
                - **GrantTime** *(datetime) --* 
        
                  The date and time the Qualification was granted to the Worker. If the Worker\'s Qualification was revoked, and then re-granted based on a new Qualification request, GrantTime is the date and time of the last call to the AcceptQualificationRequest operation.
        
                - **IntegerValue** *(integer) --* 
        
                  The value (score) of the Qualification, if the Qualification has an integer value.
        
                - **LocaleValue** *(dict) --* 
        
                  The Locale data structure represents a geographical region or location.
        
                  - **Country** *(string) --* 
        
                    The country of the locale. Must be a valid ISO 3166 country code. For example, the code US refers to the United States of America. 
        
                  - **Subdivision** *(string) --* 
        
                    The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For example, the code WA refers to the state of Washington.
        
                - **Status** *(string) --* 
        
                  The status of the Qualification. Valid values are Granted | Revoked.
        
        """
        pass
