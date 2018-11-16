from typing import Dict
from botocore.paginate import Paginator


class ListByteMatchSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-2015-08-24/ListByteMatchSets>`_
        
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
                \'ByteMatchSets\': [
                    {
                        \'ByteMatchSetId\': \'string\',
                        \'Name\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
                  A friendly name or description of the  ByteMatchSet . You can\'t change ``Name`` after you create a ``ByteMatchSet`` .
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListIPSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-2015-08-24/ListIPSets>`_
        
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
                \'IPSets\': [
                    {
                        \'IPSetId\': \'string\',
                        \'Name\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
                  A friendly name or description of the  IPSet . You can\'t change the name of an ``IPSet`` after you create it.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListRules(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-2015-08-24/ListRules>`_
        
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
                \'Rules\': [
                    {
                        \'RuleId\': \'string\',
                        \'Name\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
                  A friendly name or description of the  Rule . You can\'t change the name of a ``Rule`` after you create it.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListSizeConstraintSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-2015-08-24/ListSizeConstraintSets>`_
        
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
                \'SizeConstraintSets\': [
                    {
                        \'SizeConstraintSetId\': \'string\',
                        \'Name\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
        """
        pass


class ListSqlInjectionMatchSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-2015-08-24/ListSqlInjectionMatchSets>`_
        
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
                \'SqlInjectionMatchSets\': [
                    {
                        \'SqlInjectionMatchSetId\': \'string\',
                        \'Name\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
        """
        pass


class ListWebACLs(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-2015-08-24/ListWebACLs>`_
        
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
                \'WebACLs\': [
                    {
                        \'WebACLId\': \'string\',
                        \'Name\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
                  A friendly name or description of the  WebACL . You can\'t change the name of a ``WebACL`` after you create it.
        
            - **NextToken** *(string) --* 
        
              A token to resume pagination.
        
        """
        pass


class ListXssMatchSets(Paginator):
    def paginate(self, PaginationConfig: Dict = None) -> Dict:
        """
        
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-2015-08-24/ListXssMatchSets>`_
        
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
                \'XssMatchSets\': [
                    {
                        \'XssMatchSetId\': \'string\',
                        \'Name\': \'string\'
                    },
                ],
                \'NextToken\': \'string\'
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
        
        """
        pass
