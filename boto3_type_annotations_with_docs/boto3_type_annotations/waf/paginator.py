from typing import Dict
from botocore.paginate import Paginator


class GetRateBasedRuleManagedKeys(Paginator):
    def paginate(self, RuleId: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WAF.Client.get_rate_based_rule_managed_keys`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-2015-08-24/GetRateBasedRuleManagedKeys>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              RuleId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ManagedKeys': [
                    'string',
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ManagedKeys** *(list) --* 
              An array of IP addresses that currently are blocked by the specified  RateBasedRule . 
              - *(string) --* 
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type RuleId: string
        :param RuleId: **[REQUIRED]**
          The ``RuleId`` of the  RateBasedRule for which you want to get a list of ``ManagedKeys`` . ``RuleId`` is returned by  CreateRateBasedRule and by  ListRateBasedRules .
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


class ListActivatedRulesInRuleGroup(Paginator):
    def paginate(self, RuleGroupId: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WAF.Client.list_activated_rules_in_rule_group`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-2015-08-24/ListActivatedRulesInRuleGroup>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              RuleGroupId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ActivatedRules': [
                    {
                        'Priority': 123,
                        'RuleId': 'string',
                        'Action': {
                            'Type': 'BLOCK'|'ALLOW'|'COUNT'
                        },
                        'OverrideAction': {
                            'Type': 'NONE'|'COUNT'
                        },
                        'Type': 'REGULAR'|'RATE_BASED'|'GROUP',
                        'ExcludedRules': [
                            {
                                'RuleId': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ActivatedRules** *(list) --* 
              An array of ``ActivatedRules`` objects.
              - *(dict) --* 
                The ``ActivatedRule`` object in an  UpdateWebACL request specifies a ``Rule`` that you want to insert or delete, the priority of the ``Rule`` in the ``WebACL`` , and the action that you want AWS WAF to take when a web request matches the ``Rule`` (``ALLOW`` , ``BLOCK`` , or ``COUNT`` ).
                To specify whether to insert or delete a ``Rule`` , use the ``Action`` parameter in the  WebACLUpdate data type.
                - **Priority** *(integer) --* 
                  Specifies the order in which the ``Rules`` in a ``WebACL`` are evaluated. Rules with a lower value for ``Priority`` are evaluated before ``Rules`` with a higher value. The value must be a unique integer. If you add multiple ``Rules`` to a ``WebACL`` , the values don't need to be consecutive.
                - **RuleId** *(string) --* 
                  The ``RuleId`` for a ``Rule`` . You use ``RuleId`` to get more information about a ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule`` from AWS WAF (see  DeleteRule ).
                   ``RuleId`` is returned by  CreateRule and by  ListRules .
                - **Action** *(dict) --* 
                  Specifies the action that CloudFront or AWS WAF takes when a web request matches the conditions in the ``Rule`` . Valid values for ``Action`` include the following:
                  * ``ALLOW`` : CloudFront responds with the requested object. 
                  * ``BLOCK`` : CloudFront responds with an HTTP 403 (Forbidden) status code. 
                  * ``COUNT`` : AWS WAF increments a counter of requests that match the conditions in the rule and then continues to inspect the web request based on the remaining rules in the web ACL.  
                   ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup`` to a ``WebACL`` . In this case, you do not use ``ActivatedRule|Action`` . For all other update requests, ``ActivatedRule|Action`` is used instead of ``ActivatedRule|OverrideAction`` .
                  - **Type** *(string) --* 
                    Specifies how you want AWS WAF to respond to requests that match the settings in a ``Rule`` . Valid settings include the following:
                    * ``ALLOW`` : AWS WAF allows requests 
                    * ``BLOCK`` : AWS WAF blocks requests 
                    * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for a ``WebACL`` . 
                - **OverrideAction** *(dict) --* 
                  Use the ``OverrideAction`` to test your ``RuleGroup`` .
                  Any rule in a ``RuleGroup`` can potentially block a request. If you set the ``OverrideAction`` to ``None`` , the ``RuleGroup`` will block a request if any individual rule in the ``RuleGroup`` matches the request and is configured to block that request. However if you first want to test the ``RuleGroup`` , set the ``OverrideAction`` to ``Count`` . The ``RuleGroup`` will then override any block action specified by individual rules contained within the group. Instead of blocking matching requests, those requests will be counted. You can view a record of counted requests using  GetSampledRequests . 
                   ``ActivatedRule|OverrideAction`` applies only when updating or adding a ``RuleGroup`` to a ``WebACL`` . In this case you do not use ``ActivatedRule|Action`` . For all other update requests, ``ActivatedRule|Action`` is used instead of ``ActivatedRule|OverrideAction`` .
                  - **Type** *(string) --* 
                     ``COUNT`` overrides the action specified by the individual rule within a ``RuleGroup`` . If set to ``NONE`` , the rule's action will take place.
                - **Type** *(string) --* 
                  The rule type, either ``REGULAR`` , as defined by  Rule , ``RATE_BASED`` , as defined by  RateBasedRule , or ``GROUP`` , as defined by  RuleGroup . The default is REGULAR. Although this field is optional, be aware that if you try to add a RATE_BASED rule to a web ACL without setting the type, the  UpdateWebACL request will fail because the request tries to add a REGULAR rule with the specified ID, which does not exist. 
                - **ExcludedRules** *(list) --* 
                  An array of rules to exclude from a rule group. This is applicable only when the ``ActivatedRule`` refers to a ``RuleGroup`` .
                  Sometimes it is necessary to troubleshoot rule groups that are blocking traffic unexpectedly (false positives). One troubleshooting technique is to identify the specific rule within the rule group that is blocking the legitimate traffic and then disable (exclude) that particular rule. You can exclude rules from both your own rule groups and AWS Marketplace rule groups that have been associated with a web ACL.
                  Specifying ``ExcludedRules`` does not remove those rules from the rule group. Rather, it changes the action for the rules to ``COUNT`` . Therefore, requests that match an ``ExcludedRule`` are counted but not blocked. The ``RuleGroup`` owner will receive COUNT metrics for each ``ExcludedRule`` .
                  If you want to exclude rules from a rule group that is already associated with a web ACL, perform the following steps:
                  * Use the AWS WAF logs to identify the IDs of the rules that you want to exclude. For more information about the logs, see `Logging Web ACL Traffic Information <http://docs.aws.amazon.com/waf/latest/developerguide/logging.html>`__ . 
                  * Submit an  UpdateWebACL request that has two actions: 
                    * The first action deletes the existing rule group from the web ACL. That is, in the  UpdateWebACL request, the first ``Updates:Action`` should be ``DELETE`` and ``Updates:ActivatedRule:RuleId`` should be the rule group that contains the rules that you want to exclude. 
                    * The second action inserts the same rule group back in, but specifying the rules to exclude. That is, the second ``Updates:Action`` should be ``INSERT`` , ``Updates:ActivatedRule:RuleId`` should be the rule group that you just removed, and ``ExcludedRules`` should contain the rules that you want to exclude. 
                  - *(dict) --* 
                    The rule to exclude from a rule group. This is applicable only when the ``ActivatedRule`` refers to a ``RuleGroup`` . The rule must belong to the ``RuleGroup`` that is specified by the ``ActivatedRule`` . 
                    - **RuleId** *(string) --* 
                      The unique identifier for the rule to exclude from the rule group.
            - **NextToken** *(string) --* 
              A token to resume pagination.
        :type RuleGroupId: string
        :param RuleGroupId:
          The ``RuleGroupId`` of the  RuleGroup for which you want to get a list of  ActivatedRule objects.
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


class ListByteMatchSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WAF.Client.list_byte_match_sets`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-2015-08-24/ListByteMatchSets>`_
        
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
                'ByteMatchSets': [
                    {
                        'ByteMatchSetId': 'string',
                        'Name': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ByteMatchSets** *(list) --* 
              An array of  ByteMatchSetSummary objects.
              - *(dict) --* 
                Returned by  ListByteMatchSets . Each ``ByteMatchSetSummary`` object includes the ``Name`` and ``ByteMatchSetId`` for one  ByteMatchSet .
                - **ByteMatchSetId** *(string) --* 
                  The ``ByteMatchSetId`` for a ``ByteMatchSet`` . You use ``ByteMatchSetId`` to get information about a ``ByteMatchSet`` , update a ``ByteMatchSet`` , remove a ``ByteMatchSet`` from a ``Rule`` , and delete a ``ByteMatchSet`` from AWS WAF.
                   ``ByteMatchSetId`` is returned by  CreateByteMatchSet and by  ListByteMatchSets .
                - **Name** *(string) --* 
                  A friendly name or description of the  ByteMatchSet . You can't change ``Name`` after you create a ``ByteMatchSet`` .
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class ListGeoMatchSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WAF.Client.list_geo_match_sets`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-2015-08-24/ListGeoMatchSets>`_
        
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
                'GeoMatchSets': [
                    {
                        'GeoMatchSetId': 'string',
                        'Name': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **GeoMatchSets** *(list) --* 
              An array of  GeoMatchSetSummary objects.
              - *(dict) --* 
                Contains the identifier and the name of the ``GeoMatchSet`` .
                - **GeoMatchSetId** *(string) --* 
                  The ``GeoMatchSetId`` for an  GeoMatchSet . You can use ``GeoMatchSetId`` in a  GetGeoMatchSet request to get detailed information about an  GeoMatchSet .
                - **Name** *(string) --* 
                  A friendly name or description of the  GeoMatchSet . You can't change the name of an ``GeoMatchSet`` after you create it.
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class ListIPSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WAF.Client.list_ip_sets`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-2015-08-24/ListIPSets>`_
        
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
                'IPSets': [
                    {
                        'IPSetId': 'string',
                        'Name': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **IPSets** *(list) --* 
              An array of  IPSetSummary objects.
              - *(dict) --* 
                Contains the identifier and the name of the ``IPSet`` .
                - **IPSetId** *(string) --* 
                  The ``IPSetId`` for an  IPSet . You can use ``IPSetId`` in a  GetIPSet request to get detailed information about an  IPSet .
                - **Name** *(string) --* 
                  A friendly name or description of the  IPSet . You can't change the name of an ``IPSet`` after you create it.
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class ListLoggingConfigurations(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WAF.Client.list_logging_configurations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-2015-08-24/ListLoggingConfigurations>`_
        
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
                'LoggingConfigurations': [
                    {
                        'ResourceArn': 'string',
                        'LogDestinationConfigs': [
                            'string',
                        ],
                        'RedactedFields': [
                            {
                                'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY'|'SINGLE_QUERY_ARG'|'ALL_QUERY_ARGS',
                                'Data': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **LoggingConfigurations** *(list) --* 
              An array of  LoggingConfiguration objects.
              - *(dict) --* 
                The Amazon Kinesis Data Firehose, ``RedactedFields`` information, and the web ACL Amazon Resource Name (ARN).
                - **ResourceArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the web ACL that you want to associate with ``LogDestinationConfigs`` .
                - **LogDestinationConfigs** *(list) --* 
                  An array of Amazon Kinesis Data Firehose ARNs.
                  - *(string) --* 
                - **RedactedFields** *(list) --* 
                  The parts of the request that you want redacted from the logs. For example, if you redact the cookie field, the cookie field in the firehose will be ``xxx`` . 
                  - *(dict) --* 
                    Specifies where in a web request to look for ``TargetString`` .
                    - **Type** *(string) --* 
                      The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:
                      * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the header in ``Data`` . 
                      * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` . 
                      * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a ``?`` character, if any. 
                      * ``URI`` : The part of a web request that identifies a resource, for example, ``/images/daily-ad.jpg`` . 
                      * ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .  
                      * ``SINGLE_QUERY_ARG`` : The parameter in the query string that you will inspect, such as *UserName* or *SalesRegion* . The maximum length for ``SINGLE_QUERY_ARG`` is 30 characters. 
                      * ``ALL_QUERY_ARGS`` : Similar to ``SINGLE_QUERY_ARG`` , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in ``TargetString`` . 
                    - **Data** *(string) --* 
                      When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . The name of the header is not case sensitive.
                      When the value of ``Type`` is ``SINGLE_QUERY_ARG`` , enter the name of the parameter that you want AWS WAF to search, for example, ``UserName`` or ``SalesRegion`` . The parameter name is not case sensitive.
                      If the value of ``Type`` is any other value, omit ``Data`` .
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class ListRateBasedRules(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WAF.Client.list_rate_based_rules`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-2015-08-24/ListRateBasedRules>`_
        
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
                'Rules': [
                    {
                        'RuleId': 'string',
                        'Name': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Rules** *(list) --* 
              An array of  RuleSummary objects.
              - *(dict) --* 
                Contains the identifier and the friendly name or description of the ``Rule`` .
                - **RuleId** *(string) --* 
                  A unique identifier for a ``Rule`` . You use ``RuleId`` to get more information about a ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a ``WebACL`` or delete one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule`` from AWS WAF (see  DeleteRule ).
                   ``RuleId`` is returned by  CreateRule and by  ListRules .
                - **Name** *(string) --* 
                  A friendly name or description of the  Rule . You can't change the name of a ``Rule`` after you create it.
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class ListRegexMatchSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WAF.Client.list_regex_match_sets`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-2015-08-24/ListRegexMatchSets>`_
        
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
                'RegexMatchSets': [
                    {
                        'RegexMatchSetId': 'string',
                        'Name': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RegexMatchSets** *(list) --* 
              An array of  RegexMatchSetSummary objects.
              - *(dict) --* 
                Returned by  ListRegexMatchSets . Each ``RegexMatchSetSummary`` object includes the ``Name`` and ``RegexMatchSetId`` for one  RegexMatchSet .
                - **RegexMatchSetId** *(string) --* 
                  The ``RegexMatchSetId`` for a ``RegexMatchSet`` . You use ``RegexMatchSetId`` to get information about a ``RegexMatchSet`` , update a ``RegexMatchSet`` , remove a ``RegexMatchSet`` from a ``Rule`` , and delete a ``RegexMatchSet`` from AWS WAF.
                   ``RegexMatchSetId`` is returned by  CreateRegexMatchSet and by  ListRegexMatchSets .
                - **Name** *(string) --* 
                  A friendly name or description of the  RegexMatchSet . You can't change ``Name`` after you create a ``RegexMatchSet`` .
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class ListRegexPatternSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WAF.Client.list_regex_pattern_sets`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-2015-08-24/ListRegexPatternSets>`_
        
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
                'RegexPatternSets': [
                    {
                        'RegexPatternSetId': 'string',
                        'Name': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RegexPatternSets** *(list) --* 
              An array of  RegexPatternSetSummary objects.
              - *(dict) --* 
                Returned by  ListRegexPatternSets . Each ``RegexPatternSetSummary`` object includes the ``Name`` and ``RegexPatternSetId`` for one  RegexPatternSet .
                - **RegexPatternSetId** *(string) --* 
                  The ``RegexPatternSetId`` for a ``RegexPatternSet`` . You use ``RegexPatternSetId`` to get information about a ``RegexPatternSet`` , update a ``RegexPatternSet`` , remove a ``RegexPatternSet`` from a ``RegexMatchSet`` , and delete a ``RegexPatternSet`` from AWS WAF.
                   ``RegexPatternSetId`` is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .
                - **Name** *(string) --* 
                  A friendly name or description of the  RegexPatternSet . You can't change ``Name`` after you create a ``RegexPatternSet`` .
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class ListRuleGroups(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WAF.Client.list_rule_groups`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-2015-08-24/ListRuleGroups>`_
        
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
                'RuleGroups': [
                    {
                        'RuleGroupId': 'string',
                        'Name': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RuleGroups** *(list) --* 
              An array of  RuleGroup objects.
              - *(dict) --* 
                Contains the identifier and the friendly name or description of the ``RuleGroup`` .
                - **RuleGroupId** *(string) --* 
                  A unique identifier for a ``RuleGroup`` . You use ``RuleGroupId`` to get more information about a ``RuleGroup`` (see  GetRuleGroup ), update a ``RuleGroup`` (see  UpdateRuleGroup ), insert a ``RuleGroup`` into a ``WebACL`` or delete one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``RuleGroup`` from AWS WAF (see  DeleteRuleGroup ).
                   ``RuleGroupId`` is returned by  CreateRuleGroup and by  ListRuleGroups .
                - **Name** *(string) --* 
                  A friendly name or description of the  RuleGroup . You can't change the name of a ``RuleGroup`` after you create it.
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class ListRules(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WAF.Client.list_rules`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-2015-08-24/ListRules>`_
        
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
                'Rules': [
                    {
                        'RuleId': 'string',
                        'Name': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Rules** *(list) --* 
              An array of  RuleSummary objects.
              - *(dict) --* 
                Contains the identifier and the friendly name or description of the ``Rule`` .
                - **RuleId** *(string) --* 
                  A unique identifier for a ``Rule`` . You use ``RuleId`` to get more information about a ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a ``WebACL`` or delete one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule`` from AWS WAF (see  DeleteRule ).
                   ``RuleId`` is returned by  CreateRule and by  ListRules .
                - **Name** *(string) --* 
                  A friendly name or description of the  Rule . You can't change the name of a ``Rule`` after you create it.
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class ListSizeConstraintSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WAF.Client.list_size_constraint_sets`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-2015-08-24/ListSizeConstraintSets>`_
        
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
                'SizeConstraintSets': [
                    {
                        'SizeConstraintSetId': 'string',
                        'Name': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **SizeConstraintSets** *(list) --* 
              An array of  SizeConstraintSetSummary objects.
              - *(dict) --* 
                The ``Id`` and ``Name`` of a ``SizeConstraintSet`` .
                - **SizeConstraintSetId** *(string) --* 
                  A unique identifier for a ``SizeConstraintSet`` . You use ``SizeConstraintSetId`` to get information about a ``SizeConstraintSet`` (see  GetSizeConstraintSet ), update a ``SizeConstraintSet`` (see  UpdateSizeConstraintSet ), insert a ``SizeConstraintSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete a ``SizeConstraintSet`` from AWS WAF (see  DeleteSizeConstraintSet ).
                   ``SizeConstraintSetId`` is returned by  CreateSizeConstraintSet and by  ListSizeConstraintSets .
                - **Name** *(string) --* 
                  The name of the ``SizeConstraintSet`` , if any.
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class ListSqlInjectionMatchSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WAF.Client.list_sql_injection_match_sets`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-2015-08-24/ListSqlInjectionMatchSets>`_
        
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
                'SqlInjectionMatchSets': [
                    {
                        'SqlInjectionMatchSetId': 'string',
                        'Name': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The response to a  ListSqlInjectionMatchSets request.
            - **SqlInjectionMatchSets** *(list) --* 
              An array of  SqlInjectionMatchSetSummary objects.
              - *(dict) --* 
                The ``Id`` and ``Name`` of a ``SqlInjectionMatchSet`` .
                - **SqlInjectionMatchSetId** *(string) --* 
                  A unique identifier for a ``SqlInjectionMatchSet`` . You use ``SqlInjectionMatchSetId`` to get information about a ``SqlInjectionMatchSet`` (see  GetSqlInjectionMatchSet ), update a ``SqlInjectionMatchSet`` (see  UpdateSqlInjectionMatchSet ), insert a ``SqlInjectionMatchSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete a ``SqlInjectionMatchSet`` from AWS WAF (see  DeleteSqlInjectionMatchSet ).
                   ``SqlInjectionMatchSetId`` is returned by  CreateSqlInjectionMatchSet and by  ListSqlInjectionMatchSets .
                - **Name** *(string) --* 
                  The name of the ``SqlInjectionMatchSet`` , if any, specified by ``Id`` .
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class ListSubscribedRuleGroups(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WAF.Client.list_subscribed_rule_groups`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-2015-08-24/ListSubscribedRuleGroups>`_
        
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
                'RuleGroups': [
                    {
                        'RuleGroupId': 'string',
                        'Name': 'string',
                        'MetricName': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **RuleGroups** *(list) --* 
              An array of  RuleGroup objects.
              - *(dict) --* 
                A summary of the rule groups you are subscribed to.
                - **RuleGroupId** *(string) --* 
                  A unique identifier for a ``RuleGroup`` .
                - **Name** *(string) --* 
                  A friendly name or description of the ``RuleGroup`` . You can't change the name of a ``RuleGroup`` after you create it.
                - **MetricName** *(string) --* 
                  A friendly name or description for the metrics for this ``RuleGroup`` . The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace. You can't change the name of the metric after you create the ``RuleGroup`` .
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class ListWebACLs(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WAF.Client.list_web_acls`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-2015-08-24/ListWebACLs>`_
        
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
                'WebACLs': [
                    {
                        'WebACLId': 'string',
                        'Name': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **WebACLs** *(list) --* 
              An array of  WebACLSummary objects.
              - *(dict) --* 
                Contains the identifier and the name or description of the  WebACL .
                - **WebACLId** *(string) --* 
                  A unique identifier for a ``WebACL`` . You use ``WebACLId`` to get information about a ``WebACL`` (see  GetWebACL ), update a ``WebACL`` (see  UpdateWebACL ), and delete a ``WebACL`` from AWS WAF (see  DeleteWebACL ).
                   ``WebACLId`` is returned by  CreateWebACL and by  ListWebACLs .
                - **Name** *(string) --* 
                  A friendly name or description of the  WebACL . You can't change the name of a ``WebACL`` after you create it.
            - **NextToken** *(string) --* 
              A token to resume pagination.
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


class ListXssMatchSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`WAF.Client.list_xss_match_sets`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-2015-08-24/ListXssMatchSets>`_
        
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
                'XssMatchSets': [
                    {
                        'XssMatchSetId': 'string',
                        'Name': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            The response to a  ListXssMatchSets request.
            - **XssMatchSets** *(list) --* 
              An array of  XssMatchSetSummary objects.
              - *(dict) --* 
                The ``Id`` and ``Name`` of an ``XssMatchSet`` .
                - **XssMatchSetId** *(string) --* 
                  A unique identifier for an ``XssMatchSet`` . You use ``XssMatchSetId`` to get information about a ``XssMatchSet`` (see  GetXssMatchSet ), update an ``XssMatchSet`` (see  UpdateXssMatchSet ), insert an ``XssMatchSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete an ``XssMatchSet`` from AWS WAF (see  DeleteXssMatchSet ).
                   ``XssMatchSetId`` is returned by  CreateXssMatchSet and by  ListXssMatchSets .
                - **Name** *(string) --* 
                  The name of the ``XssMatchSet`` , if any, specified by ``Id`` .
            - **NextToken** *(string) --* 
              A token to resume pagination.
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
